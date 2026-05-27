tong_doanh_thu = 0
tong_hoa_don = 0
hoa_don_lon = 0

while True:
    tong_hoa_don += 1

    hoa_don = int(input(f"Khách hàng {tong_hoa_don} - Nhập giá trị hóa đơn: "))

    tong_doanh_thu += hoa_don

    if hoa_don >= 1000000:
        hoa_don_lon += 1

    tiep_tuc = input("Có muốn nhập tiếp không? (C/K): ")

    if tiep_tuc == "K" or tiep_tuc == "k":
        break

if tong_hoa_don > 0:
    ty_le = (hoa_don_lon / tong_hoa_don) * 100
else:
    ty_le = 0

print("--- BÁO CÁO DOANH THU CUỐI NGÀY RIKKEI STORE ---")
print("Tổng số hóa đơn đã xử lý:", tong_hoa_don, "hóa đơn.")
print("Tổng doanh thu hôm nay:", tong_doanh_thu, "VND.")
print("Số hóa đơn lớn (>= 1,000,000 VND):", hoa_don_lon, "hóa đơn.")
print("Tỷ lệ hóa đơn lớn đạt:", ty_le, "% trên tổng số đơn hàng.")
