# tb-B · BỐN NGUỒN · KHUÔN ĐẦU VÀO · ĐỘ TƯƠI

> Sổ này nói: nhận gì, cột nào bắt buộc, **mỗi nguồn đếm theo mốc nào**, và khi nào thì ⛔ **không được tính tỷ lệ**.

---

## 1. BỐN NGUỒN — VÀ MỐC RIÊNG CỦA TỪNG NGUỒN

> ⚠️ Cột **"mốc"** là cột quan trọng nhất của bảng này. Bốn nguồn ⛔ **không cùng một mốc**, và đó là lý do có `tb-C`.

| # | Nguồn | Ai xuất | Mốc của nó | Sở hữu chặng |
|---|---|---|---|---|
| ① | **Cuộc gọi** | Tổng đài / CRM | **Ngày gọi** | ② đã gọi · ③ kết nối |
| ② | **Data / lead phân bổ** | Khâu phân bổ · Marketing | **Ngày nhận data** | ① data nhận |
| ③ | **Lịch hẹn & đến khám** | CRM · lễ tân cơ sở | ★ **hai mốc**: ngày tạo hẹn **và** ngày hẹn | ④ đặt hẹn · ⑤ đến khám |
| ④ | **Ca chốt & doanh số** | CRM · Kế toán | ★ `so-B` câu 2 — **phải hỏi** | ⑥ ca chốt · ⑦ doanh số |

★ **Nguồn ③ có hai mốc và đó ⛔ không phải chuyện nhỏ.** *Đặt hẹn* đếm theo **ngày tạo hẹn**; *đến khám* đếm theo **ngày hẹn**. Một hẹn tạo thứ 5 cho thứ 7 nằm ở **hai ngày khác nhau** trong hai chặng. Lẫn hai mốc này là lỗi phổ biến nhất khi dựng `K6`.

---

## 2. CỘT BẮT BUỘC TỪNG NGUỒN

### ① Cuộc gọi

| Cột | Bắt buộc | Dùng để |
|---|---|---|
| `ngay_goi` | ✅ | Mốc của nguồn |
| ★ `ma_lead` *(hoặc `sdt_hash`)* | ✅ | **Khoá nối** — ⛔ không có thì ⛔ không dựng được cohort (`tb-C` §5) |
| `ma_nv` | ✅ | Lát cắt theo người |
| `huong` *(ra / vào)* | ✅ | ⛔ Gọi vào ⛔ không tính vào chặng ② |
| `ket_qua` | ✅ | Phân biệt **kết nối** / không bắt máy / số sai / từ chối nghe |
| `thoi_luong_giay` | 🔶 | ★ Lọc cuộc dưới ngưỡng — xem §4 |
| `gio_goi` | 🔶 | Lát cắt khung giờ, cần cho `K3`/`K6` |

⚠️ **`ket_qua` là cột quyết định chặng ③.** Nếu bản xuất chỉ có *"đã gọi / chưa gọi"* mà ⛔ không phân biệt **nói được** hay **không bắt máy**, thì chặng ③ ⛔ **không đo được** — ghi `⏸ chưa đo được: kết nối` và khe `K3` cũng `⏸`.

### ② Data / lead phân bổ

| Cột | Bắt buộc | Dùng để |
|---|---|---|
| `ngay_nhan` | ✅ | ★ **Khoá cohort** (`tb-C` §3) |
| ★ `ma_lead` | ✅ | Khoá nối |
| `nguon_data` | ✅ | Lát cắt nguồn — cần cho `K3` §4 |
| `ma_nv_duoc_giao` | ✅ | Lát cắt người · `K8` tải việc |
| `dich_vu_quan_tam` | 🔶 | Lát cắt dịch vụ |
| `trang_thai` | 🔶 | `K9` data tồn |

### ③ Lịch hẹn & đến khám

| Cột | Bắt buộc | Dùng để |
|---|---|---|
| ★ `ngay_tao_hen` | ✅ | Mốc chặng ④ |
| ★ `ngay_hen` | ✅ | Mốc chặng ⑤ |
| ★ `da_den` *(có/không)* | ✅ | **Chặng ⑤** — ⛔ không có cột này thì ⛔ không đo được show-up |
| `ma_lead` | ✅ | Khoá nối |
| `co_so` | 🔶 | Lát cắt cơ sở |
| `ly_do_huy` | 🔶 | Đọc `K6` cho sâu |

> ⛔ **Cột `da_den` ⛔ không được suy từ cột khác.** ⛔ Không lấy *"đã tạo hồ sơ"*, ⛔ không lấy *"có ca chốt"* để suy ra *"đã đến"*. Suy như thế thì `K6` biến mất và `K7` bị gộp vào nó.

### ④ Ca chốt & doanh số

