x = 10
if x > 15:
    print("Greater")
else:
    print("Smaller")


# Discount Calculator

#Bill=float(input("Please Enter the total bill: "))
Bill=300
if Bill>500:
    print(f"Bill is graterthan 500 so 20% Discount: {Bill-(Bill*0.2)}")

# Age Category Checker
#age=int(input("Please Enter the person Age: "))
age=13
if age >=0 and age <= 12:
    print("Child")
elif age>=13 and age <= 19:
    print("Teen")
elif age>=20 and age <= 59:
    print("Adult")
else:
    print("Senior citizen")


# Login System

correct_username = "admin"
correct_password = "1234"

# user= input("please enter the username: ")
# password=input("please enter the password: ")

user = "admin"
password = "1234"


print(user,password)

if user == correct_username and password == correct_password:
    print("Login Successful")
else:
    print("invalid credentials check once...")


# Number is Even or Odd

x=20
if x%2==0:
    print("Number is even")
else:
    print("Number is odd")

#Student Grade System
grade=13
if grade >=90:
    print("Grade A")
elif grade>=75:
    print("Grade B")
elif grade>=60:
    print("Grade C")
else:
    print("Fail")

#Traffic Signal System

signal="Gre"

if signal=='red':
    print("Stop")
elif signal=='yellow':
    print("Ready")
else:
    print("Go") 

#ATM Cash Withdrawal

balance = 5000
withdraw = 5050

if balance< withdraw:
    print("Insufficient Balance")
elif withdraw%100==0:
    print("Cash Withdrawn")
else:
    print("Amount should be multiple of 100")