# Prompt · `ĐỌC` — nhận bốn nguồn, qua CỔNG N và CỔNG Đ

> Bước này ⛔ **không in báo cáo nào**. Nó chỉ trả lời: **cái gì trong kỳ này đáng tin**.

---

```
ĐỌC bốn nguồn kỳ <KỲ>.

Đính kèm / dán:
 ① cuộc gọi (tổng đài)      — <CSV / link Sheet / dán tay>
 ② data phân bổ             — <…>
 ③ lịch hẹn & đến khám      — <…>
 ④ ca chốt & doanh số       — <…>

── CỔNG N · in TRƯỚC mọi con số ──
① BẢNG TÌNH TRẠNG NGUỒN
   mỗi nguồn: đủ / ⚠️ CŨ / ⛔ THIẾU · dạng (CSV·Sheet·dán tay) · XUẤT LÚC NÀO
   ⚠ "Cập nhật" là LÚC FILE ĐƯỢC XUẤT, ⛔ KHÔNG phải ngày lớn nhất trong dữ liệu.
     Ca chốt LUÔN có ngày muộn hơn cuộc gọi vì nó ở cuối phễu — lấy ngày lớn
     nhất làm độ tươi thì mọi nguồn đều trông như "cũ".
② KHOÁ NỐI: có `ma_lead` hoặc `sdt_hash` không?
   ⛔ Không có → ⛔ KHÔNG dựng được cohort → chỉ đọc được CÁCH ① HOẠT ĐỘNG.
③ CỘT THIẾU: nguồn nào thiếu cột bắt buộc → chặng nào thành "⏸".
④ KỲ: khoảng ngày của từng nguồn có khớp kỳ đang báo không.
⑤ ★ HỆ QUẢ — liệt kê CHÍNH XÁC: khe nào tính được · khe nào ⏸ và vì nguồn nào.

⛔ Chưa in ô ⑤ thì ⛔ KHÔNG chạy tiếp. Ô ⑤ là ô cho người đọc biết
  CÁI GÌ TRONG BÁO CÁO NÀY ĐÁNG TIN.

── CỔNG Đ · bảy câu định nghĩa doanh số (so-B §1) ──
Hỏi tôi, in ra, ⛔ KHÔNG tự trả lời, ⛔ KHÔNG đặt mặc định:
 ① ghi nhận / thực thu / đã thực hiện?
 ② mốc: ngày chốt / ngày thực hiện / ngày thu tiền?
 ③ gộp hay trừ: hoàn tiền · chiết khấu · voucher · trả góp · tặng kèm?
 ④ tính ai: khách mới · cũ quay lại · tái khám · walk-in?
 ⑤ quy về trục nào?
 ⑥ đã gồm VAT chưa?
 ⑦ khách nhiều dịch vụ/thương hiệu thì tính vào đâu?

⛔ Chưa chốt bảy câu → ⛔ KHÔNG in con số doanh số nào. In các chặng ①–⑤
  (⛔ không cần doanh số) và ghi "⏸ chặng ⑥⑦ chờ CỔNG Đ".
```

---

## ★ Đổi mã NGAY ở bước này, ⛔ không ở bước xuất

```
tên nhân viên      → NV-xx   (bảng quy đổi do quản lý giữ, NGOÀI file báo cáo)
số điện thoại      → băm một chiều
tên khách          → KH-xxx
cột ghi chú tự do  → ⛔ BỎ HẲN
```

⚠️ **Vì sao phải ở bước đọc:** đổi ở bước xuất thì **tên thật còn lại trong mọi file trung gian** — và một trong số đó sẽ bị gửi đi, bị commit, hoặc nằm lại trên máy ai đó. Đổi ở bước đọc thì ⛔ **không có bản nào chứa tên để mà lọt**.

★ Mã `NV-xx` phải **bền giữa các kỳ**. `NV-03` kỳ này và kỳ sau phải là **cùng một người**, nếu không thì mọi so sánh trước/sau đào tạo đều vô nghĩa.

---

## Dạng dán tay — bốn luật

```
① ĐỌC ĐƯỢC GÌ THÌ LẤY, ⛔ KHÔNG SUY PHẦN CÒN LẠI.
   "gọi hết" → chặng ② = 45. "kết nối" ⛔ KHÔNG CÓ → ⏸ chưa đo được.
② ⛔ KHÔNG có ma_lead → đoạn này ⛔ KHÔNG vào cohort.
   Gắn nhãn "nguồn dán tay · ⛔ không vào cohort".
③ GHI NGUYÊN VĂN vào phụ lục, kèm ai dán và lúc nào.
④ ⚠ "mai 3 khách đến" là DỰ KIẾN, ⛔ KHÔNG phải đã đến.
   ⛔ Không đưa vào chặng ⑤. Muốn in thì cột riêng, nhãn "(dự kiến)".
```

★ **Ảnh chụp** xử như dán tay, cộng một luật: ⛔ **không đọc số từ ảnh mờ**. Ghi `⏸ ảnh ⛔ không đọc được` và xin lại — ⛔ **không đoán chữ số**.

---

## Google Sheet

★ Đọc **trong chat** qua connector Google Sheets — script ⛔ không có quyền truy cập.
Dán **link sheet** và nói rõ **tab nào là nguồn nào**:

```
ĐỌC bốn nguồn kỳ <KỲ>, lấy từ sheet này: <link>
 · tab "Cuoc goi"   → nguồn ①
 · tab "Data"       → nguồn ②
 · tab "Lich hen"   → nguồn ③
 · tab "Chot"       → nguồn ④
⚠ Nói rõ mỗi tab được cập nhật lần cuối lúc nào — tôi ⛔ không đoán được
  điều đó từ nội dung sheet.
```

---

```bash
python tools/tb.py doc du-lieu/ --ky "27/10-02/11"
```
