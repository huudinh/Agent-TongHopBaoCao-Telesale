# tb-G · ★★ RIÊNG TƯ · MÃ NHÂN VIÊN · BỐN RÀO AN TOÀN

> ⚠️ **Sổ này ⛔ không có ngoại lệ.** Nó kế thừa `Agent-QC-Telesale/knowledge/ts-G` — module mà chính nó tự khai là *"module duy nhất không có ngoại lệ"*.
> ⛔ Chưa đọc hết §5 thì ⛔ không được xuất file nào.

---

## 1. ★ XUNG ĐỘT ĐÃ GIẢI — VÌ SAO BÁO CÁO DÙNG MÃ, ⛔ KHÔNG DÙNG TÊN

`ts-G` §1 luật ②, nguyên văn:

> *"⛔ Không đưa tên thật nhân viên vào báo cáo tổng hợp. Dùng `NV-07`. **Bảng quy đổi mã do quản lý giữ, ⛔ không nằm trong file báo cáo**."*

Agent này **chính là** một báo cáo tổng hợp. Và yêu cầu vận hành là: **trưởng nhóm phải biết kèm ai**.

★ **Hai điều đó ⛔ không mâu thuẫn, nếu tách đúng chỗ:**

```
┌─────────────────────────────┐        ┌──────────────────────────────┐
│  BÁO CÁO  (lưu hành)        │        │  BẢNG QUY ĐỔI  (quản lý giữ) │
│  out/bao-cao-*.md           │        │  ma-nhan-vien.csv            │
├─────────────────────────────┤        ├──────────────────────────────┤
│  NV-03 · 42 lead · K5 yếu   │  ◄──►  │  NV-03 = <tên thật>          │
│  NV-07 · 38 lead · K4 yếu   │        │  NV-07 = <tên thật>          │
└─────────────────────────────┘        └──────────────────────────────┘
      ⛔ KHÔNG có tên                      ⛔ KHÔNG commit, ⛔ không gửi
      ✅ Gửi được, lưu được                ✅ Chỉ quản lý mở
```

★ **Trưởng nhóm vẫn kèm được đúng người** — họ giữ khoá. Nhưng **file lưu hành ⛔ không mang tên**, nên nó gửi được, lưu được, và một lần chia sẻ nhầm ⛔ không thành sự cố dữ liệu lao động.

⚠️ **`ma-nhan-vien.csv` và `ma-nhan-vien.json` đã bị `.gitignore` chặn.** ⛔ Không gỡ. ⛔ Không đặt bảng quy đổi vào `out/`, ⛔ không dán nó vào chat, ⛔ không để nó thành một tab trong cùng Google Sheet với báo cáo.

★ **Mã phải BỀN giữa các kỳ.** `NV-03` kỳ này và `NV-03` kỳ sau phải là **cùng một người**, nếu không thì mọi so sánh trước/sau đào tạo đều vô nghĩa. Mã sinh **một lần**, ⛔ không sinh lại mỗi kỳ.

---

## 2. ⛔ ĐỔI MÃ NGAY Ở BƯỚC ĐỌC — ⛔ KHÔNG ĐỔI Ở BƯỚC XUẤT

> Đây là khác biệt kỹ thuật quan trọng, ⛔ không phải chuyện thứ tự.

```
✅ ĐÚNG:  đọc nguồn → ĐỔI MÃ NGAY → mọi file trung gian đều đã sạch
⛔ SAI :  đọc nguồn → xử lý → xuất → đổi mã ở bước cuối
```

★ **Vì sao:** cách sai để lại **tên thật trong mọi file trung gian** — `out/*.json`, log, file tạm. Một trong số đó sẽ bị gửi đi, hoặc bị commit, hoặc nằm lại trên máy ai đó. Đổi ở bước đọc thì **⛔ không có bản nào chứa tên để mà lọt**.

### Bốn thứ đổi/băm ngay ở bước đọc

| Dữ kiện | Thành | Vì sao |
|---|---|---|
| Tên nhân viên | `NV-xx` | `ts-G` §1 ② |
| Số điện thoại khách | `sdt_hash` *(băm một chiều)* | Vẫn nối được phễu mà ⛔ không giữ số |
| Tên khách | `KH-xxx` | `ts-G` §1 ① |
| Ghi chú tự do của nhân viên | ⛔ **Bỏ hẳn** | Thường chứa tên, số, tình trạng sức khoẻ khách lẫn vào |

