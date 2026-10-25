# STUDENT ATTENDANCE REGISTER
# Using Text File

def add_student():
    f = open("students.txt", "a")

    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")

    f.write(roll + "|" + name + "\n")
    f.close()

    print("Student added successfully!")


def mark_attendance():
    roll = input("Enter Roll Number: ")
    date = input("Enter Date (DD-MM-YYYY): ")
    status = input("Enter P for Present / A for Absent: ").upper()

    if status == "P":
        status = "Present"
    elif status == "A":
        status = "Absent"
    else:
        print("Invalid choice!")
        return

    f = open("attendance.txt", "a")
    f.write(roll + "|" + date + "|" + status + "\n")
    f.close()

    print("Attendance marked successfully!")


def view_attendance():
    roll = input("Enter Roll Number: ")

    try:
        f = open("attendance.txt", "r")
        found = False

        print("\nAttendance Record")
        print("--------------------------")

        for line in f:
            data = line.strip().split("|")

            if data[0] == roll:
                print("Date:", data[1], " Status:", data[2])
                found = True

        f.close()

        if not found:
            print("No attendance record found.")

    except FileNotFoundError:
        print("Attendance file does not exist.")


def attendance_percentage():
    roll = input("Enter Roll Number: ")

    try:
        f = open("attendance.txt", "r")

        total = 0
        present = 0

        for line in f:
            data = line.strip().split("|")

            if data[0] == roll:
                total = total + 1

                if data[2] == "Present":
                    present = present + 1

        f.close()

        if total == 0:
            print("No attendance record found.")
        else:
            percentage = (present / total) * 100

            print("\nTotal Classes :", total)
            print("Present       :", present)
            print("Absent        :", total - present)
            print("Attendance %  :", round(percentage, 2), "%")

    except FileNotFoundError:
        print("Attendance file does not exist.")


def view_students():
    try:
        f = open("students.txt", "r")

        print("\nStudent List")
        print("--------------------------")

        for line in f:
            data = line.strip().split("|")
            print("Roll No:", data[0], " Name:", data[1])

        f.close()

    except FileNotFoundError:
        print("No students registered.")


# MAIN PROGRAM

while True:

    print("\n==============================")
    print("   STUDENT ATTENDANCE SYSTEM")
    print("==============================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Mark Attendance")
    print("4. View Attendance")
    print("5. Attendance Percentage")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        mark_attendance()

    elif choice == "4":
        view_attendance()

    elif choice == "5":
        attendance_percentage()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
