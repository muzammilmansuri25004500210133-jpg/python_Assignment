class Student:
    def __init__(self):
        self.rno=1
        self.nm="abc"
    def getData(self):
        self.rno=int(input("Enter Roll no : "))
        self.nm=input("Enter Name : ")
    def putData(self):
        print("Roll no is : ",self.rno)
        print("Name is : ",self.nm)
class Internal(Student):
    def __init__(self):
        self.itotal=200
    def getData(self):
        super().getData()
        self.itotal=int(input("Enter internal marks : "))
    def putData(self):
        super().putData()
        print("toatal internal marks is : ",self.itotal)
class External(Internal):
    def __init__(self):
        self.etotal=200
    def getData(self):
        super().getData()
        self.etotal=int(input("Enter External marks : "))
    def putData(self):
        super().putData()
        print("toatal External marks is : ",self.etotal)
e1=External()
e1.getData()
e1.putData()