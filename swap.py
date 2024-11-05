
# This is the very first way of swapping two numbers in python using the addition and subtraction operators
x,y =10,20
x= x + y
y= x - y
x= x - y
print(x,y)

# This is the second method using the third variable
a,b = 30,60
temp = a
a = b
b = temp
print(a,b)

