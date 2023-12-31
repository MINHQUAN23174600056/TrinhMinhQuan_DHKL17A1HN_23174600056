 # BT 5
year = int(input("Năm nhập vào ?"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
   print(f"{year} là năm nhuận")
else:
   print(f"{year} không phải năm nhuận") 