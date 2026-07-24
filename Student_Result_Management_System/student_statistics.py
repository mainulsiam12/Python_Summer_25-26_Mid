import numpy as np

class Statistics:

    def show_statistics(self, students):

        if len(students) == 0:

            print("No Student Data Found.")

            return

        percentage_list = []

        topper = students[0]

        for student in students:

            percentage_list.append(student.percentage())

            if student.percentage() > topper.percentage():

                topper = student

        percentage_array = np.array(percentage_list)

        print("\n CLASS STATISTICS ")

        print("Total Students :", len(students))

        print("Highest Percentage :", np.max(percentage_array))

        print("Lowest Percentage :", np.min(percentage_array))

        print("Average Percentage :", np.mean(percentage_array))

        print("\n TOPPER STUDENT ")

        topper.display()