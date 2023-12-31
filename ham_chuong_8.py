#1
def tim_max_min():
    x = eval(input("Nhập a, b, c, d:"))
    so_lon_nhat = max(x)
    so_nho_nhat = min(x)
    print("Max =", so_lon_nhat)
    print("Min =", so_nho_nhat)

#2
def abs():
    x = int(input("Nhập x:"))
    gia_tri_truyet_doi = abs(x)
    print(f"|{x}| = ", gia_tri_truyet_doi)

#3
def giai_pt_bac_nhat():
    a = int(input("Nhập hệ số a:"))
    b = int(input("Nhập hệ số b:"))
    print("Phương trình bậc nhất:", f"{a}x+{b}=0")
    if a == 0:
        if b == 0:
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        x = -b/a
    print("Nghiệm x =", x)   

#4
def tinh_S_tamgiac():
    import math
    a = eval(input("Nhập cạnh tam giác a:"))
    b = eval(input("Nhập cạnh tam giác b:"))
    c = eval(input("Nhập cạnh tam giác c:"))
    p = (a+b+c)/2
    S = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("Diện tích tam giác =", S)

#5
def kt_nam_nhuan():
    year = int(input("Năm nhập vào ?"))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} là năm nhuận")
    else:
        print(f"{year} không phải năm nhuận") 

#6
def tinh_phi_taxi():
    loai_xe = int(input("Loại xe 4 or 7 ? "))
    so_km = eval(input("Nhập số km: "))
    tg_cho = eval(input("Nhập thời gian chờ: "))
    tien_cuoc = float(0)
    tien_di_chuyen = float(0)
    if tg_cho >=5:
        tien_cho=(tg_cho-5)*0.8
    else:
        tien_cho=0          
    if loai_xe==4:
        if so_km <=0.8:
            tien_di_chuyen=0.8*11000
        elif so_km <=20:
            tien_di_chuyen=0.8*11000+(20-so_km)*12100
        else:
            tien_di_chuyen=0.8*11000+(20-0.8)*12100+(so_km-20)*10000
        tien_cuoc=tien_cho+tien_di_chuyen
        print("Cước phí xe 4 chỗ là %0.2f"%tien_cuoc)
    if loai_xe==7:
        if so_km <=0.8:
            tien_cuoc+tien_cho+0.8*13000
        elif so_km <=30:
            tien_di_chuyen=tien_cho+0.8*13000+(30-so_km)*14100
        else:
            tien_di_chuyen=tien_cho+0.8*13000+(30-0.8)*14100+(so_km-30)*12000
        tien_cuoc=tien_cho+tien_di_chuyen
        print("Cước phí xe 7 chỗ là %0.2f"%tien_cuoc)       

#7
def tinh_tien_dien():
    a=eval(input("Nhập số kwh tiêu thụ:"))
    if a>=0:
        if a<=50:
            print("Tổng số tiền phải trả:",a*1678,"đồng")
        elif a<=100:
            print("Tổng số tiền phải trả:",50*1678+(a-50)*1734,"đồng")
        elif a<=200:
            print("Tổng số tiền phải trả:",50*(1678+1734)+(a-100)*2014,"đồng")
        elif a<=300:
            print("Tổng số tiền phải trả:",50*(1678+1734+2014)+(a-200)*2536,"đồng")
        elif a<=400:
            print("Tổng số tiền phải trả:",50*(1678+1734+2014+2536)+(a-300)*2834,"đồng")
        else:
            print("Tổng số tiền phải trả:",50*(1678+1734+2014+2536+2834)+(a-400)*2927,"đồng")

#8
def tinh_gia_phong():
    print("các loại mã phòng:")
    print("1-Standard")
    print("2-Superior Garden View")
    print("3-Superior Ocean View")
    print("4-Garden View Bungalow")
    print("5-Pool View Bungalow")
    print("6-Family Room")
    print("7-Beach Front Bungalow")
    print("8-VIP sea View")
    a=eval(input("Nhập loại mã phòng:"))
    b=eval(input("Nhập số đêm:"))
    if a>0 & a<=8:
        if a==1: c=1260000
        elif a==2: c=1550000
        elif a==3: c=1830000
        elif a==4: c=1830000
        elif a==5: c=2120000
        elif a==6: c=2120000
        elif a==7: c=2540000
        elif a==8: c=4800000
        else: 
            print("Vui lòng chọn lại mã phòng")
    else: print("Vui lòng chọn lại mã phòng") 
    if b==1:
        print("Giá tiền phòng là:",c,"đồng")
    elif b==2:
        print("Giá tiền phòng là:",c*b*0.75,"đồng") 
    elif b==3:
        print("Giá tiền phòng là:",c*b*0.75,"đồng") 
    elif b>=4:
        print("Giá tiền phòng là:",c*b*0.7,"đồng")       
    else:
        print("Vui lòng nhập lại số đêm")

