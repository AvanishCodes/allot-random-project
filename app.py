from random import randint as rI

# Welcome Message
print("This is an application to allot random projects based on the input of the teacher")

numberOfStudents = int(input("\nWhat is the number of students in your class : "))

numberOfProjects = int(input("\nWhat is the number of projects you want to allot : "))

rollNumberPrefix = input("\nEnter the prefix of the roll number of the students : ")

fileName = input("\nEnter the name of the file that you want the details to save into(without spaces), e.g. allottedProject123 : ")

# Take the projects names input from the teacher
print("\nNow input the names of the projects : ")
print("\nWarning: Enter a single project in a single line only")
print()

projects  = []
for i in range(numberOfProjects):
    projects.append(input(f"Enter the project number {i+1} : "))

print("You have entered the following projects : ")
for i in range(numberOfProjects):
    print(f"{i+1}. {projects[i]}")

print("Do You want any edit(s) in any project(s): press Y/y for yes")
check = input()

if check == "y" or check == "y":
    while(True):
        index = input("Enter the index at which you want the change : ")
        if index < numberOfProjects:
            print("Enter the new name of the project : ")
            newName = input()
            project[index] = newName
        else:
            print(f"There are only {numberOfProjects}, please select from them only!")
        print("You have entered the following projects : ")
        for i in range(numberOfProjects):
            print(f"{i+1}. {projects[i]}")
        check = input("\nDo You want any more edit(s) in any project(s): press Y/y for yes")
        if check != "Y" and check != "y":
            break


print("Alloting the projects to the students: ")
fileName = f"{fileName}.txt"
fI = open(fileName, "w")

for i in range(numberOfStudents):
    allottedProject = projects[rI(0, numberOfProjects-1)]
    formattedRollNumber = rollNumberPrefix + f"{i+1}"
    print(f"{formattedRollNumber}. {allottedProject}")
    data = f"{formattedRollNumber}. {allottedProject}\n"
    fI.write(data)
