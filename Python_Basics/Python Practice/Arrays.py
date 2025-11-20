import array as arr

# Creating the array and appending values from user input and searching for a value in the array
array1=arr.array('i',[23,45,76,89])

print(array1)
print(array1[0])

print(array1.buffer_info())

n=int(input("Enter the length of the array:"))

for i in range(n):
    x=int(input("Enter the next value:"))
    array1.append(x)
print(array1)

searchnum=int(input("Enter the searching value to know the Index: "))

for i in range(len(array1)):
    if array1[i]==searchnum:
        print("index of the value is: ",i)
        break
else:   
    print("Value not found in the array")


# direct meathod to search the value in the array
print(array1.index(searchnum))