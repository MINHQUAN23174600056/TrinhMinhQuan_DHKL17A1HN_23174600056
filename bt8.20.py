 # BT 20
import math
x=int(input("Nhập x:"))
ex=1
n=1
t=x
while math.fabs(t)>=0.0001:
    ex +=t
    n +=1
    t *=(x/n)
print("Giá trị gần đúng của e^x là:",ex) 