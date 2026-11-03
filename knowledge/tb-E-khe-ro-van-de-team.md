# tb-E · ★★ CHÍN KHE RÒ · "VẤN ĐỀ TEAM ĐANG GẶP"

> Sổ này biến một bảng số thành **một danh sách việc có người nhận**.
> ⛔ Chưa đọc hết §5 thì ⛔ không được đưa khe nào vào mục *"vấn đề của team"*.

---

## 1. VÌ SAO PHẢI CÓ BỘ KHE CỐ ĐỊNH

Nếu mỗi kỳ agent tự nhìn bảng rồi *"nhận xét"*, sẽ xảy ra ba chuyện:

```
① Kỳ nào cũng ra một danh sách khác nhau → ⛔ không theo dõi được việc nào
   đã sửa, việc nào quay lại.
② Khe nào SỐ NHÌN GIỜ XẤU NHẤT thì được nhắc — ⛔ không phải khe nào
   ĐANG MẤT NHIỀU NHẤT.
③ Khe thuộc HỆ THỐNG bị viết thành khe của khối, và khối bị đào tạo về
   một việc ⛔ không phải của họ — kỳ này qua kỳ khác.
```

★ Nên bộ khe là **cố định, có mã, có ngưỡng, có người nhận**. Kỳ nào cũng chạy đủ chín khe; khe nào **chưa đo được** thì ghi `⏸ chưa đo được` kèm lý do — ⛔ **không bỏ khỏi danh sách**.

---

## 2. CHÍN KHE — BẢNG CHÍNH

| Mã | Khe | Đo bằng | Thuộc chặng | Người nhận mặc định |
|---|---|---|---|---|
| **`K1`** | **Data để nguội** | Trung vị `data nhận → gọi lần 1` | ①→② | Khâu **phân bổ** |
| **`K2`** | **Data chưa gọi hết** | % lead trong cohort ⛔ chưa có cuộc nào | ①→② | **Trưởng nhóm** |
| **`K3`** | **Gọi mà ⛔ không kết nối** | `kết nối ÷ đã gọi` *(theo lead)* | ②→③ | ★ Xem §4 — **hai gốc** |
| **`K4`** | **Bỏ lead quá sớm** | Trung vị số lần gọi trước khi lead bị dừng | ②→③ | **Trưởng nhóm** |
| **`K5`** | **Kết nối mà ⛔ không đặt được hẹn** | `đặt hẹn ÷ kết nối` | ③→④ | **Đào tạo** *(nối `Agent-QC-Telesale`)* |
| **`K6`** | ★ **Đặt hẹn mà ⛔ không đến** *(no-show)* | `đến khám ÷ đặt hẹn` | ④→⑤ | Khâu **nhắc hẹn** |
| **`K7`** | **Đến khám mà ⛔ không chốt** | `ca chốt ÷ đến khám` | ⑤→⑥ | ⚠️ **⛔ KHÔNG phải khe của khối** — xem §3 |
| **`K8`** | **Tải việc lệch** | Chênh lệch số lead/người giữa người cao nhất và thấp nhất | ngang | **Trưởng nhóm** |
| **`K9`** | **Data tồn dồn** | Số lead quá `n` ngày ⛔ chưa xử lý xong, và **xu hướng của nó** | tích luỹ | **Trưởng nhóm** + phân bổ |

⚠️ **Mọi ngưỡng đều là `⚠ chưa có ngưỡng` cho tới khi khối chốt.** ⛔ **Agent ⛔ không tự đặt ngưỡng** — xem `tb-D` §4. Chưa có ngưỡng thì khe vẫn được in, kèm **số thật + xu hướng**, và ghi rõ ⛔ chưa so được *"đạt / chưa đạt"*.

---

## 3. ★★ `K7` — KHE ⛔ KHÔNG PHẢI CỦA KHỐI TELESALE

