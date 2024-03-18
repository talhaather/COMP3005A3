#!/usr/bin/python
# Muhammad Talha Ather 101230176 COMP3005 A3 P1

import psycopg2

# Create and populate table
def createTable():
      # Create Table
      cursor.execute("CREATE TABLE IF NOT EXISTS STUDENTS\
            (STUDENT_ID SERIAL PRIMARY KEY NOT NULL,\
            FIRST_NAME TEXT NOT NULL,\
            LAST_NAME TEXT NOT NULL,\
            EMAIL TEXT UNIQUE NOT NULL,\
            ENROLLMENT_DATE DATE)")

      # Populate Table
      cursor.execute("INSERT INTO STUDENTS (first_name, last_name, email, enrollment_date) VALUES\
            ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),\
            ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),\
            ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02')")

# Delete STUDENTS table, used in testing
def dropTable():
      cursor.execute("DROP TABLE STUDENTS")

# Print all students to console
def getAllStudents():
      # Grabbing all students into cursor
      cursor.execute("SELECT * from STUDENTS")
      rows = cursor.fetchall()

      # Looping through all students and printing to console
      print("student_id, first_name, last_name, email, date_enrolled")
      for tuple in rows:
            print(str(tuple[0])+",", str(tuple[1])+",", str(tuple[2])+",", str(tuple[3])+",", str(tuple[4]), "\n")


# Add student into database, formatting all parameters into strings when adding into query
def addStudent(first_name, last_name, email, enrollment_date):
      query = "INSERT INTO STUDENTS (first_name, last_name, email, enrollment_date) VALUES (" + \
            "'" + first_name + "', '" + last_name + "', '" + email + "', '" + enrollment_date + "')"
      cursor.execute(query)

# Update student with id = student_id and set their email to new_email
def updateStudentEmail(student_id, new_email):
      query = "UPDATE STUDENTS set EMAIL = " + new_email + " where STUDENT_ID = " + student_id
      cursor.execute(query)

# Delete student with given student_id
def deleteStudent(student_id):
      query = "DELETE from STUDENTS where STUDENT_ID = " + student_id
      cursor.execute(query)

# Main code
def main():
      # Prompt user input
      print("\nWhat would you like to do? (Enter 1, 2, 3, 4, 5)\n   1. Create and Populate Table\n   2. getAllStudents\n   3. addStudent\n   4. updateStudentEmail\n   5. deleteStudent()\n")
      option = input()
      print()
      
      # Check user input
      if (int(option) == 1):
            # Error Check
            try:
                  # Create and Initialize Table
                  createTable()
                  print("Table Created\n")
            except:
                  # Tell user that table is already made
                  print("Error: Table already initialized\n")


      elif (int(option) == 2):
            # Error Check
            try:
                  # Print all Students
                  getAllStudents()
            except:
                  # Report to user
                  print("Error: Could not return students\n")


      elif (int(option) == 3):
            # Error Check
            try:
                  # Get user input for function parameters
                  fname = input("Enter First Name: ")
                  lname = input("Enter Last Name: ")
                  email = input("Enter Email: ")
                  date = input("Enter Date: ")
                  addStudent(fname, lname, email, date)
                  print("Student Added\n")
            except:
                  # Report to user
                  print("Error: Could not add student\n")


      elif (int(option) == 4):
            # Error Check
            try:
                  # Get user input for function parameters
                  id = input("Enter ID: ")
                  newEmail = input("Enter New Email: ")
                  updateStudentEmail(id, newEmail)
                  print("Email Updated\n")
            except:
                  # Report to user
                  print("Error: Could not update student\n")


      elif (int(option) == 5):
            # Error Check
            try:
                  # Get user input for function parameters
                  delId = input("Enter ID to delete: ")
                  deleteStudent(delId)
                  print("Student Deleted\n")
            except:
                  # Report to user
                  print("Error: Could not delete student\n")

      # Closing connections
      connect.commit()
      connect.close()


# Error checking
try:
      # Connecting to database
      connect = psycopg2.connect(database = "test", user = "postgres", password = "popo12u9", host = "127.0.0.1", port = "5432")
      cursor = connect.cursor()

      # Run program
      main()


except:
      # Report error to user
      print("Error: Could not connect\n")


