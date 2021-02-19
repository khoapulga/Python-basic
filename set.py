# la container
# duoc gioi han boi cap {}
# la nhung phan tu cua set, phan cach nhau boi dau phay
#khong chua phan tu trung lap
# chua hashable object nhung ban than set ko p la hashable

set_1 ={45,54}
print(set_1)
print(type(set_1))

set_2 = {'how kteam'}
print(set_2)


set_3 ={(69,'free education'),(1,2,3)}
print(set_3)
# toan tu tru
print ({1,2,3}-{2,3})
# toan tu va
print({1,2,3}&{4,5})
# toan tu hoac
print({1,2,3}|{5})
## cac phuong thuc
#clear(): xoa phan tu trong set
#pop(): lay gia tri dau tien cua set
set_1.pop()
print(set_1)
#remove : loai bo phan tu trong set
set_3.remove((1,2,3))
print(set_3)
#discard: loai bo gia tri value trong set ( giong remove) nhung neu sai thi tra ve set cu
#copy: tra ve ban sao cua set
#add : them value vao set neu value trong set thi bo qua
set_3.add(34)
print(set_3)

print(4%4)