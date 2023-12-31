 #BT 2
def read_report_file(file):
    with open("HumptyDumpty.txt", "r", encoding = "utf-8") as file:
        a = file.read()
    lines = a.count("\n")+1
    words = len(a.split())
    chars = len(a)
    print("Content of file: \n", a)
    print("----Report: Lines/ Words/ Char----")
    print("Lines: ",lines,"Words: ", words,"Chars: ",chars)
file = input("Nhập tên tập tin: ")
read_report_file(file)
