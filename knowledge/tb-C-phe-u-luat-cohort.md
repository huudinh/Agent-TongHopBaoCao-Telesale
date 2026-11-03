# tb-C · ★★ PHỄU MỘT MẠCH · LUẬT COHORT

> Sổ khó nhất của repo, và là **lý do agent này tồn tại**.
> Bốn nguồn rời ⛔ không tự nối được với nhau — vì **mỗi nguồn đếm theo một mốc thời gian khác**.
> ⛔ Chưa đọc hết §3 thì ⛔ không được chia một con số của nguồn này cho một con số của nguồn khác.

---

## 1. PHỄU TELESALE — BẢY CHẶNG

```
① DATA NHẬN   →  ② ĐÃ GỌI  →  ③ KẾT NỐI  →  ④ ĐẶT HẸN  →  ⑤ ĐẾN KHÁM  →  ⑥ CA CHỐT  →  ⑦ DOANH SỐ
   nguồn ②        nguồn ①       nguồn ①       nguồn ③        ★ nguồn ③       nguồn ④        nguồn ④
```

| # | Chặng | Định nghĩa | Nguồn sở hữu | Mốc của nguồn đó |
|---|---|---|---|---|
| ① | **Data nhận** | Số lead được phân về khối trong kỳ | ② Data phân bổ | **Ngày nhận data** |
| ② | **Đã gọi** | Số lead có ít nhất **một** cuộc gọi ra | ① Tổng đài | **Ngày gọi** |
| ③ | **Kết nối** | Số lead **nói được** với khách *(⛔ không phải số cuộc gọi)* | ① Tổng đài | **Ngày gọi** |
| ④ | **Đặt hẹn** | Số lead có lịch hẹn được tạo | ③ Lịch hẹn | **Ngày tạo hẹn** |
| ⑤ | ★ **Đến khám** | Số lead **đến thật** *(show-up)* | ③ Lịch hẹn | **Ngày hẹn** |
| ⑥ | **Ca chốt** | Số ca khách đồng ý và ký | ④ Doanh số | **Ngày chốt** |
| ⑦ | **Doanh số** | Tiền | ④ Doanh số | ★ `so-B` câu 2 |

★ **Chặng ⑤ là chặng quan trọng nhất và hay bị bỏ nhất.** Nhiều báo cáo nhảy từ *đặt hẹn* sang *ca chốt* — nghĩa là **bỏ mất khe rò nặng nhất của telesale**: khách nhận hẹn rồi ⛔ không đến. ⛔ **Không được lấy *đặt hẹn* thay cho *đến khám*.** ⛔ Không có số đến khám → ghi `⚠ chưa đo được show-up` và **để trống**.

⚠️ **Chặng ③ ⛔ không phải số cuộc gọi.** Một lead bị gọi 6 lần mới nói được là **1 kết nối**, ⛔ không phải 6. Tổng đài xuất ra **số cuộc**; phễu cần **số lead**. Đổi đơn vị sai ở đây làm mọi tỷ lệ phía sau sai theo (`tb-D` §2).

---

## 2. ⛔ VÌ SAO ⛔ KHÔNG CHIA SỐ CỦA HÔM NAY CHO NHAU

> Đây là sai số lớn nhất của mọi báo cáo tổng hợp telesale, và nó ⛔ **không nhìn ra được từ bảng**.

Một lead đi qua phễu **mất nhiều ngày**:

```
Thứ 2  09:00  data về                    → đếm vào "data nhận" NGÀY THỨ 2
Thứ 3  14:20  gọi lần 1, không bắt máy   → đếm vào "đã gọi"    NGÀY THỨ 3
Thứ 4  10:05  gọi lần 2, nói được        → đếm vào "kết nối"   NGÀY THỨ 4
Thứ 5  16:40  đặt hẹn cho thứ 7          → "đặt hẹn" THỨ 5 · "đến khám" THỨ 7
Thứ 7  10:00  đến khám                   → đếm vào "đến khám"  NGÀY THỨ 7
Tuần sau      chốt ca                    → "ca chốt" TUẦN SAU
```

★ **Nghĩa là:** `ca chốt hôm nay` ⛔ **không** đến từ `data nhận hôm nay`.

```
⛔ SAI :  tỷ lệ chốt hôm nay = ca chốt hôm nay ÷ data nhận hôm nay
```

Con số đó ⛔ không có nghĩa gì, và nó sai **theo hai chiều cùng lúc**: data về nhiều hôm nay thì tỷ lệ tụt *(dù ⛔ chưa ai làm gì sai)*; data về ít hôm nay thì tỷ lệ vọt *(dù ⛔ chưa ai làm gì tốt)*.

⚠️ Và nó **luôn khớp tổng**, nên ⛔ không ai phát hiện ra.

