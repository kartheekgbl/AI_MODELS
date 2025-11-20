print("Printing fibonacci series based on user input")

def fibonacci(n):
    a,b=0,1
    print("Fibonacci series:")
    print(a, end=' ')

    for i in range(2,n):
        a=a+b
        print(a, end=' ')
        # Update a and b for the next iteration
        # t=a
        # a=b
        # b=t
    # Swpping a and b
        a,b=b,a
fibonacci(int(input("Enter the pf number of terms: ")))