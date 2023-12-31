 # BT 17
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: ")) 
def ucln(a, b):   
    while b != 0:       
        a,b = b, a % b 
    return a
def bcnn(a,b):
    bcnn = (a*b) // ucln(a,b)
    return bcnn               
print(f"Bội chung nhỏ nhất của {a} và {b} là: {bcnn(a, b)}")