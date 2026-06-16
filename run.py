import main

sms = main.StudentManagementSystem()
while True:
    print("\n====== STUDENT MANAGEMENT SYSTEM ======")
    print("Enter 1 to Add student: ")
    print("Enter 2 to View student: ")
    print("Enter 3 to Search student: ")
    print("Enter 4 to Update student: ")
    print("Enter 5 to Delete student: ")
    print("Enter 6 to Display Topper student: ")
    print("Enter 7 to Exit : ")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        sms.add_student()

    elif choice == 2:
        sms.view_students()
    
    elif choice == 3:
        sms.search_stu()
    elif choice == 4:
        sms.update_marks()
    elif choice == 5:
        sms.delete_student()
    elif choice == 6:
        sms.display_topper()
    elif choice == 7:
        break