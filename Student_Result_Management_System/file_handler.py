from student import Student

class FileHandler:

    # Save Student Data
    def save_students(self, students):

        try:

            file = open("students.txt", "w")

            for student in students:

                data = student.id + ","
                data = data + student.name + ","
                data = data + str(student.marks[0]) + ","
                data = data + str(student.marks[1]) + ","
                data = data + str(student.marks[2])

                file.write(data)
                file.write("\n")

            file.close()

            print("Student Data Saved Successfully.")

        except:

            print("Error Saving Student Data.")

    # Load Student Data
    def load_students(self):

        students = []

        try:

            file = open("students.txt", "r")

            for line in file:

                line = line.strip()

                if line == "":

                    continue

                data = line.split(",")

                if len(data) == 5:

                    student = Student()

                    student.id = data[0]
                    student.name = data[1]

                    student.marks.append(float(data[2]))
                    student.marks.append(float(data[3]))
                    student.marks.append(float(data[4]))

                    students.append(student)

            file.close()

        except FileNotFoundError:

            print("No Previous Data Found.")

        except:

            print("Error Loading Student Data.")

        return students