> ⚠️ Đây là khe hay bị gán sai nhất, và gán sai nó làm khối telesale chịu một việc họ ⛔ không điều khiển được.

```
Khách ĐẾN KHÁM rồi mới quyết định mua. Quyết định đó xảy ra:
  · trên ghế khám, sau khi bác sĩ tư vấn
  · sau khi khách nhìn thấy cơ sở, giá cuối, lịch mổ
  · có khi sau khi về nhà bàn với người nhà

→ Việc của khối telesale DỪNG Ở CHẶNG ⑤ ĐẾN KHÁM.
```

★ **`K7` vẫn được in**, vì nó là thông tin quản lý cần. Nhưng nó in ở **mục riêng**, kèm đúng một dòng:

> *"`K7` là khe **sau** khi khách đến cơ sở. Nó ⛔ **không** thuộc trách nhiệm khối telesale, và ⛔ **không** vào mục việc của khối. In ở đây để quản lý khối biết **chất lượng hẹn mình đưa sang đang được chuyển hoá thế nào**."*

⚠️ **Nhưng có một ngoại lệ, và nó quan trọng:** nếu `K7` xấu **chỉ ở một nguồn data** hoặc **chỉ ở một nhóm dịch vụ**, thì có thể khối đang **đặt hẹn cho người chưa đủ sẵn sàng** — tức là `K5` tốt một cách giả tạo *(đặt hẹn dễ dãi)*. Lúc đó `K5` và `K7` phải **đọc cùng nhau**, ⛔ không đọc rời.

★ Dấu hiệu nhận ra: `K5` **tăng** mà `K6` hoặc `K7` **giảm** cùng kỳ → ⛔ **không phải tiến bộ**, mà là đẩy vấn đề xuống chặng sau.

---

## 4. ★ `K3` CÓ HAI GỐC — PHẢI TÁCH TRƯỚC KHI GIAO VIỆC

`K3` *(gọi mà ⛔ không kết nối)* trông như một khe của người gọi. Thường ⛔ không phải.

| Dấu hiệu | Gốc | Người nhận |
|---|---|---|
| Tỷ lệ kết nối **thấp đều ở mọi người**, và **thấp theo nguồn data** | 🔴 **Chất lượng data** — số sai, số trùng, số đã bán cho nơi khác | **⛔ LỖI HỆ** → khâu cấp data |
| Tỷ lệ kết nối thấp **chỉ ở một vài người** | Người — giờ gọi, số lần gọi, cách gọi | Trưởng nhóm |
| Thấp đều, nhưng **lệch hẳn theo khung giờ** | Lịch trực đặt sai giờ khách bắt máy | ⛔ Lỗi hệ → vận hành |
| Thấp đều, và `K1` **cũng** cao | ★ Data để nguội — gọi muộn thì ⛔ không ai bắt máy | ⛔ Lỗi hệ → phân bổ |

★ **Phép tách, chạy trước khi giao việc:**

```
Cắt K3 theo NGUỒN DATA, rồi cắt theo NGƯỜI, rồi cắt theo KHUNG GIỜ.
  · lệch theo NGUỒN   → lỗi hệ (data)
  · lệch theo NGƯỜI   → việc của trưởng nhóm
  · lệch theo GIỜ     → lỗi hệ (lịch trực)
  · ⛔ không lệch đâu cả, thấp đều → ⚠ chưa kết luận được, cần thêm kỳ
```

⚠️ Mỗi lát cắt cần **≥30 lead** mới so được (`tb-A` §6). Dưới ngưỡng thì ghi `⚠ chưa đủ mẫu`, ⛔ không kết luận.

---

## 5. ★★ CỔNG V — PHÂN LỖI HỆ / LỖI NGƯỜI TRƯỚC KHI VÀO MỤC "VẤN ĐỀ CỦA TEAM"

> ⛔ Chưa chạy phép thử này thì khe đó ⛔ **không được vào mục việc của khối**.

### Phép thử một câu

