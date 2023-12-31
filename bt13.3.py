 #BT 3
def write_file():
    ten_tap_tin = input("Nhập tên tập tin: ")
    noi_dung = input("Nhập nội dung: ")
    with open(ten_tap_tin, 'w') as file:
        file.write(noi_dung)
    print("Đã ghi nội dung vào tập tin", ten_tap_tin)
    with open(ten_tap_tin, 'r') as file:
        noi_dung_sau_ghi = file.read()
    print(noi_dung_sau_ghi)
write_file()