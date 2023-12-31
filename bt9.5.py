 #BT 5
 #BT 4
n = float(input("Nhập n:"))
x = float(input("Nhập x:"))
def tinh_A():
    A = (x**2 + x + 1)**n + (x**2 - x + 1)**n
    print("A =", A)
tinh_A()