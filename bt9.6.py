 #BT 6
def so_nguyen_to(n):
    if n <= 1:
        return False 
    for i in range(2, n):
        if n % i == 0: 
            return False  
    return True
n = int(input("Nhập số tự nhiên:"))
if so_nguyen_to(n):
    print(f"{n} là số nguyên tố")
else:
    print(f"{n} không phải số nguyên tố")