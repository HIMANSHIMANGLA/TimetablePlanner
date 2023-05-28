import random 
import numpy as np

# Initialize variables
lst = []
d = 0
p = 0

# Get number of subjects from user
subnum = int(input("Enter number of subjects: "))

# Input subject names and their frequencies
for i in range(0, subnum):
    sub = input("Enter subject: ")
    f = int(input("Enter frequency: "))
    d = d + f
    for i in range(0, f):
        lst.append(sub)

# Check if total frequency exceeds 35
if d > 35:
    print("Invalid input")
else:
    # Add "Free" slots to fill up the total timetable
    for i in range(0, 35 - d):
        ele = "Free"
        lst.append(ele)

# Define timetable dimensions
R = 7
C = 5

# Get number of timetables from user
k = int(input("Enter number of timetables: "))

# Generate timetables
for p in range(k):
    lst1 = []
    matrix = []
    m = []
    time = ["9-10", "10-11", "11-12", "12-1", "2-3", "3-4", "4-5"]

    # Assign subjects randomly to timetable slots
    for i in range(R):
        a = []
        for j in range(C):
            item = lst[0]
            a.append(item)
            lst.remove(item)
            lst1.append(item)
        matrix.append(a)
        m = np.array(matrix)
        matrix1 = m.T
        for e in range(5):
            random.shuffle(matrix1[e])
        m1 = np.array(matrix1)
        matrix2 = m1.T

    # Add subjects back to the list for future timetables
    for m in range(35):
        lst.append(lst1[m])

    # Print timetable
    print()
    print("------------------TimeTable", p + 1, "------------------")
    
    # Print headings
    headings = ["TIME", "MON", "TUE", "WED", "THU", "FRI"]
    for heading in headings:
        print(heading.rjust(15), end="")
    print()

    # Print timetable slots
    for i in range(R):
        print(time[i].rjust(15), end="")
        for j in range(C):
            print(matrix2[i][j].rjust(15), end="")
        print()

    print()

