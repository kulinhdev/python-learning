import sqlite3
from prettytable import PrettyTable

conn = sqlite3.connect('students.sqlite')
c = conn.cursor()


def create_table():
    try:
        c.execute('''
            CREATE TABLE students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            email TEXT,
            address TEXT
        );
        ''')

        conn.commit()
    except sqlite3.OperationalError:
        print("This table already exists!")
    else:
        print("Create table successfully!")


def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    email = input("Enter student email: ")
    address = input("Enter student address: ")

    c.execute("INSERT INTO students (name, age, email, address) VALUES (?, ?, ?, ?)", (name, age, email, address))

    conn.commit()

    print(f"{c.rowcount} record(s) inserted.")


def update_student():
    id = int(input("Enter student id: "))

    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    email = input("Enter student email: ")
    address = input("Enter student address: ")

    c.execute("UPDATE students SET name=?, age=?, email=?, address=? WHERE id=?", (name, age, email, address, id))

    conn.commit()

    print(f"{c.rowcount} record(s) updated.")


def delete_student():
    id = int(input("Enter student id: "))

    c.execute("DELETE FROM students WHERE id=?", (id,))

    conn.commit()

    print(f"{c.rowcount} record(s) deleted.")


def get_students():
    c.execute('SELECT * FROM students')

    rows = c.fetchall()

    # Create a table with column names
    table = PrettyTable(['ID', 'Name', 'Age', 'Email', 'Address'])

    # Add each row to the table
    for row in rows:
        table.add_row(row)

    print(table)


def sort_students_by_age():
    c.execute('SELECT * FROM students ORDER BY age')

    rows = c.fetchall()

    # Create a table with column names
    table = PrettyTable(['ID', 'Name', 'Age', 'Email', 'Address'])

    # Add each row to the table
    for row in rows:
        table.add_row(row)

    print(table)


def find_students_by_name():
    name = input("Enter student name: ")

    c.execute('SELECT * FROM students WHERE name LIKE ?', (f'%{name}%',))

    rows = c.fetchall()

    # Create a table with column names
    table = PrettyTable(['ID', 'Name', 'Age', 'Email', 'Address'])

    # Add each row to the table
    for row in rows:
        table.add_row(row)

    print(table)


while True:
    print("\n=== Menu Options: ===")
    print("1. Create table")
    print("2. Add student")
    print("3. Update student")
    print("4. Delete student")
    print("5. Get all students")
    print("6. Sort students by age")
    print("7. Find students by name")
    print("8. Exit")

    option = int(input("Enter option: "))

    if option == 1:
        create_table()
    elif option == 2:
        add_student()
    elif option == 3:
        update_student()
    elif option == 4:
        delete_student()
    elif option == 5:
        get_students()
    elif option == 6:
        sort_students_by_age()
    elif option == 7:
        find_students_by_name()
    elif option == 8:
        break
    else:
        print("Invalid option. Please try again.")

conn.close()