```
"Người giỏi nhất khối, với đúng những gì hệ thống đang cấp hôm nay,
 có làm khác được không?"

  ⛔ KHÔNG  →  LỖI HỆ. Vào mục VIỆC HỆ THỐNG, có tên người cấp.
                ⛔ Không vào mục việc của khối. ⛔ Không vào nội dung đào tạo.
  ✅ CÓ     →  việc của khối. Vào mục việc, có người nhận và hạn.
```

★ Phép thử này kế thừa nguyên văn rào ③ của `Agent-QC-Telesale` (`ts-B` §6 / `id-F` §7) — ⛔ không viết lại, dùng đúng câu đó để hai agent nói cùng một thứ.

### Bảng tra nhanh — khe nào thường là lỗi hệ

| Khe | Thường là | Vì sao |
|---|---|---|
| `K1` data để nguội | ⛔ **Lỗi hệ** *(phân bổ)* | Người gọi ⛔ không quyết được lúc data về tay mình |
| `K2` chưa gọi hết | Tuỳ — xem **tải việc** `K8` | Chưa gọi hết vì quá tải là **lỗi hệ**; vì ⛔ không gọi là việc của khối |
| `K3` ⛔ không kết nối | ★ **Hai gốc** — §4 | |
| `K4` bỏ quá sớm | Việc của khối | Số lần gọi là việc người gọi quyết |
| `K5` ⛔ không đặt được hẹn | Việc của khối *(đào tạo)* | ⚠️ Trừ khi thiếu dữ kiện để tư vấn → lỗi hệ |
| `K6` no-show | ⛔ **Lỗi hệ** *(nhắc hẹn)* nếu ⛔ chưa có quy trình nhắc | Có quy trình rồi mà ⛔ không làm → việc của khối |
| `K7` ⛔ không chốt | ⛔ **Không phải khe của khối** — §3 | |
| `K8` tải lệch | ⛔ **Lỗi hệ** *(phân bổ)* | Người gọi ⛔ không chia data cho mình |
| `K9` tồn dồn | ⛔ **Lỗi hệ** nếu data vào nhiều hơn năng lực xử lý | Đây là bài toán **công suất**, ⛔ không phải bài toán cố gắng |

⚠️ **Năm trong chín khe thường là lỗi hệ.** Nếu một kỳ nào đó **cả chín khe** đều vào mục việc của khối thì gần như chắc chắn **CỔNG V ⛔ chưa chạy**.

---

## 6. XẾP THỨ TỰ KHE — ⛔ KHÔNG XẾP THEO SỐ XẤU NHẤT

```
Xếp theo SỐ LEAD BỊ MẤT Ở KHE ĐÓ, ⛔ không theo tỷ lệ xấu nhất.

Lead mất ở một khe = (số vào khe) − (số ra khỏi khe)
```

★ **Vì sao:** một khe có tỷ lệ `20%` nhưng chỉ `15` lead đi qua thì mất `12` lead. Một khe tỷ lệ `75%` mà `800` lead đi qua thì mất `200`. **Khe thứ hai đáng sửa trước**, dù con số `75%` nhìn đẹp hơn.

⚠️ Và ⛔ **không nhân lead mất với giá trị đơn để ra "tiền mất"** — trừ khi khối đã chốt một con số giá trị đơn. ⛔ Agent ⛔ không tự đặt con số đó (`tb-D` §4). Chưa có thì xếp theo **số lead**, và nói rõ đã xếp theo cách đó.

---

## 7. MỘT KHE ĐƯỢC BÁO NHƯ THẾ NÀO — SÁU Ô

