##3
set_={5,8,1,9,4}
tong = 0
for a in set_:
    tong+=a
print(tong)

for val in "string":
    if val == "i":
        break
    print(val)

print("Kết thúc!")
### vong lap duyet mot dic
dic = {"hello":"world","member":67}
for key,value  in dic.items():
    print(key,'->',value)

list1 = [5,{6,7,8},("hello",4,5)]
for i in range(len(list1)):
    i+=1
print(list1)