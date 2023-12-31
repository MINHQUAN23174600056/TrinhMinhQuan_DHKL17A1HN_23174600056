 #BT 4
import math
a = int(input("Nhập cạnh tam giác a:"))
b = int(input("Nhập cạnh tam giác b:"))
c = int(input("Nhập cạnh tam giác c:"))
p = (a+b+c)/2
S = math.sqrt(p*(p-a)*(p-b)*(p-c))
print("Diện tích tam giác =", S)