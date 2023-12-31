 #BT 1
numbers = [int(x) for x in input("Nhập danh sách số, cách nhau bằng dấu cách:").split()]
#Hàm Split trả lại danh sách của chuỗi sau khi chia các chuỗi này dựa vào các dấu phân tách
gtnn = min(numbers)
gtln = max(numbers)
print(f"Gia tri nho nhat: {gtnn}")
print(f"Gia tri lon nhat: {gtln}")