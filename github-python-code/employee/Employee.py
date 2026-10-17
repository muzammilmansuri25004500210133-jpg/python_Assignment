class Emp:
    def __init__(self, e_id=0, e_nm="", e_bs=1000):
        self.e_id = e_id
        self.e_nm = e_nm
        self.e_bs = e_bs
        self.hra = 0
        self.da = 0
        self.pf = 0
        self.ns = 0

    def getData(self):
        self.e_id = int(input("Enter employee id : "))
        self.e_nm = input("Enter employee name : ")
        self.e_bs = int(input("Enter employee salary : "))

    def calSalary(self):
        if self.e_bs < 5000:
            self.hra = self.e_bs * 0.10
            self.pf = self.e_bs * 0.20
            self.da = self.e_bs * 0.05
        elif self.e_bs < 10000:
            self.hra = self.e_bs * 0.20
            self.pf = self.e_bs * 0.40
            self.da = self.e_bs * 0.10
        else:
            self.hra = self.e_bs * 0.30
            self.pf = self.e_bs * 0.60
            self.da = self.e_bs * 0.15

        self.ns = self.e_bs + self.hra + self.da - self.pf

    def putData(self):
        print("\n--- Employee Details ---")
        print("--------------------------------------")
        print("Employee ID : ", self.e_id)
        print("Employee Name : ", self.e_nm)
        print("Employee Salary : ", self.e_bs)
        print("Employee HRA : ", self.hra)
        print("Employee DA : ", self.da)
        print("Employee PF : ", self.pf)
        print("--------------------------------------")
        print("Employee Net Salary : ", self.ns)

