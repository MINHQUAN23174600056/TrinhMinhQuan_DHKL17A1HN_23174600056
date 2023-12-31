 # BT 3
# GIẢI PT BẬC NHẤT AX + B = 0
a = int(input("Nhập hệ số a:"))
b = int(input("Nhập hệ số b:"))
print("Phương trình bậc nhất:", f"{a}x+{b}=0")
if a == 0:
    if b == 0:
        print("Phương trình vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    x = -b/a
    print("Nghiệm x =", x)             