ma_so_bi_an = 79
doan_dung = False

for luot in range(1, 6):
    so_doan = int(input(f"Lượt đoán {luot} - Nhập số của bạn: "))

    if so_doan == ma_so_bi_an:
        print("=> Chúc mừng! Bạn đã đoán chính xác mã số may mắn!")
        doan_dung = True
        break

    elif so_doan < ma_so_bi_an:
        print("=> Gợi ý: Số của bạn nhỏ hơn mã số may mắn!")

    else:
        print("=> Gợi ý: Số của bạn lớn hơn mã số may mắn!")

if doan_dung == False:
    print("=> Bạn đã hết lượt chơi. Chúc may mắn lần sau!")

print("--- TRÒ CHƠI KẾT THÚC ---")
