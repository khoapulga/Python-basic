# cach nhau boi dau phay- co the cho 1 list ben trong 1 list
list1 = [1,2,3,"day la 1 phan tu cua list",[3,4,2]]
print(list1)
# them phan tu o mot list rong
list_rong = []
list_rong.append(1)
print(list_rong)
# cu phap list-in ra phan tu trong list
list_moi = [1,2,4,"hello","chao"]
for i in list_moi:
    print(i)

# them va liet ke phan tu trong list tu 0-29   
rong = []
for i in range(0,10):
    rong.append(i)
    print(rong)
# dung list  dua ra danh sach tung phan tu cua chuoi or de sao chep chuoi

#ko dung cho so 
a =list('khoapulgak2')
print(a)
#toan tu trong list
#list +list
b= [1,2]
c=["howkteam","hello"]
print(b+c)
#lay phan tu trong list ( -1 la lay phan tu cuoi)
d = c[0]
print(d)
# thay doi gia tri cua list
list_moi =[1,2,4,'hello','howkteam']
list_moi[2]="hello world"
print (list_moi)
##bai tap
s = 'aaaaaaaAAAAAaaa//123123//000000//&&TTT%%abcxyznontqfadf'
a = s[35:38]
print(a)
code = s.split('&&')[-1].split('%%')[0]
print(code)

print(len(s))