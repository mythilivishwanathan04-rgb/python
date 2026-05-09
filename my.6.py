'''#Q.NO:1
#Welcome Function
def welcome_student(name):
    print("Welcome,", name + "!")

welcome_student("Mythili")'''


'''#Q.NO:2
#Square Function
def square(num):
    return num * num

print(square(5))'''


'''#Q.NO:3
#Area of circle
import math

def area_of_circle(radius):
    return math.pi * radius * radius
r = 7
print(area_of_circle(5))'''


'''#Q.NO:4
def withdraw(balance, amount):
    # Check if amount is multiple of 100
    if amount % 100 != 0:
        return "Withdrawal amount must be a multiple of 100"

    # Check if balance is sufficient
    if amount > balance:
        return "Insufficient balance"

    # Deduct amount
    balance -= amount
    return f"Withdrawal successful. Remaining balance: {balance}"

balance = 10000

print(withdraw(balance, 1200))  
print(withdraw(balance, 1250))  
print(withdraw(balance, 6000))'''

