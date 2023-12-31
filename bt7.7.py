 # BT 7
so_tien_muon_doi = int(input("Số tiền muốn đổi:"))
so_to_500k = so_tien_muon_doi // 500000
so_tien_muon_doi = so_tien_muon_doi % 500000
so_to_200k = so_tien_muon_doi // 200000
so_tien_muon_doi = so_tien_muon_doi % 200000
so_to_100k = so_tien_muon_doi // 100000
so_tien_muon_doi = so_tien_muon_doi % 100000
so_to_50k = so_tien_muon_doi // 50000
so_tien_muon_doi = so_tien_muon_doi % 50000
print("Số tờ 500,000:", so_to_500k)
print("Số tờ 200,000:", so_to_200k)
print("Số tờ 100,000:", so_to_100k)
print("Số tờ 50,000:", so_to_50k)
print("Tiền còn lại:", so_tien_muon_doi)