---

## 3. ★★ HAI CÁCH ĐỌC — MỖI CÁCH TRẢ LỜI MỘT CÂU KHÁC NHAU

Agent này **luôn in cả hai**, và **ghi rõ cách nào đang dùng**.

### Cách ① · ĐỌC THEO NGÀY VIỆC *(hoạt động)*

> **Câu trả lời:** *"Hôm nay khối làm được bao nhiêu việc?"*

Mỗi chặng đếm theo **mốc của chính nguồn đó**, ⛔ **không chia chặng này cho chặng kia**.

```
NGÀY 03/11 — HOẠT ĐỘNG                     ⛔ CÁC SỐ NÀY KHÔNG CHIA CHO NHAU
  data nhận   : 120
  đã gọi      : 340 lead  (1.180 cuộc)
  kết nối     : 215 lead
  đặt hẹn     :  48
  đến khám    :  31
  ca chốt     :  12
```

✅ **Dùng được:** so từng dòng với **ngưỡng tuyệt đối** của khối · phát hiện **sự cố** *(một dòng về 0)* · xem **tải việc**.
⛔ **⛔ Không dùng được:** tính tỷ lệ chuyển đổi · kết luận hiệu quả · so hiệu suất hai nhóm.

### Cách ② · ĐỌC THEO COHORT *(hiệu quả)*

> **Câu trả lời:** *"Lô data về ngày X cuối cùng ra được bao nhiêu?"*

**Khoá lô theo `ngày nhận data`**, rồi theo **chính lô đó** đi suốt phễu, **bất kể việc xảy ra ngày nào**.

```
COHORT: data nhận 27/10  (n = 120 lead)        ← mẫu số CỐ ĐỊNH là 120
  đã gọi      : 118   98%          ✅ chia được, vì cùng một lô
  kết nối     :  74   62%
  đặt hẹn     :  29   24%
  đến khám    :  18   15%
  ca chốt     :   9    7,5%
  doanh số    : …
  ⏳ cohort CHƯA ĐÓNG — còn 6 lead đang hẹn, 11 lead chưa gọi đủ 5 lần
```

✅ **Chỉ cách này tính được tỷ lệ chuyển đổi.** Mẫu số là **một lô cố định**.

### ★ Luật cửa sổ chín — ⛔ cohort chưa đóng thì ⛔ chưa kết luận

```
Một cohort CHƯA ĐÓNG khi còn lead đang ở giữa phễu.
Ngưỡng đóng mặc định đề nghị:  `⚠ chờ khối chốt`   ⛔ KHÔNG tự đặt.

⚠ Đọc một cohort chưa đóng là đọc một con số CHẮC CHẮN CÒN TĂNG.
  → Luôn in nhãn ⏳ CHƯA ĐÓNG + còn bao nhiêu lead đang ở giữa phễu.
  → ⛔ KHÔNG so một cohort chưa đóng với một cohort đã đóng.
    Đó là so một việc đang làm với một việc đã xong.
```

★ **Đây là lỗi so sánh kinh điển:** *"cohort tuần này 4%, tuần trước 7,5% → đang tụt"* — trong khi cohort tuần này **mới chạy 3 ngày**. ⛔ Không phải tụt; nó **chưa xong**.

---

## 4. BẢNG TRA — CÂU HỎI NÀO DÙNG CÁCH NÀO

| Câu hỏi của quản lý | Cách đọc | Kỳ |
|---|---|---|
| *"Hôm nay có ai không gọi cuộc nào không?"* | ① hoạt động | NGÀY |
| *"Data hôm nay về bao nhiêu, gọi hết chưa?"* | ① hoạt động | NGÀY |
| *"Tổng đài có lỗi gì không?"* | ① hoạt động | NGÀY |
| *"Tỷ lệ kết nối của khối đang là bao nhiêu?"* | ★ ② cohort | TUẦN |
| *"Data nguồn nào ra ca tốt hơn?"* | ★ ② cohort | TUẦN · THÁNG |
| *"Khe nào đang rò nặng nhất?"* | ★ ② cohort | TUẦN |
| *"Sau đào tạo có khá hơn không?"* | ★ ② cohort, **tách trước/sau** | THÁNG |
| *"Tháng này so tháng trước thế nào?"* | ② cohort, **chỉ các cohort ĐÃ ĐÓNG** | THÁNG |

⚠️ **Mọi câu hỏi có chữ *"tỷ lệ"* đều phải trả lời bằng cách ②.** ⛔ Không có ngoại lệ.

---

## 5. KHOÁ NỐI — NỐI BẰNG GÌ

Bốn nguồn chỉ nối được khi có **một khoá chung**:

