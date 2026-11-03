# CHANGELOG

## v1.0 · 03/11/2026 — bản đầu

Agent tổng hợp báo cáo **Ngày · Tuần · Tháng** cho khối Telesale Kangnam, cộng một lệnh thứ tư — `VẤN ĐỀ` — là lệnh quản lý dùng nhiều nhất.

### Dựng

- 8 sổ tri thức `tb-A` … `tb-H`
- `SYSTEM-PROMPT.md` *(11.584 ký tự)* · `SYSTEM-PROMPT-NGAN.md` *(7.954 — còn **46** dư)*
- `tools/tb.py` — `doc` · `ngay` · `tuan` · `thang` · `van-de` · `kiem`
- 4 prompt mẫu · 4 file dữ liệu mẫu khớp nhau *(640 cuộc · 242 lead · 48 hẹn · 15 ca)*
- `.gitignore` chặn `ma-nhan-vien.csv` **ngay từ commit đầu** — ⛔ không để nó từng tồn tại trong history

### Bốn luật gốc

**① Cohort — `tb-C`.** Một lead đi qua phễu trong **nhiều ngày**, nên `ca chốt hôm nay ÷ data nhận hôm nay` ⛔ **sai cả hai chiều**: tử số đến từ lô cũ, mẫu số chưa chạy hết. ★ Cái làm nó nguy hiểm là **nó luôn khớp tổng**, nên ⛔ không ai phát hiện. Hai cách đọc: **① HOẠT ĐỘNG** *(mỗi chặng đếm trên mốc của chính nguồn đó, ⛔ không chia cho nhau)* và **② COHORT** *(lô khoá theo `ngay_nhan`, mẫu số cố định — cách **duy nhất** tính được tỷ lệ chuyển đổi)*.

**② Ba đơn vị đếm — `tb-D` §2.** `CUỘC` *(tổng đài xuất ra)* ≠ `LEAD` *(phễu cần — mọi tỷ lệ chuyển đổi)* ≠ `CA` *(ca chốt)*. ★ Một lead gọi 6 lần mới nói được là **1 kết nối**, ⛔ không phải 1/6. Đo kết nối theo **cuộc** rồi kết luận *"kết nối kém"* là **phạt đúng cái việc nên khen**.

**③ `CỔNG V` — `tb-E` §5.** Trước khi giao một khe rò cho ai: *"Người giỏi nhất khối, với đúng những gì hệ thống đang cấp hôm nay, có làm khác được không?"* ⛔ **Không** → **lỗi hệ**, vào **mục riêng**, có tên người cấp. ★ **Năm trong chín khe thường là lỗi hệ.** Một kỳ mà cả chín khe đều thành việc của khối thì gần như chắc chắn **cổng này ⛔ chưa chạy**.

**④ Ba kỳ ba việc — `tb-A`.** ⛔ **Không phải một báo cáo ba cỡ.** `NGÀY` = cái đang cháy *(so **ngưỡng**, ⛔ không so hôm qua, ⛔ không in tỷ lệ chuyển đổi, ⛔ không in xu hướng)* · `TUẦN` = chẩn đoán · `THÁNG` = xu hướng *(**phải** chỉnh số ngày làm việc + cơ cấu nhân sự **trước** mọi so sánh)*.

### Riêng tư — `tb-G`

Báo cáo in `NV-xx`; **bảng quy đổi do quản lý giữ, nằm ngoài file báo cáo và bị `.gitignore` chặn**. ★ Đổi mã **ở bước ĐỌC**, ⛔ không ở bước xuất — vì cột ghi chú tự do bị **bỏ hẳn** ngay lúc đọc, trước khi có cơ hội đi đâu.

`CỔNG R` chạy **bằng máy** qua `ghi_file()`: mọi lần ghi đều đi qua nó, và trượt thì **`sys.exit(2)` — từ chối ghi**, ⛔ không chỉ cảnh báo.

### ⚠ Ba lỗi bắt được khi chạy thử

**① ★★ Độ tuổi nguồn tính sai THEO CẤU TRÚC.** Ban đầu lấy **ngày lớn nhất trong dữ liệu** làm *"nguồn mới đến đâu"*. Cách đó ⛔ **không thể đúng**: `ca chốt` **luôn** có ngày muộn hơn `cuộc gọi` vì nó ở **cuối phễu** — nên nguồn nào ở cuối cũng trông *"mới"*, nguồn nào ở đầu cũng trông *"cũ"*. Kết quả: **cả bốn nguồn báo `CŨ`, ⛔ không khe nào tính được.** Ghi trong `tb.py`:

