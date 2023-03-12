import mysql.connector

# establish a connection to the database
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student_crud"
)

# create a cursor object
cursor = cnx.cursor()

# CREATE Operation:
def create_student(name, email, birthday, phone, address):
    sql = "INSERT INTO students (name, email, birthday, phone, address) VALUES (%s, %s, %s, %s, %s)"
    values = (name, email, birthday, phone, address)
    cursor.execute(sql, values)
    cnx.commit()
    print("Student created successfully!")

# READ Operation:
def read_students():
    sql = "SELECT * FROM students"
    cursor.execute(sql)
    rows = cursor.fetchall()
    return rows

# UPDATE Operation:
def update_student(id, name, email, birthday, phone, address):
    sql = "UPDATE students SET name=%s, email=%s, birthday=%s, phone=%s, address=%s WHERE id=%s"
    values = (name, email, birthday, phone, address, id)
    cursor.execute(sql, values)
    cnx.commit()
    print("Student updated successfully!")

# DELETE Operation:
def delete_student(id):
    sql = "DELETE FROM students WHERE id=%s"
    value = (id,)
    cursor.execute(sql, value)
    cnx.commit()
    print("Student deleted successfully!")


# Sorting and Filtering:
def sort_students(field):
    sql = f"SELECT * FROM students ORDER BY {field}"
    cursor.execute(sql)
    rows = cursor.fetchall()
    return rows

def filter_students(field, value):
    sql = f"SELECT * FROM students WHERE {field} LIKE %s"
    val = ("%" + value + "%")
    cursor.execute(sql, (val,))
    rows = cursor.fetchall()
    return rows

# create_student("Alice", "alice@example.com", "2000-01-01", "123-456-7890", "123 Main St")
# create_student("Bob", "bob@example.com", "2000-02-02", "234-567-8901", "456 Oak Ave")
# create_student("Charlie", "charlie@example.com", "2000-03-03", "345-678-9012", "789 Maple Rd")

while True:
    print("\n=== Please select an operation: ===" )
    print("1. Create a student")
    print("2. Read all students")
    print("3. Update a student")
    print("4. Delete a student")
    print("5. Sort students by field")
    print("6. Filter students by field")
    print("0. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        name = input("Enter name: ")
        email = input("Enter email: ")
        birthday = input("Enter birthday: ")
        phone = input("Enter phone: ")
        address = input("Enter address: ")
        create_student(name, email, birthday, phone, address)
        
    elif choice == "2":
        rows = read_students()
        for row in rows:
            print(row)
    
    elif choice == "3":
        id = input("Enter student id: ")
        name = input("Enter new name: ")
        email = input("Enter new email: ")
        birthday = input("Enter new birthday: ")
        phone = input("Enter new phone: ")
        address = input("Enter new address: ")
        update_student(id, name, email, birthday, phone, address)
        
    elif choice == "4":
        id = input("Enter student id: ")
        delete_student(id)
    
    elif choice == "5":
        field = input("Enter field to sort by: ")
        rows = sort_students(field)
        for row in rows:
            print(row)
    
    elif choice == "6":
        field = input("Enter field to filter by: ")
        value = input("Enter value to filter: ")
        rows = filter_students(field, value)
        for row in rows:
            print(row)
    
    elif choice == "0":
        break

    else:
        print("Invalid option. Please try again.")
    
