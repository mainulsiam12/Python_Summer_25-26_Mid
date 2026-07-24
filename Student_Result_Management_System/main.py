from manager import StudentManager

manager = StudentManager()

while True:

    
    print(" STUDENT RESULT MANAGEMENT SYSTEM ")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Save Student Data")
    print("7. Show Statistics")
    print("8. Exit")
    

    choice = input("Enter Your Choice : ")

    if choice == "1":

        manager.add_student()

    elif choice == "2":

        manager.view_students()

    elif choice == "3":

        manager.search_student()

    elif choice == "4":

        manager.update_student()

    elif choice == "5":

        manager.delete_student()

    elif choice == "6":

        manager.save_students()

    elif choice == "7":

        manager.show_statistics()

    elif choice == "8":

        answer = input("Do You Want To Save Data? (Y/N) : ")

        if answer == "Y" or answer == "y":

            manager.save_students()

        print("Thank You")

        break

    else:

        print("Invalid Choice.")