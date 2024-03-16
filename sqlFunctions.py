#!/usr/bin/python
# Muhammad Talha Ather 101230176 COMP3005 A3 P1

import psycopg2

# Connecting to database
connect = psycopg2.connect(database = "test", user = "postgres", password = "popo12u9", host = "127.0.0.1", port = "5432")
current = connect.cursor()


def createTable():
      # Create and populate table
      current.execute("CREATE TABLE IF NOT EXISTS STUDENTS\
            (STUDENT_ID SERIAL PRIMARY KEY NOT NULL,\
            FIRST_NAME TEXT NOT NULL,\
            LAST_NAME TEXT NOT NULL,\
            EMAIL TEXT UNIQUE NOT NULL,\
            ENROLLMENT_DATE DATE)")

      current.execute("INSERT INTO STUDENTS (first_name, last_name, email, enrollment_date) VALUES \
            ('John', 'Doe', 'john.doe@example.com', '2023-09-01'), \
            ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'), \
            ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02')")

def dropTable():
      # Delete table, useful for testing
      current.execute("DROP TABLE STUDENTS")

def getAllStudents():
      # Grabbing all students into current
      current.execute("SELECT * from STUDENTS")
      rows = current.fetchall()

      # Looping through all students and getting the needed attributes
      for row in rows:
            print("STUDENT ID = ", row[0])
            print("FIRST NAME = ", row[1])
            print("LAST NAME = ", row[2])
            print("EMAIL = ", row[3])
            print("ENROLLMENT DATE = ", row[4], "\n")

# Add student into database, formatting all parameters into strings when adding into query
def addStudent(first_name, last_name, email, enrollment_date):
      query = "INSERT INTO STUDENTS (first_name, last_name, email, enrollment_date) VALUES (" + \
            "'" + first_name + "', '" + last_name + "', '" + email + "', '" + enrollment_date + "')"
      current.execute(query)

# Update student with id = student_id and set their email to new_email
def updateStudentEmail(student_id, new_email):
      query = "UPDATE STUDENTS set EMAIL = " + new_email + " where STUDENT_ID = " + student_id
      current.execute(query)

# Delete student with given student_id
def deleteStudent(student_id):
      query = "DELETE from STUDENTS where STUDENT_ID = " + student_id
      current.execute(query)

# Main code
def main():
      #dropTable()
      #createTable()
      #getAllStudents()
      #addStudent("Barack", "Obama", "barackobama@gmail.com", "2023-03-06")
      #addStudent("Donald", "Trump", "donaldtrump@gmail.com", "2023-04-01")
      #getAllStudents()
      #updateStudentEmail("2", "'student@newemail.com'")
      #getAllStudents()
      #updateStudentEmail("3", "'student@newemail.com'")
      deleteStudent('1')
      getAllStudents()

      # Closing connections
      connect.commit()
      connect.close()

# Run program
main()
