import random

# For Choosing Password Difficulty
def complexity():
    difficulty = int(input("1.Easy(only small alphabets)\n2.Medium(small alphabets with capital "
                           "alphabets)\n3.Hard(small and capital alphabets with special characters)\nEnter The "
                           "Complexity(1-3):"))
    return difficulty

# For Easy Difficulty
def easy(size):
    password = ""
    small = "abcdefghijklmnopqrstuvwxyz"
    for i in range(size):
        password = password + random.choice(small)
    return password

# For medium Difficulty
def medium(size):
    password = ""
    small = "abcdefghijklmnopqrstuvwxyz"
    big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in range(size):
        password = password + random.choice(small + big)
    return password

# For hard Difficulty
def hard(size):
    password = ""
    small = "abcdefghijklmnopqrstuvwxyz"
    big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special = "!@#$%^&*()<>?"
    for i in range(size):
        password = password + random.choice(small + big + special)
    return password

n=1
while n==1:
    # For Length
    length = int(input("Enter The length of password:"))
    comp = 4

    #for right choice
    while comp >= 4:
        if comp != 4:
            print("Enter Valid Choice...")
        comp = complexity()
    if comp == 1:
        code = easy(length)
    elif comp == 2:
        code = medium(length)
    elif comp == 3:
        code = hard(length)
    print("Password generated---->", code)
    n=int(input("DO you want to continue Yes(1) or No(2):"))
    if n!=1 and n!=2:
        n = int(input("DO you want to continue Yes(1) or No(2):"))