| Cột | Bắt buộc | Dùng để |
|---|---|---|
| `ngay_<mốc>` | ✅ | ★ Mốc phải khai rõ là **chốt / thực hiện / thu tiền** (`so-B` câu 2) |
| `ma_lead` | ✅ | Khoá nối |
| `ma_nv` | ✅ | Lát cắt người |
| `so_tien` | ✅ | Chặng ⑦ |
| `dich_vu` | 🔶 | Lát cắt dịch vụ |
| `loai_khach` | 🔶 | `so-B` câu 4 — mới / cũ / walk-in |

⚠️ **Nguồn ④ ⛔ không được đọc khi bảy câu của `so-B` chưa chốt** — CỔNG Đ của `tb-A` §4. Ba loại doanh số *(ghi nhận · thực thu · đã thực hiện)* **luôn khác nhau**, và một con số ⛔ không khai loại nào thì ⛔ không so được với bất cứ bảng nào khác.

---

## 3. BA DẠNG ĐẦU VÀO

| Dạng | Cách đọc | Ghi chú |
|---|---|---|
| **Excel / CSV** | `python tools/tb.py doc du-lieu/` — script đọc cả bốn file | Dạng **chuẩn**. ⛔ `du-lieu/` đã bị `.gitignore` chặn |
| **Google Sheet** | ★ Đọc **trong chat** qua connector Google Sheets, ⛔ không qua script | Dán **link sheet** + nói rõ **tab nào là nguồn nào**. Script ⛔ không có quyền truy cập |
| **Dán text / ảnh chụp** | Agent đọc trực tiếp trong chat | ⚠️ Xem §5 — dạng này **bẩn nhất** và có luật riêng |

★ **Trộn ba dạng trong cùng một kỳ là bình thường** *(ví dụ: tổng đài xuất CSV, lịch hẹn là Google Sheet, data phân bổ do trưởng nhóm dán tay)*. Nhưng mỗi nguồn phải khai rõ **dạng** và **lúc cập nhật** — xem §4.

---

## 4. ★★ ĐỘ TƯƠI — BẢNG TÌNH TRẠNG NGUỒN, IN TRƯỚC MỌI SỐ

> ⚠️ Đây là bảng mà một agent tổng hợp **bắt buộc** phải có và một báo cáo đơn nguồn thì không cần. ⛔ Thiếu nó thì mọi tỷ lệ đi qua hai nguồn đều có thể sai mà ⛔ không ai biết.

```
TÌNH TRẠNG NGUỒN — kỳ <…>

  ① Cuộc gọi        ✅ đủ    · CSV   · cập nhật 03/11 08:15
  ② Data phân bổ    ✅ đủ    · Sheet · cập nhật 03/11 07:40
  ③ Lịch hẹn        ⚠️ CŨ    · Sheet · cập nhật 02/11 18:00   ← thiếu 1 ngày
  ④ Doanh số        ⛔ THIẾU · —     · chưa xuất

⛔ HỆ QUẢ — in ngay dưới bảng:
   · ⛔ KHÔNG tính được K6 (đến khám ÷ đặt hẹn) — nguồn ③ cũ 1 ngày
   · ⛔ KHÔNG tính được K7 và chặng ⑥⑦ — thiếu nguồn ④
   · ✅ Tính được K1 K2 K3 K4 K8 K9
```

### Ba luật của độ tươi

```
① MỘT NGUỒN THIẾU → mọi tỷ lệ ĐI QUA nguồn đó là "⏸ chưa đo được".
   ⛔ KHÔNG tính bằng số cũ. ⛔ KHÔNG ngoại suy.

② MỘT NGUỒN CŨ HƠN KỲ ĐANG BÁO → cũng xử như THIẾU cho phần ngày bị hụt.
   ⚠ Đây là bẫy nặng hơn "thiếu": số VẪN RA, chỉ là mẫu số bị hụt
     → tỷ lệ ĐẸP GIẢ. Và ⛔ không nhìn ra được từ bảng.

③ HAI NGUỒN KHÁC GIỜ CẬP NHẬT → tỷ lệ giữa chúng chỉ đọc được tới
   MỐC CŨ HƠN trong hai mốc. Ghi rõ mốc đó.
```

★ **Luật ② là luật chặn CỔNG N.** Ví dụ thật: tổng đài cập nhật 08:15 hôm nay, doanh số mới cập nhật hết hôm qua → `ca chốt ÷ kết nối` có **mẫu số của 2 ngày** và **tử số của 1 ngày**. Tỷ lệ đó thấp giả, và kỳ sau nó *"tăng vọt"* mà ⛔ không ai làm gì.

---

## 5. ★ DẠNG DÁN TAY — LUẬT RIÊNG

Trưởng nhóm dán một đoạn như thế này là bình thường:

