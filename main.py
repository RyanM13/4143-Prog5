# Ryan Mathews
# CMPS 4143 Cont-Prog
# Tina Johnson
# 12/1/2024
# This program takes a file of students with grades and gives you menu to do things like add students, add grades, view grades, etc.
# It also can name your new text file of students with the same format and name+1 as the original file. Press 6 to exit (Sentinel value)

import os

# Switch statment for python, not the same as c++ but works
def switch(argument,grades,name):
    match argument:
        case 1:
           AddStudent(grades) 
        case 2:
            AddGrades(grades)
        case 3:
            ViewGrades(grades)
        case 4:
            ViewAllGrades(grades)
        case 5:
            SaveFile(grades, name)
            

# Printed menu for user to pick option, calls switch statment to call different function 
def menu(grades,name):
    argument = 0
    while argument != 6:
        print("1. Add a student name with grades")
        print("2. Add one or more grades to a student already in the list")
        print("3. View the grades for a given student along with the grade average")
        print("4. View all students with grades")
        print("5. Save updates in file with same name and in same form as original file")
        print("6. exit")

        argument = int(input("Enter the number for your option: "))
        switch(argument, grades,name)

# Add a student and add some grades to the file
def AddStudent(grades):
    name = input("Enter the name of the student: ")
    grades[name] = None
    grade = [] 
    value = 0

# Sentinel value to stop while loop
    while value != -1:
        value = int(input("(Enter -1 to stop)  Enter the students grades: "))
        # Checking range and making sure not to add -1 to the file
        if value != -1 and value >=0 and value <= 100:
            grade.append(value)
        else:
            print("Sentinel value entered. Or number not in range.\n")


    # Add values to the new key
    grades[name] = grade
        
    print(name, grades[name])
    
    

# Add grades to a certain key/student. 
def AddGrades(grades):
    student = input("Student: ")

    # Making sure the value is in the dictionary 
    while student not in grades:
        student = input("Student not in database. Enter Student: ")

    new_grade = [] 
    value = 0
    # Sentinel value
    while(value != -1):
        value = int(input("(-1 to stop) Grades: ")) 
        # Check range 
        if value != -1 and value >=0 and value <= 100:
            new_grade.append(value)
        else:
            print("Sentinel value entered. Or number not in range.\n")
            

    # Add new values to key
    grades[student].extend(new_grade)

    # Print student name as well (Things to do)
    print(student, grades[student])

    
# View certain students grades  
def ViewGrades(grades):
    student = input("Students name: ")
    # Checking to make sure value is in the dictionary  
    while student not in grades:
        student = input("Student not in database. Enter Student: ")

    # Getting the average using built in functions 
    average = sum(grades[student])/ len(grades[student])

    print(student + "'s grades: ", grades[student] )
    print("Average: ", average)

# View all students grades in the dictionary 
def ViewAllGrades(grades):
    # Going though all keys and values in dictionary and printing them
    for key, value in grades.items():
        print(key, " Grades: ", value )

    
# Save file with the same name and format as the original file
def SaveFile(grades, name):
    # Counter to avoid overriding the file
    counter = 1
    # Renaming the new file with the counter
    filename = f"{name.split('.')[0]}{counter}.txt" 
    # Checking to make sure file doesn't already exist
    while os.path.exists(filename):
        counter += 1
        filename = f"{name.split('.')[0]}{counter}.txt"

    # Open new file and write the dictionary to it
    with open(filename, "w") as file:
        # Looping through the keys and values
        for key, values in grades.items():
            grades_string = ""
            for grade in values:
                grades_string += str(grade) + '\t' 
            # Storing grades as strings 
            grades_string = grades_string.strip()  
            # Writing to the file 
            file.write(f"{key}\t{grades_string}\n") 

# Main function 
def main():
    file_name = 'grades.txt'

    # Opening the file (Also closing the file)
    with open(file_name, 'r') as file:
        lines = file.readlines()

    # Dictionary
    grades = {}


    # Looping through the txt file and inserting the lines in a dictionary
    for line in lines:
        section = line.strip().split('\t')
        key = section[0]
        val = [int(x) for x in section[1:]]
        grades[key] = val

        
    # Calling the menu
    menu(grades,file_name)

# Running main
if __name__ == "__main__":
    main()