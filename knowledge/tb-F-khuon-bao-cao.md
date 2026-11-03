# tb-F · KHUÔN BA BÁO CÁO · BA DÒNG BẮT BUỘC

> Sổ này là thứ quản lý **thật sự đọc**. Ba khuôn, ⛔ không phải một khuôn ba cỡ (`tb-A` §3).

---

## 1. ★★ BA DÒNG BẮT BUỘC — IN TRÊN **MỌI** BÁO CÁO

> Gộp từ `so-B` §2 *(định nghĩa doanh số)* và `ts-F` §2 *(mẫu)*, cộng một dòng riêng của agent tổng hợp.

```
① ĐỊNH NGHĨA  : doanh số [ghi nhận/thực thu/đã thực hiện] · mốc [chốt/thực hiện/thu tiền]
                 · phạm vi [khách nào · gồm/trừ gì]
② MẪU & KỲ    : cohort [ngày nhận data] n=120 · [ĐÃ ĐÓNG / ⏳ chưa đóng, còn n lead]
                 · kỳ 27/10–02/11
③ ★ NGUỒN     : ① tổng đài ✅ 03/11 08:15 · ② data ✅ 07:40 · ③ lịch hẹn ⚠️ CŨ 02/11
                 · ④ doanh số ⛔ THIẾU
                 → ⛔ KHÔNG tính được: K6 · K7 · chặng ⑥⑦
```

⛔ **Thiếu một trong ba dòng thì ⛔ không phát hành.** Mỗi dòng chặn một kiểu đọc sai:

| Thiếu | Hậu quả |
|---|---|
| ① | Bảng này bị đem so với sổ Kế toán, và cuộc họp nói về **định nghĩa** thay vì nói về việc |
| ② | `62%` ⛔ không biết là `74/120` hay `5/8`; và ⛔ không biết cohort đã xong chưa |
| ③ ★ | **Dòng riêng của agent tổng hợp.** Thiếu nó thì một tỷ lệ có mẫu số hụt trông y như một tỷ lệ thật |

★ **Mọi tỷ lệ in kèm mẫu số:** `74/120 · 62%`. ⛔ Không in `62%` trơ trọi.
★ **Mọi con số ghi đơn vị:** `340 lead (1.180 cuộc)`. ⛔ Không trộn cuộc với lead (`tb-D` §2).

---

## 2. KHUÔN BÁO CÁO **NGÀY** — điều hành

> **Một màn hình.** Quản lý đọc lúc đầu giờ để biết **hôm nay làm gì**. ⛔ Không có xu hướng, ⛔ không có xếp hạng.

```
BÁO CÁO NGÀY · <ngày> · Khối Telesale Kangnam
[ba dòng bắt buộc §1]

① HOẠT ĐỘNG HÔM QUA/HÔM NAY          ← cách ① của tb-C §3, ⛔ KHÔNG chia cho nhau
   data nhận  120 lead
   đã gọi     340 lead  (1.180 cuộc)
   kết nối    215 lead
   đặt hẹn     48
   đến khám    31
   ca chốt     12                      ⚠️ nguồn ④ cập nhật tới <giờ>

② ⛔ SỰ CỐ — cần xử trong hôm nay      ← chỉ in khi CÓ, ⛔ không in mục rỗng
   · nhóm 3: ⛔ 0 cuộc gọi cả buổi sáng          → <người nhận>
   · data về 0 từ 14h, tồn 62 lead chưa giao     → <người nhận>
   · tổng đài mất kết nối 11:20–12:05            → <người nhận>

③ SO NGƯỠNG                            ← ⛔ KHÔNG so với hôm qua
   tỷ lệ gọi hết data   118/120 · 98%   ⚠ chưa có ngưỡng
   tải việc lệch nhất   NV-03 62 lead / NV-11 19 lead   ⚠ chưa có ngưỡng

④ ⏸ CHƯA ĐO ĐƯỢC
   · K6 no-show — nguồn ③ cũ 1 ngày
```

### ⛔ Bốn thứ báo cáo NGÀY ⛔ không được có

```
⛔ "giảm 20% so với hôm qua"      → một ngày là mẫu nhiễu (tb-A §3)
⛔ bất kỳ tỷ lệ chuyển đổi nào    → tỷ lệ chỉ đọc được từ cohort (tb-C §3)
⛔ xếp hạng nhân viên             → tb-G §3 ④
⛔ mục rỗng "⛔ không có sự cố"    → in mục rỗng mỗi ngày thì mục đó
                                    thành vô hình đúng ngày có sự cố
```

