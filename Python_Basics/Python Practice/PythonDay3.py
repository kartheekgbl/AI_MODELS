#Day 3: Operators & Conditionals

# Check if a number is even or odd.

k=input("Enter a number:")
if int(k)%2==0:
    print("Even")
    print(k,"Even")
else:
    print(k,"Odd")
3

# Find the largest of 3 numbers.

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))

if a>b and a>c:
    print(a, "is the largest number")
elif b>a and b>c:
    print(b, "is the largest number")
else: 
    print(c, "is the largest number")

# Check if a year is a leap year.
year=int(input("Enter a year: "))
if (year%4==0 and year%100!=0) or (year%400==0):
    print(year, "is a leap year")