| Khoá | Nối được gì | Điều kiện |
|---|---|---|
| ★ **`ma_lead`** | Cả bảy chặng | Lý tưởng. ⛔ Nếu không có thì phễu cohort ⛔ không dựng được |
| **`sdt_hash`** | Cả bảy chặng | Thay thế được, nhưng phải **hash trước khi ra khỏi hệ** (`tb-G` §2) |
| `ma_nv` + `ngày` | Chỉ cắt theo người | ⛔ Không dựng được cohort |
| Chỉ có số tổng mỗi nguồn | ⛔ Chỉ được cách ① | **Phải nói thẳng điều này ở đầu báo cáo** |

### ⛔ Khi ⛔ KHÔNG có khoá nối

> Đây là tình huống **rất hay gặp** ở kỳ đầu, và nó ⛔ không phải lý do để bịa.

```
⛔ KHÔNG có ma_lead và ⛔ KHÔNG có sdt_hash
  → ⛔ KHÔNG dựng được cohort
  → Báo cáo chỉ in được cách ① HOẠT ĐỘNG
  → In nguyên văn dòng này lên đầu báo cáo:

    "⚠ Kỳ này CHƯA NỐI ĐƯỢC bốn nguồn (thiếu khoá lead dùng chung).
     Mọi số dưới đây là SỐ VIỆC TRONG NGÀY, ⛔ KHÔNG phải tỷ lệ chuyển đổi.
     ⛔ Không chia các dòng cho nhau.
     → Việc chặn: cấp mã lead dùng chung — <ai cấp>."
```

⚠️ ⛔ **Không lấy tổng chia tổng rồi gọi nó là tỷ lệ chuyển đổi.** Đó chính là cái sai của §2, chỉ là viết gọn hơn.

---

## 6. ĐỘ TRỄ — CON SỐ PHẢI ĐO, ⛔ KHÔNG ĐƯỢC ĐOÁN

Mỗi cohort đo thêm **ba độ trễ trung vị** *(trung vị, ⛔ không phải trung bình — một lead chốt sau 90 ngày sẽ kéo lệch trung bình)*:

```
data nhận → gọi lần 1    : ? giờ      ★ chỉ số của KHÂU PHÂN BỔ
kết nối   → đặt hẹn      : ? ngày     ★ chỉ số của KHÂU TƯ VẤN
đặt hẹn   → đến khám     : ? ngày     ★ chỉ số của KHÂU NHẮC HẸN
```

★ **Ba con số này quyết định `ngưỡng đóng cohort`.** Nếu trung vị `đặt hẹn → đến khám` là 5 ngày, thì một cohort 3 ngày tuổi ⛔ **chưa thể** có số đến khám đúng — và đọc nó là đọc một con số đang chạy.

⚠️ `data nhận → gọi lần 1` là độ trễ **đắt nhất**: lead để quá lâu thì tỷ lệ kết nối tụt theo, và đó ⛔ **không phải lỗi người gọi** — đó là khâu phân bổ (`tb-E` khe `K1`).

---

## 7. ⛔ LUẬT KHÔNG CỘNG NGANG

> Kế thừa `so-B` §2 và `ts-F` §3 — ⛔ không viết lại, chỉ nhắc lại hệ quả cho agent này.

```
⛔ Bốn lát cắt (người · dịch vụ · nguồn data · ca trực) ⛔ KHÔNG cộng ngang.
   Cùng một lead xuất hiện ở cả bốn bảng.

⛔ Doanh số của báo cáo này ⛔ KHÔNG cộng với doanh số Cơ sở hay Tập đoàn
   của Agent-Order-SoLieu — khác trục, khác mốc (so-B §2).

★ Mọi tỷ lệ in kèm MẪU SỐ: `74/120 · 62%`. ⛔ Không in `62%` trơ trọi.
```

---

## 8. TỰ KIỂM SỔ NÀY

- [ ] Có chỗ nào chia **số của nguồn này** cho **số của nguồn khác** theo cùng một ngày không?
- [ ] Mọi tỷ lệ chuyển đổi có đi từ **cohort** không, hay đi từ số ngày?
- [ ] Cohort nào **chưa đóng** mà vẫn bị đem so với cohort đã đóng?
- [ ] Nhãn ⏳ **CHƯA ĐÓNG** + số lead đang ở giữa phễu có in chưa?
- [ ] Chặng **kết nối** đếm theo **lead** hay theo **cuộc gọi**?
- [ ] Chặng **đến khám** có bị thay bằng **đặt hẹn** không?
- [ ] ⛔ Không có khoá nối: đã in **nguyên văn dòng cảnh báo** §5 chưa, hay đã lấy tổng chia tổng?
- [ ] Ba độ trễ dùng **trung vị** hay trung bình?
- [ ] Mọi tỷ lệ có **mẫu số** đi kèm chưa?
