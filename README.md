# Agent · Tổng hợp báo cáo · Khối Telesale Kangnam

> Khối Telesale mỗi ngày sinh ra **nhiều báo cáo rời**. Agent này **gộp chúng thành một bản duy nhất** cho quản lý đọc, và chỉ ra **khối đang tắc ở khe nào**.

`v1.0` · 03/11/2026 · khối **Telesale** · Kangnam Korean Aesthetic Hospital

---

## ★ Bốn nguồn → một phễu → bốn báo cáo

```
  ① Cuộc gọi · tổng đài   ┐
  ② Data / lead phân bổ   ├──►  MỘT PHỄU MỘT MẠCH  ──►  ① NGÀY   · điều hành
  ③ Lịch hẹn & đến khám   │          (tb-C)             ② TUẦN   · chẩn đoán
  ④ Ca chốt & doanh số    ┘                             ③ THÁNG  · xu hướng
                                                        ④ ⛔ VẤN ĐỀ · cái đang tắc
```

★ **Agent này là người GỘP, ⛔ không phải người ĐO.** Nó nhận số của người khác và chịu trách nhiệm cho **một việc**: làm cho những con số đó **đứng được cạnh nhau** mà ⛔ không nói dối.

| Việc | ⛔ Không phải của agent này | Của ai |
|---|---|---|
| Chấm chất lượng cuộc gọi — nghe, bóc tách, `K1`–`K6` | | `Agent-QC-Telesale` |
| **Định nghĩa doanh số** — ghi nhận/thực thu · mốc · phạm vi | | `Agent-Order-SoLieu` *(`so-B` 7 câu chốt)* |
| Chẩn đoán số quảng cáo, phân bổ ngân sách | | `Agent-AdsReport-Kangnam` |
| Dựng chiến dịch tái khai thác data tồn | | `Agent-CRM-Automation` |
| Gọi khách · sửa CRM · ra quyết định nhân sự | | ⛔ Không agent nào |

---

## ★★ Ba kỳ — ba việc khác nhau, ⛔ không phải một báo cáo ba cỡ

| Kỳ | Trả lời | ⛔ Không được làm |
|---|---|---|
| **NGÀY** | *Hôm nay cái gì đang cháy, ai cần giúp ngay?* | ⛔ **Không kết luận xu hướng** · ⛔ không tỷ lệ chuyển đổi · ⛔ không xếp hạng |
| **TUẦN** | *Khe nào rò, vì sao, tuần tới ai làm gì?* | ⛔ Không kết luận về người dưới ngưỡng mẫu |
| **THÁNG** | *Đi lên hay xuống, cơ cấu đổi thế nào?* | ⛔ Không so tháng mà chưa chỉnh **ngày làm việc** và **cơ cấu nhân sự** |

⛔ **Báo cáo NGÀY so với NGƯỠNG, ⛔ không so với hôm qua.** Một ngày của khối telesale là mẫu nhỏ và nhiễu: một người nghỉ phép làm số cuộc tụt 15%; data về muộn làm tỷ lệ tụt rồi hôm sau vọt. *"Giảm 20% so với hôm qua"* gần như **luôn** là nhiễu — nói câu đó mỗi ngày thì ba tháng sau ⛔ không ai đọc báo cáo nữa.

★ **Ngoại lệ duy nhất:** một **sự cố** *(data về 0 · tổng đài lỗi · một nhóm ⛔ không gọi cuộc nào)* thì báo ngay. Đó là **sự cố**, ⛔ không phải xu hướng.

---

## ★★ Luật cohort — luật sâu nhất của repo

Một lead đi qua phễu **mất nhiều ngày**: data về thứ 2 → gọi thứ 3 → kết nối thứ 4 → hẹn thứ 5 → đến khám thứ 7 → chốt tuần sau.

```
⛔ SAI :  tỷ lệ chốt hôm nay = ca chốt hôm nay ÷ data nhận hôm nay
```

Con số đó sai **theo hai chiều cùng lúc**: data về nhiều hôm nay thì tỷ lệ tụt *(dù ⛔ chưa ai làm gì sai)*; về ít thì vọt *(dù ⛔ chưa ai làm gì tốt)*. Và nó **luôn khớp tổng**, nên ⛔ không ai phát hiện ra.

