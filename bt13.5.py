 #BT 5 
import csv
def read_file_csv():
    file_name = input("Nhập tên tập tin: \n")
    with open(file_name,'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)
read_file_csv()
