 # BT 15
S = 0
while True:
    num = int(input("Nhập một số nguyên (số kết thúc là số 0):")) 
    if num == 0:
        break
    S += num
print("S = ", S)    