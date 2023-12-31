 #BT 8
import datetime
import locale
day = int(input("Nhập ngày: \n"))
month = int(input("Nhập tháng: \n"))
year = int(input("Nhập năm: \n"))
#Xuất theo định dạng ngày-tháng-năm
date = datetime.datetime(year,month,day)
print("Ngày tháng năm vừa nhập: ", date.strftime("%d-%m-%Y"))

#Tính thứ của ngày nhập vào
weekday = date.strftime("%A")
print(date.strftime("%d-%m-%Y"), "là", weekday)

#Kiểm tra năm nhuận
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Năm", year, "là năm nhuận")
else:
    print("Năm", year, "không phải năm nhuận")

#Tính số ngày trong tháng
if month == 2:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        ngay_trong_thang = 29
    else:
        ngay_trong_thang = 28
elif month in [4,6,9,11]:
    ngay_trong_thang = 30
else:
    ngay_trong_thang = 31
print("Tháng", month, "có", ngay_trong_thang, "ngày")