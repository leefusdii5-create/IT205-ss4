so_hoa_don = int(input("Nhập số lượng hóa đơn trong ca: "))

max_hoa_don = 0
min_hoa_don = 0

for i in range(1, so_hoa_don + 1):
    hoa_don = int(input(f"Nhập giá trị hóa đơn thứ {i}: "))

    if i == 1:
        max_hoa_don = hoa_don
        min_hoa_don = hoa_don

    if hoa_don > max_hoa_don:
        max_hoa_don = hoa_don

    if hoa_don < min_hoa_don:
        min_hoa_don = hoa_don

print("--- KẾT QUẢ KIỂM TOÁN CA RIKKEI STORE ---")
print("Hóa đơn có giá trị cao nhất:", max_hoa_don, "VND")
print("Hóa đơn có giá trị thấp nhất:", min_hoa_don, "VND")
