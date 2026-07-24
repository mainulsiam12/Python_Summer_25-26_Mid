class Student:

    def __init__(self):

        self.id = ""
        self.name = ""
        self.marks = []

    def input_student(self):

        while True:

            self.id = input("Enter Student ID : ").strip()

            if self.id == "":

                print("Student ID Cannot Be Empty.")

            else:

                break

        while True:

            self.name = input("Enter Student Name : ").strip()

            if self.name == "":

                print("Student Name Cannot Be Empty.")

            else:

                break

        self.marks = []

        subjects = ("Python", "Math", "English")

        for subject in subjects:

            while True:

                try:

                    mark = float(input("Enter " + subject + " Marks : "))

                    if mark < 0 or mark > 100:

                        print("Invalid Marks.")

                    else:

                        self.marks.append(mark)

                        break

                except:

                    print("Please Enter Numeric Value")

    def total(self):

        return sum(self.marks)

    def percentage(self):

        return self.total() / len(self.marks)

    def grade(self):

        percentage = self.percentage()

        if percentage >= 80:

            return "A+"

        elif percentage >= 70:

            return "A"

        elif percentage >= 60:

            return "B"

        elif percentage >= 50:

            return "C"

        elif percentage >= 40:

            return "D"

        else:

            return "F"

    def status(self):

        if self.percentage() >= 40:

            return "PASS"

        else:

            return "FAIL"

    def display(self):

    

        print("Student ID :", self.id)

        print("Student Name :", self.name)

        print("Marks :", self.marks)

        print("Total :", self.total())

        print("Percentage :", self.percentage())

        print("Grade :", self.grade())

        print("Status :", self.status())
