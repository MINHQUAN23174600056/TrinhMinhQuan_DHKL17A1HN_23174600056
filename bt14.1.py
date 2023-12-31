 #BT 1
try:
    a, b, c = map(float, input("Nhập 3 cạnh của tam giác: ").split())
    if a <= 0  or b <= 0 or c <= 0:
        raise ValueError("Độ dài cạnh không phù hợp: ")
    if a <= 0 or b <= 0 or c <=0 or a + b <= c or b + c <= a or a + c <= b:
        raise ValueError("Không phải là tam giác: ")
except  ValueError as e:
    print("Lỗi thử lại sau")
else:
    print("Đây là 3 cạnh của tam giác")