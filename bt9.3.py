 #BT 3
can_nang = float(input("Nhập cân nặng(kg):"))
chieu_cao = float(input("Nhập chiều cao(m):"))
def bmi():
    bmi = can_nang / (chieu_cao**2)
    if bmi < 18.5:
        return(print("Gầy"))
    elif bmi >= 18.5 and bmi < 25:
        print("Bình thường")
    else:
        print("Thừa cân")
    print("Chỉ số BMI:",bmi)
bmi()