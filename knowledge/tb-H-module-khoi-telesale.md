# tb-H · MODULE KHỐI TELESALE KANGNAM

> **Module brand/khối.** Đây là file **duy nhất** trong `knowledge/` chứa dữ kiện riêng của khối. Dựng agent này cho một khối telesale khác = **thay file này**, ⛔ không sửa bảy sổ còn lại.
>
> ★ Đây là **sổ nhập từ ngoài**: dữ kiện ở đây do **khối cấp**, ⛔ không do repo suy ra. Bốn luật của sổ nhập từ ngoài ở §5.

---

## 1. ⛔ TÌNH TRẠNG: PHẦN LỚN SỔ NÀY CÒN TRỐNG

> ⚠️ **Đọc mục này trước khi dùng bất kỳ con số nào của repo.**

Repo được dựng **trước khi** khối cấp dữ kiện vận hành. Nghĩa là:

```
✅ CHẠY ĐƯỢC NGAY : đọc bốn nguồn · dựng phễu · dựng cohort · đo chín khe
                     · đo ba độ trễ · xuất ba báo cáo · đổi mã NV-xx
⏸ CHƯA CHẠY ĐƯỢC : so "đạt / chưa đạt" bất cứ chỉ số nào
                     · đóng cohort đúng lúc
                     · nói một khe là "nặng" hay "nhẹ"
```

★ Đó ⛔ **không phải lỗi của bộ công cụ** — đó là `tb-D` §4 đang làm đúng việc của nó: **⛔ không tự đặt ngưỡng**. Báo cáo vẫn ra số thật và xu hướng; nó chỉ ⛔ không phán xét.

---

## 2. ★★ MƯỜI SLOT KHỐI PHẢI CẤP

| # | Slot | Chặn gì | Ai cấp |
|---|---|---|---|
| ① | ★ **Bảy câu định nghĩa doanh số** (`so-B` §1) | **CỔNG Đ** — ⛔ chặn mọi con số doanh số | Quản lý khối + Kế toán |
| ② | ★ **Có mã lead dùng chung bốn nguồn chưa?** | ⛔ Chặn **toàn bộ phễu cohort** → chỉ còn đọc được cách ① hoạt động (`tb-C` §5) | IT / CRM |
| ③ | ★ **Ngưỡng đóng cohort** *(bao nhiêu ngày)* | ⛔ Chặn việc biết cohort nào đọc được (`tb-C` §3) | Quản lý khối — ★ suy được từ `tre_den` sau 2–3 kỳ |
| ④ | **Ngưỡng chín khe** `K1`–`K9` | ⛔ Chặn mọi câu *"đạt / chưa đạt"* | Quản lý khối |
| ⑤ | **Số ngày coi là "data tồn"** *(`n` của `K9`)* | ⛔ Chặn khe `K9` | Quản lý khối + phân bổ |
| ⑥ | **Khung giờ ca trực** | ⛔ Chặn lát cắt theo ca · đọc `K3` theo giờ | Vận hành |
| ⑦ | **Mốc "nhân viên mới"** *(dưới bao nhiêu tháng)* | ⛔ Chặn việc tách cũ/mới (`ts-F` §4) | Quản lý khối + Nhân sự |
| ⑧ | **Danh sách nhóm & người** → sinh `ma-nhan-vien.csv` | ⛔ Chặn lát cắt theo người và theo nhóm | Quản lý khối *(giữ riêng, `tb-G` §1)* |
| ⑨ | **Tên hệ thống nguồn** *(tổng đài nào · CRM nào)* | Chỉ ảnh hưởng dòng ③ ba dòng bắt buộc | Vận hành / IT |
| ⑩ | **Giá trị đơn trung bình** *(nếu muốn quy ra tiền)* | ⛔ Chặn việc xếp khe theo tiền mất (`tb-E` §6) | Quản lý khối — ⚠️ **không bắt buộc** |

★ **Slot ① và ② là hai slot chặn nặng nhất.** Thiếu ① thì ⛔ không in được doanh số; thiếu ② thì ⛔ **không có phễu** — và phễu là lý do tồn tại của repo.

⚠️ **Slot ⑩ ⛔ không bắt buộc, và đừng ép.** Thiếu nó thì xếp khe theo **số lead mất** — cách đó đã đủ để quyết sửa khe nào trước.

