# Prompt · `CỔNG R` — kiểm riêng tư trước khi xuất

> ⛔ Không file nào được xuất trước khi chạy đủ **sáu câu** này. Bốn câu đầu chạy **bằng máy**, ⛔ không bằng mắt.

---

```
CỔNG R — kiểm riêng tư cho <tên file>.

① TÊN NHÂN VIÊN
   Tìm mọi tên trong bảng quy đổi, trên file sắp xuất.
   Tìm thấy dù một lần → ⛔ DỪNG, ⛔ không xuất.
   ⚠ Kiểm cả trong TÊN FILE và trong phụ lục "nguyên văn dán tay".

② DỮ KIỆN KHÁCH
   SĐT · email · tên khách · địa chỉ → ⛔ phải KHÔNG CÓ.
   ⚠ Bắt SĐT bằng cách ĐẾM CHỮ SỐ, ⛔ không bằng một khuôn độ dài cố định:
     "0912345678" · "091 234 5678" · "091.234.5678" · "+84912345678"
     phải bắt được HẾT. Một cổng bỏ sót một kiểu viết là một cổng
     ⛔ KHÔNG DÙNG ĐƯỢC — vì người gửi ⛔ không biết nó đã bỏ sót.

③ CỘT GHI CHÚ TỰ DO
   ⛔ Phải KHÔNG TỒN TẠI trong file xuất, kể cả rỗng.
   ★ Đây là chỗ rò nhiều nhất và hay bị bỏ qua nhất, vì nó ⛔ không phải
     cột số nên ⛔ không ai nghĩ tới. Nhưng nó là nơi nhân viên gõ
     "chị Lan 098… muốn nâng mũi trước Tết".

④ BẢNG QUY ĐỔI
   ma-nhan-vien.* ⛔ phải KHÔNG nằm trong out/, ⛔ không nằm trong bất cứ
   thứ gì sắp gửi đi, ⛔ không là một tab trong cùng Sheet với báo cáo.

⑤ NGƯỠNG MẪU NGƯỜI
   Người nào dưới 10 cuộc mà vẫn có nhận định riêng → ⛔ DỪNG.

⑥ CÂU CHÂN BẢNG
   Mọi bảng có mã NV-xx mang đúng câu này:
   "Số liệu dùng để phân việc kèm cặp. Không phải căn cứ kỷ luật
    hay xếp hạng công khai."
```

---

```bash
python tools/tb.py kiem out/bao-cao-tuan-....md
```

★ Hàm `kiem_rieng_tu()` chạy đúng sáu câu trên, và **mọi lần ghi file đều đi qua `ghi_file()`** — ⛔ không ghi trực tiếp ở chỗ khác. Trượt thì **từ chối ghi**, ⛔ không chỉ cảnh báo.

⚠️ **Chạy tay thì ⛔ sẽ có kỳ quên.** Và một tên lọt ra rồi thì ⛔ **không gỡ lại được** — báo cáo đã nằm trong hộp thư của người khác.

---

## Bản rút gọn — để gửi ra ngoài khối

| | Bản đầy đủ | Bản rút gọn |
|---|---|---|
| Ai nhận | Quản lý khối · trưởng nhóm | Ngoài khối · ban điều hành |
| Lát cắt theo người | ✅ có, mã `NV-xx` | ⛔ **Không có** |
| Khe rò | ✅ cả chín, đủ sáu ô | 🔶 Ba khe đầu, ⛔ không có ô *"người nhận"* |
| Việc hệ thống | ✅ có tên người cấp | ✅ **GIỮ** |
| Phụ lục nguyên văn | ✅ có | ⛔ **Không có** |

★ **Mục *"việc hệ thống"* là mục duy nhất ⛔ không bị rút gọn** — vì nó là phần người ngoài khối **phải thấy mới gỡ được**. Rút nó đi thì bản gửi ra chỉ còn những việc khối tự làm, và **cái đang chặn thật thì ⛔ không ai biết**.

---

## ⛔ Lọc và gộp — không ra quyết định

```
Agent đưa số, bằng chứng và phương án. NGƯỜI THẬT KÝ.

⛔ Không đề xuất kỷ luật · cắt thưởng · xếp hạng công khai · cho nghỉ.
⛔ Không kết luận về CON NGƯỜI — chỉ về VIỆC và về KHE.
```

★ Một bản tổng hợp của máy dùng làm căn cứ kỷ luật là cách nhanh nhất để cả khối thôi tin vào nó. Và khi họ thôi tin thì **dữ liệu đầu vào hỏng theo** — ⛔ không ai nhập thật nữa, trạng thái lead thành *"đã gọi"* hết. Lúc đó agent này mất **thứ duy nhất nó có**.
