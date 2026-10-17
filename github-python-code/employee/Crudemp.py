import Employee
emplst = []
   
while True:
    print("==========Employee Menu==========")
    print("\n1.Add employee\n2.Display\n3.Search\n4.Update\n5.Delete\n6.Exit")
    choise=int(input("Enter your choice: "))
    #Add or insert record
    if choise==1:
        emp=Employee.Emp()
        emp.getData()
        found=False
        for e in emplst:
            if e.e_id==emp.e_id:
                found=True
                break
        if found:
            print("Data exist")
        else:
            emplst.append(emp)
            print("Data added successfully...!")
    #Display
    elif choise==2:
        if len(emplst)==0:
            print("No employee data available")
        else:
            for e in emplst:
                e.calSalary()
                e.putData()
    #Search
    elif choise==3:
        eid=int(input("Enter the employee id for search: "))
        if len(emplst)==0:
            print("No employee data available")
        else:
            for e in emplst:
                if eid==emp.e_id:
                    found=True
                    break
        if found:
            print("Data found..!")
            for e in emplst:
                e.calSalary()
                e.putData()
        else:
            print("Data are not found...!!!")
    #Update   
    elif choise==4:
            key=int(input("Enter Employee Id: "))
            found=False
            for i in range(len[emplst]):
                if(str(emplst[i].e_id)==key):
                    emp=Employee.Emp()
                    emp.e_nm=input("Enter name: ")
                    emp.e_bs=int(input("Enter salary: "))
                    emp.e_id=emplst[i].e_id
                    emp.calSalary()
                    emplst[i]=emp
                    found=True
                    break
            if not found:
                print("Employee not found..!")
            '''
            key=input("Enter id to Update")
            found=False
            for e in emplst:
                if(str(e.eid)==key):
                    print("\nEmployee Found..!!)
                    e.putData()

                    print("Enter new employee details: ")
                    e.getData()
                    e.calSalary()
                    e.putData()

                    print("\nEmployee updated successfully..!")
                    break
            if not found:
                print("Employee not found...")
                break
            '''
    #Delete
    elif choise==5:
        key=input("Enter employee EID or Name to delete: ")
        
        found=False

        for emp in emplst:
            if(str(emp.e_id)==key or emp.e_nm.lower()==key.lower()):
                emplst.remove(emp)
                print("Employee deleted successfully..!")
                found=True
                break
            if not found:
                print("Employee not found..!")
    #Exit
    elif choise==6:
        print("Programe terminated..!!!")
        break
    else:
        print("Invalid choise..")


