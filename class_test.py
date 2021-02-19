class animal:
    def __init__(self,name):
        self.name = name
    def inten(self):
        return(self.name)
class student(animal):
    def __init__(self,name):
        super().__init__(name)

a = student('khoa')
print(a.inten())