 # BT 7
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