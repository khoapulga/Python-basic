# phan tu duoc gioi han bang cap {}
# phan tu duoc phan cach boi dau phay ","
# phan tu cua dict phai la mot cap key-value
# cap key-value duoc phan cach boi dau hai cham
# cac key la hash object

# vi du :
dict1= {'name':'ktem','member':69}
print(dict1)
# khoi tao 1 dict rong
dict_rong = {}
# 4 cach dung constructor
#cach 1 : dung dict
#cach 2: dung mapping object
#cach 3 : dung iterable : dict(iterable)
#vd :
iter_ = [('name','Kteam'),('member',69)]
dic = dict(iter_)
print(dic)
print(type(dic))
print(type(iter_))
#cach 4: tao bang keyword arguments
dic2 = dict(name = 'how kteam',member = 69)
print(dic2)
# su dung phuong thuc fromkeys
iter1 = ('name','number')
dic3 = dict.fromkeys(iter1,'no love no life')
print(dic3)
print(dic['name'])
# thay doi noi dung trong dict
dic['name'] = "death likes a wind"
print(dic)
# them mot phan tu vao dict( thay doi phan tu)
dic2['member'] = dic2['member']+1
print(dic2)
