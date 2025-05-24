import numpy as np

arr=np.array([1,2,3,4,5],int)
print(arr)

print(arr[0])

# different ways of creating the arrays in numpy
# We have 6 ways to create the arrays in numpy
arr1=np.array([1,2,3,4,5],int) # Creates an array of integers
print
arr2=np.array([1.0,2.0,3.0,4.0,5.0],float)  # Creates an array of floats
print(arr2)
arr=np.linspace(1,10,5)  # Creates an array with 5 evenly spaced values between 1 and 10
print(arr)
arr3=np.logspace(1,10,2)  # Creates an array with values from 1 to 10 with a step of 2
print(arr3)
arr4=np.arange(1,10,2)  # Creates an array with values from 1 to 10 with a step of 2
print(arr4)
arr5=np.zeros((2,3))  # Creates a 2D array with 2 rows and 3 columns filled with zeros
print(arr5)
arr6=np.ones((2,3))  # Creates a 2D array with 2 rows and 3 columns filled with ones
print(arr6)
arr7=np.empty((2,3))  # Creates a 2D array with 2 rows and 3 columns filled with random values
print(arr7)



# Coying arrays
arr8=np.copy(arr1)  # Creates a copy of the array
print(arr8)
arr9=arr1.view()  # Creates a view of the array
print(arr9)
# Modifying the original array will not affect the view
arr1[0]=10
print(arr1)
print(arr9)  # The view will not change 