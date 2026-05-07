'''#Q.NO:1
for i in range(1, 11):
    print(i)

i = 1
while i <= 10:
    print(i)
    i += 1'''


'''#Q.NO:2
    i = 1
while i<= 10:
    if i%2==0:
        print(i)
    i += 1'''


'''#Q.NO:3
n = int(input("Enter N:"))
i = 1
total = 0
while i<=n:
    total += 1
    i += 1
print("Sum=",total)'''


'''#Q.NO:4
num = int(input("Enter number:"))
i = 1
while i<= 10:
    print(num,"X",i,"=",num*i)
    i += 1'''
    
'''#Q.NO:5
n= int(input("Enter number:"))
fact = 1
i = 1
while i <= n:
    fact*=i
    i+=1
print("Factorial =", fact)'''

'''#Q.NO:6
num = int(input("Enter number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reverse =", rev)'''


'''#Q.NO:7
num = int(input("Enter number: "))
count = 0

while num > 0:
    num = num // 10
    count += 1

print("Digits =", count)'''


'''#Q.NO:8
num = int(input("Enter number: "))
i = 2
flag = 0

while i < num:
    if num % i == 0:
        flag = 1
        break
    i += 1

if flag == 0 and num > 1:
    print("Prime")
else:
    print("Not Prime")'''


'''#Q.NO:9
n = int(input("Enter terms: "))
a, b = 0, 1
i = 1

while i <= n:
    print(a)
    c = a + b
    a = b
    b = c
    i += 1'''

'''#Q.NO:10
i = 1
while i <= 4:
    print("*" * i)
    i += 1
i = 1
while i <= 10:
    print("*" * i)
    i += 1'''

'''#Q.NO:11
import random

num = random.randint(1, 100)
while True:
    guess = int(input("Guess number: "))
    
    if guess == num:
        print("Correct!")
        break
    elif guess < num:
        print("Too low")
    else:
        print("Too high")'''

'''#Q.NO:12
correct_user = "admin"
correct_pass = "1234"
attempts = 3

while attempts > 0:
    user = input("Username: ")
    pwd = input("Password: ")
    
    if user == correct_user and pwd == correct_pass:
        print("Login Success")
        break
    else:
        attempts -= 1
        print("Attempts left:", attempts)'''

'''#Q.NO:13
nums = [10, 45, 2, 99, 23]
largest = nums[0]

for n in nums:
    if n > largest:
        largest = n

print("Largest =", largest)'''


'''#Q.NO:14
text = "python programming"
count = 0

for ch in text:
    if ch in "aeiou":
        count += 1

print("Vowels =", count)'''


'''#Q.NO:15
balance = 1000

while True:
    print("1.Check 2.Deposit 3.Withdraw 4.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Balance:", balance)

    elif choice == 2:
        amt = int(input("Amount: "))
        balance += amt

    elif choice == 3:
        amt = int(input("Amount: "))
        if amt <= balance:
            balance -= amt
        else:
            print("Insufficient balance")

    elif choice == 4:
        break'''


'''#Q.NO:16
num = int(input("Enter number: "))
temp = num
sum = 0

while num > 0:
    digit = num % 10
    sum += digit ** 3
    num = num // 10

if temp == sum:
    print("Armstrong")
else:
    print("Not Armstrong")'''


'''#Q.NO:17
num = int(input("Enter number: "))
temp = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")'''

#Q.NO:18
for i in range(1, 5):
    for j in range(1, i+1):
        print(j, end="")
    print()
for i in range(1, 10):
    for j in range(1, i+1):
        print(j, end="")
    print()    
