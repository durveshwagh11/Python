def matrix(r, c):
    out = []
    for i in range(r):
        row = []
        for j in range(c):
            k = int(input(f"Enter [{i}][{j}]:"))
            row.append(k)
        out.append(row)
    return out


def addition(A, B):
    result = [[0 for i in range(c)] for i in range(r)]
    for i in range(len(A)):
        for j in range(len(A[0])):
            result[i][j]=A[i][j]+B[i][j]
            for n in result:
                print(n)

def subtraction(A, B):
    result = [[0 for i in range(c)] for i in range(r)]
    for i in range(len(A)):
        for j in range(len(A[0])):
            result[i][j]=A[i][j]-B[i][j]
            for n in result:
                print(n)

def multiplication(A,B):
    result = [[0 for i in range(c)] for i in range(r)]
    for i in range(len(A)):
        for j in range(len(A[0])):
            for k in range(len(B)):
                result[i][j]=result[i][j]+A[i][j]*B[i][j]
    for n in result:
        print(n)

def transpose(A, B):
    result = [[0 for i in range(c)] for i in range(r)]
    for i in range(len(A)):
        for j in range(len(A[0])):
            result[j][i]=A[i][j]
            for n in result:
                print(n)

print("Welcome to matrix operation program")

while True:
    print("\n Main Menu")
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.Transpose")
    print("5.exit")

    choice = int(input("Enter the choice:"))

    if choice== 1:
        r = int(input("Enter the number of rows:"))
        c = int(input("Enter the number of columns:"))

        print("matrix A is:")
        A= matrix(r, c)

        print("matrix B is:")
        B = matrix(r, c)

        print("\nAddition of matrix A & b is:")
        addition(A, B)

    elif choice ==2:

        r = int(input("Enter the number of rows"))
        c = int(input("Enter the number of columns"))

        print("matrix A is:")
        A = matrix(r, c)

        print("matrix B is:")
        B = matrix(r, c)

        print("\nSubtraction of matrix A & b is:")
        subtraction(A, B)

    elif choice== 3:

        r = int(input("Enter the number of rows"))
        c = int(input("Enter the number of columns"))

        print("matrix A is:")
        A = matrix(r, c)

        print("matrix B is:")
        B = matrix(r, c)

        print("\nMultiplication of matrix A & b is:")
        multiplication(A, B)

    elif choice== 4:

        r = int(input("Enter the number of rows"))
        c = int(input("Enter the number of columns"))

        print("matrix A is:")
        A = matrix(r, c)

        print("\nTranspose of matrix A & is:")
        transpose(A)

    elif choice==5:
        break

    else:
      print("you have wrong value")



