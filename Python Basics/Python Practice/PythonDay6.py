# Day 6 Topics: Lists & Strings
# 1. Create a list of 5 favorite fruits. Print each using a loop.

fruits = ["apple", "banana", "cherry", "date", "elderberry"]


print([fruits[i] for i in range(len(fruits))])

for i in range(len(fruits)):
    print(fruits[i])
# 🔹 2. Add a new fruit to the list and remove one. Print the updated list.

fruits.append("Goava")
fruits.remove("banana")
print(fruits)

# 🔹 3. Take a string from the user and:
# Print the first and last characters

input=input("Enter a string: ")
print(input[0]) # Print the first character
print(input[-1]) # Print the last character


# Print its length
print(len(input)) # Print the length of the string
# 🔹 4. Count how many vowels are in a string.

vowels = "aeiouAEIOU"
print(([char for char in input if char in vowels])) # Count the number of vowels in the string


# 🔹 5. Sort a list of numbers entered by the user.

numlist=int(input("Enter the number of elements in the list: "))
nums=[]
for i in range(numlist):
    nums.append(int(input("Enter a number: ")))
nums.sort()
print(nums) # Print the sorted list of numbers

# python
# Copy
# Edit
# # Sample hint for #5:
# nums = input("Enter numbers separated by space: ").split()
# nums = [int(n) for n in nums]
# nums.sort()
# print(nums)