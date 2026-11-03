# Prompt · `NGÀY` · `TUẦN` · `THÁNG`

> Yêu cầu `ĐỌC` đã chạy. **Ba kỳ ba việc khác nhau** — ⛔ không phải một báo cáo ba cỡ.

---

## `NGÀY` — điều hành

```
BÁO CÁO NGÀY <ngày>.

① HOẠT ĐỘNG — cách ① của tb-C: mỗi chặng đếm theo mốc của CHÍNH NGUỒN ĐÓ.
   ⛔ KHÔNG chia chặng này cho chặng kia. ⛔ KHÔNG in tỷ lệ chuyển đổi nào.
② ⛔ SỰ CỐ — chỉ in khi CÓ. Mỗi dòng kèm người nhận.
   Sự cố = thứ VỀ 0, thứ BẰNG TOÀN BỘ MẪU, thứ DỪNG HẲN:
     · data về 0 · không cuộc gọi nào · một người ⛔ không gọi gì
     · tổng đài mất kết nối · data tồn vọt
③ SO NGƯỠNG — ⛔ KHÔNG so với hôm qua.
④ ⏸ CHƯA ĐO ĐƯỢC — khe nào và vì nguồn nào.

⛔ BỐN THỨ BÁO CÁO NGÀY ⛔ KHÔNG ĐƯỢC CÓ:
  ⛔ "giảm 20% so với hôm qua"   → một ngày là mẫu nhiễu
  ⛔ bất kỳ tỷ lệ chuyển đổi nào  → tỷ lệ chỉ đọc được từ cohort
  ⛔ xếp hạng nhân viên
  ⛔ mục rỗng "không có sự cố"    → in mỗi ngày thì mục đó thành vô hình
                                   đúng ngày có sự cố
```

★ **Mục ② là mục duy nhất quản lý đọc mỗi ngày** — nên nó ⛔ không được loãng.

---

## `TUẦN` — chẩn đoán *(báo cáo chính của khối)*

```
BÁO CÁO TUẦN <kỳ>.

① PHỄU COHORT — cách ② của tb-C. Mẫu số CỐ ĐỊNH là n của lô.
   ★ So ba cohort ĐÃ ĐÓNG gần nhất. ⛔ KHÔNG so với cohort đang chạy.
   ★ Mỗi cohort in nhãn [ĐÃ ĐÓNG] hoặc [⏳ CHƯA ĐÓNG — còn n lead giữa phễu].
② ĐỘ TRỄ — ba trung vị (⛔ không trung bình):
   data→gọi 1 (phân bổ) · kết nối→hẹn (tư vấn) · hẹn→đến khám (nhắc hẹn)
③ ★★ BA KHE MẤT NHIỀU LEAD NHẤT — xếp theo SỐ LEAD MẤT, ⛔ không theo
   tỷ lệ xấu nhất. Mỗi khe đủ SÁU Ô:
     ① số thật (kèm mẫu số) ② lead mất ③ xu hướng ④ ★ CẮT RA
     ⑤ GỐC (chạy CỔNG V) ⑥ NGƯỜI NHẬN + HẠN
④ VIỆC CỦA KHỐI — chỉ khe đã qua CỔNG V và kết luận là việc của khối
⑤ ⛔ VIỆC HỆ THỐNG — MỤC RIÊNG, ⛔ KHÔNG gộp vào ④
⑥ LÁT CẮT THEO NGƯỜI — mã NV-xx, xếp theo SỐ LEAD (⛔ không theo khe yếu,
   xếp theo khe yếu là xếp hạng người bằng đường vòng).
   ⚠ Người <10 cuộc: ghi "chưa đủ mẫu", ⛔ KHÔNG nhận định.
   + câu chân bảng.
⑦ ⏸ CHƯA ĐO ĐƯỢC · KHE QUAY LẠI ≥2 KỲ (nếu có → ĐƯA LÊN ĐẦU)
```

⚠️ **Ô ④ *"cắt ra"* là ô làm cho khe trở nên sửa được.** *"No-show 62%"* là một con số. *"Hẹn chiều muộn chỉ 41%"* là **một việc**.

---

## `THÁNG` — xu hướng & cơ cấu

```
BÁO CÁO THÁNG <tháng>.

① ⚠️ HAI ĐIỀU CHỈNH — IN TRƯỚC MỌI SO SÁNH:
   · số ngày làm việc tháng này / tháng trước  → ⛔ không so thẳng
   · cơ cấu nhân sự (vào / nghỉ)               → ⛔ không kết luận xu hướng
                                                  khi chưa tách cũ/mới
② PHỄU THEO THÁNG — ⛔ CHỈ cohort ĐÃ ĐÓNG.
   ⚠ Cohort những ngày cuối tháng thường CHƯA ĐÓNG → ghi riêng
     "n cohort chưa đóng, loại khỏi so sánh", ⛔ không gộp vào số tháng.
③ XU HƯỚNG BA THÁNG — từng chặng, kèm hai điều chỉnh ở ①
④ TÁCH CŨ / MỚI — ⛔ không gộp một tỷ lệ chung
⑤ HIỆU QUẢ ĐÀO TẠO — ⚠ CÙNG người · CÙNG nhóm dịch vụ · CÙNG tiêu chí
⑥ KHE SỐNG DAI — khe qua ≥2 kỳ mà số ⛔ không đổi
   ★ khe sang kỳ thứ 3 → ⛔ không còn là việc của trưởng nhóm. Ghi thẳng.
⑦ VIỆC HỆ THỐNG CÒN TREO — kèm số kỳ đã treo.
   ★ treo ≥3 kỳ → ĐƯA LÊN ĐẦU báo cáo, ⛔ không để phụ lục.
```

⚠️ **Mục ① ⛔ không được bỏ.** *"Tháng này giảm 12%"* có khi chỉ là *"tháng này ít hơn 2 ngày làm việc"*. Và *"mọi chỉ số tiến trình đều tụt"* có khi chỉ là *"vừa tuyển 3 người"*.

---

## Ba dòng bắt buộc — in trên **cả ba** báo cáo

```
① ĐỊNH NGHĨA : doanh số [ghi nhận/thực thu/đã thực hiện] · mốc · phạm vi
② MẪU & KỲ   : cohort [ngày] n=? · [ĐÃ ĐÓNG / ⏳ chưa đóng, còn n lead] · kỳ
③ ★ NGUỒN    : bốn nguồn đủ/cũ/thiếu + XUẤT LÚC NÀO
                → ⛔ KHÔNG tính được: <liệt kê khe>
```

⛔ **Thiếu một dòng → ⛔ không phát hành.** ★ Mọi tỷ lệ kèm **mẫu số**: `74/120 · 62%`.

---

```bash
python tools/tb.py ngay  --ngay 2026-11-03
python tools/tb.py tuan  --ky "27/10-02/11"
python tools/tb.py thang --thang 2026-10
```
