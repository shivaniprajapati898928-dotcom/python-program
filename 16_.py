# Write a Python program using mysql.connector to connect to a MySQL database, create a table students, insert multiple records, and display them. And, extend the program to allow user-driven operations: 
# • Add new records 
# • Update marks 
# • Delete a record 
# • Search by roll number 

import mysql.connector

# Connect to MySQL
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",        
        password="root",     
        database="school"    
    )
    cursor = conn.cursor()
    print("Connected to MySQL Database")

    # Create table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            roll_no INT PRIMARY KEY,
            name VARCHAR(50),
            marks FLOAT
        )
    """)
    print("Table 'students' is ready.")

    # Insert multiple records
    students = [
        (1, "Sumit", 85.5),
        (2, "Amit", 90.0),
        (3, "Shivani", 78.0)
    ]
    cursor.executemany("INSERT IGNORE INTO students (roll_no, name, marks) VALUES (%s, %s, %s)", students)
    conn.commit()
    print("Sample records inserted.")

    # Function to display all records
    def display_all():
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        print("\n Student Records:")
        print("----------------------------")
        for row in rows:
            print(f"Roll No: {row[0]}, Name: {row[1]}, Marks: {row[2]}")
        print("----------------------------")

    # Function to add a new record
    def add_record():
        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))
        cursor.execute("INSERT INTO students VALUES (%s, %s, %s)", (roll, name, marks))
        conn.commit()
        print("Record added successfully!")

    # Function to update marks
    def update_marks():
        roll = int(input("Enter Roll No to update: "))
        new_marks = float(input("Enter new Marks: "))
        cursor.execute("UPDATE students SET marks = %s WHERE roll_no = %s", (new_marks, roll))
        conn.commit()
        print("Marks updated successfully!")

    # Function to delete a record
    def delete_record():
        roll = int(input("Enter Roll No to delete: "))
        cursor.execute("DELETE FROM students WHERE roll_no = %s", (roll,))
        conn.commit()
        print("Record deleted successfully!")

    # Function to search a student by roll number
    def search_record():
        roll = int(input("Enter Roll No to search: "))
        cursor.execute("SELECT * FROM students WHERE roll_no = %s", (roll,))
        row = cursor.fetchone()
        if row:
            print(f"Found: Roll No: {row[0]}, Name: {row[1]}, Marks: {row[2]}")
        else:
            print("No record found.")

    # Menu-driven operations
    while True:
        print("\n===== STUDENT MANAGEMENT MENU =====")
        print("1. Display all records")
        print("2. Add new record")
        print("3. Update marks")
        print("4. Delete a record")
        print("5. Search by roll number")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_all()
        elif choice == '2':
            add_record()
        elif choice == '3':
            update_marks()
        elif choice == '4':
            delete_record()
        elif choice == '5':
            search_record()
        elif choice == '6':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

except mysql.connector.Error as err:
    print("Database Error:", err)
except Exception as e:
    print("Unexpected Error:", e)
finally:
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection closed.")
