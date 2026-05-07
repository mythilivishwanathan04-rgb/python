'''#while loop python
#Q.NO:1
i = 1
while i<50:
    print(i)         
    i+=1
    print("loop end")'''

'''#Q.NO:2
i = 20
while i>15:        
    print(i)
    i-=1
    
i = 15
while i>0:        
    print(i)
    i-=1'''
    





'''#Break statement    
#Q.NO:1
for i in range(1, 11):
    if i == 5:
        break
    print(i)'''


'''#Q.NO:2
i = 1

while i <= 10:
    if i == 7:
        break
    
    print(i)
    i += 1'''

'''#Q.NO:3
password = "python123"

while True:
    user = input("Enter password: ")

    if user == password:
        print("Access Granted")
        break

    print("Wrong Password")'''


'''#Continue statement
#Q.NO:1
for i in range(1, 11):

    if i == 5:
        continue

    print(i)'''

'''#Q.NO:2
i = 0

while i < 10:
    i += 1

    if i == 6:
        continue

    print(i)'''

#Q.NO:3
for letter in "MYTHILI":

    if letter == "H":
        continue

    print(letter)
