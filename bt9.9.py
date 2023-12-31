 #BT 9
dt_ht = lambda r: r**2 * 3.14 
cvi_ht = lambda r: 2 * r *  3.14
dt_hcn = lambda a, b: a * b
cvi_hcn = lambda a, b: (a + b) * 2
r = float(input("Nhập bán kính hình tròn: "))
a = float(input("Nhập chiều dài hình chữ nhật: "))
b = float(input("Nhập chiều rộng hình chữ nhật: "))
print("Diện tích hình tròn:", dt_ht(r))
print("Chu vi hình tròn:", cvi_ht(r))
print("Diện tích hình chữ nhật:", dt_hcn(a,b))
print("Chu vi hình chữ nhật:", cvi_hcn(a,b))