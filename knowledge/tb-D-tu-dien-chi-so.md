# tb-D · TỪ ĐIỂN CHỈ SỐ · ⛔ KHÔNG ĐẶT CHỈ SỐ MỚI

> Sổ này **chủ yếu trỏ sang nơi khác**. Đó là chủ ý: phần lớn chỉ số của khối Telesale **đã có chủ**, và đặt lại tên cho chúng là cách chắc chắn nhất để hai báo cáo nói hai con số khác nhau.

---

## 1. ★★ AI SỞ HỮU CHỈ SỐ NÀO

| Nhóm chỉ số | Sổ sở hữu | Agent này được làm gì |
|---|---|---|
| **Định nghĩa doanh số** — ghi nhận/thực thu/đã thực hiện · mốc · phạm vi · VAT · combo | `Agent-Order-SoLieu` → **`so-B` §1** *(bảy câu chốt)* | ⛔ **Chỉ HỎI và IN.** ⛔ Không tự trả lời, ⛔ không đặt mặc định |
| **Chất lượng cuộc gọi** — `K1`–`K6`, cờ đỏ, ba mức | `Agent-QC-Telesale` → **`ts-B`** | ⛔ **Chỉ ĐỌC LẠI kết quả.** ⛔ Không chấm lại, ⛔ không quy thành điểm số |
| **Chỉ số marketing** — CPL, ROAS, chi phí/ca chốt | `so-B` §3 · `Agent-AdsReport-Kangnam` | 🔶 Dùng lại tên, ⛔ không định nghĩa lại |
| ★ **Chặng phễu & khe rò** — ①→⑦, `K1`–`K9` | ★ **`tb-C` · `tb-E`** *(sổ này)* | ✅ Đây là phần agent này **sở hữu** |
| ★ **Độ trễ** — ba trung vị | ★ **`tb-C` §6** | ✅ Sở hữu |

⚠️ **Va chạm mã phải nhớ:** `Agent-QC-Telesale` dùng **`K1`–`K6`** cho **sáu nhóm tiêu chí chấm cuộc gọi**. Repo này dùng **`K1`–`K9`** cho **chín khe rò phễu**. **Cùng chữ `K`, hai nghĩa.**

```
★ Quy ước BẮT BUỘC khi viết: luôn ghi kèm ngữ cảnh.
    "khe K3"        → khe rò của repo này
    "nhóm QC K3"    → nhóm tiêu chí của Agent-QC-Telesale

⛔ KHÔNG viết "K3" trơ trọi trong bất cứ báo cáo nào.
⛔ KHÔNG đổi tên bộ nào — cả hai đã dùng trong tài liệu đang lưu hành.
```

★ Đây là một va chạm **đã biết và đã ghi**, ⛔ không phải một lỗi chờ phát hiện. Cách xử giống cách `Agent-InsightDashboard-KNQT` xử va chạm `id-L`: **ghi lại, ⛔ không đổi tên**.

---

## 2. ★ BA ĐƠN VỊ ĐẾM — ⛔ ĐỪNG TRỘN

> Trộn ba đơn vị này là sai số âm thầm hay gặp nhất của báo cáo telesale.

| Đơn vị | Là gì | Nguồn xuất ra | Dùng cho |
|---|---|---|---|
| **CUỘC** | Một lần bấm gọi | ★ Tổng đài xuất ra **cái này** | Tải việc · năng suất · `K4` |
| **LEAD** | Một khách hàng tiềm năng | ★ Phễu cần **cái này** | Mọi tỷ lệ chuyển đổi (`tb-C`) |
| **CA** | Một dịch vụ đã chốt | CRM / Kế toán | Chặng ⑥ · doanh số |

```
Một LEAD có thể nhận 6 CUỘC và sinh ra 2 CA.

⛔ SAI :  tỷ lệ kết nối = số cuộc nói được ÷ số cuộc gọi ra
✅ ĐÚNG:  tỷ lệ kết nối = số LEAD nói được ÷ số LEAD đã gọi
```

★ **Vì sao quan trọng:** một khối gọi lại nhiều lần sẽ có *"tỷ lệ kết nối theo cuộc"* **thấp** nhưng *"theo lead"* **cao** — tức là họ đang làm **đúng**. Đo theo cuộc rồi kết luận *"kết nối kém"* là **phạt đúng cái việc nên khen**.

⚠️ Mọi con số trong báo cáo phải ghi rõ đơn vị: `340 lead (1.180 cuộc)`. ⛔ Không in số trơ trọi.

---

## 3. CHỈ SỐ AGENT NÀY SỞ HỮU — ĐỊNH NGHĨA ĐỦ