#9
def count_down():
    count_down = int(input("Input number:"))
    print(count_down)
    while count_down > 0:
        count_down = count_down -1
        print(count_down)
    print("Start!!!")

#10
def gia_tri10():
    n = int(input("Nhập n:"))
    x = float(input("Nhập x:"))
    S = (x**2 + 1)**n
    print("S=(x*x + 1)^n =", S) 

#11
def gia_tri11():
    n = int(input("Nhập n:"))
    x = float(input("Nhập x:"))
    A =  (x**2 + x + 1)**n + (x**2 - x + 1)**n
    print("A=(x^2 + x + 1)^n + (x^2 - x + 1)^n =", A)

#12
def snt():
    x = int(input("Nhập số cần kiểm tra:")) 
    if x < 2:
        return False
    for i in range(2,int(x**0.5)+1):
        if x % i == 0: 
            return False
    return True        

#14
def tinh_tong():
    N = int(input("N = "))
    S = 0
    for i in range(N):
        so = int(input("Nhập số nguyên thứ {}:".format(i+1)))
        S += so
    print("Tổng của {} số nguyên là = {}".format(N,S))    

#13
import math
n = eval(input("Nhập số n: "))
def A(n):
    j = []
    a = 0
    for i in range(1,n):
        j.append(i)
    for v in j:
        a = a + v
    return print("A = ",a)
def B(n):
    j = []
    a = 0
    for i in range(1,n):
        if i%2==0:
            j.append(i)
    for v in j:
        a = a + v
    return print("B = ",a)
def C(n):
    j = []
    a = 1
    for i in range(1,n):
        j.append(i)
    for v in j:
        a = a*v
    return print("C = ",a)
def D(n):
    j = []
    a = 1
    for i in range(1,n):
        if i%3==0:
            j.append(i)
    for v in j:
        a = a + v
    return print("D = ",a)
def E(n):
    j = []
    a = 0
    for i in range(2,n+1):
        if i>0:
            for k in range(2,int(math.sqrt(i))+1):
                if i%k ==0:
                    break
            else:
                j.append(i)
    for v in j:
        a = a + v
    print("E = ",a)    
def F(n):
    j = []
    a = 1
    for i in range(1,n):
        j.append(i**-1)
    for v in j:
        if i%2==0:
            a = a + v
        else:
            a = a - v 
    return print("F = ",a - 1)

#15
def tinh_tong_so_nguyen():
    S = 0
    while True:
        num = int(input("Nhập một số nguyên (số kết thúc là số 0):")) 
        if num == 0:
            break
        S += num
    print("S = ", S)   

#16
def ucln():   
    a = int(input("Nhập số nguyên a: "))
    b = int(input("Nhập số nguyên b: ")) 
    while b != 0:       
        a,b = b, a % b 
    return a

#17
def bcnn():
    a = int(input("Nhập số nguyên a: "))
    b = int(input("Nhập số nguyên b: ")) 
    if a < 0 or b < 0:
        if a < 0 or b < 0:
            print("a, b phải lớn hơn 0")
    max = a
    if max < b:
        max = b
    while True:
        if max % a == 0 and max % b == 0:
            print(f"BCNN({a},{b}) = {max}")
            break
        max = max + 1

#18
def so_hoan_hao():
    x = int(input("Nhập số nguyên x:"))  
    tong = 0
    for i in range(1, n):
        if (n % i) == 0:
            tong += i
    if tong == n:
        return True
    else:
        return False

#19
def reverse():
    x = input("Nhập vào:")  
    string = list(string)
    string.reverse()
    return "".join(string)  

#20
def tinh_e_mu_x():
    x=int(input("Nhập x:"))
    ex=1
    n=1
    t=x
    while math.fabs(t)>=0.0001:
        ex +=t
        n +=1
        t *=(x/n)
    return ex
  