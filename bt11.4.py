 #BT 4
list = []
while True:
    gia_tri = int(input("Nhập giá trị: "))
    list.append(gia_tri)
    nhap_tiep = int(input("Tiếp tục nhập giá trị? 1:Có, 0:Không  "))
    if nhap_tiep == 0:
        break
x = int(input("Nhập giá trị cần tìm x: "))
print("List:", list)
#Tổng các giá trị trong list
tong_list = sum(list)
print("Tổng các giá trị trong list:", tong_list)

# Đếm số lần xuất hiện của x trong list
so_lan_xh = list.count(x)
print(x, "xuất hiện", so_lan_xh, "lần trong list")
print(x, "không lớn hơn tất cả các số trong list")

#Tạo list mới chứa các số lớn hơn x
so_lon_hon_x = [so for so in list if so > x]
print("Các số lớn hơn", x, "trong list", so_lon_hon_x)