| Cách đọc | Trả lời câu gì | Dùng cho |
|---|---|---|
| **① HOẠT ĐỘNG** — mỗi chặng theo mốc của **chính nguồn đó**, ⛔ không chia cho nhau | *Hôm nay khối làm được bao nhiêu việc?* | NGÀY · sự cố · tải việc |
| ★ **② COHORT** — khoá lô theo **ngày nhận data**, theo lô đó đi suốt phễu | *Lô data về ngày X cuối cùng ra được bao nhiêu?* | ★ **Chỉ cách này tính được tỷ lệ chuyển đổi** |

⚠️ **Mọi câu hỏi có chữ *"tỷ lệ"* phải trả lời bằng cách ②.** ⛔ Không ngoại lệ.
★ **Luật cửa sổ chín:** cohort còn lead giữa phễu là **chưa đóng** → luôn in nhãn `⏳ CHƯA ĐÓNG + còn n lead`; ⛔ **không so cohort chưa đóng với cohort đã đóng** — đó là so một việc **đang làm** với một việc **đã xong**.

Luật đầy đủ: [`knowledge/tb-C-phe-u-luat-cohort.md`](knowledge/tb-C-phe-u-luat-cohort.md)

---

## Chín khe rò — "vấn đề team đang gặp"

| Mã | Khe | Thường là |
|---|---|---|
| `K1` | Data để nguội *(trung vị `data → gọi 1`)* | ⛔ **Lỗi hệ** · phân bổ |
| `K2` | Data chưa gọi hết | Tuỳ — xem tải việc `K8` |
| `K3` | Gọi mà ⛔ không kết nối | ★ **Hai gốc** — phải tách |
| `K4` | Bỏ lead quá sớm | Việc của khối |
| `K5` | Kết nối mà ⛔ không đặt được hẹn | Việc của khối · đào tạo |
| `K6` | Đặt hẹn mà ⛔ không đến *(no-show)* | ⛔ **Lỗi hệ** · nhắc hẹn |
| `K7` | Đến khám mà ⛔ không chốt | ⚠️ **⛔ Không phải khe của khối** |
| `K8` | Tải việc lệch | ⛔ **Lỗi hệ** · phân bổ |
| `K9` | Data tồn dồn | ⛔ **Lỗi hệ** nếu vào > năng lực |

### ★★ CỔNG V — phép thử một câu, chạy cho **từng** khe

```
"Người giỏi nhất khối, với đúng những gì hệ thống đang cấp hôm nay,
 có làm khác được không?"

  ⛔ KHÔNG → LỖI HỆ. Vào mục VIỆC HỆ THỐNG, có tên người cấp.
             ⛔ Không vào mục việc của khối, ⛔ không vào nội dung đào tạo.
  ✅ CÓ    → việc của khối, có người nhận + hạn.
```

⚠️ **Năm trong chín khe thường là lỗi hệ.** Nếu một kỳ **cả chín khe** đều vào mục việc của khối thì gần như chắc chắn **CỔNG V ⛔ chưa chạy** — và khối đang bị đào tạo về những việc ⛔ không phải của họ.

★ **Xếp khe theo SỐ LEAD MẤT**, ⛔ không theo tỷ lệ xấu nhất: khe `20%` với 15 lead mất **12** lead; khe `75%` với 800 lead mất **200**. Khe thứ hai sửa trước.

---

## Bốn cổng chặn

| Cổng | Chặn gì |
|---|---|
| **CỔNG N** | ⛔ Không tính tỷ lệ đi qua hai nguồn khi một nguồn **thiếu hoặc cũ**. ⚠️ Nguồn **cũ** nguy hơn nguồn **thiếu**: số vẫn ra, mẫu số hụt → **tỷ lệ đẹp giả** |
| **CỔNG Đ** | ⛔ Không in doanh số khi **bảy câu của `so-B` chưa chốt** |
| **CỔNG V** | ⛔ Không đưa khe vào mục việc của khối khi **chưa phân lỗi hệ / lỗi người** |
| **CỔNG R** | ⛔ Không xuất file khi còn **tên thật nhân viên** hoặc **dữ kiện khách** — chạy **bằng máy**, `tb.py` **từ chối ghi file** |

---

## ★★ Riêng tư — ⛔ không có ngoại lệ

