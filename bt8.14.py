 # BT 14
N = int(input("N = "))
S = 0
for i in range(N):
    so = int(input("Nhập số nguyên thứ {}:".format(i+1)))
    S += so
print("Tổng của {} số nguyên là = {}".format(N,S))    