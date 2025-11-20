
a=10
b=20
print(f'Result is : {a%b}')

a=10
b=2
b+=a
print(f'Result is : {b}')

x=5
x*=2
print(f'Result is : {x}')

print(10>20 or 5<10)

x=10
print(f"x is 10 {x is 10}")

c="abc"
l="abcdef"
print(c in l)

# MEMBERSHIP OPERATORS IN and NOT IN - return bool value
names = ["ram", "sita"]
print("ram" in names)     # True
print("krishna" not in names)


# IDENTITY OPERATORS - IS and ISNOT - return bool value
x = [1, 2]
y = x
print(x is y)     # True
