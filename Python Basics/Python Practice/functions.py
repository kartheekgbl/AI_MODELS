# def of a function
# fuctions are small blocks of code that perform a specific task

def greet(greeting):
    print(greeting)


greet("Congratualations! You have completed the Python Basics course.")


#Lambda functions are small anonymous functions defined using the `lambda` keyword. They can take any number of arguments but can only have one expression.

f=lambda x: x * 2
print(f(5))  # Output: 10

# We have 3 functions in lambda function
# filter, map, and reduce
# 1. Filter: Filters elements from a list based on a condition
# def is_even(num):
#     return num % 2 == 0
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda a:a%2==0, numbers))
print(even_numbers)  # Output: [2, 4, 6]


# 2. Map: Applies a function to each element in a list
# def square(num):
#     return num ** 2
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25, 36]

# 3. Reduce: Applies a function cumulatively to the items of a sequence, reducing it to a single value
from functools import reduce
# def add(x, y):    
#     return x + y
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)  # Output: 21 


# Example for Decorators
def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function
@decorator_function
def display():
    print("Display function executed")
display()  # Output: Wrapper executed before display
# Display function executed