d ={'team':'kteam',(1,2):69}
print(d)
#phuong thuc copy
#clear()
#get()
# lay value cua key- 
value = d.get("team")
print(value)
#items - > tra ket qua ve tuple
ketqua = list(d.items())
print(ketqua[0])
# keys lay ra ds key, value lay ra ds value
print(d.values())
print(d.keys())
print(d.pop('team'))
defal = d.setdefault("hello","son")
print(d)
defal = d.setdefault("hello")
print(d)

dic4 = {"ktem":"name","how":"much"}
print(dic4)
lisst1 = list(dic4)
print(lisst1)
tup = tuple(lisst1)
print(tup)
sse = set(tup)
print(sse)
print(type(sse))