---

## 3. DỮ KIỆN ĐÃ BIẾT

| Hạng mục | Nội dung |
|---|---|
| **Thương hiệu** | Kangnam Korean Aesthetic Hospital *(HCI Group)* |
| **Khối** | Telesale — gọi ra trên data do Marketing và các nguồn khác cấp |
| **Mốc cuối của khối** | ★ **ĐẾN KHÁM** (chặng ⑤). Việc chốt xảy ra **trên ghế khám** → khe `K7` ⛔ không thuộc khối (`tb-E` §3) |
| **Agent cùng khối** | `Agent-QC-Telesale` *(chấm cuộc gọi)* · `Agent-Order-SoLieu` *(định nghĩa doanh số)* · `Agent-CRM-Automation` *(tái khai thác data tồn)* |

⚠️ **Mọi thứ khác — số nhóm, số người, khung giờ, tên hệ thống, ngưỡng — đều là slot ở §2.** ⛔ Repo ⛔ không suy ra, ⛔ không lấy của brand khác, ⛔ không lấy của khối khác.

---

## 4. ★ MỘT LUẬT RIÊNG CỦA KHỐI NÀY

> Khối Telesale **⛔ không điều khiển hai đầu phễu**.

```
ĐẦU VÀO  : data do Marketing / nguồn khác cấp.
            Chất lượng data xấu → khe K3 xấu, và đó ⛔ KHÔNG phải lỗi khối
            (tb-E §4). Khối chỉ điều khiển: gọi khi nào, gọi mấy lần, nói gì.

ĐẦU RA   : quyết định mua xảy ra TRÊN GHẾ KHÁM.
            Khe K7 ⛔ KHÔNG thuộc khối (tb-E §3).
```

★ **Nghĩa là phần khối thật sự điều khiển là chặng ② → ⑤** — bốn khe `K2` `K4` `K5` và một nửa `K3`. Mọi báo cáo phải làm rõ điều đó, nếu không khối sẽ bị đo bằng những thứ họ ⛔ không quyết được, và chỉ số sẽ **thôi phản ánh việc họ làm**.

⚠️ Và đó cũng là lý do `tb-E` §5 *(CỔNG V)* nặng ở agent này hơn ở các agent khác: **năm trong chín khe thường là lỗi hệ**.

---

## 5. LUẬT SỔ NHẬP TỪ NGOÀI

```
① GIỮ NGUYÊN VĂN dữ kiện khối cấp, để còn đối chiếu.
② Khối sửa thì sổ này sửa theo. ⛔ KHÔNG sửa ngược lại.
③ ⛔ Repo KHÔNG tự đặt thêm slot nào, ⛔ không tự điền slot trống.
   Thiếu thì BÁO LẠI để bổ sung ở bản sau.
④ Slot nào treo ≥3 kỳ → đưa LÊN ĐẦU báo cáo (tb-F §4 ⑦),
   ⛔ không để trong phụ lục.
```

★ Khi một slot được cấp, ghi vào `doc/CHANGELOG.md`: **slot nào · ai cấp · ngày · mở được khe nào**. Dòng cuối là dòng quan trọng — nó cho biết **việc cấp dữ kiện đó đổi được gì**, chứ ⛔ không chỉ là một ô đã điền.

---

## 6. TỰ KIỂM SỔ NÀY

- [ ] Có con số nào trong báo cáo **không** đến từ nguồn, mà đến từ sổ này **tự suy** không?
- [ ] Slot ① *(bảy câu định nghĩa)* đã cấp chưa? Nếu chưa, báo cáo có in doanh số không?
- [ ] Slot ② *(mã lead dùng chung)* đã có chưa? Nếu chưa, báo cáo có in **tỷ lệ chuyển đổi** nào không?
- [ ] Có ngưỡng nào trong báo cáo **không** đến từ slot ④ không?
- [ ] Khe `K3` và `K7` có được ghi rõ là **⛔ không hoàn toàn thuộc khối** chưa? (§4)
- [ ] Slot nào treo ≥3 kỳ đã lên **đầu** báo cáo chưa?
- [ ] `ma-nhan-vien.csv` có đang nằm ngoài repo và ngoài `out/` chưa? (`tb-G` §1)
