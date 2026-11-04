# template/ — BỐN FILE MẪU BỐN NGUỒN

> ⚠️ **Mọi giá trị trong bốn file `MAU_*.csv` là DỮ LIỆU BỊA** để minh hoạ định dạng
> và để chạy thử `tools/tb.py`. ⛔ Không phải số liệu thật, ⛔ không phải nhân sự thật
> của khối Telesale. Sáu cái tên trong cột `ma_nv` là **tên bịa**, đặt ở đó có chủ đích:
> dữ liệu thô từ tổng đài **có** tên, và bước ĐỌC của agent phải đổi tên → `NV-xx`.
> Giữ tên trong file mẫu là để còn chỗ kiểm thử bước đổi mã đó.

| File | Nguồn | Khoá nối |
|---|---|---|
| `MAU_1-cuoc-goi.csv` | ① Cuộc gọi · tổng đài | `ma_lead` |
| `MAU_2-data-phan-bo.csv` | ② Data / lead phân bổ | `ma_lead` |
| `MAU_3-lich-hen.csv` | ③ Lịch hẹn & đến khám | `ma_lead` |
| `MAU_4-ca-chot.csv` | ④ Ca chốt & doanh số | `ma_lead` |

## Chạy thử

```bash
mkdir du-lieu && cp template/MAU_*.csv du-lieu/
python tools/tb.py doc du-lieu/ --ky "26/10-02/11"
```

## ⛔ Khi thay bằng dữ liệu thật

Đổ vào `du-lieu/` *(đã bị `.gitignore` chặn)*, ⛔ **không** ghi đè `template/`.
Bảng tra `ma-nhan-vien.csv` giữ ngoài git — xem [`tb-G`](../knowledge/tb-G-rieng-tu-rao-an-toan.md).
