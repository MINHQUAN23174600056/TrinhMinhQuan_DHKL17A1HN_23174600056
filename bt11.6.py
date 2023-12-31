 #BT 6
list = [74,74,72,72,73,69,69,71,76,71]
inch = [chieu_cao * 0.0254 for chieu_cao in list]
print("3 chiều cao đầu tiên là: ", inch[:3])
print("3 chiều cao cuối cùng là: ", inch[:-3])
chieu_cao_tb = sum(inch)/len(inch)
chieu_cao_ln = max(inch)
chieu_cao_nn = min(inch)
print("Chiều cao trung bình:", chieu_cao_tb)
print("Chiều cao lớn nhất:", chieu_cao_ln)
print("Chiều cao nhỏ nhất:", chieu_cao_nn)

inch.sort()
print("List theo giá trị tăng dần:", inch)
inch.sort(reverse=True)
print("List theo giá trị giảm dần:", inch)