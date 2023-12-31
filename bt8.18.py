 # BT 18
def so_hoan_hao(n):
    tong = 0
    for i in range(1, n):
        if (n % i) == 0:
            tong += i
    if tong == n:
        return True
    else:
        return False
x = int(input("Nhập số nguyên x:"))  
if so_hoan_hao(x):
    print(f"{x} là số hoàn hảo")    
else:
    print(f"{x} không phải số hoàn hảo")