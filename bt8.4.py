 # BT 4
import math
a = eval(input("Nhập cạnh tam giác a:"))
b = eval(input("Nhập cạnh tam giác b:"))
c = eval(input("Nhập cạnh tam giác c:"))
p = (a+b+c)/2
S = math.sqrt(p*(p-a)*(p-b)*(p-c))
print("Diện tích tam giác =", S)

# Đkiện tạo thành 1 tam giác
