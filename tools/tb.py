#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tb.py — Agent tổng hợp báo cáo · Khối Telesale Kangnam

BON NGUON ROI  ──►  MOT PHE U MOT MACH  ──►  NGAY · TUAN · THANG · VAN DE

Hai thu quan trong nhat trong file nay:

① ĐỔI MÃ NV NGAY Ở BƯỚC ĐỌC (tb-G §2).
   ⛔ Khong doi o buoc xuat — neu doi o buoc xuat thi ten that con lai
   trong MOI file trung gian, va mot trong so do se bi gui di.

② MOI LAN GHI FILE DI QUA ghi_file(), ham nay chay CONG R (tb-G §5)
   va TU CHOI GHI neu con ten that / du kien khach.

    python tools/tb.py doc     du-lieu/            --ky "27/10-02/11"
    python tools/tb.py ngay    --ngay 2026-11-03
    python tools/tb.py tuan    --ky "27/10-02/11"
    python tools/tb.py thang   --thang 2026-10
    python tools/tb.py van-de  --ky "27/10-02/11"
    python tools/tb.py kiem    out/bao-cao-tuan-....md
"""

import argparse
import csv
import glob
import hashlib
import io
import json
import os
import re
import statistics
import sys
from datetime import datetime, date

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(GOC, "out")
MA_NV = os.path.join(GOC, "ma-nhan-vien.csv")      # ⛔ .gitignore chan — tb-G §1

CAU_CHAN = ("Số liệu dùng để phân việc kèm cặp. "
            "Không phải căn cứ kỷ luật hay xếp hạng công khai.")

# tb-B §2 — cot bat buoc tung nguon
NGUON = {
    "1-cuoc-goi":      {"ten": "Cuộc gọi",        "moc": "ngay_goi",
                        "bat_buoc": ["ngay_goi", "ma_lead", "ma_nv", "huong", "ket_qua"]},
    "2-data-phan-bo":  {"ten": "Data phân bổ",    "moc": "ngay_nhan",
                        "bat_buoc": ["ngay_nhan", "ma_lead", "nguon_data", "ma_nv_duoc_giao"]},
    "3-lich-hen":      {"ten": "Lịch hẹn",        "moc": "ngay_tao_hen",
                        "bat_buoc": ["ngay_tao_hen", "ngay_hen", "ma_lead", "da_den"]},
    "4-ca-chot":       {"ten": "Ca chốt",         "moc": "ngay_chot",
                        "bat_buoc": ["ngay_chot", "ma_lead", "so_tien"]},
}

# Cot ⛔ BO HAN ngay o buoc doc — tb-G §2
BO_HAN = ["ghi_chu", "ghi_chu_nv", "note", "notes", "nhan_xet", "ten_khach",
          "ho_ten", "sdt", "so_dien_thoai", "phone", "email", "dia_chi"]

TEN_KHE = {
    "K1": "Data để nguội",
    "K2": "Data chưa gọi hết",
    "K3": "Gọi mà không kết nối",
    "K4": "Bỏ lead quá sớm",
    "K5": "Kết nối mà không đặt được hẹn",
    "K6": "Đặt hẹn mà không đến (no-show)",
    "K7": "Đến khám mà không chốt",
    "K8": "Tải việc lệch",
    "K9": "Data tồn dồn",
}
# tb-E §5 — goc thuong gap. "?" = phai tach moi biet (K3)
GOC_KHE = {"K1": "he", "K2": "?", "K3": "?", "K4": "nguoi", "K5": "nguoi",
           "K6": "he", "K7": "ngoai-khoi", "K8": "he", "K9": "he"}


# ────────────────────────────────────────────────────────────────
# 0 · TIEN ICH
# ────────────────────────────────────────────────────────────────

def ngay(s):
    """'2026-11-03' -> date. Tra None neu khong doc duoc."""
    s = (s or "").strip()[:10]
    try:
        return datetime.strptime(s, "%Y-%m-%d").date()
    except ValueError:
        return None


def ty_le(tu, mau):
    """tb-F §1 — MOI ty le in kem MAU SO. ⛔ Khong bao gio tra ve '62%' tron."""
    if not mau:
        return "⏸ chưa đo được"
    return "%d/%d · %d%%" % (tu, mau, round(tu * 100.0 / mau))


def trung_vi(xs):
    """tb-C §6 — TRUNG VI, ⛔ khong phai trung binh: mot lead chot sau 90 ngay
    se keo lech trung binh."""
    xs = [x for x in xs if x is not None]
    return round(statistics.median(xs), 1) if xs else None


def nap(ten):
    p = os.path.join(OUT, ten)
    if not os.path.exists(p):
        return None
    with io.open(p, encoding="utf-8") as f:
        return json.load(f)


# ────────────────────────────────────────────────────────────────
# 1 · ĐỔI MÃ — NGAY Ở BƯỚC ĐỌC (tb-G §2)
# ────────────────────────────────────────────────────────────────

class BangMa:
    """Giu ban do ten that -> NV-xx. BEN giua cac ky (tb-G §1).

    File ma-nhan-vien.csv ⛔ DA BI .gitignore CHAN va ⛔ khong bao gio
    duoc ghi vao out/.
    """

    def __init__(self):
        self.ten2ma, self.ma2ten = {}, {}
        if os.path.exists(MA_NV):
            with io.open(MA_NV, encoding="utf-8-sig") as f:
                for r in csv.DictReader(f):
                    t, m = (r.get("ten") or "").strip(), (r.get("ma") or "").strip()
                    if t and m:
                        self.ten2ma[t], self.ma2ten[m] = m, t

    def ma(self, ten):
        ten = (ten or "").strip()
        if not ten:
            return ""
        if ten not in self.ten2ma:
            m = "NV-%02d" % (len(self.ten2ma) + 1)
            self.ten2ma[ten], self.ma2ten[m] = m, ten
        return self.ten2ma[ten]

    def luu(self):
        with io.open(MA_NV, "w", encoding="utf-8-sig", newline="") as f:
            w = csv.writer(f)
            w.writerow(["ma", "ten"])
            for m in sorted(self.ma2ten, key=lambda x: int(x.split("-")[1])):
                w.writerow([m, self.ma2ten[m]])

    def ten_that(self):
        return list(self.ma2ten.values())


def bam_sdt(s):
    """SDT -> hash mot chieu. Van noi duoc phe u ma ⛔ khong giu so."""
    s = re.sub(r"\D", "", s or "")
    return ("H" + hashlib.sha256(s.encode()).hexdigest()[:10]) if s else ""


# ────────────────────────────────────────────────────────────────
# 2 · ĐỌC BỐN NGUỒN  (tb-B)
# ────────────────────────────────────────────────────────────────

def doc_mot(duong, khoa, bm):
    """Doc mot file nguon. ĐỔI MÃ + BO CỘT NHẠY CẢM NGAY TAI DAY."""
    with io.open(duong, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    ra, bo_cot = [], set()
    for r in rows:
        moi = {}
        for k, v in r.items():
            kl = (k or "").strip().lower()
            if kl in BO_HAN and kl not in ("sdt", "so_dien_thoai", "phone"):
                bo_cot.add(kl)                       # ⛔ bo han — tb-G §2 ④
                continue
            if kl in ("sdt", "so_dien_thoai", "phone"):
                moi["sdt_hash"] = bam_sdt(v)         # bam, ⛔ khong giu so
                bo_cot.add(kl)
                continue
            if kl in ("ma_nv", "ma_nv_duoc_giao"):
                moi[kl] = bm.ma(v)                   # ★ doi ma NGAY O BUOC DOC
                continue
            moi[kl] = (v or "").strip()
        ra.append(moi)
    thieu = [c for c in NGUON[khoa]["bat_buoc"] if ra and c not in ra[0]]
    return ra, sorted(bo_cot), thieu


def lenh_doc(args):
    thu_muc = args.duong
    bm = BangMa()
    du, tinh_trang = {}, []

    for khoa, meta in NGUON.items():
        hit = glob.glob(os.path.join(thu_muc, "*%s*.csv" % khoa))
        if not hit:
            tinh_trang.append({"nguon": meta["ten"], "trang_thai": "thieu",
                               "file": "", "cap_nhat": "", "thieu_cot": [], "n": 0})
            du[khoa] = []
            continue
        p = sorted(hit)[-1]
        rows, bo_cot, thieu = doc_mot(p, khoa, bm)
        moc = meta["moc"]
        ngays = sorted({r.get(moc, "") for r in rows if ngay(r.get(moc))})
        du[khoa] = rows
        # ⚠ "Do tuoi" = LUC FILE DUOC XUAT, ⛔ KHONG phai ngay lon nhat trong du lieu.
        #   Lay ngay lon nhat la sai THEO CAU TRUC: ca chot LUON co ngay muon hon
        #   cuoc goi vi no o cuoi phe u — nen moi nguon se luon trong nhu "cu" hon
        #   nguon sau no. tb-B §4 noi "cap nhat luc nao", do la METADATA cua file.
        mt = datetime.fromtimestamp(os.path.getmtime(p)).replace(
            second=0, microsecond=0)
        tinh_trang.append({
            "nguon": meta["ten"], "trang_thai": "du" if not thieu else "thieu-cot",
            "file": os.path.basename(p),
            "cap_nhat": mt.isoformat(sep=" ")[:16],
            "khoang": (ngays[0] + " → " + ngays[-1]) if ngays else "",
            "thieu_cot": thieu, "bo_cot": bo_cot, "n": len(rows),
        })

    bm.luu()

    # ── CONG N: mot nguon xuat TRE HON nguon moi nhat qua 24h thi xu nhu THIEU
    #   cho phan ngay bi hut (tb-B §4 luat ②). Day moi la "cu" dung nghia:
    #   file duoc xuat luc nao, ⛔ khong phai du lieu ket thuc ngay nao.
    moc = [t["cap_nhat"] for t in tinh_trang if t["cap_nhat"]]
    if moc:
        moi_nhat = max(moc)
        for t in tinh_trang:
            if t["trang_thai"] != "du" or not t["cap_nhat"]:
                continue
            a = datetime.fromisoformat(t["cap_nhat"])
            b = datetime.fromisoformat(moi_nhat)
            if (b - a).total_seconds() > 24 * 3600:
                t["trang_thai"] = "cu"
                t["cu_hon"] = "xuất %s · mới nhất %s" % (t["cap_nhat"], moi_nhat)

    co_khoa = all(any("ma_lead" in r for r in du[k][:1]) for k in NGUON if du[k])
    du_nguon = {t["nguon"]: t["trang_thai"] for t in tinh_trang}

    # ── khe nao tinh duoc (tb-B §6 o ⑤)
    can = {"K1": ["Data phân bổ", "Cuộc gọi"], "K2": ["Data phân bổ", "Cuộc gọi"],
           "K3": ["Cuộc gọi"], "K4": ["Cuộc gọi"],
           "K5": ["Cuộc gọi", "Lịch hẹn"], "K6": ["Lịch hẹn"],
           "K7": ["Lịch hẹn", "Ca chốt"], "K8": ["Data phân bổ"],
           "K9": ["Data phân bổ"]}
    tinh_duoc, khong = [], {}
    for k, ns in can.items():
        xau = [n for n in ns if du_nguon.get(n) in ("thieu", "cu", "thieu-cot")]
        if xau:
            khong[k] = xau
        else:
            tinh_duoc.append(k)

    data = {
        "schema": "tong-hop-telesale/1",
        "ky": args.ky, "tao_luc": datetime.now().astimezone().replace(
            microsecond=0).isoformat(),
        "tinh_trang_nguon": tinh_trang,
        "co_khoa_noi": co_khoa,
        "khe_tinh_duoc": tinh_duoc,
        "khe_khong_tinh_duoc": khong,
        "so_nv": len(bm.ten2ma),
        "du_lieu": du,
    }
    ghi_file("doc-nguon.json", json.dumps(data, ensure_ascii=False, indent=2), bm)

    # ── in CONG N
    print("\n── CỔNG N · TÌNH TRẠNG NGUỒN ──")
    bieu = {"du": "✅ đủ", "cu": "⚠️ CŨ", "thieu": "⛔ THIẾU", "thieu-cot": "⚠️ thiếu cột"}
    for t in tinh_trang:
        print("  %-16s %-14s %-26s %s dòng%s" % (
            t["nguon"], bieu.get(t["trang_thai"], t["trang_thai"]),
            t.get("khoang", "") or "—", t["n"],
            ("  ⛔ thiếu cột: " + ",".join(t["thieu_cot"])) if t["thieu_cot"] else ""))
        if t.get("bo_cot"):
            print("      ⛔ đã BỎ HẲN cột nhạy cảm: %s" % ", ".join(t["bo_cot"]))
    print("\n  Khoá nối (ma_lead) : %s" % ("✅ có → dựng được cohort" if co_khoa
                                           else "⛔ KHÔNG → chỉ đọc được HOẠT ĐỘNG"))
    print("  Khe tính được      : %s" % " ".join(tinh_duoc))
    if khong:
        for k, v in khong.items():
            print("  ⏸ %s — vì nguồn: %s" % (k, ", ".join(v)))
    print("\n  Đã đổi mã %d nhân viên → NV-xx. Bảng quy đổi: ma-nhan-vien.csv"
          % len(bm.ten2ma))
    print("  ⛔ File đó đã bị .gitignore chặn — ⛔ không commit, ⛔ không gửi.")


# ────────────────────────────────────────────────────────────────
# 3 · PHỄU  (tb-C)
# ────────────────────────────────────────────────────────────────

def hanh_trinh(du):
    """Dung mot ban ghi cho tung LEAD — xuong song cua cohort (tb-C §3)."""
    L = {}

    def o(ml):
        return L.setdefault(ml, {"ma_lead": ml, "nhan": None, "nguon": "", "nv": "",
                                 "goi": [], "goi_1": None, "ket_noi": None,
                                 "so_lan_goi": 0, "tao_hen": None, "ngay_hen": None,
                                 "gio_hen": "", "da_den": None, "chot": None,
                                 "tien": 0, "trang_thai": ""})

    for r in du.get("2-data-phan-bo", []):
        x = o(r.get("ma_lead", ""))
        x["nhan"] = ngay(r.get("ngay_nhan"))
        x["nguon"] = r.get("nguon_data", "")
        x["nv"] = r.get("ma_nv_duoc_giao", "")
        x["trang_thai"] = r.get("trang_thai", "")

    for r in du.get("1-cuoc-goi", []):
        if (r.get("huong") or "ra") != "ra":
            continue                                  # ⛔ goi VAO khong tinh chang ②
        x = o(r.get("ma_lead", ""))
        d = ngay(r.get("ngay_goi"))
        x["goi"].append((d, r.get("ket_qua", ""), r.get("gio_goi", "")))
        x["so_lan_goi"] += 1
        if d and (x["goi_1"] is None or d < x["goi_1"]):
            x["goi_1"] = d
        if r.get("ket_qua") == "ket_noi" and d and (x["ket_noi"] is None or d < x["ket_noi"]):
            x["ket_noi"] = d
        if not x["nv"]:
            x["nv"] = r.get("ma_nv", "")

    for r in du.get("3-lich-hen", []):
        x = o(r.get("ma_lead", ""))
        x["tao_hen"] = ngay(r.get("ngay_tao_hen"))
        x["ngay_hen"] = ngay(r.get("ngay_hen"))
        x["gio_hen"] = r.get("gio_hen", "")
        x["da_den"] = (r.get("da_den", "").lower() in ("co", "có", "1", "true", "yes"))

    for r in du.get("4-ca-chot", []):
        x = o(r.get("ma_lead", ""))
        x["chot"] = ngay(r.get("ngay_chot"))
        try:
            x["tien"] += float(r.get("so_tien") or 0)
        except ValueError:
            pass

    L.pop("", None)
    return L


def hoat_dong(L, d):
    """CÁCH ① — moi chang dem theo moc CUA CHINH NGUON DO.
    ⛔ CAC SO NAY KHONG CHIA CHO NHAU (tb-C §3)."""
    cuoc = sum(1 for x in L.values() for g in x["goi"] if g[0] == d)
    return {
        "ngay": d.isoformat(),
        "data_nhan": sum(1 for x in L.values() if x["nhan"] == d),
        "da_goi_lead": len({x["ma_lead"] for x in L.values()
                            if any(g[0] == d for g in x["goi"])}),
        "cuoc": cuoc,
        "ket_noi": len({x["ma_lead"] for x in L.values()
                        if any(g[0] == d and g[1] == "ket_noi" for g in x["goi"])}),
        "dat_hen": sum(1 for x in L.values() if x["tao_hen"] == d),
        "den_kham": sum(1 for x in L.values() if x["ngay_hen"] == d and x["da_den"]),
        "ca_chot": sum(1 for x in L.values() if x["chot"] == d),
    }


def cohort(L, d, nguong_dong=None):
    """CÁCH ② — khoa lo theo NGAY NHAN DATA. Mau so CO DINH (tb-C §3)."""
    lo = [x for x in L.values() if x["nhan"] == d]
    n = len(lo)
    if not n:
        return None
    dang_giua = sum(1 for x in lo
                    if (x["tao_hen"] and not x["chot"] and x["da_den"] is not False)
                    or (x["goi"] and not x["ket_noi"] and x["so_lan_goi"] < 5)
                    or (not x["goi"] and x["trang_thai"] != "chua_goi"))
    tuoi = (date.today() - d).days
    dong = (nguong_dong is not None and tuoi >= nguong_dong and dang_giua == 0)
    return {
        "ngay_nhan": d.isoformat(), "n": n, "tuoi_ngay": tuoi,
        "da_dong": dong, "dang_giua_phe_u": dang_giua,
        "da_goi": sum(1 for x in lo if x["goi"]),
        "ket_noi": sum(1 for x in lo if x["ket_noi"]),
        "dat_hen": sum(1 for x in lo if x["tao_hen"]),
        "den_kham": sum(1 for x in lo if x["da_den"]),
        "ca_chot": sum(1 for x in lo if x["chot"]),
        "tien": sum(x["tien"] for x in lo),
        "tre_goi_1_gio": trung_vi([(x["goi_1"] - x["nhan"]).days * 24
                                   for x in lo if x["goi_1"] and x["nhan"]]),
        "tre_hen_ngay": trung_vi([(x["tao_hen"] - x["ket_noi"]).days
                                  for x in lo if x["tao_hen"] and x["ket_noi"]]),
        "tre_den_ngay": trung_vi([(x["ngay_hen"] - x["tao_hen"]).days
                                  for x in lo if x["ngay_hen"] and x["tao_hen"]]),
    }


# ────────────────────────────────────────────────────────────────
# 4 · CHÍN KHE  (tb-E)
# ────────────────────────────────────────────────────────────────

def do_khe(L, cos, tinh_duoc):
    """Moi khe: so that · lead mat · cat ra · goc. ⛔ Khong ngưỡng — tb-D §4."""
    K, lo = {}, [x for x in L.values() if x["nhan"]]

    def cat(ten, lay, dk_tu, dk_mau):
        """Cat mot khe theo mot truc. ⛔ Nhom <30 lead -> khong so (tb-A §6)."""
        nh = {}
        for x in lo:
            k = lay(x)
            if not k:
                continue
            a = nh.setdefault(k, [0, 0])
            a[1] += 1 if dk_mau(x) else 0
            a[0] += 1 if dk_tu(x) else 0
        return {"truc": ten,
                "nhom": [{"ten": k, "so": ty_le(v[0], v[1]), "n": v[1],
                          "du_mau": v[1] >= 30}
                         for k, v in sorted(nh.items(), key=lambda z: -z[1][1])]}

    def dat(ma, tu, mau, mat, cats=None, ghi=""):
        K[ma] = {"ma": ma, "ten": TEN_KHE[ma],
                 "tinh_duoc": ma in tinh_duoc,
                 "so": ty_le(tu, mau) if ma in tinh_duoc else "⏸ chưa đo được",
                 "lead_mat": mat if ma in tinh_duoc else None,
                 "nguong": "⚠ chưa có ngưỡng",
                 "goc": GOC_KHE[ma], "cat": cats or [], "ghi_chu": ghi}

    # K1 · data de nguoi
    tre = [(x["goi_1"] - x["nhan"]).days * 24 for x in lo if x["goi_1"]]
    nguoi = sum(1 for x in lo if x["goi_1"] and (x["goi_1"] - x["nhan"]).days >= 2)
    dat("K1", nguoi, len([x for x in lo if x["goi_1"]]), nguoi,
        ghi="trung vị data→gọi 1: %s giờ" % (trung_vi(tre) if tre else "⏸"))

    # K2 · chua goi het
    chua = sum(1 for x in lo if not x["goi"])
    dat("K2", chua, len(lo), chua)

    # K3 · goi ma khong ket noi  — ★ HAI GOC, phai tach (tb-E §4)
    dg = [x for x in lo if x["goi"]]
    kn = sum(1 for x in dg if x["ket_noi"])
    dat("K3", len(dg) - kn, len(dg), len(dg) - kn, cats=[
        cat("nguồn data", lambda x: x["nguon"],
            lambda x: bool(x["goi"]) and not x["ket_noi"], lambda x: bool(x["goi"])),
        cat("người", lambda x: x["nv"],
            lambda x: bool(x["goi"]) and not x["ket_noi"], lambda x: bool(x["goi"])),
        cat("khung giờ gọi 1", lambda x: (x["goi"][0][2][:2] + "h") if x["goi"] else "",
            lambda x: bool(x["goi"]) and not x["ket_noi"], lambda x: bool(x["goi"])),
    ])

    # K4 · bo lead qua som
    bo_som = sum(1 for x in dg if not x["ket_noi"] and x["so_lan_goi"] <= 1)
    dat("K4", bo_som, len([x for x in dg if not x["ket_noi"]]), bo_som,
        ghi="trung vị số lần gọi trước khi dừng: %s"
            % (trung_vi([x["so_lan_goi"] for x in dg if not x["ket_noi"]]) or "⏸"))

    # K5 · ket noi ma khong dat duoc hen
    kns = [x for x in lo if x["ket_noi"]]
    h = sum(1 for x in kns if x["tao_hen"])
    dat("K5", len(kns) - h, len(kns), len(kns) - h)

    # K6 · no-show  — cat theo KHUNG GIO HEN
    hs = [x for x in lo if x["tao_hen"]]
    den = sum(1 for x in hs if x["da_den"])
    dat("K6", len(hs) - den, len(hs), len(hs) - den, cats=[
        cat("khung giờ hẹn", lambda x: x["gio_hen"][:2] + "h" if x["gio_hen"] else "",
            lambda x: bool(x["tao_hen"]) and not x["da_den"], lambda x: bool(x["tao_hen"])),
    ])

    # K7 · den kham ma khong chot — ⛔ KHONG phai khe cua khoi (tb-E §3)
    dks = [x for x in lo if x["da_den"]]
    c = sum(1 for x in dks if x["chot"])
    dat("K7", len(dks) - c, len(dks), len(dks) - c,
        ghi="⚠️ K7 là khe SAU khi khách đến cơ sở. Nó ⛔ KHÔNG thuộc trách nhiệm "
            "khối telesale và ⛔ không vào mục việc của khối. In ở đây để quản lý "
            "biết chất lượng hẹn mình đưa sang đang được chuyển hoá thế nào.")

    # K8 · tai viec lech
    per = {}
    for x in lo:
        if x["nv"]:
            per[x["nv"]] = per.get(x["nv"], 0) + 1
    if per:
        hi, low = max(per.values()), min(per.values())
        K["K8"] = {"ma": "K8", "ten": TEN_KHE["K8"], "tinh_duoc": "K8" in tinh_duoc,
                   "so": "cao nhất %d lead · thấp nhất %d lead · lệch %.1f lần"
                         % (hi, low, (hi / low) if low else 0),
                   "lead_mat": None, "nguong": "⚠ chưa có ngưỡng", "goc": "he",
                   "cat": [{"truc": "người", "nhom": [
                       {"ten": k, "so": "%d lead" % v, "n": v, "du_mau": v >= 30}
                       for k, v in sorted(per.items(), key=lambda z: -z[1])]}],
                   "ghi_chu": ""}
    else:
        dat("K8", 0, 0, 0)

    # K9 · data ton don
    ton = [x for x in lo if x["trang_thai"] == "chua_goi" or
           (not x["chot"] and x["nhan"] and (date.today() - x["nhan"]).days >= 7)]
    dat("K9", len(ton), len(lo), len(ton),
        ghi="⚠ 'n ngày' coi là tồn: ⛔ chưa có — slot ⑤ của tb-H")
    return K


# ────────────────────────────────────────────────────────────────
# 5 · CỔNG R  (tb-G §5) — chay BANG MAY
# ────────────────────────────────────────────────────────────────

# ⚠ Bat SDT bang CACH DEM CHU SO, ⛔ khong bang mot khuon do dai co dinh.
#   Ban dau dung r"...\d{3}[\s.\-]?\d{3,4}" va no BO SOT "0912345678" — mot lo
#   that trong mot cong rieng tu. Mot cong bo sot mot kieu viet la mot cong
#   KHONG DUNG DUOC, vi nguoi gui ⛔ khong biet no da bo sot.
RE_SO_DAI = re.compile(r"(?<![\d])(?:\+?84|0)[\d\s.\-]{7,14}(?![\d])")
RE_MAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")


def tim_sdt(s):
    """Tra ve chuoi SDT dau tien tim thay, hoac None.

    Luat: mot cum bat dau bang 0 hoac +84, va sau khi bo dau cach/cham/gach
    thi con 9-11 chu so. Bat duoc ca "0912345678", "091 234 5678",
    "091.234.5678", "+84912345678".
    """
    for m in RE_SO_DAI.finditer(s or ""):
        so = re.sub(r"\D", "", m.group(0))
        if so.startswith("84"):
            so = "0" + so[2:]
        if 9 <= len(so) <= 11 and so[0] == "0" and so[1] in "35789":
            return m.group(0).strip()
    return None


def kiem_rieng_tu(noi_dung, bm, la_bao_cao=True):
    """Sau cau kiem cua CONG R. Tra ve list loi — rong la qua."""
    loi = []
    for t in (bm.ten_that() if bm else []):
        if t and t in noi_dung:
            loi.append("tên thật nhân viên lọt vào: %r" % t)
    sdt = tim_sdt(noi_dung)
    if sdt:
        loi.append("số điện thoại: %s" % sdt)
    m = RE_MAIL.search(noi_dung)
    if m:
        loi.append("email: %s" % m.group(0))
    for c in BO_HAN:
        if re.search(r'"%s"\s*:' % re.escape(c), noi_dung):
            loi.append("cột nhạy cảm còn trong file: %s" % c)
    if la_bao_cao and ("NV-" in noi_dung) and (CAU_CHAN not in noi_dung):
        loi.append("có lát cắt người mà thiếu câu chân bảng (tb-G §4 rào ①)")
    return loi


def ghi_file(ten, noi_dung, bm=None):
    """⛔ MOI lan ghi file di qua day. Tu choi ghi neu truot CONG R."""
    loi = kiem_rieng_tu(noi_dung, bm, la_bao_cao=ten.endswith(".md"))
    if loi:
        print("\n⛔ CỔNG R CHẶN — ⛔ KHÔNG ghi %s" % ten)
        for x in loi[:20]:
            print("   · " + x)
        print("\n→ Sửa rồi chạy lại. Xem tb-G §5.")
        sys.exit(2)
    if not os.path.isdir(OUT):
        os.makedirs(OUT)
    p = os.path.join(OUT, ten)
    with io.open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(noi_dung)
    print("→ %s" % os.path.relpath(p, GOC))
    return p


# ────────────────────────────────────────────────────────────────
# 6 · BA DÒNG BẮT BUỘC  (tb-F §1)
# ────────────────────────────────────────────────────────────────

def ba_dong(d, co, ky):
    tt = d["tinh_trang_nguon"]
    bieu = {"du": "✅", "cu": "⚠️ CŨ", "thieu": "⛔ THIẾU", "thieu-cot": "⚠️ thiếu cột"}
    ng = " · ".join("%s %s xuất %s" % (t["nguon"], bieu.get(t["trang_thai"], ""),
                                       t["cap_nhat"] or "—") for t in tt)
    khong = d.get("khe_khong_tinh_duoc") or {}
    mau = "⏸ chưa dựng được cohort (thiếu khoá nối)"
    if co:
        mau = "cohort %s · n=%d · %s" % (
            co["ngay_nhan"], co["n"],
            "ĐÃ ĐÓNG" if co["da_dong"] else
            "⏳ CHƯA ĐÓNG — còn %d lead giữa phễu" % co["dang_giua_phe_u"])
    return "\n".join([
        "> **① ĐỊNH NGHĨA** · doanh số `⚠ chưa chốt — slot ① của tb-H`"
        " · mốc `⚠ chưa chốt` · phạm vi `⚠ chưa chốt`",
        "> **② MẪU & KỲ** · %s · kỳ %s" % (mau, ky),
        "> **③ NGUỒN** · %s" % ng,
        ">" if not khong else "> → ⛔ **KHÔNG tính được:** %s" % " · ".join(
            "%s (%s)" % (k, ", ".join(v)) for k, v in khong.items()),
    ])


# ────────────────────────────────────────────────────────────────
# 7 · LỆNH BÁO CÁO
# ────────────────────────────────────────────────────────────────

def _nap_tat():
    d = nap("doc-nguon.json")
    if not d:
        print("⛔ Chưa có out/doc-nguon.json. Chạy `doc` trước.")
        sys.exit(1)
    return d, hanh_trinh(d["du_lieu"]), BangMa()


def khe_md(K, ma):
    k = K.get(ma)
    if not k:
        return ""
    o = ["### `%s` · %s" % (k["ma"], k["ten"]),
         "",
         "- **① số thật:** %s" % k["so"],
         "- **② lead mất:** %s" % ("%d" % k["lead_mat"] if k["lead_mat"] is not None else "—"),
         "- **③ ngưỡng:** %s" % k["nguong"],
         "- **⑤ gốc:** %s" % {"he": "⛔ **LỖI HỆ** — vào mục việc hệ thống",
                              "nguoi": "việc của khối",
                              "?": "⚠️ **chưa phân được** — phải tách (tb-E §4)",
                              "ngoai-khoi": "⚠️ **⛔ không phải khe của khối**"}[k["goc"]],
         "- **⑥ người nhận:** `⏸ chưa có — slot ⑧ của tb-H`"]
    if k.get("ghi_chu"):
        o.append("- *%s*" % k["ghi_chu"])
    for c in k.get("cat", []):
        dong = [x for x in c["nhom"] if x["du_mau"]][:6]
        nho = len([x for x in c["nhom"] if not x["du_mau"]])
        o += ["", "- **④ cắt theo %s:**" % c["truc"]]
        for x in dong:
            o.append("  - `%s` %s" % (x["ten"], x["so"]))
        if nho:
            o.append("  - *%d nhóm dưới 30 lead → `⚠ chưa đủ mẫu`, ⛔ không so*" % nho)
    return "\n".join(o) + "\n"


def lenh_ngay(args):
    d, L, bm = _nap_tat()
    dd = ngay(args.ngay)
    h = hoat_dong(L, dd)
    su_co = []
    if h["data_nhan"] == 0:
        su_co.append("⛔ **data về 0** trong ngày")
    if h["cuoc"] == 0:
        su_co.append("⛔ **không có cuộc gọi nào** trong ngày")
    per = {}
    for x in L.values():
        for g in x["goi"]:
            if g[0] == dd and x["nv"]:
                per[x["nv"]] = per.get(x["nv"], 0) + 1
    im = [n for n in {x["nv"] for x in L.values() if x["nv"]} if n not in per]
    if im:
        su_co.append("⛔ **%d người ⛔ không gọi cuộc nào:** %s" % (len(im), ", ".join(sorted(im))))

    md = ["# Báo cáo NGÀY · %s · Khối Telesale Kangnam" % dd.isoformat(), "",
          ba_dong(d, None, dd.isoformat()), "",
          "## ① Hoạt động trong ngày", "",
          "> ⛔ **Các số dưới đây ⛔ KHÔNG chia cho nhau** — mỗi dòng đếm theo mốc của"
          " chính nguồn đó (`tb-C` §3 cách ①).", "",
          "| Chặng | Số |", "|---|---|",
          "| ① data nhận | %d lead |" % h["data_nhan"],
          "| ② đã gọi | %d lead (%d cuộc) |" % (h["da_goi_lead"], h["cuoc"]),
          "| ③ kết nối | %d lead |" % h["ket_noi"],
          "| ④ đặt hẹn | %d |" % h["dat_hen"],
          "| ⑤ đến khám | %d |" % h["den_kham"],
          "| ⑥ ca chốt | %d |" % h["ca_chot"], ""]
    if su_co:
        md += ["## ② ⛔ SỰ CỐ — cần xử trong hôm nay", ""] + \
              ["- %s → `⏸ người nhận chưa có`" % s for s in su_co] + [""]
    md += ["## ③ So ngưỡng", "",
           "| Chỉ số | Số thật | Ngưỡng |", "|---|---|---|",
           "| gọi hết data trong ngày | %s | ⚠ chưa có ngưỡng |"
           % ty_le(h["da_goi_lead"], h["data_nhan"] or h["da_goi_lead"]), "",
           "> ⛔ **Báo cáo NGÀY ⛔ không kết luận xu hướng và ⛔ không in tỷ lệ chuyển đổi.**"
           " Một ngày là mẫu nhỏ và nhiễu (`tb-A` §3). Tỷ lệ chuyển đổi chỉ đọc được từ"
           " **cohort** — xem báo cáo TUẦN.", ""]
    ghi_file("bao-cao-ngay-%s.md" % dd.isoformat(), "\n".join(md), bm)


def _cohorts(L, nguong=None):
    ds = sorted({x["nhan"] for x in L.values() if x["nhan"]})
    return [c for c in (cohort(L, x, nguong) for x in ds) if c]


def lenh_tuan(args):
    d, L, bm = _nap_tat()
    cos = _cohorts(L)
    K = do_khe(L, cos, d["khe_tinh_duoc"])
    co = cos[-1] if cos else None
    xep = sorted([k for k in K.values() if k["lead_mat"]],
                 key=lambda k: -k["lead_mat"])[:3]

    md = ["# Báo cáo TUẦN · %s · Khối Telesale Kangnam" % args.ky, "",
          ba_dong(d, co, args.ky), ""]
    if not d["co_khoa_noi"]:
        md += ["> ⚠️ **Kỳ này CHƯA NỐI ĐƯỢC bốn nguồn** (thiếu khoá lead dùng chung)."
               " Mọi số dưới đây là **SỐ VIỆC TRONG NGÀY**, ⛔ **KHÔNG phải tỷ lệ chuyển"
               " đổi**. ⛔ Không chia các dòng cho nhau. → Việc chặn: cấp mã lead dùng"
               " chung — `⏸ ai cấp: slot ② của tb-H`.", ""]

    md += ["## ① Phễu cohort", "",
           "| Cohort | n | đã gọi | kết nối | đặt hẹn | đến khám | ca chốt | tình trạng |",
           "|---|---|---|---|---|---|---|---|"]
    for c in cos[-6:]:
        md.append("| %s | %d | %s | %s | %s | %s | %s | %s |" % (
            c["ngay_nhan"], c["n"], ty_le(c["da_goi"], c["n"]),
            ty_le(c["ket_noi"], c["n"]), ty_le(c["dat_hen"], c["n"]),
            ty_le(c["den_kham"], c["n"]), ty_le(c["ca_chot"], c["n"]),
            "⏳ chưa đóng · %d giữa phễu" % c["dang_giua_phe_u"]))
    md += ["", "> ⚠️ **Ngưỡng đóng cohort ⛔ chưa có** — slot ③ của `tb-H`. Nên **mọi**"
           " cohort ở đây đều mang nhãn ⏳, và ⛔ **không so cohort nào với cohort nào**"
           " (`tb-C` §3 luật cửa sổ chín).", "",
           "## ② Độ trễ (trung vị)", "",
           "| Độ trễ | Số | Chỉ số của khâu |", "|---|---|---|"]
    for ten, khoa, khau in [("data → gọi 1", "tre_goi_1_gio", "phân bổ"),
                            ("kết nối → hẹn", "tre_hen_ngay", "tư vấn"),
                            ("hẹn → đến khám", "tre_den_ngay", "nhắc hẹn")]:
        vs = [c[khoa] for c in cos if c[khoa] is not None]
        md.append("| %s | %s | %s |" % (
            ten, ("%s %s" % (trung_vi(vs), "giờ" if "gio" in khoa else "ngày"))
            if vs else "⏸ chưa đo được", khau))
    md += ["", "## ③ Ba khe mất nhiều lead nhất", "",
           "> Xếp theo **số lead mất**, ⛔ không theo tỷ lệ xấu nhất (`tb-E` §6).", ""]
    for k in xep:
        md.append(khe_md(K, k["ma"]))
    md += ["## ④ Việc của khối", "",
           "| Khe | Việc | Ai nhận | Hạn | Kỳ sau nhìn gì |", "|---|---|---|---|---|"]
    for k in K.values():
        if k["goc"] == "nguoi" and k["lead_mat"]:
            md.append("| `%s` | %s | `⏸ slot ⑧` | `⏸` | `%s` |"
                      % (k["ma"], k["ten"], k["ma"]))
    md += ["", "## ⑤ ⛔ VIỆC HỆ THỐNG — mục riêng, ⛔ không gộp vào ④", "",
           "| Khe | Thiếu gì | Ai cấp | Cấp rồi gỡ được gì |", "|---|---|---|---|"]
    for k in K.values():
        if k["goc"] == "he":
            md.append("| `%s` · %s | `⏸ chưa khai` | `⏸ slot của tb-H` | gỡ khe `%s` |"
                      % (k["ma"], k["ten"], k["ma"]))
    md += ["", "## ⑥ Lát cắt theo người", "",
           "| Mã | Lead | Khe yếu nhất |", "|---|---|---|"]
    per = {}
    for x in L.values():
        if x["nv"]:
            per[x["nv"]] = per.get(x["nv"], 0) + 1
    for nv, n in sorted(per.items(), key=lambda z: -z[1]):
        md.append("| `%s` | %d | %s |" % (nv, n,
                  "`⚠ chưa đủ mẫu` (<10 cuộc)" if n < 10 else "`⏸ cần ngưỡng`"))
    md += ["", "> %s" % CAU_CHAN, "",
           "## ⑦ ⏸ Chưa đo được", ""]
    for k in K.values():
        if not k["tinh_duoc"]:
            md.append("- `%s` %s — thiếu nguồn: %s" % (
                k["ma"], k["ten"],
                ", ".join(d["khe_khong_tinh_duoc"].get(k["ma"], []))))
    md += ["", "## ⑧ `K7` — mục riêng", "", khe_md(K, "K7")]
    ghi_file("bao-cao-tuan-%s.md" % re.sub(r"[^0-9A-Za-z]+", "-", args.ky).strip("-"),
             "\n".join(md), bm)


def lenh_thang(args):
    d, L, bm = _nap_tat()
    cos = _cohorts(L)
    md = ["# Báo cáo THÁNG · %s · Khối Telesale Kangnam" % args.thang, "",
          ba_dong(d, cos[-1] if cos else None, args.thang), "",
          "## ① ⚠️ HAI ĐIỀU CHỈNH — đọc trước mọi so sánh", "",
          "| Điều chỉnh | Tình trạng |", "|---|---|",
          "| số ngày làm việc tháng này / tháng trước | `⏸ chưa khai` — ⛔ **không so thẳng** |",
          "| cơ cấu nhân sự (vào / nghỉ trong tháng) | `⏸ chưa khai` — ⛔ **không kết luận"
          " xu hướng khi chưa tách cũ/mới** |", "",
          "> ⚠️ *\"Tháng này giảm 12%\"* có khi chỉ là *\"tháng này ít hơn 2 ngày làm"
          " việc\"*. Và *\"mọi chỉ số tiến trình đều tụt\"* có khi chỉ là *\"vừa tuyển 3"
          " người\"* (`tb-F` §4).", "",
          "## ② Phễu theo tháng — ⛔ chỉ cohort ĐÃ ĐÓNG", "",
          "> ⛔ **Ngưỡng đóng cohort chưa có** (slot ③ của `tb-H`) → ⛔ **không cohort"
          " nào được coi là đã đóng**, nên mục này ⏸ **chưa dựng được**.", "",
          "- Tổng cohort trong dữ liệu: **%d**, tất cả mang nhãn ⏳ chưa đóng" % len(cos),
          "", "## ③ Tách cũ / mới", "",
          "> `⏸ chưa dựng được` — thiếu **mốc \"nhân viên mới\"** (slot ⑦ của `tb-H`)."
          " ⛔ Không gộp người cũ và người mới vào một tỷ lệ chung (`ts-F` §4).", "",
          "## ④ Hiệu quả đào tạo", "",
          "> `⏸ chưa dựng được` — cần đầu ra của `Agent-QC-Telesale` cho **cùng người ·"
          " cùng nhóm dịch vụ · cùng tiêu chí**, trước và sau đào tạo.", ""]
    ghi_file("bao-cao-thang-%s.md" % args.thang, "\n".join(md), bm)


def lenh_van_de(args):
    d, L, bm = _nap_tat()
    cos = _cohorts(L)
    K = do_khe(L, cos, d["khe_tinh_duoc"])
    xep = sorted([k for k in K.values() if k["lead_mat"]], key=lambda k: -k["lead_mat"])
    md = ["# ⛔ VẤN ĐỀ · %s · Khối Telesale Kangnam" % args.ky, "",
          ba_dong(d, cos[-1] if cos else None, args.ky), "",
          "## 🔴 Ba khe mất nhiều lead nhất", ""]
    for k in xep[:3]:
        md.append(khe_md(K, k["ma"]))
    md += ["## 🟠 Việc của khối", ""]
    n = 0
    for k in K.values():
        if k["goc"] == "nguoi" and k["lead_mat"]:
            md.append("- `%s` %s — mất **%d lead** · `⏸ ai nhận: slot ⑧` · `⏸ hạn`"
                      % (k["ma"], k["ten"], k["lead_mat"]))
            n += 1
    if not n:
        md.append("*⛔ Không có khe nào đã phân được gốc là việc của khối.*")
    md += ["", "## ⛔ Việc hệ thống", ""]
    for k in K.values():
        if k["goc"] == "he":
            md.append("- `%s` %s — `⏸ ai cấp` · cấp rồi **gỡ được khe %s**"
                      % (k["ma"], k["ten"], k["ma"]))
    md += ["", "## ⚠️ Khe chưa phân được gốc — ⛔ chưa giao cho ai", ""]
    for k in K.values():
        if k["goc"] == "?":
            md.append("- `%s` %s — phải **tách ba lát cắt** trước khi giao việc"
                      " (`tb-E` §4). Xem mục ④ của khe này ở báo cáo TUẦN."
                      % (k["ma"], k["ten"]))
    md += ["", "## ⏸ Chưa đo được", ""]
    for k in K.values():
        if not k["tinh_duoc"]:
            md.append("- `%s` %s — thiếu nguồn: %s" % (
                k["ma"], k["ten"], ", ".join(d["khe_khong_tinh_duoc"].get(k["ma"], []))))
    md += ["", "## ℹ️ `K7` — ⛔ không phải khe của khối", "", khe_md(K, "K7")]
    # CONG R bat dung: ban nay CO in ma NV-xx (lat cat cua khe K8) nen PHAI co
    # cau chan bang — tb-G §4 rao ①. ⛔ Khong bo cau nay de "cho gon".
    md += ["---", "", "> %s" % CAU_CHAN, ""]
    ghi_file("van-de-%s.md" % re.sub(r"[^0-9A-Za-z]+", "-", args.ky).strip("-"),
             "\n".join(md), bm)


def lenh_kiem(args):
    with io.open(args.duong, encoding="utf-8") as f:
        nd = f.read()
    loi = kiem_rieng_tu(nd, BangMa(), la_bao_cao=args.duong.endswith(".md"))
    print("CỔNG R · %s" % os.path.basename(args.duong))
    if not loi:
        print("✅ Qua 6 câu kiểm riêng tư.")
        return
    print("⛔ %d lỗi:" % len(loi))
    for x in loi:
        print("   · " + x)
    sys.exit(2)


# ────────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser(description="Tổng hợp báo cáo khối Telesale")
    sub = ap.add_subparsers(dest="lenh")

    p = sub.add_parser("doc", help="đọc bốn nguồn · đổi mã NV ngay ở bước đọc")
    p.add_argument("duong")
    p.add_argument("--ky", required=True)
    p.set_defaults(fn=lenh_doc)

    p = sub.add_parser("ngay", help="báo cáo NGÀY — điều hành")
    p.add_argument("--ngay", required=True)
    p.set_defaults(fn=lenh_ngay)

    p = sub.add_parser("tuan", help="báo cáo TUẦN — chẩn đoán khe rò")
    p.add_argument("--ky", required=True)
    p.set_defaults(fn=lenh_tuan)

    p = sub.add_parser("thang", help="báo cáo THÁNG — xu hướng")
    p.add_argument("--thang", required=True)
    p.set_defaults(fn=lenh_thang)

    p = sub.add_parser("van-de", help="⛔ chỉ khe rò, ⛔ không số nền")
    p.add_argument("--ky", required=True)
    p.set_defaults(fn=lenh_van_de)

    p = sub.add_parser("kiem", help="chạy CỔNG R tay trên một file")
    p.add_argument("duong")
    p.set_defaults(fn=lenh_kiem)

    a = ap.parse_args()
    if not getattr(a, "fn", None):
        ap.print_help()
        sys.exit(1)
    a.fn(a)


if __name__ == "__main__":
    main()
