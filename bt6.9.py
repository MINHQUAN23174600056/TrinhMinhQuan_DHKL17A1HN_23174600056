 # BT 9
lai_suat_1_nam = float(input("Nhập lãi suất 1 năm(%):"))
so_tien_gui =  float(input("Nhập số tiền gửi:"))
so_thang_gui = int(input("Nhập số tháng gửi:"))
tien_lai = (so_tien_gui * so_thang_gui) * (lai_suat_1_nam / 12)
tien_von_lai = so_tien_gui + tien_lai
print("Tiền lãi:", tien_lai)
print("Tiền vốn + lãi:", tien_von_lai)