```
K6 · ĐẶT HẸN MÀ KHÔNG ĐẾN
① SỐ THẬT     : 18/29 đến khám · 62%   (cohort 27/10, ĐÃ ĐÓNG)
② MẤT BAO NHIÊU: 11 lead
③ XU HƯỚNG    : 3 cohort gần nhất 58% → 61% → 62%   (⚠ chưa có ngưỡng)
④ CẮT RA      : lệch theo KHUNG GIỜ HẸN — hẹn sáng 74%, hẹn chiều muộn 41%
⑤ GỐC         : ⛔ LỖI HỆ — chưa có quy trình nhắc hẹn trước 24h
                 (phép thử §5: người giỏi nhất cũng không nhắc được
                  nếu hệ không có kênh nhắc)
⑥ NGƯỜI NHẬN  : <khâu nhắc hẹn / vận hành> — hạn <ngày>
```

★ **Ô ④ *"cắt ra"* là ô làm cho khe trở nên sửa được.** *"No-show 62%"* là một con số. *"Hẹn chiều muộn chỉ 41%"* là **một việc**: đổi khung giờ hẹn.

⚠️ **Ô ⑥ ⛔ không được để trống.** Một khe ⛔ không có người nhận là một khe sẽ xuất hiện lại kỳ sau, nguyên văn.

---

## 8. KHE QUAY LẠI — LUẬT HAI KỲ

```
Một khe xuất hiện 2 KỲ LIỀN mà số ⛔ không đổi
  → ⛔ KHÔNG phải vấn đề của khối nữa.
  → Hoặc GỐC đã phân sai (chạy lại §5), hoặc NGƯỜI NHẬN sai, hoặc
    việc đã giao mà ⛔ không ai làm được vì thiếu quyền/thiếu công cụ.

★ Ghi rõ "khe này đã sang kỳ thứ n" và ĐƯA LÊN ĐẦU báo cáo.
⛔ Không in lại y nguyên như một khe mới.
```

⚠️ Khe sang **kỳ thứ ba** thì ⛔ không còn là việc của trưởng nhóm — nó là việc cần **cấp trên của trưởng nhóm** quyết. Nói thẳng điều đó.

---

## 9. ĐẦU RA CHUẨN CỦA MỤC "VẤN ĐỀ TEAM ĐANG GẶP"

```
① BA KHE MẤT NHIỀU LEAD NHẤT  — mỗi khe đủ sáu ô §7
② VIỆC CỦA KHỐI               — các khe đã qua CỔNG V, có người nhận + hạn
③ ⛔ VIỆC HỆ THỐNG            — mục RIÊNG, có tên người cấp dữ kiện/công cụ
④ ⏸ KHE CHƯA ĐO ĐƯỢC          — và thiếu cái gì mới đo được
⑤ KHE QUAY LẠI ≥2 KỲ          — §8, đưa lên đầu
⑥ K7 — mục riêng, kèm đúng dòng của §3
```

⚠️ **Mục ③ ⛔ không được gộp vào mục ②.** Gộp lại là cách một lỗi hệ được ghi thành việc của khối — và đó chính là chuyện sổ này tồn tại để chặn.

---

## 10. TỰ KIỂM SỔ NÀY

- [ ] Chạy đủ **chín khe** chưa, hay chỉ in khe nào có số?
- [ ] Khe nào `⏸ chưa đo được` đã ghi **thiếu cái gì** chưa?
- [ ] ★ **CỔNG V** đã chạy cho **từng** khe chưa? Có khe lỗi hệ nào lọt vào mục việc của khối?
- [ ] `K7` có nằm ở **mục riêng** kèm đúng dòng §3 chưa?
- [ ] `K3` đã **tách ba lát cắt** (nguồn · người · giờ) trước khi giao việc chưa?
- [ ] `K5` tăng mà `K6`/`K7` giảm — đã đọc **cùng nhau** chưa? (§3 ngoại lệ)
- [ ] Xếp khe theo **số lead mất** hay theo tỷ lệ xấu nhất?
- [ ] Có nhân lead mất với một **giá trị đơn tự đặt** không?
- [ ] Mọi khe có **người nhận + hạn** chưa?
- [ ] Khe quay lại ≥2 kỳ đã đưa lên **đầu** báo cáo chưa?
