# 01 · Cài đặt

Ba cách dùng agent này. Chọn một.

> ⚠️ Agent này dựng riêng cho **khối Telesale Kangnam**. ⛔ **Không nạp lẫn tri thức của repo này với `Agent-QC-Telesale` vào cùng một Project** — hai repo dùng **cùng chữ `K`, hai nghĩa** *(`K1`–`K6` nhóm tiêu chí chấm cuộc gọi · `K1`–`K9` khe rò phễu)*. Trộn vào thì agent sẽ gọi khe rò là tiêu chí chấm và ⛔ không ai biết bảng nào đúng.

---

## A · Claude Project *(khuyến nghị)*

1. Tạo Project mới, tên: **Tổng hợp báo cáo Telesale**.
2. Dán toàn bộ [`SYSTEM-PROMPT.md`](../SYSTEM-PROMPT.md) *(11.584 ký tự)* vào ô **Custom instructions**.
3. Nạp vào **Knowledge**: 8 file trong [`knowledge/`](../knowledge/) + 4 file trong [`prompts/`](../prompts/).
4. ★ Nạp thêm **hai sổ của khối khác** — chúng **thắng** sổ của repo này khi mâu thuẫn:
   - `Agent-Order-SoLieu/knowledge/so-B-tu-dien-doanh-so.md` — **bảy câu chốt định nghĩa doanh số**
   - `Agent-QC-Telesale/knowledge/ts-G-ranh-gioi-rieng-tu.md` — **riêng tư, ⛔ không có ngoại lệ**
5. Nạp file dữ liệu của kỳ khi chạy: bốn nguồn.

---

## B · ChatGPT Custom GPT

Ô **Instructions** giới hạn 8.000 ký tự → dán [`SYSTEM-PROMPT-NGAN.md`](../SYSTEM-PROMPT-NGAN.md) *(7.954 ký tự — còn 46 dư)*. Phần còn lại nạp vào **Knowledge** như cách A.

```bash
python tools/dem-ngan.py
```

---

## C · Gemini Gem

Ô **Chỉ dẫn**: dán [`SYSTEM-PROMPT.md`](../SYSTEM-PROMPT.md). Knowledge như cách A.

---

## Chuẩn bị dữ liệu mỗi kỳ

```
du-lieu/                          ⛔ đã bị .gitignore chặn
├── *1-cuoc-goi*.csv        ① tổng đài      — mốc: ngày gọi
├── *2-data-phan-bo*.csv    ② phân bổ       — mốc: ngày nhận data  ★ khoá cohort
├── *3-lich-hen*.csv        ③ CRM/lễ tân    — ★ HAI mốc: ngày tạo hẹn + ngày hẹn
└── *4-ca-chot*.csv         ④ CRM/kế toán   — mốc: so-B câu 2, phải hỏi
```

★ **Script tìm file theo từ khoá trong tên** *(`1-cuoc-goi`, `2-data-phan-bo`…)*, nên tên file xuất ra có tiền tố/hậu tố gì cũng được, miễn chứa từ khoá đó.

### ★ Cột bắt buộc — thiếu thì chặng đó thành `⏸`

| Nguồn | Cột bắt buộc |
|---|---|
| ① cuộc gọi | `ngay_goi` · ★ `ma_lead` · `ma_nv` · `huong` · `ket_qua` |
| ② data | `ngay_nhan` · ★ `ma_lead` · `nguon_data` · `ma_nv_duoc_giao` |
| ③ lịch hẹn | `ngay_tao_hen` · ★ `ngay_hen` · `ma_lead` · ★ `da_den` |
| ④ ca chốt | `ngay_<mốc>` · `ma_lead` · `so_tien` |

⚠️ **Cột `ket_qua` của nguồn ① là cột quyết định chặng ③.** Nếu bản xuất chỉ có *"đã gọi / chưa gọi"* mà ⛔ không phân biệt **nói được** hay **không bắt máy**, thì chặng ③ ⛔ **không đo được** — và khe `K3` cũng `⏸`.

⚠️ **Cột `da_den` ⛔ không được suy từ cột khác.** ⛔ Không lấy *"đã tạo hồ sơ"*, ⛔ không lấy *"có ca chốt"* để suy ra *"đã đến"*. Suy như thế thì khe `K6` **biến mất** và `K7` bị gộp vào nó.

### ★★ `ma_lead` — cột quan trọng nhất của cả repo

⛔ **Không có `ma_lead` (hoặc `sdt_hash`) ở cả bốn nguồn thì ⛔ không dựng được cohort** — và cohort là thứ duy nhất tính được tỷ lệ chuyển đổi. Khi đó báo cáo chỉ in được **số việc trong ngày** và phải nói thẳng điều đó.

---

## Google Sheet

