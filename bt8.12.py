 # BT 12
x = int(input("Nhập số cần kiểm tra:")) 
def snt(x):
    if x < 2:
        return False
    for i in range(2,int(x**0.5)+1):
        if x % i == 0: 
            return False
    return True        
if snt(x):
    print(x, "là số nguyên tố")
else:
    print(x, "không là số nguyên tố")