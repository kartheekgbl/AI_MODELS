# def greet(name="John"):
#     print("Hello, " + name + "!")

# greet()

# # Write a function to add two numbers and return the result.

# def add(k,l):
#     return k+l

# print(add(5,10))

# # Write a function to check if a number is even or odd.

# def iseven(number):
#     if number%2==0:
#         print(number,"Is even")
#     else:
#         print(number,"Is odd")

# iseven(int(input("Enter a number: ")))


# # Write a function that prints the multiplication table of a number (up to 10).

# def multplicationtable(number):
#     for i in range(1,11):
#         print(number, "*", i, "=", number*i)
# multplicationtable(int(input("Enter a number: ")))

# Write a function to calculate the factorial of a number using a loop.

def factorial(number):
    fact=1
    for i in range(1,number+1):
        fact*=i
    return fact
print(factorial(int(input("Enter a number: "))))

# Create a function that takes a name and age and prints:

def greet_user(name, age):
    print("Hi", name, "you are", age, "years old!")
greet_user(name=input("Enter your name:"), age=input('Enter your age: '))

# "Hi John, you are 25 years old!"

