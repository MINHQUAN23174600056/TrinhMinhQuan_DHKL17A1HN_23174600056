 # BT 19
def reverse(string):
    string = list(string)
    string.reverse()
    return "".join(string)  
x = input("Nhập vào:")  
print("Chuỗi đã được đảo ngược là: ", reverse(x))