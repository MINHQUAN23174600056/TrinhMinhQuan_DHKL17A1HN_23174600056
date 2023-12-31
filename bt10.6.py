 #BT 6
#GIẢI PT BẬC 2 : AX^2 + BX + C = 0
import math
a = float(input("Nhập a:"))
b = float(input("Nhập b:"))
c = float(input("Nhập c:"))
if a != 0:
    delta = b**2 - 4*a*c
    if delta > 0:
      print("Đây là phương trình bậc 2")
      print("Phương trình có 2 nghiệm phân biệt:")
      x1 = (-b + math.sqrt(delta)) / (2*a)
      x2 = (-b - math.sqrt(delta)) / (2*a)
      print("x1=",x1,",","x2=",x2)
    elif delta==0:
      print("Phương trình có nghiệm kép:")
      x0 = -b / (2*a)  
      print("x0=",x0)
    else:
      print("Phương trình vô nghiệm.")