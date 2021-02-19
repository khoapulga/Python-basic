n = input("nhap so n: ")
n= int(n)
sum = 0
i =1 
while(i<=n):
    
    sum = sum + i
    i+=1
print("tong la :",sum )
## break va continue
## dem va in cac so nho hon hai
n =0 
while n <=2 :
    print("cac so nho hon hai la %d"%n)
    n+=1
else:
    print(n,"khong nho hon hai")
## su dung break de ket thuc vong lap
list1 =[]
dem = 1 
while dem<10: 
    dem+=1
    if dem %2 == 0:
        
        continue
    print("so le la:%d"%dem)
    

print(dem)
## bai tap
five_even_number =[]
k_number =1 
while len(five_even_number)<5:
    if(k_number%2==0):
        five_even_number.append(k_number)
        
    
    k_number+=1
print(five_even_number)

        
    
        