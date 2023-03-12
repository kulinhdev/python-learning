import sqlite3
from prettytable import PrettyTable


class Student:
    def __init__(self, name, age, email, address):
        self.name = name
        self.age = age
        self.email = email
        self.address = address


class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()

    def create_table(self):
        try:
            self.c.execute('''
                CREATE TABLE students (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER,
                email TEXT,
                address TEXT
            );
            ''')

            self.conn.commit()
        except sqlite3.OperationalError:
            print("This table already exists!")
        else:
            print("Create table successfully!")

    def add_student(self, student):
        self.c.execute(
            "INSERT INTO students (name, age, email, address) VALUES (?, ?, ?, ?)",
            (student.name, student.age, student.email, student.address),
        )
        self.conn.commit()
        print(f"{self.c.rowcount} record(s) inserted.")

    def update_student(self, id, student):
        self.c.execute(
            "UPDATE students SET name=?, age=?, email=?, address=? WHERE id=?",
            (student.name, student.age, student.email, student.address, id),
        )
        self.conn.commit()
        print(f"{self.c.rowcount} record(s) updated.")

    def delete_student(self, id):
        self.c.execute("DELETE FROM students WHERE id=?", (id,))
        self.conn.commit()
        print(f"{self.c.rowcount} record(s) deleted.")

    def get_students(self):
        self.c.execute("SELECT * FROM students")
        rows = self.c.fetchall()

        # Create a table with column names
        table = PrettyTable(["ID", "Name", "Age", "Email", "Address"])

        # Add each row to the table
        for row in rows:
            table.add_row(row)

        print(table)

    def sort_students_by_age(self):
        self.c.execute("SELECT * FROM students ORDER BY age")
        rows = self.c.fetchall()

        # Create a table with column names
        table = PrettyTable(["ID", "Name", "Age", "Email", "Address"])

        # Add each row to the table
        for row in rows:
            table.add_row(row)

        print(table)

    def find_students_by_name(self, name):
        self.c.execute("SELECT * FROM students WHERE name LIKE ?", (f"%{name}%",))
        rows = self.c.fetchall()

        # Create a table with column names
        table = PrettyTable(["ID", "Name", "Age", "Email", "Address"])

        # Add each row to the table
        for row in rows:
            table.add_row(row)

        print(table)


db = Database("students.sqlite")

while True:
    print("\n" + "=" * 80)
    print(" " * 30 + "Menu Options")
    print("=" * 80)
    # print("Option\tDescription")
    # print("-" * 80)
    print("1\tCreate table")
    print("2\tAdd student")
    print("3\tUpdate student")
    print("4\tDelete student")
    print("5\tGet all students")
    print("6\tSort students by age")
    print("7\tFind students by name")
    print("8\tExit")
    print("=" * 80)

    option = int(input("Enter option: "))

    if option == 1:
        db.create_table()
    elif option == 2:
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        email = input("Enter student email: ")
        address = input("Enter student address: ")
        student = Student(name, age, email, address)
        db.add_student(student)
    elif option == 3:
        id = int(input("Enter student ID: "))
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        email = input("Enter student email: ")
        address = input("Enter student address: ")
        student = Student(name, age, email, address)
        db.update_student(id, student)
    elif option == 4:
        id = int(input("Enter student ID: "))
        db.delete_student(id)
    elif option == 5:
        db.get_students()
    elif option == 6:
        db.sort_students_by_age()
    elif option == 7:
        name = input("Enter student name: ")
        db.find_students_by_name(name)
    elif option == 8:
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")