class Abc:
    def __init__(self):
        self.a=10
        self._b=20
        self.__c=30
    def putData(self):
        print(self.a)
        print(self._b)
        print(self.__c)
class Xyz(Abc):
    def showData(self):
        print("a=",self.a)
        print("_b=",self._b)
       # print(self.__c)
x1=Xyz()
x1.showData()
print(x1.a)
print(x1._b)
#print(x1.__c)