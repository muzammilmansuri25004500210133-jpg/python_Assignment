coaching_students = []

def add_student():
    sid = int(input("Enter Student ID: "))
    sname = input("Enter Student Name: ")
    batch = input("Enter Batch Time (e.g., 4PM-5PM): ")
    fees = int(input("Enter Fees Paid: "))
    student_data = {"StudentID": sid, "StudentName": sname, "BatchTime": batch, "FeesPaid": fees}
    coaching_students.append(student_data)
    print("Student registered successfully!")

def display_all():
    if not coaching_students:
        print("Registry is empty. No students found.")
        return
    print("=================================================================")
    print("Student ID     Student Name      Batch Time     Fees Paid")
    print("=================================================================")
    for s in coaching_students:
        print(s["StudentID"], "                  ", s["StudentName"], "              ", s["BatchTime"], "          ", s["FeesPaid"])

def search_student():
    sid = int(input("Enter Student ID to search: "))
    found = 0
    for s in coaching_students:
        if s["StudentID"] == sid:
            found = 1
            break
    if found == 1:
        print("Student Found!")
        print("=================================================================")
        print("Student ID     Student Name      Batch Time     Fees Paid")
        print("=================================================================")
        print(s["StudentID"], "                  ", s["StudentName"], "              ", s["BatchTime"], "          ", s["FeesPaid"])
    else:
        print("Student record not found.")

def update_batch():
    sid = int(input("Enter Student ID to update details: "))
    found = 0
    for s in coaching_students:
        if s["StudentID"] == sid:
            found = 1
            break
    if found == 1:
        print("Student Found!")
        print("What do you want to update?")
        print("1. Update Batch Time")
        print("2. Update Fees Paid")
        print("3. Update Both (Batch & Fees)")
        
        choice = input("Enter choice (1-3): ")
        
        if choice == "1":
            new_batch = input("Enter New Batch Time: ")
            s["BatchTime"] = new_batch
            print("Batch updated successfully!")
        elif choice == "2":
            new_fees = int(input("Enter New Fees Paid: "))
            s["FeesPaid"] = new_fees
            print("Fees updated successfully!")
        elif choice == "3":
            new_batch = input("Enter New Batch Time: ")
            new_fees = int(input("Enter New Fees Paid: "))
            s["BatchTime"] = new_batch
            s["FeesPaid"] = new_fees
            print("Batch and Fees updated successfully!")
        else:
            print("Invalid choice! No changes made.")
            return
        print("=================================================================")
        print("Student ID     Student Name      Batch Time     Fees Paid")
        print("=================================================================")
        print(s["StudentID"], "            ", s["StudentName"], "            ", s["BatchTime"], "       ", s["FeesPaid"])
    else:
        print("Student record not found.")


def delete_student():
    sid = int(input("Enter Student ID to remove: "))
    found = 0
    for s in coaching_students:
        if s["StudentID"] == sid:
            coaching_students.remove(s)
            found = 1
            print("Student record deleted successfully!")
            break
    if found == 0:
        print("Student record not found.")

def total_fees_collected():
    if not coaching_students:
        print("Total collection is 0.")
        return
    
    total = 0
    for s in coaching_students:
        total = total + s["FeesPaid"]
    print(f"Total Fees Collected in Coaching: Rs. {total}")
