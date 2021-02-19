#Chuoi
string = "this is a man"
string2 = " who met me yesterday"
string3= string+"\n"+string2
print(string3)
string4 = string2 * 3
print(string4)
#kiem tra chuoi trong chuoi
string5 = string2 in string
print(string5)
#lay ki tu trong chuoi
chuoi = string[2]
print(chuoi)
#lay ki tu cuoi trong chuoi
chuoi2 = string[len(string)-1]
print (chuoi2)
# cat chuoi - cat tu vi tri 1 den vi tri 3. den 3 la dung nen ko lay vi tri 3
chuoi_cat = string[1:3]
print(chuoi_cat)
# ep kieu du lieu- tu chuoi thanh so
songuyen = int("23")
sothuc=float("4.5")
print(songuyen*sothuc)
#ep tu so thanh cuoi
main_string = str(69)
substring ="hello"
print(main_string+substring)
#formating string
a = "This is a dangerous message"
print("%s you dont have to open it"%a)
b="this is a book"
print("%s"%b)
#format by f-string( dinh danh bang chuoi f-string)
f='make your life better'
result = f'{f}-change your mind'#dung f se thay gia tri cua string f .
print(result)
# dinh dang by format
string_format = '1:{one},2:{two}'.format(one=111,two=222)
print(string_format)
# can le
row_1 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')
row_2 = '| {:<6} | {:^15} | {:>10} |'.format('ID', 'Ho va ten', 'Noi sinh')
row_3 = '| {:<6} | {:^15} | {:>10} |'.format('123', 'Yui Hatano', 'Japanese')
row_4 = '| {:<6} | {:^15} | {:>10} |'.format('6969', 'Sunny Leone', 'Canada')
row_5 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')

print(row_1)
print(row_2)
print(row_3)
print(row_4)
print(row_5)

# viet hoa chu cai dau ham capitalize
chuoi_ban_dau = 'how kteam -free education'
chuoi_viet_hoa = chuoi_ban_dau.capitalize()
print(chuoi_viet_hoa)
# ham title,uppder,lower,swapcase
# phuong thuc join
#replace ('mot ki tu or mot chuoi','chuoi moi')
#split tach chuoi
a ="this is my favourite book"
b= a.split(' ')
print(b)
#count (dem)
chuoi_dem = a.count('i')
print (chuoi_dem)

num1 =10;
num2 ="hello"
num3 =  100.0
ghepchuoi = "{}*{}={}".format(num1,num2,num3)
format_f = f"num1 * num2 =num3"
format_pt = "%d * %s = %d"%(num1,num2,num3)
print(format_pt)
print(format_f)
print(ghepchuoi)
print(num2.join("hello"))
print(num2.replace('l','3'))
print(len(num2))