##bai 1
diem_toan = input('Nhap diem Toan:')
diem_ly = input('Nhap diem Ly: ')
diem_hoa = input('Nhap diem Hoa:')

a = float(diem_toan)
b =float(diem_ly)
c = float(diem_hoa)

tong = a+b+c
if (tong>15 and a>=4 and b>=4 and c>=4):
    print('thi dau')
    if( a>=5 and c>=5 and c>=5 ):
        print("hoc deu")
    else:
        print("hoc khong deu")
else:
    print("truot")
    
## bai 2
'''
time = input("nhap so gio lam: ")
luong = input("nhap luong: ")

time = float(time)
luong = float(luong)

tong_luong = time * luong
if(time>40):
    luong_moi = (time - 40) * 1.5 * luong + 40 * luong
    print('Tong so luong cua nhan vien nay la: %f' %luong_moi)
else:
    print('tong so luong cua nhan vien nay la:%f'%tong_luong)
'''

### bai 3
'''
a = input("nhap so nguyen thu nhat: ")
b =input("nhap so nguyen thu hai: ")
c = input("nhap so nguyen thu ba: ")

a=int(a)
b=int(b)
c=int(c)

if(a >b and a > c):
    if(b>c):
        print(a,b,c)
    else:
        print(a,c,b)
elif (b>a and b >c):
    if(a>c):
        print(b,a,c)
    else:
        print(b,c,a)
elif(c>a and c>b):
    if(b>a):
        print(c,b,a)
    else:
        print(c,a,b)
'''