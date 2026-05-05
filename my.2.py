'''color=(input("enter the color"))
if color=="blue":
    print("will buy the dress")
elif color=="red":
    print("will buy the dress")
else:
    print("not buy")'''
'''cake=(input("enter the cake"))
if cake=="brownie":
    print("will buy the cake")
elif cake=="strawberry":
    print("will buy the cake")
else:
    print("not buy")'''
'''junkfood=(input("enter the junkfood"))
if junkfood=="pizza":
    print("no eat the junkfood")
elif junkfood=="burger":
    print("no eat the junkfood")
else:
    print("eat the food")'''


'''for i in range(5):
   print(i)
   
for i in range(5+1):
    pr1int(i)

for p in range(2,7):
    print(p)

for p in range(2,7,2):
    print(p)

for m in "mythili and poorinma are sister":
    print(m)
    
for m in "vishwanathan weds nandhini devi":
    print(m)
    
for m in "i love briyani":
    print(m)'''


'''age = int(input("Enter your age: "))
citizen = input("Are you a citizen (yes/no): ")

if age >= 18:
    if citizen == "yes":
        print("Eligible to vote")
    else:
        print("Not eligible (not a citizen)")
else:
    print("Not eligible (age below 18)")'''

'''marks = int(input("Enter marks: "))

if marks >= 35:
    if marks >= 75:
        print("Distinction")
    else:
        print("Pass")
else:
    print("Fail")'''


'''num = int(input("Enter a number: "))

if num > 0:
    if num % 2 == 0:
        print("Positive Even Number")
    else:
        print("Positive Odd Number")
else:
    print("Negative Number")'''


'''a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b:
    if a > c:
        print("A is largest")
    else:
        print("C is largest")
else:
    if b > c:
        print("B is largest")
    else:
        print("C is largest")'''

'''num = int(input("Enter a number: "))

if num >= 0:
    if num == 0:
        print("Zero")
    else:
        if num % 2 == 0:
            print("Positive Even")
        else:
            print("Positive Odd")
else:
    print("Negative Number")'''


'''passwords = ["1234", "admin", "mythili"]

user_pass = input("Enter password: ")

if user_pass in passwords:
    print("Access Granted")
else:
    print("Access Denied")'''


'''data = {
    "mythili": "1234",
    "poornima": "abcd",
    "madhu": "pass"
}

attempts = 3

while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in data and data[username] == password:
        print("Login Successful")
        break
    else:
        attempts -= 1
        print("Wrong details")
        print("Attempts left:", attempts)

if attempts == 0:
    print("Account Locked")
    data = {
    "mythili": "1234",
    "poornima": "abcd",
    "madhu": "pass"
}

attempts = 3

while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in data and data[username] == password:
        print("Login Successful")
        break
    else:
        attempts -= 1
        print("Wrong details")
        print("Attempts left:", attempts)

if attempts == 0:
    print("Account Locked")'''

    
'''fruits = ["apple", "banana", "mango"]

item = input("Enter fruit name: ")

if item in fruits:
    print("Available")
else:
    print("Not Available")'''


'''rows = 5

for i in range(rows, 0, -1):
    for j in range(rows - i):
        print(" ", end="")   # space
    for k in range(2*i - 1):
        print("*", end="")   # star
    print()'''

'''n = 14

for i in range(n, 0, -1):
    print("*" * i)'''

'''rows = 5

for i in range(rows, 0, -1):
    for j in range(rows - i):
        print(" ", end="")   # space
    for k in range(2*i - 1):
        print("*", end="")   # star
    print()'''

for i in range(5):
    for j in range(5):(i);
        #print("*",end="")
        #print()

        
