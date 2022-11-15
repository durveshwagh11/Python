def frequency():
    str = input("Enter a string\n")

    s = str.split()

    print(s)

    count = 0
    char = input("Enter a character to find frequency of it\n")

    for i in range(len(str)):
        if str[i] == char:
            count += 1
    print(count)


def largest():
    str1 = input("Enter the string\n")
    l = list(str1.split())
    print(l)
    largestword = " "
    for i in l:
        if len(i) > len(largestword):
            largestword = i

    print("Largest word is ", largestword)


def reverse():
    str2 = input("Enter a string to reverse\n")
    l = list(str2.split())
    print(l)
    revstring = " "
    for i in range(len(str2), 0, -1):
        revstring = revstring + str2[i - 1]

    print(revstring)


def palindrome():
    str2 = input("Enter a string\n")
    revstring = ""  # str2[::-1]

    for i in range(len(str2), 0, -1):
        revstring = revstring + str2[i - 1]
    print(revstring)

    if str2 == revstring:

        print("palindrome")
    else:
        print("not a palindrome")

def word_frequency():
    str = input("Enter the string\n")
    str2 = str.split(" ")
    str3 = []
    for s in str2:
        if s not in str3:
            str3.append(s)
    for a in range(len(str3)):
        print("Frequency of words", str3[a],"is",str2.count(str3[a]))

def index():
    str1 = input("Enter the string\n")
    str2 =list(str1.split(' '))
    print(str2)
    str3 = input("Enter the part of the string you want index of \n")
    #ind=str2.index(str3)
    #print(ind)
    for i in range(len(str2)):
        if str3 == str2[i]:
            print(i)







while (True):
    print("1.Frequency of a character in string")
    print("2.Largest word in string")
    print("3.Reverse of string")
    print("4.Palindrome")
    print("5.Word frequency in string")
    print("6.Index of any word from string")
    ch = int(input("enter your choice\n"))

    if ch == 1:
        frequency()
    elif ch == 2:
        largest()
    elif ch == 3:
        reverse()
    elif ch == 4:
        palindrome()
    elif ch == 5:
        word_frequency()
    elif ch == 6:
        index()
    elif ch > 6 or ch < 1:
        print("Invalid")
        break