⚠️ **Cột ghi chú tự do là chỗ rò nhiều nhất và hay bị bỏ qua nhất.** Nó ⛔ không phải cột số, nên ⛔ không ai nghĩ tới nó — nhưng nó là nơi nhân viên gõ *"chị Lan 098… muốn nâng mũi trước Tết"*. ⛔ **Không giữ cột này.** Cần nội dung hội thoại thì đó là việc của `Agent-QC-Telesale`, ⛔ không phải của agent này.

---

## 3. ⛔ BỐN ĐIỀU ⛔ KHÔNG BAO GIỜ LÀM

Kế thừa `ts-G` §1, áp nguyên văn:

```
① ⛔ KHÔNG đưa tên · SĐT · email · địa chỉ · tình trạng sức khoẻ của khách
   vào báo cáo, dashboard, hay file trung gian. Dùng KH-xxx.

② ⛔ KHÔNG đưa tên thật nhân viên vào báo cáo tổng hợp. Dùng NV-xx.
   Bảng quy đổi do quản lý giữ, ⛔ KHÔNG nằm trong file báo cáo.

③ ⛔ KHÔNG commit, ⛔ không upload, ⛔ không gửi qua kênh công khai
   file dữ liệu gốc. du-lieu/ và out/ đã bị .gitignore chặn — ⛔ không gỡ.

④ ⛔ KHÔNG xếp hạng công khai. Lát cắt theo người dùng để BIẾT KÈM AI,
   ⛔ không để xếp ai trên ai.
```

---

## 4. ★ BỐN RÀO AN TOÀN CỦA LÁT CẮT THEO NGƯỜI

> Lát cắt theo người là lát cắt **duy nhất** gắn số với một con người. Nó chỉ hợp lệ khi đủ **cả bốn** rào.

```
① SỐ ĐỂ KÈM CẶP, ⛔ KHÔNG ĐỂ KỶ LUẬT.
   Mọi bảng có lát cắt người mang đúng câu này ở chân bảng:
   "Số liệu dùng để phân việc kèm cặp. Không phải căn cứ kỷ luật
    hay xếp hạng công khai."

② ⛔ KHÔNG KẾT LUẬN DƯỚI NGƯỠNG MẪU.
   < 10 cuộc/người trong kỳ → ⛔ không kết luận riêng về người đó.
   Ghi "chưa đủ mẫu". ⛔ Không hạ ngưỡng để "có bảng cho đẹp".

③ LỖI HỆ ⛔ KHÔNG TRỪ ĐIỂM NGƯỜI.
   Chạy CỔNG V (tb-E §5) TRƯỚC khi gắn một khe vào một người.
   Năm trong chín khe thường là lỗi hệ.

④ ⛔ KHÔNG SO NGƯỜI CŨ VỚI NGƯỜI MỚI TRONG MỘT TỶ LỆ CHUNG.
   Tách riêng (ts-F §4). Nhân viên mới kéo tỷ lệ chung xuống và
   che mất vấn đề thật của nhóm cũ.
```

⚠️ **Rào ③ là rào hay bị quên nhất**, và ở agent này nó nặng hơn ở các agent khác — vì **phần lớn khe rò của phễu telesale ⛔ không nằm trong tay người gọi**: data về muộn, data sai số, ⛔ chưa có quy trình nhắc hẹn, tải việc chia lệch. Gắn những khe đó vào tên một người là **chấm sai người**.

---

## 5. ★★ CỔNG R — KIỂM TRƯỚC KHI XUẤT, CHẠY **BẰNG MÁY**

⛔ Không file nào được xuất trước khi chạy đủ **sáu câu** này.