★ **Mục ② là mục duy nhất quản lý đọc mỗi ngày.** Nên nó ⛔ không được loãng. Chỉ in **sự cố** — thứ về 0, thứ bằng toàn bộ mẫu, thứ dừng hẳn (`tb-D` §4 ngoại lệ).

---

## 3. KHUÔN BÁO CÁO **TUẦN** — chẩn đoán

> Đây là báo cáo **chính** của khối. Nó trả lời: *khe nào đang rò, vì sao, tuần tới ai làm gì.*

```
BÁO CÁO TUẦN · <kỳ> · Khối Telesale Kangnam
[ba dòng bắt buộc §1]

① PHỄU COHORT                          ← cách ② của tb-C §3
   cohort data nhận <ngày> · n=120 · ĐÃ ĐÓNG
     đã gọi    118/120  98%
     kết nối    74/120  62%
     đặt hẹn    29/120  24%
     đến khám   18/120  15%
     ca chốt     9/120  7,5%
   ★ So ba cohort ĐÃ ĐÓNG gần nhất, ⛔ không so với cohort đang chạy

② ĐỘ TRỄ (trung vị)
   data → gọi 1    : 6,5 giờ
   kết nối → hẹn   : 1,2 ngày
   hẹn → đến khám  : 4,8 ngày    ★ quyết định ngưỡng đóng cohort

③ ★★ BA KHE MẤT NHIỀU LEAD NHẤT        ← tb-E §6, xếp theo SỐ LEAD mất
   mỗi khe đủ sáu ô của tb-E §7

④ VIỆC CỦA KHỐI                        ← đã qua CỔNG V
   mỗi việc: làm gì · ai nhận · hạn · tuần sau nhìn chỉ số nào

⑤ ⛔ VIỆC HỆ THỐNG                      ← MỤC RIÊNG, ⛔ không gộp vào ④
   mỗi dòng: thiếu gì · chặn khe nào · ai cấp · cấp rồi gỡ được gì

⑥ LÁT CẮT THEO NGƯỜI                   ← mã NV-xx, ⛔ không tên
   NV-xx · n lead · khe yếu nhất · khe mạnh nhất
   [câu chân bảng của tb-G §4 rào ①]
   ⚠️ người dưới 10 cuộc: ghi "chưa đủ mẫu", ⛔ không nhận định

⑦ ⏸ CHƯA ĐO ĐƯỢC + KHE QUAY LẠI ≥2 KỲ  ← khe quay lại đưa LÊN ĐẦU nếu có
```

⚠️ **Mục ⑤ ⛔ không được gộp vào mục ④.** Gộp lại là cách một lỗi hệ được ghi thành việc của khối — và nó sẽ ở đó mãi (`tb-E` §1 ③).

★ **Mục ⑥ xếp theo gì:** xếp theo **số lead**, ⛔ không xếp theo khe yếu. Xếp theo khe yếu là **xếp hạng người** bằng đường vòng.

---

## 4. KHUÔN BÁO CÁO **THÁNG** — xu hướng & cơ cấu

> Báo cáo này **chỉ đọc cohort đã đóng**. Và nó phải chỉnh theo hai thứ trước khi nói bất cứ điều gì về xu hướng.

```
BÁO CÁO THÁNG · <tháng> · Khối Telesale Kangnam
[ba dòng bắt buộc §1]

① ⚠️ HAI ĐIỀU CHỈNH — in TRƯỚC mọi so sánh
   số ngày làm việc  : tháng này 24 · tháng trước 26   → ⛔ không so thẳng
   cơ cấu nhân sự    : +3 người mới, −1 nghỉ
                      → ⛔ KHÔNG kết luận xu hướng khi chưa tách cũ/mới

② PHỄU THEO THÁNG — chỉ cohort ĐÃ ĐÓNG
   ⚠️ Cohort của những ngày cuối tháng thường CHƯA ĐÓNG
      → ⛔ không gộp vào số tháng. Ghi riêng "n cohort chưa đóng, loại khỏi so sánh"

③ XU HƯỚNG BA THÁNG — từng chặng, kèm hai điều chỉnh ở ①

④ TÁCH CŨ / MỚI                        ← ts-F §4
   nhóm cũ (≥3 tháng) · nhóm mới (<3 tháng), ⛔ không gộp một tỷ lệ chung

⑤ HIỆU QUẢ ĐÀO TẠO                     ← nối Agent-QC-Telesale
   trước/sau đào tạo · ⚠️ CÙNG người · CÙNG nhóm dịch vụ · CÙNG tiêu chí

⑥ KHE SỐNG DAI — khe qua ≥2 kỳ mà số ⛔ không đổi (tb-E §8)
   ★ khe sang kỳ thứ 3 → ⛔ không còn là việc của trưởng nhóm, ghi thẳng điều đó

⑦ VIỆC HỆ THỐNG CÒN TREO — kèm số kỳ đã treo
   ★ treo ≥3 kỳ → đưa LÊN ĐẦU báo cáo, ⛔ không để phụ lục
```

