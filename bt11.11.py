 #BT 11
tuple = ['red','green','yellow','blue','black','white','pick','orange','red','blue']
print("Tuple:", tuple)
chuoi_duong = int(input("Nhập số từ 0 đến 9: "))
chuoi_am = int(input("Nhập số từ -1 đến -9: "))
gia_tri_duong =  tuple[chuoi_duong]
gia_tri_am = tuple[chuoi_am]
chuoi_can_tim = input("Nhập chuỗi cần tìm: ")
so_lan_xh = tuple.count(chuoi_can_tim)
print(f"Tuple[{chuoi_duong}] = {gia_tri_duong}")
print(f"Tuple[{chuoi_am}] = {gia_tri_am}")
print(f"{chuoi_can_tim} xuất hiện trong tuple {so_lan_xh} lần")