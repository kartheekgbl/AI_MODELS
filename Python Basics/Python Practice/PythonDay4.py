# Day 4: Loops in Python

# Practice Tasks Recap (Plomes):
# Print numbers from 1 to 10 using while.
k=1
while k<=10:
    print(k)
    k+=1

# Print even numbers from 1 to 20 using for.
for i in range (1, 20):
    if i%2==0:
        print(i)

# Print pattern:
# 1
# 12
# 123

for i in range (1, 4):
    for j in range(1, i+1):
        print(j, end="")
    print("\n")
# Sum of all numbers 1–100.

sum=0
for i in range(1,100):
    sum+=i
print("Sum of all numbers from 1 to 100 is: ", sum)

# Break when number divisible by 3 & 7.
while True:
    k=int(input("Enter the number: "))
    if(k%3==0):
        print(k,"This is devisible by 3")
        break
    elif(k%7==0):
        print(k,"This is devisible by 7")
        break