> *"⚠ 'Độ tuổi' = LÚC FILE ĐƯỢC XUẤT, ⛔ KHÔNG phải ngày lớn nhất trong dữ liệu. Lấy ngày lớn nhất là sai THEO CẤU TRÚC: ca chốt LUÔN có ngày muộn hơn cuộc gọi vì nó ở cuối phễu."*

→ Sửa: lấy **`mtime` của file**, và *"cũ"* = xuất chậm hơn nguồn mới nhất **>24h**.

**② `CỔNG R` chặn đúng `van-de`.** Báo cáo `VẤN ĐỀ` in `NV-xx` trong lát cắt của khe `K8` nhưng **thiếu câu chân bảng** → cổng từ chối ghi. ★ Đây là **cổng hoạt động đúng**, ⛔ không phải lỗi của cổng. Sửa bằng cách thêm câu chân vào `van-de`.

**③ ★ Khuôn bắt SĐT bỏ sót một kiểu viết.** Bản đầu dùng `\d{3}[\s.\-]?\d{3,4}` và nó ⛔ **bỏ sót `0912345678`** — một lỗ thật trong một cổng riêng tư. Ghi trong `tb.py`:

> *"Một cổng bỏ sót một kiểu viết là một cổng KHÔNG DÙNG ĐƯỢC, vì người gửi ⛔ không biết nó đã bỏ sót."*

→ Sửa: `tim_sdt()` **đếm chữ số** thay vì khớp khuôn độ dài. Nay bắt được `0912345678` · `091 234 5678` · `091.234.5678` · `+84912345678` · `0987 654 321`, và ⛔ không bắt oan ngày tháng, mã lead, số tiền.

★ Lỗi ① thuộc **cùng họ** với những lỗi nặng nhất của các repo cùng hệ: nó cho ra một con số **trông hợp lý**, ⛔ không gây lỗi chạy, và ⛔ **không nhìn ra được từ bảng** — chỉ lộ ra khi hỏi *"vì sao cả bốn nguồn đều cũ?"*.

### Đã kiểm

```
python tools/tb.py doc du-lieu/ --ky "26/10-02/11"
  → CỔNG N: bốn nguồn ✅ đủ · ma_lead có ở cả bốn → cohort dựng được
  → cả CHÍN khe tính được · 6 tên nhân viên đổi thành NV-xx
python tools/tb.py ngay | tuan | thang | van-de      → ✅ xuất đủ
python tools/tb.py kiem <cả bốn báo cáo>             → ✅ CỔNG R qua
phép thử rò (tên thật · SĐT · email)                 → ✅ CHẶN cả ba
```

### ⚠ Chưa có

- ⛔ **Chưa chạy trên dữ liệu thật.** Mọi con số trong kho này đến từ **mẫu sinh ra**, ⛔ không phải số của khối.
- ⛔ **Chưa có ngưỡng nào do khối chốt** → mọi so sánh ngày in `⚠ chưa có ngưỡng`. ★ Agent ⛔ **không tự đặt ngưỡng**, và ⛔ không lấy trung bình ba kỳ *(đó là lấy hiện trạng làm chuẩn)*.
- ⛔ **Chưa có mốc doanh số do `Agent-Order-SoLieu` chốt** → dòng định nghĩa in `[ghi nhận/thực thu/đã thực hiện]` cho người đọc tự chọn, cho tới khi có câu trả lời.
- ⛔ **Chưa có giá trị đơn trung bình** → khe rò xếp theo **số lead mất**, ⛔ không quy ra tiền.

### ★ Hai trùng mã **có chủ ý** — ⛔ không đổi tên

| Mã | Nghĩa ở đây | Nghĩa ở nơi khác |
|---|---|---|
| `K1`–`K9` | **khe rò phễu** | `K1`–`K6` = **nhóm tiêu chí chấm cuộc gọi** *(`Agent-QC-Telesale`)* |

⛔ **Không nạp tri thức hai repo này vào cùng một Project.** Quy ước khi viết: luôn viết **"khe `K3`"** hoặc **"nhóm QC `K3`"**, ⛔ không bao giờ viết `K3` trần.
