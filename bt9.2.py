 #BT 2
nam = int(input("Nhập năm:"))
def tinh_can(nam):
    can = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
    can_index = nam % 10
    if can_index == 0:
        return can[0]
    elif can_index < 0:
        return can[can_index + 10]
    else:
        return can[can_index]
def tinh_chi(nam):
    chi = ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi"]
    chi_index = nam % 12
    if chi_index == 0:
        return chi[0]
    elif chi_index < 0:
        return chi[chi_index + 12]
    else:
        return chi[chi_index]
nam_can = tinh_can(nam)
nam_chi = tinh_chi(nam)
print(f"Năm {nam} lịch âm là năm {nam_can} {nam_chi}")