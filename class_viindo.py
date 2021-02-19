# ke thua trong python
class person:
    def __init__(self,name,tuoi,gioitinh):
        self.name=name
        self.tuoi=tuoi
        self.gioitinh=gioitinh
    def getname(self):
        return self.name
class student(person):
    def gettuoi(self):
        return self.tuoi
student1 = person("khoa","23","nam")
print(student1.name)
print(student1.tuoi)
print(student1.gioitinh)
print(student1.getname())
class employee(person):
    pass
employee = person("hoang","23","nam")
print(employee.getname())
## kiem tra xem co phai chuoi con khong
print(issubclass(student,person))
## kiem tra xem doi tuong thuoc lop student co su dung phuong thuc cua person khong
print(isinstance(student1,person))
####  Da ke thua trong python

    