★ Đọc **trong chat** qua connector Google Sheets — `tb.py` ⛔ **không có quyền truy cập Sheet**. Dán link + nói rõ tab nào là nguồn nào, **và mỗi tab cập nhật lần cuối lúc nào** *(agent ⛔ không đoán được điều đó từ nội dung sheet)*.

## Dán text / ảnh chụp

Được, nhưng đoạn dán tay ⛔ **không có `ma_lead`** nên nó ⛔ **không vào cohort** — chỉ đóng góp vào *số việc trong ngày*, và được gắn nhãn `nguồn dán tay · ⛔ không vào cohort`. Luật đầy đủ ở [`tb-B`](../knowledge/tb-B-bon-nguon-dau-vao.md) §5.

---

## Chạy thử ngay

```bash
mkdir du-lieu && cp template/MAU_*.csv du-lieu/
python tools/tb.py doc     du-lieu/ --ky "26/10-02/11"
python tools/tb.py ngay    --ngay 2026-10-28
python tools/tb.py tuan    --ky "26/10-02/11"
python tools/tb.py van-de  --ky "26/10-02/11"
python tools/tb.py kiem    out/van-de-26-10-02-11.md
```

---

## ⚠️ Trước khi gửi báo cáo đi — bốn câu

```
① Đã chạy CỔNG R chưa?    python tools/tb.py kiem <file>
② ma-nhan-vien.csv có đang nằm ngoài out/ và ngoài thứ sắp gửi không?
③ Gửi ra NGOÀI KHỐI thì dùng BẢN RÚT GỌN (tb-G §7):
   ⛔ bỏ lát cắt người · ⛔ bỏ phụ lục · ✅ GIỮ mục việc hệ thống
④ Báo cáo có in đủ BA DÒNG BẮT BUỘC chưa?
   Thiếu một dòng → ⛔ không phát hành.
```

★ **Mục *"việc hệ thống"* là mục duy nhất ⛔ không bị rút gọn** khi gửi ra ngoài khối — vì nó là phần người ngoài **phải thấy mới gỡ được**.

---

## Kiểm sau khi cài — 8 câu

| Câu hỏi | Phải trả lời đúng | Nằm ở |
|---|---|---|
| ★★ *"Tỷ lệ chốt hôm nay bao nhiêu?"* | ⛔ **Câu hỏi này ⛔ không trả lời được theo ngày.** Ca chốt hôm nay ⛔ không đến từ data nhận hôm nay. Phải đọc theo **cohort** | `tb-C` §2–3 |
| ★★ *"Hôm nay giảm 20% so với hôm qua, có vấn đề gì không?"* | ⛔ **Một ngày là mẫu nhiễu** — ⛔ không kết luận xu hướng trên báo cáo ngày. So với **ngưỡng**, ⛔ không so với hôm qua | `tb-A` §3 |
| ★★ *"Khe `K6` no-show 62%, giao cho trưởng nhóm sửa nhé?"* | ⛔ **Chạy CỔNG V trước.** `K6` thường là **lỗi hệ** *(chưa có quy trình nhắc hẹn)* → vào mục **việc hệ thống**, ⛔ không vào việc của khối | `tb-E` §5 |
| ★ *"Khe nào xấu nhất thì sửa trước?"* | ⛔ **Không** — xếp theo **số lead mất**, ⛔ không theo tỷ lệ xấu nhất. Khe `75%` với 800 lead mất nhiều hơn khe `20%` với 15 lead | `tb-E` §6 |
| ★ *"Tỷ lệ kết nối của khối là bao nhiêu?"* | Đếm theo **LEAD**, ⛔ không theo cuộc. Một lead gọi 6 lần mới nói được là **1 kết nối**. Đo theo cuộc rồi nói *"kết nối kém"* là **phạt đúng cái việc nên khen** | `tb-D` §2 |
| ★ *"Đặt hẹn 48 ca, coi như 48 khách đến nhé?"* | ⛔ **Không.** ⛔ Không lấy *đặt hẹn* thay cho *đến khám* — đó là khe rò nặng nhất của telesale | `tb-C` §1 |
| ★ *"In tên nhân viên vào báo cáo cho trưởng nhóm dễ đọc?"* | ⛔ **Không.** Dùng `NV-xx`; **bảng quy đổi do quản lý giữ, ngoài file báo cáo**. Trưởng nhóm vẫn kèm được đúng người vì họ giữ khoá | `tb-G` §1 |
| *"Ngưỡng tỷ lệ kết nối nên đặt bao nhiêu?"* | ⛔ **Agent ⛔ không tự đặt ngưỡng.** ⛔ Không lấy trung bình ba kỳ *(đó là lấy hiện trạng làm chuẩn)*. Ghi `⚠ chưa có ngưỡng` + số thật + xu hướng | `tb-D` §4 |

★ **Hai câu đầu là hai câu agent sai tự tin nhất.** Cả hai đều cho ra một con số trông hợp lý, **luôn khớp tổng**, và ⛔ không nhìn ra được từ bảng.
