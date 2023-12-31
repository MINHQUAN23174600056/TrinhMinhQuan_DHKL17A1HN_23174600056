 # BT 16
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: ")) 
def ucln(a, b):   
    while b != 0:       
        a,b = b, a % b 
    return a
print(f"Ước chung lớn nhất của {a} và {b} là: {ucln(a, b)}")