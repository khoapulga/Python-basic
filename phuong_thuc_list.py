# phuong thuc dem mot phan tu trong list xuat hien bn lan
a= [1,2,3,4,5,6]
c = a.count(2)
print(c)
# index dua ra vi tri cua phan tu trong list
d = a.index(3)
print(d)
# copy : sao chep  1 list tuong tu
list_moi = [2,3,4,5]
#clear : xoa moi phan tu
#append: them phan tu
list_them = list_moi.append([5,6])
print(list_moi)
#extend : them tung phan tu
list_open = list_moi.extend(["hello","world"])
print(list_moi)
# insert: them phan tu x vao vi tri y
list_moi.insert(0,"this is a man")# them string "this is a man" vao vi tri dau
print(list_moi)
#pop: bo di phan tu thu i trong list -> tra ve gia tri do
bien_bo = list_moi.pop(1)
print(bien_bo)
#remove : bo di phan tu dau tien trong list co gia tri x
bien_remove = list_moi.remove(3)
print(bien_remove)
print(list_moi)
##phuong thuc reverse() : dao nguoc chuoi
list_moi.reverse()
print(list_moi)
## phuong thuc sort : cac phan tu phai cung kieu du lieu
list_moi.sort()
print(list_moi)