Kế thừa `Agent-QC-Telesale/knowledge/ts-G`, module mà chính nó khai là *"module duy nhất không có ngoại lệ"*.

```
┌─────────────────────────────┐        ┌──────────────────────────────┐
│  BÁO CÁO  (lưu hành)        │        │  BẢNG QUY ĐỔI  (quản lý giữ) │
│  out/bao-cao-*.md           │        │  ma-nhan-vien.csv            │
├─────────────────────────────┤        ├──────────────────────────────┤
│  NV-03 · 42 lead · K5 yếu   │  ◄──►  │  NV-03 = <tên thật>          │
└─────────────────────────────┘        └──────────────────────────────┘
      ⛔ KHÔNG có tên                      ⛔ KHÔNG commit, ⛔ không gửi
      ✅ Gửi được, lưu được                ✅ Chỉ quản lý mở
```

★ **Trưởng nhóm vẫn kèm được đúng người** — họ giữ khoá. Nhưng **file lưu hành ⛔ không mang tên**, nên một lần chia sẻ nhầm ⛔ không thành sự cố dữ liệu lao động.

⚠️ `ma-nhan-vien.csv` **đã bị `.gitignore` chặn**. ⛔ Không gỡ. ⛔ Không để nó vào `out/`, ⛔ không dán vào chat, ⛔ không để thành một tab trong cùng Sheet với báo cáo.

★ **Đổi mã NGAY ở bước đọc, ⛔ không ở bước xuất** — đổi ở bước xuất thì tên thật còn lại trong **mọi file trung gian**, và một trong số đó sẽ bị gửi đi.

⛔ **LỌC VÀ GỘP — KHÔNG RA QUYẾT ĐỊNH.** Agent đưa số, bằng chứng và phương án. **Người thật ký.** ⛔ Không đề xuất kỷ luật, cắt thưởng, xếp hạng, cho nghỉ.

---

## Bốn lệnh

```bash
python tools/tb.py doc     du-lieu/ --ky "27/10-02/11"   # CỔNG N + CỔNG Đ + đổi mã
python tools/tb.py ngay    --ngay 2026-11-03
python tools/tb.py tuan    --ky "27/10-02/11"
python tools/tb.py thang   --thang 2026-10
python tools/tb.py van-de  --ky "27/10-02/11"            # ★ lệnh dùng nhiều nhất
python tools/tb.py kiem    out/bao-cao-tuan-....md       # CỔNG R
```

⛔ **Không có lệnh nào chạy ba kỳ một lúc** — ba kỳ ba việc khác nhau.
★ `VẤN ĐỀ` chạy **độc lập** cho cả ba kỳ: bỏ hết số nền, chỉ còn **cái đang tắc + ai sửa**.

### Chạy thử ngay khi chưa có dữ liệu thật

```bash
mkdir du-lieu && cp template/MAU_*.csv du-lieu/
python tools/tb.py doc du-lieu/ --ky "26/10-02/11"
```

Bốn file mẫu **khớp nhau theo hành trình lead nhiều ngày** và cài sẵn: lead gọi 6 lần mới nói được · lead bỏ sau 1 lần · hẹn rồi ⛔ không đến · data để nguội 3 ngày · một nguồn data có tỷ lệ kết nối thấp hẳn *(khe `K3` gốc **hệ**)* · tải việc lệch 3 lần · một người dưới ngưỡng mẫu · cohort cuối kỳ chưa đóng.

---

## 8 sổ tri thức

| Sổ | Nội dung |
|---|---|
| [`tb-A`](knowledge/tb-A-vai-tro-ba-ky.md) | ★ Vai trò · **ba kỳ ba việc** · bốn cổng · ngưỡng mẫu |
| [`tb-B`](knowledge/tb-B-bon-nguon-dau-vao.md) | Bốn nguồn · cột bắt buộc · ★ **độ tươi** · dạng dán tay |
| [`tb-C`](knowledge/tb-C-phe-u-luat-cohort.md) | ★★ Phễu bảy chặng · **luật cohort** · ba độ trễ |
| [`tb-D`](knowledge/tb-D-tu-dien-chi-so.md) | Ai sở hữu chỉ số nào · **ba đơn vị đếm** · ⛔ không tự đặt ngưỡng |
| [`tb-E`](knowledge/tb-E-khe-ro-van-de-team.md) | ★★ **Chín khe rò** · CỔNG V · xếp theo lead mất |
| [`tb-F`](knowledge/tb-F-khuon-bao-cao.md) | Khuôn ba báo cáo · **ba dòng bắt buộc** · sáu luật viết |
| [`tb-G`](knowledge/tb-G-rieng-tu-rao-an-toan.md) | ★★ **Riêng tư** · mã `NV-xx` · bốn rào · CỔNG R |
| [`tb-H`](knowledge/tb-H-module-khoi-telesale.md) | Module khối · ★ **10 slot khối phải cấp** |

