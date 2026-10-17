import CoachingOp as c1

while True:
    print("\n*** COACHING CENTER REGISTRY SYSTEM ***")
    print("1. Add New Student")
    print("2. Display All Students")
    print("3. Update Student Batch Time")
    print("4. Delete Student Record")
    print("5. Search Student by ID")
    print("6. Show Total Fees Collected")
    print("7. Exit")
    
    choice = input("Enter your choice (1-7): ")
    print("---------------------------------")
    
    if choice == "1":
        c1.add_student()
    elif choice == "2":
        c1.display_all()
    elif choice == "3":
        c1.update_batch()
    elif choice == "4":
        c1.delete_student()
    elif choice == "5":
        c1.search_student()
    elif choice == "6":
        c1.total_fees_collected()
    elif choice == "7":
        print("Exiting Coaching System. Goodbye!")
        break
    else:
        print("Invalid option selected. Please choose between 1 and 7.")
