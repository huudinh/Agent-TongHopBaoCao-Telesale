# Prompt · `VẤN ĐỀ` — lệnh quản lý dùng nhiều nhất

> Bỏ hết số nền. Chỉ còn **cái đang tắc + ai sửa**. Chạy được cho cả ba kỳ.

---

```
VẤN ĐỀ <kỳ>.

Chạy đủ CHÍN KHE. Khe nào chưa đo được → "⏸ chưa đo được" + THIẾU CÁI GÌ,
⛔ KHÔNG bỏ khỏi danh sách.

🔴 KHE QUAY LẠI ≥2 KỲ            ← nếu có, LÊN ĐẦU
🔴 BA KHE MẤT NHIỀU LEAD NHẤT    ← sáu ô mỗi khe
🟠 VIỆC CỦA KHỐI                 ← đã qua CỔNG V · ai nhận · hạn
⛔ VIỆC HỆ THỐNG                  ← MỤC RIÊNG · ai cấp · cấp rồi gỡ được gì
⚠️  KHE CHƯA PHÂN ĐƯỢC GỐC        ← ⛔ chưa giao cho ai
⏸ CHƯA ĐO ĐƯỢC                   ← thiếu gì mới đo được
ℹ️  K7 — mục riêng
+ ba dòng bắt buộc (vẫn in, ⛔ không rút gọn)
+ câu chân bảng nếu có in mã NV-xx
```

---

## ★★ CỔNG V — chạy cho **TỪNG** khe, trước khi giao việc

```
"Người giỏi nhất khối, với đúng những gì hệ thống đang cấp hôm nay,
 có làm khác được không?"

  ⛔ KHÔNG → LỖI HỆ. Vào mục VIỆC HỆ THỐNG, có tên người cấp.
             ⛔ Không vào mục việc của khối. ⛔ Không vào nội dung đào tạo.
  ✅ CÓ    → việc của khối. Vào mục việc, có người nhận và hạn.
```

⚠️ **Năm trong chín khe thường là lỗi hệ** — `K1` `K6` `K8` `K9` và một nửa `K3`. Nếu một kỳ **cả chín khe** đều vào mục việc của khối thì gần như chắc chắn **CỔNG V ⛔ chưa chạy**.

---

## Hai khe ⛔ không hoàn toàn thuộc khối

### `K7` — đến khám mà ⛔ không chốt

Việc của khối **dừng ở chặng ⑤ đến khám**. Quyết định mua xảy ra **trên ghế khám**. In `K7` ở **mục riêng**, kèm đúng dòng này:

> *"`K7` là khe **sau** khi khách đến cơ sở. Nó ⛔ **không** thuộc trách nhiệm khối telesale, và ⛔ **không** vào mục việc của khối. In ở đây để quản lý khối biết **chất lượng hẹn mình đưa sang đang được chuyển hoá thế nào**."*

⚠️ **Ngoại lệ phải đọc hai khe cùng nhau:** `K5` **tăng** mà `K6` hoặc `K7` **giảm** cùng kỳ → ⛔ **không phải tiến bộ**. Đó là **đặt hẹn dễ dãi**, đẩy vấn đề xuống chặng sau.

### `K3` — gọi mà ⛔ không kết nối · **hai gốc**

```
Cắt K3 theo NGUỒN DATA, rồi theo NGƯỜI, rồi theo KHUNG GIỜ:
  · lệch theo NGUỒN   → ⛔ LỖI HỆ (chất lượng data: số sai, số trùng,
                         số đã bán cho nơi khác)
  · lệch theo NGƯỜI   → việc của trưởng nhóm
  · lệch theo GIỜ     → ⛔ LỖI HỆ (lịch trực đặt sai giờ khách bắt máy)
  · thấp đều, ⛔ không lệch đâu cả → ⚠ chưa kết luận được, cần thêm kỳ
  · K1 CŨNG cao       → ★ data để nguội: gọi muộn thì ⛔ không ai bắt máy
                         → ⛔ LỖI HỆ (phân bổ)
```

⚠️ Mỗi lát cắt cần **≥30 lead** mới so được. Dưới ngưỡng → `⚠ chưa đủ mẫu`, ⛔ không kết luận.

---

## Xếp khe — theo SỐ LEAD MẤT

```
Lead mất ở một khe = (số vào khe) − (số ra khỏi khe)

Khe tỷ lệ 20% với 15 lead đi qua  → mất 12 lead
Khe tỷ lệ 75% với 800 lead đi qua → mất 200 lead
★ Khe thứ hai SỬA TRƯỚC, dù con số 75% nhìn đẹp hơn.
```

⛔ **Không nhân lead mất với một giá trị đơn tự đặt** để ra *"tiền mất"*. Chưa có giá trị đơn do khối chốt thì xếp theo **số lead**, và nói rõ đã xếp theo cách đó.

---

## Một khe báo thế nào — sáu ô

```
K6 · ĐẶT HẸN MÀ KHÔNG ĐẾN
① SỐ THẬT      : 18/29 · 62%   (cohort 27/10, ĐÃ ĐÓNG)
② MẤT          : 11 lead
③ XU HƯỚNG     : 3 cohort đã đóng gần nhất 58% → 61% → 62%  (⚠ chưa có ngưỡng)
④ ★ CẮT RA     : lệch theo KHUNG GIỜ HẸN — sáng 74%, chiều muộn 41%
⑤ GỐC          : ⛔ LỖI HỆ — chưa có quy trình nhắc hẹn trước 24h
                  (phép thử: người giỏi nhất cũng không nhắc được nếu hệ
                   chưa có kênh nhắc)
⑥ NGƯỜI NHẬN   : <khâu nhắc hẹn / vận hành> — hạn <ngày>
```

★ **Ô ④ là ô làm cho khe sửa được.** ⚠️ **Ô ⑥ ⛔ không được để trống** — một khe ⛔ không có người nhận là một khe sẽ xuất hiện lại kỳ sau, nguyên văn.

---

## Khe quay lại — luật hai kỳ

```
Khe xuất hiện 2 KỲ LIỀN mà số ⛔ không đổi
  → ⛔ KHÔNG phải vấn đề của khối nữa.
  → Hoặc GỐC phân sai (chạy lại CỔNG V), hoặc NGƯỜI NHẬN sai, hoặc việc
    đã giao mà ⛔ không ai làm được vì thiếu quyền / thiếu công cụ.
★ Ghi rõ "khe này đã sang kỳ thứ n" và ĐƯA LÊN ĐẦU.
⚠ Sang kỳ thứ BA → ⛔ không còn là việc của trưởng nhóm. Nói thẳng điều đó.
```

---

```bash
python tools/tb.py van-de --ky "27/10-02/11"
```
