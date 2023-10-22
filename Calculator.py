# For subtraction
def sub_1(a, b):
    return a - b

# For addition
def add(a, b):
    return a + b

# For subtraction
def sub_2(a, b):
    return b - a

# For multiplication
def mul(a, b):
    return a * b

# For division
def div_1(a, b):
    return a / b

# For division
def div_2(a, b):
    return b / a


n = 1
res = 0
# Loop for Continue
while n != 2:
    # User input
    number_1 = int(input("Enter The Number 1:\n"))
    number_2 = int(input("Enter The Number 2:\n"))
    # Menu
    print("Choose The Option You want to perform on the numbers:\n1.Addtion(+)\n2.Subtraction("
          "number_1-number_2)\n3.Subtraction(number_2-number_1)\n4.Multiplication(*)\n5.Division("
          "number_1/number_2)\n6.Division(number_2/number_1)")

    # Choice For operation
    choice = int(input("Enter The Choose from 1-6:\n"))
    if choice == 1:
        res = add(number_1, number_2)
        print("Addition--->", res)
    elif choice == 2:
        res = sub_1(number_1, number_2)
        print("B subtracted from A--->", res)
    elif choice == 3:
        res = sub_2(number_1, number_2)
        print("A subtracted from B--->", res)
    elif choice == 4:
        res = mul(number_1, number_2)
        print("Multiplication--->", res)
    elif choice == 5:
        res = div_1(number_1, number_2)
        print("B divide from A--->", res)
    elif choice == 6:
        res = div_2(number_1, number_2)
        print("A divide from B--->", res)
    else:
        print("Please Enter Right Choice (1-6)")
    n = int(input("Do you want to continue 1.Yes 2.No:\n"))
print("Thank You!!")