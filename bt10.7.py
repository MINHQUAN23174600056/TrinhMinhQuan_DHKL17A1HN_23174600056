 #BT 7
s = input("Nhập chuỗi s:")
s_sub = input("Nhập chuỗi con s_sub:")
s_find = input("Nhập chuỗi tìm s_find:")
s_replace = input("Nhập chuỗi thay thế s_replace:")
print("Chuỗi s", s)
#Loại bỏ khoảng trắng ở đầu và cuối chuỗi
s = s.strip()
print("Chuỗi sau khi loại bỏ khoảng trắng ở đầu và cuối chuỗi:", s)

#In chuỗi với kí tự đầu chuỗi viết hoa
s = s.capitalize() 
print("Chuỗi với kí tự đầu chuỗi viết hoa", s.capitalize())

#Đếm và in ra số lần chuỗi con s_sub xuất hiện trong chuỗi s
so_lan_xh = s.count(s_sub)
print("Số lần s_sub xuất hiện trong s:", so_lan_xh)

#Tìm kiếm s_find trong s và thay thế bằng s_replace
s = s.replace(s_find,s_replace)
print("Chuỗi s sau khi tìm kiếm và thay thế:", s)