```
① TÊN NHÂN VIÊN
   Tìm mọi tên trong bảng quy đổi, trên file sắp xuất.
   Tìm thấy dù một lần → ⛔ DỪNG, ⛔ không xuất.
   ⚠ Kiểm cả trong TÊN FILE và trong phụ lục "nguyên văn dán tay".

② DỮ KIỆN KHÁCH
   SĐT · email · tên khách · địa chỉ → ⛔ phải không có.
   ⚠ Regex SĐT phải bắt cả dạng có dấu cách và dấu chấm.

③ CỘT GHI CHÚ TỰ DO
   ⛔ Phải KHÔNG TỒN TẠI trong file xuất, kể cả rỗng (§2).

④ BẢNG QUY ĐỔI
   ma-nhan-vien.* ⛔ phải KHÔNG nằm trong out/ và ⛔ không nằm trong
   bất cứ thứ gì sắp gửi đi.

⑤ NGƯỠNG MẪU NGƯỜI
   Người nào dưới 10 cuộc mà vẫn có nhận định riêng → ⛔ DỪNG.

⑥ CÂU CHÂN BẢNG
   Mọi bảng có lát cắt người mang đúng câu của rào ① §4.
```

⚠️ **Câu ① ② ③ ④ phải chạy bằng máy, ⛔ không bằng mắt.** `tools/tb.py` có hàm `kiem_rieng_tu()` chạy đúng sáu câu trên và **từ chối ghi file** nếu trượt. Mọi lần ghi file đều đi qua `ghi_file()` — ⛔ không ghi trực tiếp ở chỗ khác.

★ Chạy tay thì ⛔ **sẽ có kỳ quên**. Và một tên lọt ra rồi thì ⛔ không gỡ lại được: báo cáo đã nằm trong hộp thư của người khác.

---

## 6. ⛔ LỌC VÀ GỘP — KHÔNG RA QUYẾT ĐỊNH

```
Agent đưa số, bằng chứng và phương án. NGƯỜI THẬT KÝ.

⛔ Không đề xuất kỷ luật · cắt thưởng · xếp hạng công khai · cho nghỉ.
⛔ Không kết luận về CON NGƯỜI — chỉ kết luận về VIỆC và về KHE.
```

★ Một bản tổng hợp của máy dùng làm căn cứ kỷ luật là cách nhanh nhất để cả khối thôi tin vào nó. Và khi họ thôi tin thì **dữ liệu đầu vào hỏng theo** — ⛔ không ai nhập thật nữa, trạng thái lead thành *"đã gọi"* hết. Lúc đó agent này mất **thứ duy nhất nó có**.

---

## 7. BẢN RÚT GỌN — ĐỂ GỬI RỘNG

Khi báo cáo cần gửi ra ngoài khối *(ban điều hành, khối khác)*, xuất **bản rút gọn**:

| | Bản đầy đủ | Bản rút gọn |
|---|---|---|
| Ai nhận | Quản lý khối · trưởng nhóm | Ngoài khối |
| Lát cắt theo người | ✅ có, mã `NV-xx` | ⛔ **Không có** |
| Khe rò | ✅ cả chín, đủ sáu ô | 🔶 Ba khe đầu, ⛔ không có ô *"người nhận"* |
| Việc hệ thống | ✅ có tên người cấp | ✅ **Giữ** — đây là phần ngoài khối cần biết |
| Phụ lục nguyên văn | ✅ có | ⛔ **Không có** |

★ **Mục *"việc hệ thống"* là mục duy nhất ⛔ không bị rút gọn** — vì nó là phần mà người ngoài khối **phải thấy mới gỡ được**. Rút nó đi thì bản gửi ra chỉ còn những việc khối tự làm, và cái đang chặn thật thì ⛔ không ai biết.

---

## 8. TỰ KIỂM SỔ NÀY

- [ ] Sáu câu của **CỔNG R** §5 đã chạy **bằng máy** chưa?
- [ ] Đổi mã ở **bước đọc** hay bước xuất?
- [ ] Cột **ghi chú tự do** đã bỏ hẳn chưa — kể cả trong file trung gian?
- [ ] `ma-nhan-vien.*` có nằm trong `out/` hoặc trong thứ sắp gửi không?
- [ ] Mã `NV-xx` có **bền** giữa các kỳ không, hay sinh lại mỗi kỳ?
- [ ] Người dưới 10 cuộc có nhận định riêng nào không?
- [ ] ★ **CỔNG V** đã chạy trước khi gắn khe vào người chưa?
- [ ] Người cũ và người mới có bị gộp vào **một tỷ lệ chung** không?
- [ ] Câu chân bảng có ở **mọi** bảng có lát cắt người chưa?
- [ ] Bản rút gọn còn giữ mục **việc hệ thống** chưa?
