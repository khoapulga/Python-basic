# cong thuc
def hello(n):
    print("welcome:",n)
hello('khoa')
###
def DemTen(Name):
 
    return len(Name)
 
DienTen = "Quantrimang.com"
 
print(DemTen(DienTen))
# __doc___ : goi la doc string : giai thich chuc nang cua ham
# paramater la bien duoc goi trong ham
#argusmetn la gia tri truyen vao paramater
# vi du o def hello : n la para con khoa la args
# default paramater
#vd
def thisinh(name,age,text ="sinh vien vmu"):
    print("thong tin thi sinh:",name,age)
thisinh("Bui Dang Khoa",24)
def old(name,dateofbirth,country):
    print("Sinh vien %s tuoi %s quoc tich %s"%(name,dateofbirth,country))
old("bui dang khoa","23","vienam")
## su dung keyword argument
def hihi(a,b,c,d):
    print(a+b+c+d)
hihi(a=5,c=7,d=9,b=3)
hihi(3,4,5,5)
#unpacking dung *
def ktem(a,b,c,d,e):
    print(a,b,c,d,e)

lst =[1,2,3,4,5]
ktem(*lst)
#packing argument voi * -> ra tuple
def ktem(*args):
    print(args)
    print(type(args))
ktem("hkteam","hello",1,2)
#unpacking voi ** muon lay ca gia tri key ma value cua dic
dic ={'name':'khoa','howkteam':'free education'}
def dicc(name,howkteam):
    print("name->",name)
    print("howkteam->",howkteam)
dicc(**dic)
#packing voi ** -- > ra mot dict
def dic2(**kwargs):
    print(kwargs)
    print(type(kwargs))
dic2(name ="kteam",member ="bui dang khoa")
def plus(*args):
    print(args)
    print(type(args))
plus('howkteam',2,3,4)
# co the khong truyen arg cho * argss hoac ** argss
def test(*argss,**kwargss):
    print(argss)
    print(kwargss)
test(name='hello')
#### loacl va global
def make_global():
    global x
    x = 1
def local():
    x = 5
    print('x in local:',x)
make_global()
print(x)
local()
print(x)
## dung return -- > co the gan nhieu gia tri tuong ung cho ham
def congthuc(chieudai,chieurong):
    chuvi = (chieudai+chieurong) *2
    s =chieudai * chieurong 
    return chuvi,s
chieurong =5 
chieudai = 10
chuvi,dientich = congthuc(chieudai,chieurong)
print(chuvi,dientich) 
# yield
#lambda
ave = lambda a,b,c:(a+b+c)/3
print(ave(2,3,4))
# default arguments
x =lambda  x, a=2: x**2
print(x(3))
# global and local lambda:
def kk():
    mem = lambda x: x +  ' is a member of kteam'
    return mem
call_men = kk()
print(call_men('khoa'))
### list
ktem_list = [lambda x: x**2,lambda x: x**4]
for uni in ktem_list:
    print(uni(3))

