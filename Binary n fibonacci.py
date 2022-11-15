def binarysearch(roll, x):
    low = 0
    high = len(roll) - 1

    while high >= low:
        mid = (low + high) // 2

        if roll[mid] == x:
            return mid
            break
        elif roll[mid] > x:
            high = mid - 1
        elif roll[mid] < x:
            low = mid + 1
    return -1


def fibonacciSearch(roll, x):
    n = len(roll)
    offset = -1
    fn_2 = 0
    fn_1 = 1
    fn = fn_1 + fn_2
    while fn < n:
        temp = fn
        fn_2 = fn_1
        fn_1 = temp
        fn = fn_2 + fn_1
    while fn > 1:
        index = min((offset + fn_2), n - 1)
        if roll[index] == x:
            return index
        elif roll[index] > x:
            fn = fn_2
            fn_1 = fn_1 - fn_2
            fn_2 = fn_2 - fn_1  # Moving two down
        elif roll[index] < x:
            fn = fn_1
            fn_1 = fn_2
            fn_2 = fn - fn_1
            offset = index
    return -1


roll_no = [2, 3, 4, 5, 6, 7, 8, 9]
n = len(roll_no)
key = int(input("enter the roll no to check whether he or she attended the training program"))
while True:
    print("1.Binary Search\n2.Fibonacci Search\n3.Exit")
    ch = int(input("Enter the choice"))
    if ch == 1:
        result = binarysearch(roll_no, key)
        if result == -1:
            print("Roll no : ", key, " not attended training program")
        else:
            print("Roll no : ", key, " attended training program")
    elif ch == 2:
        result = fibonacciSearch(roll_no, key)
        if result == -1:
            print("Roll no : ", key, " not attended training program")
        else:
            print("Roll no : ", key, " attended training program")
    elif ch == 3:
        break
    else:
        print("Enter valid choice")