```
Nhóm 2 ngày 3/11: data 45, gọi hết, hẹn 8 ca, mai 3 khách đến
```

### Bốn luật xử dạng dán tay

```
① ĐỌC ĐƯỢC GÌ THÌ LẤY, ⛔ KHÔNG SUY PHẦN CÒN LẠI.
   "gọi hết" → chặng ② = 45. "kết nối" ⛔ KHÔNG CÓ → ⏸ chưa đo được.

② ⛔ KHÔNG CÓ ma_lead → đoạn này ⛔ KHÔNG vào được cohort.
   Nó chỉ đóng góp vào cách ① HOẠT ĐỘNG (tb-C §3).
   → In nhãn: "nguồn dán tay · ⛔ không vào cohort".

③ GHI NGUYÊN VĂN vào phụ lục báo cáo, kèm ai dán và lúc nào.
   Để kỳ sau còn đối chiếu được khi số lệch.

④ ⚠ "mai 3 khách đến" là DỰ KIẾN, ⛔ KHÔNG phải đã đến.
   ⛔ Không đưa vào chặng ⑤. Chặng ⑤ chỉ nhận số ĐÃ XẢY RA.
```

⚠️ **Luật ④ là luật hay bị phá nhất ở báo cáo ngày.** Số *"dự kiến"* và số *"đã xảy ra"* nằm cùng một dòng thì hôm sau ⛔ không ai biết dòng đó nghĩa gì. Nếu phải in dự kiến thì in ở **cột riêng có nhãn `(dự kiến)`**.

★ **Ảnh chụp** xử như dán tay, cộng thêm một luật: ⛔ **không đọc số từ ảnh mờ hoặc bị che**. Ghi `⏸ ảnh ⛔ không đọc được` và xin lại — ⛔ **không đoán chữ số**.

---

## 6. CỔNG N — KIỂM NGUỒN, IN TRƯỚC KHI CHẠY

```
① BỐN NGUỒN: nguồn nào đủ · cũ · thiếu   → bảng §4
② KHOÁ NỐI : có ma_lead / sdt_hash không → quyết định có dựng được cohort
③ CỘT THIẾU: nguồn nào thiếu cột bắt buộc → chặng nào thành "⏸"
④ KỲ       : khoảng ngày của từng nguồn có khớp kỳ đang báo không
⑤ HỆ QUẢ   : liệt kê CHÍNH XÁC khe nào tính được, khe nào ⏸
```

⛔ **Không chạy tiếp khi ô ⑤ chưa in.** Ô ⑤ là ô làm cho người đọc biết **cái gì trong báo cáo này đáng tin**.

---

## 7. ⛔ BỐN THỨ ⛔ KHÔNG ĐƯỢC LÀM VỚI ĐẦU VÀO

```
① ⛔ KHÔNG điền số thiếu bằng số kỳ trước, bằng trung bình, hay bằng
   ngoại suy. Thiếu là "⏸ chưa đo được".

② ⛔ KHÔNG đổi đơn vị âm thầm. Tổng đài đếm CUỘC, phễu cần LEAD
   (tb-C §1). Đổi thì phải ghi rõ đã đổi thế nào.

③ ⛔ KHÔNG loại bản ghi mà ⛔ không ghi số đã loại và vì sao.
   Ví dụ cuộc dưới 20 giây: loại được, nhưng PHẢI in
   "loại n cuộc dưới 20 giây" — vì nó đổi mẫu số.

④ ⛔ KHÔNG đưa tên thật nhân viên hay dữ kiện khách vào bất cứ file
   trung gian nào. Hash/đổi mã NGAY Ở BƯỚC ĐỌC (tb-G §2).
```

---

## 8. TỰ KIỂM SỔ NÀY

- [ ] Bảng **tình trạng nguồn** §4 đã in **trước** mọi con số chưa?
- [ ] Ô ⑤ của CỔNG N — liệt kê khe nào tính được / khe nào `⏸` — có chưa?
- [ ] Có nguồn nào **cũ hơn kỳ đang báo** mà vẫn được dùng để tính tỷ lệ không?
- [ ] Nguồn ③ có **hai mốc** riêng cho *đặt hẹn* và *đến khám* chưa, hay dùng chung một mốc?
- [ ] Cột `da_den` có bị **suy** từ cột khác không?
- [ ] Chặng ③ *kết nối* đếm theo **lead** chưa, hay vẫn là số cuộc?
- [ ] Nguồn ④ đã qua **CỔNG Đ** *(bảy câu `so-B`)* chưa?
- [ ] Đoạn **dán tay** đã gắn nhãn *"⛔ không vào cohort"* và lưu nguyên văn chưa?
- [ ] Số **dự kiến** có bị trộn vào cột đã xảy ra không?
- [ ] Số bản ghi **bị loại** đã in chưa?
