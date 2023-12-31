 #BT 7
L = [1, 2, 3, 4]
thresh = 2
def elementwise_greater_than(L,thresh):
    kq = []
    for i in L:
        kq.append(i > thresh)
    return kq
print(elementwise_greater_than(L, thresh))