| Chỉ số | Công thức | Đơn vị | Điều kiện |
|---|---|---|---|
| `tl_goi` | `đã gọi ÷ data nhận` | lead | ★ Cohort |
| `tl_ket_noi` | `kết nối ÷ đã gọi` | lead | ★ Cohort |
| `tl_hen` | `đặt hẹn ÷ kết nối` | lead | ★ Cohort |
| ★ `tl_den_kham` | `đến khám ÷ đặt hẹn` | lead | ★ Cohort · ⛔ không suy từ cột khác |
| `tl_chot` | `ca chốt ÷ đến khám` | ca/lead | ★ Cohort · ⚠️ khe `K7`, ⛔ không phải của khối |
| `tl_phe_u` | `ca chốt ÷ data nhận` | — | ★ Cohort **ĐÃ ĐÓNG**. ⛔ Không đọc khi cohort còn chạy |
| `tre_goi_1` | Trung vị `data nhận → gọi lần 1` | giờ | — |
| `tre_hen` | Trung vị `kết nối → đặt hẹn` | ngày | — |
| `tre_den` | Trung vị `đặt hẹn → đến khám` | ngày | ★ Quyết định ngưỡng đóng cohort |
| `tai_viec` | Số lead/người trong kỳ | lead | `K8` |
| `ton_data` | Số lead quá `n` ngày chưa xử lý xong | lead | `K9` · `n` do khối chốt |

⛔ **Mười một chỉ số trên là toàn bộ.** Cần thêm một chỉ số → nó phải **thay** một cái ở đây, hoặc thuộc sổ khác. ⛔ Không thêm chỉ số thứ mười hai mà ⛔ không nói nó thay cái gì (`tb-A` §4 luật nghỉ mục).

---

## 4. ★★ NGƯỠNG — ⛔ AGENT ⛔ KHÔNG TỰ ĐẶT

```
Mọi ngưỡng trong repo này đều là  ⚠ chưa có ngưỡng  cho tới khi KHỐI CHỐT.

⛔ KHÔNG lấy trung bình ba kỳ gần nhất làm ngưỡng.
   → Đó là lấy hiện trạng làm chuẩn: khối đang kém thì ngưỡng cũng kém,
     và báo cáo sẽ nói "đạt" trong khi thực tế đang rò.

⛔ KHÔNG lấy ngưỡng của khối khác, brand khác, hay của một agent khác.
⛔ KHÔNG lấy con số trong tài liệu đào tạo làm ngưỡng nếu nó chưa được chốt
   CHO KỲ NÀY.
```

### Chưa có ngưỡng thì báo cáo làm gì

```
✅ In SỐ THẬT, kèm mẫu số.
✅ In XU HƯỚNG ba cohort đã đóng gần nhất — xu hướng đọc được mà
   ⛔ không cần ngưỡng.
✅ In "⚠ chưa có ngưỡng — ⛔ chưa so được đạt/chưa đạt".
⛔ KHÔNG dùng chữ "thấp", "kém", "tốt", "ổn" cho một con số
   chưa có ngưỡng. Đó là gán một phán xét mà ⛔ không có căn cứ.
```

★ **Ngoại lệ duy nhất:** một con số **về 0** hoặc **bằng toàn bộ mẫu** thì gọi tên được ngay, ⛔ không cần ngưỡng — vì đó là **sự cố**, ⛔ không phải một mức. Ví dụ: *"nhóm 3 ⛔ không gọi cuộc nào hôm nay"*.

---

## 5. ⛔ BA CHỈ SỐ ⛔ KHÔNG ĐƯỢC TẠO RA

```
① ⛔ KHÔNG tạo "ĐIỂM TỔNG" cho một nhân viên.
   Agent-QC-Telesale CỐ TÌNH không cho điểm số (ts-B §2), vì cuộc gọi có
   nhóm phụ thuộc audio và bản ghi hay mất tiếng. Quy K1–K6 của QC thành
   một con số ở đây là phá đúng cái luật đó, bằng đường vòng.

② ⛔ KHÔNG tạo "XẾP HẠNG" nhân viên trong báo cáo tổng hợp.
   ts-G §2 · tb-G §3. Lát cắt theo người dùng để BIẾT KÈM AI,
   ⛔ không để xếp ai trên ai.

③ ⛔ KHÔNG tạo "TIỀN MẤT" bằng cách nhân lead mất với một giá trị đơn
   tự đặt (tb-E §6). Chưa có giá trị đơn do khối chốt thì xếp theo
   SỐ LEAD, và nói rõ đã xếp theo cách đó.
```

---

## 6. TỰ KIỂM SỔ NÀY

- [ ] Có chỉ số nào **mới** được đặt ra mà ⛔ không thay cái nào cũ không?
- [ ] Có chỗ nào viết `K3` **trơ trọi** mà ⛔ không ghi *"khe"* hay *"nhóm QC"* không?
- [ ] Mọi tỷ lệ kết nối đếm theo **lead** chưa, hay theo cuộc?
- [ ] Mọi con số có **ghi đơn vị** *(cuộc / lead / ca)* chưa?
- [ ] Có ngưỡng nào **tự đặt** không — kể cả dạng *"trung bình ba kỳ"*?
- [ ] Có dùng chữ *"thấp / kém / tốt"* cho con số **chưa có ngưỡng** không?
- [ ] Có **điểm tổng** hay **xếp hạng** nhân viên nào trong báo cáo không?
- [ ] Có con số *"tiền mất"* nào nhân từ một giá trị đơn **tự đặt** không?
