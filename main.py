class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

students = []

while True:
    print("\n1.Add Student")
    print("2.View Student")
    print("3.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        roll = int(input("Enter roll: "))

        s = Student(name, roll)
        students.append(s)

    elif choice == 2:
        for s in students:
            print(f"Name: {s.name}, Roll: {s.roll}")

    elif choice == 3:
        break