from student import Student
from file_handler import FileHandler
from student_statistics import Statistics

class StudentManager:

    def __init__(self):

     self.file = FileHandler()

     self.statistics = Statistics()

     self.students = self.file.load_students()

     self.student_ids = set()

     for student in self.students:

        self.student_ids.add(student.id)

    # Add Student
    def add_student(self):

        student = Student()

        student.input_student()

        if student.id in self.student_ids:

            print("Student ID Already Exists.")

            return

        self.students.append(student)

        self.student_ids.add(student.id)

        print("Student Added Successfully.")

    # View All Students
    def view_students(self):

        if len(self.students) == 0:

            print("No Student Found.")

            return

        count = 1

        for student in self.students:

            print("\nStudent", count)

            student.display()

            count += 1

    # Search Student
    def search_student(self):

        student_id = input("Enter Student ID : ").strip()

        found = False

        for student in self.students:

            if student.id == student_id:

                student.display()

                found = True

                break

        if found == False:

            print("Student Not Found.")

    # Update Student
    def update_student(self):

        student_id = input("Enter Student ID : ").strip()

        found = False

        for student in self.students:

            if student.id == student_id:

                student.marks = []

                subjects = ("Python", "Math", "English")

                for subject in subjects:

                    while True:

                        try:

                            mark = float(input("Enter " + subject + " Marks : "))

                            if mark < 0 or mark > 100:

                                print("Invalid Marks.")

                            else:

                                student.marks.append(mark)

                                break

                        except:

                            print("Please Enter Numeric Value.")

                print("Student Updated Successfully.")

                found = True

                break

        if found == False:

            print("Student Not Found.")

    # Delete Student
    def delete_student(self):

        student_id = input("Enter Student ID : ").strip()

        found = False

        for student in self.students:

            if student.id == student_id:

                self.students.remove(student)

                self.student_ids.remove(student.id)

                print("Student Deleted Successfully.")

                found = True

                break

        if found == False:

            print("Student Not Found.")
    
    
    # Save Student Data
    def save_students(self):

        self.file.save_students(self.students)
    
    
    # Show Statistics
    def show_statistics(self):

        self.statistics.show_statistics(self.students)