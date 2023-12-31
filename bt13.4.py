 #BT 4
def write_end_of_file():
    file = input("Nhập tên tập tin: ")
    f = open(file+".txt",'w')
    while True:
        noi_dung = input("Nhập nội dung: ")
        f.write(noi_dung+"\n")
        lua_chon = input("Bạn có muốn tiếp tục ghi nội dung vào file? 1:Có; 0:Không \n")
        if lua_chon == "0":
            break
    f.close()
    f = open(file+".txt",'r')
    f_nd = f.read()
    f.close()
    print("Nội dung tập tin sau khi ghi: ")
    print(f_nd)
write_end_of_file()
    