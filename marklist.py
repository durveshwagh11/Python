Marklist = []
NOS = int(input("Enter the number of students:\n"))
for i in range(NOS):
    Marks = int(input("Enter the Marks of the students:\n"))
    Marklist.append(Marks)
print("Marks of the students are : \n", Marklist)


def Avg(n):
    sum = 0
    for i in range(len(Marklist)):
        if Marklist[i] != 'a':
            sum = sum + int(Marklist[0])

            avg = sum / n
    print("\nAverage score of the class is:")


def high():

    highest = Marklist [0]
    for i in range(len(Marklist)):
        if Marklist[i]!='a':
            if [i] > highest:
                highest = Marklist[i]

    print("\nhighest marks are:",highest)

def lowest():

    lowest  = Marklist[0]
    for i in range(len(Marklist)):
        if Marklist[i]!= 'a':
            if Marklist[i] <  lowest:
                lowest = Marklist[i]

    print("\nlowest marks are:", lowest)

def absent():

    absent = 0
    for i in range(len(Marklist)):
        if Marklist[i] == 'a':
            absent+=1

def highestfrequency():
    count = 0
    mark = Marklist[0]
    for i in Marklist:
        if i !="a":
            freq = Marklist.count(i)
            if freq > count:
                count = freq
                marks = i
    print("Marks with high freq:",Marks)

while True:
    print("\nEnter your choice")
    print("\n1.Average score")
    print("\n2.highest marks")
    print("\n3.lowest marks")
    print("\n4.total absent students")
    print("\n5.Display marks with highest frequency")
    print("\n6.Exit")

    ch = int(input("\nEnter choice"))

    if ch == 1:
        Avg(n)

    elif ch == 2:
        high()

    elif ch == 3:
        lowest()

    elif ch == 4:
        absent()

    elif ch == 5:
        highestfrequency()

    elif ch == 6:
        exit()
