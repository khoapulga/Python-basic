#duoc gioi han boi cap ()
#cac phan tu ngan cach boi dau ,
#tuple co kha nang chua moi gia tri
#toc do truy xuat cua tuple nhanh hon list
#dung luong chiem trong bo nho it hon list
#bao ve du lieu cua ban se khong thay doi
# co the dung lam key cua dictionary

#khoi tao 1 bien tupl va in ra man hinh
#la mot hash object-khong the chinh sua noi dung
tup = (1,2,4,3,8,"howkteam",(8,9,10))
print(tup)
# generater expression
tup1 =(i for i in range(10) if i %2 ==0)
a =tuple(tup1)
print(a)
 # toan tu cua tuple giong toan tu cua string
 #toan tu cong
b = tup + (2,4,6)
print(b)
#toan tu nhan
#toan tu in
c = 2 in tup
print(c)
##  lay phan tu giong nhu list
phan_tu_dau = tup[2]
print (phan_tu_dau)
# len: lay do dai
do_dai = len(tup)
print(do_dai)
# lay phan tu tu bn -> bn
dao_nguoc = tup[::-1]
print(dao_nguoc)
# 
tup2 =(1,2,5,4)
hello = sorted(tup2)
print(hello)
# 
