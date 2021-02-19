## ham init khoi tao - coi self nhu 1 object 
class footballer:
    def __init__(self,ten,tuoi,quoctich):
        self.name = ten
        self.old = tuoi
        self.country = quoctich
    def offline(self):
        return "hello my name is:" + self.name
cau_thu_1 = footballer("messi","32","VietNam")
print("ten cua cau thu:",cau_thu_1.name)
print("tuoi:",cau_thu_1.old)
print("quoc tich:",cau_thu_1.country)
print(cau_thu_1.offline())
### thuoc tinh cua lop
class champ:
    power = 103
    def __init__(self,ten,do_kho):
        self.fullname = ten
        self.do_kho = do_kho
    @classmethod
    def cap_nhat_power(cls,pw):
        cls.power=  pw
champ_1 = champ("ashe","4")
champ_2 = champ("zed","5")
## add class
class animal:
    pass
#print(champ_1.fullname,champ_1.do_kho)
print(champ_1.cap_nhat_power(34))
print(champ_1.power)
print(champ_2.power)# cap nhat toan bo
    