⚠️ **Mục ① là mục ⛔ không được bỏ.** *"Tháng này giảm 12%"* có khi chỉ là *"tháng này ít hơn 2 ngày làm việc"* (`so-C` §③). Và *"mọi chỉ số tiến trình đều tụt"* có khi chỉ là *"vừa tuyển 3 người"* (`ts-F` §4).

---

## 5. KHUÔN `VẤN ĐỀ` — lệnh quản lý dùng nhiều nhất

> Bỏ hết số nền. Chỉ còn **cái đang tắc + ai sửa**. Chạy được cho cả ba kỳ.

```
VẤN ĐỀ · <kỳ> · Khối Telesale Kangnam
[ba dòng bắt buộc §1 — vẫn bắt buộc, ⛔ không rút gọn]

🔴 KHE QUAY LẠI ≥2 KỲ            ← nếu có, LÊN ĐẦU
🔴 BA KHE MẤT NHIỀU LEAD NHẤT    ← sáu ô mỗi khe (tb-E §7)
🟠 VIỆC CỦA KHỐI                 ← ai nhận · hạn
⛔ VIỆC HỆ THỐNG                  ← ai cấp · gỡ được gì
⏸ CHƯA ĐO ĐƯỢC                   ← thiếu gì mới đo được
ℹ️  K7 — mục riêng, kèm đúng dòng của tb-E §3
```

★ **Ba dòng bắt buộc vẫn phải in**, dù đây là bản ngắn nhất. Một danh sách vấn đề ⛔ không khai mẫu và nguồn thì ⛔ không ai kiểm lại được, và nó biến thành một danh sách ý kiến.

---

## 6. GIỌNG — SÁU LUẬT VIẾT

```
① SỐ TRƯỚC, DIỄN GIẢI SAU.  "18/29 · 62% đến khám" rồi mới nói nghĩa.
② MỖI VIỆC CÓ: làm gì · ai nhận · hạn · đo bằng chỉ số nào.
   ⛔ Thiếu một trong bốn thì đó ⛔ không phải một việc, đó là một nhận xét.
③ ⛔ KHÔNG dùng "thấp · kém · tốt · ổn" cho con số CHƯA CÓ NGƯỠNG (tb-D §4).
④ ⛔ KHÔNG viết "nên cải thiện", "cần chú ý hơn", "tăng cường".
   Những câu đó ⛔ không chỉ ra việc gì và ⛔ không ai nhận được.
⑤ MỌI KẾT LUẬN TRUY NGƯỢC ĐƯỢC: về cohort nào, nguồn nào, mốc nào.
⑥ ⛔ KHÔNG nói về CON NGƯỜI. Nói về VIỆC và về KHE (tb-G §6).
```

★ **Phép thử luật ④:** đọc câu kết luận lên và hỏi *"ai sẽ làm gì vào thứ Hai?"* — ⛔ không trả lời được thì câu đó ⛔ chưa viết xong.

---

## 7. TỰ KIỂM SỔ NÀY

- [ ] **Ba dòng bắt buộc** §1 có trên **mọi** báo cáo, kể cả bản `VẤN ĐỀ`, chưa?
- [ ] Dòng ③ **nguồn + độ tươi** có liệt kê **khe nào ⛔ không tính được** chưa?
- [ ] Báo cáo **NGÀY** có tỷ lệ chuyển đổi nào không? Có so với hôm qua không?
- [ ] Mọi tỷ lệ có **mẫu số** chưa? Mọi số có **đơn vị** chưa?
- [ ] Báo cáo **TUẦN**: mục việc hệ thống có bị **gộp** vào mục việc của khối không?
- [ ] Mục lát cắt người xếp theo **số lead** hay theo khe yếu?
- [ ] Báo cáo **THÁNG**: đã in **hai điều chỉnh** *(ngày làm việc · cơ cấu nhân sự)* **trước** mọi so sánh chưa?
- [ ] Cohort **chưa đóng** có bị gộp vào số tháng không?
- [ ] Có câu nào dạng *"nên cải thiện"* mà ⛔ không có người nhận không?
- [ ] Mọi việc có đủ **bốn thứ** *(làm gì · ai · hạn · đo bằng gì)* chưa?
