 #BT 12
a = (1,2,3,4)
b = (5,6,7,8)
print("Tuple a:", a)
print("Tuple b:", b)
c = a + b
d = tuple(sorted(c))
print("Tuple c:", c)
print("Tuple d:", d)

print("Tuple[3] =", d[3])
print("3 phần tử cuối cùng của tuple d", d[-3:])