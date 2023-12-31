 #BT 6
import csv
def write_csv_file():
    file = input("Nhập tên tập tin: ")
    f = open(file,'w')
    while True:
        noi_dung = input()
        f.write(noi_dung+"\n")
        lua_chon = input()
        if lua_chon == "0":
            break
    f = open(file,'r')
    f_nd = f.read()
    f.close()
    print(f_nd)
write_csv_file()