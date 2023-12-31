 #BT 5
list = []
so_nguyen_to = []
so_am = []
so_duong = []
while True:
    gia_tri = int(input("Nhập giá trị: "))
    list.append(gia_tri)
    nhap_tiep = int(input("Tiếp tục nhập giá trị? 1:Có, 0:Không  "))
    if nhap_tiep == 0:
        break
print("List:", list)
# Các số nguyên tố trong list
for so in list:
    if so < 0:
        so_am.append(so)
    elif so > 0:
        so_duong.append(so)
    
    snt = True
    if so > 1:
        for i in range(2, int(so/2)+1):
            if (so % i) == 0:
                snt = False
                break
    else:
        snt = False
    
    if snt:
        so_nguyen_to.append(so)
print("các số nguyên tố trong list:", so_nguyen_to)
print("Các phần tử âm trong list:", so_am)
print("Các phần tử dương trong list:", so_duong)

# Trung bình cộng các phần tử âm, dương
tba = sum(so_am)/len(so_am) 
tbd = sum(so_duong)/len(so_duong)
print("Trung bình cộng các phần tử âm:", tba)
print("Trung bình cộng các phần tử dương:", tbd)

# Giá trị min max trong list
min = min(list)
max = max(list)
print("Giá trị max trong list:", max)
print("Giá trị min trong list:", min)

# sắp xếp tăng dần
sx = sorted(list)
print("List sắp tăng dần: ", sx)
