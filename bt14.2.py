 #BT 2
so_truoc = [None, None, None]
while True:
        try:
            so = input("Nhập một số nguyên dương (nhập 0 để kết thúc): ")
            so = int(so)
            if so < 0:
                raise ValueError("Lỗi số âm")
            elif so == 0:
                break
            elif so == so_truoc[0] == so_truoc[1] == so_truoc[2]:
                raise ValueError("Lỗi nhập lặp lại")
            else:
                so_truoc = [so, so_truoc[0], so_truoc[1]]
        except ValueError as e:
            print("Lỗi không xác định vui lòng thử lại")