★ **Dựng agent này cho một khối telesale khác = thay `tb-H`**, ⛔ không sửa bảy sổ còn lại.

| Thẻ bộ não | Ký tự | Dùng cho |
|---|---|---|
| [`SYSTEM-PROMPT.md`](SYSTEM-PROMPT.md) | 11.584 | Claude Project · Gemini Gem |
| [`SYSTEM-PROMPT-NGAN.md`](SYSTEM-PROMPT-NGAN.md) | 7.954 | ChatGPT *(ô Instructions giới hạn 8.000)* |

---

## ⚠️ Va chạm mã — đã biết, ⛔ không đổi tên

> `Agent-QC-Telesale` dùng **`K1`–`K6`** cho **sáu nhóm tiêu chí chấm cuộc gọi**. Repo này dùng **`K1`–`K9`** cho **chín khe rò phễu**. **Cùng chữ `K`, hai nghĩa.**

```
★ Quy ước BẮT BUỘC: luôn ghi kèm ngữ cảnh.
    "khe K3"       → khe rò của repo này
    "nhóm QC K3"   → nhóm tiêu chí của Agent-QC-Telesale
⛔ KHÔNG viết "K3" trơ trọi. ⛔ KHÔNG đổi tên bộ nào — cả hai đã dùng
   trong tài liệu đang lưu hành.
```

---

## ⏸ Mười slot khối phải cấp

Repo **chạy được ngay** phần đọc nguồn · dựng phễu · dựng cohort · đo chín khe · đo ba độ trễ · xuất bốn báo cáo · đổi mã. Nhưng **⛔ chưa so được *"đạt / chưa đạt"* bất cứ chỉ số nào** — vì `tb-D` §4 đang làm đúng việc của nó: ⛔ **không tự đặt ngưỡng**.

Hai slot chặn nặng nhất:

| # | Slot | Chặn gì |
|---|---|---|
| ① | **Bảy câu định nghĩa doanh số** *(`so-B` §1)* | ⛔ Chặn **mọi con số doanh số** — CỔNG Đ |
| ② | **Mã lead dùng chung bốn nguồn** | ⛔ Chặn **toàn bộ phễu cohort** → chỉ còn đọc được cách ① |

Mười slot đầy đủ: [`knowledge/tb-H`](knowledge/tb-H-module-khoi-telesale.md) §2.

---

## ⛔ Dữ liệu

`du-lieu/` · `out/` · **`ma-nhan-vien.csv`** đã bị `.gitignore` chặn. ⛔ Không commit, ⛔ không gửi qua kênh công khai.

---

## Tài liệu

| File | Nội dung |
|---|---|
| [`doc/01-cai-dat.md`](doc/01-cai-dat.md) | Ba cách cài · ★ **cột bắt buộc mỗi nguồn** · bốn câu trước khi gửi · **8 câu kiểm sau khi cài** |
| [`doc/CHANGELOG.md`](doc/CHANGELOG.md) | Bốn luật gốc · ★ **ba lỗi bắt được khi chạy thử** · những gì ⛔ chưa có |
| [`prompts/`](prompts/) | 4 prompt mẫu: `đọc` · `ba báo cáo` · `vấn đề` · `riêng tư` |

★ **Đọc `01-cai-dat.md` phần *"8 câu kiểm sau khi cài"* trước khi phát hành bản đầu tiên.** Hai câu đầu trong đó là hai câu agent **sai tự tin nhất** — cả hai đều cho ra một con số trông hợp lý và **luôn khớp tổng**.
"# Agent-TongHopBaoCao-Telesale" 
