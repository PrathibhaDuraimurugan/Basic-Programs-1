# (using third variable)
x = 1305
y = 1905

temp = x
print ("the value of temp variable is", temp)

x = y
print("the value of x is", x)

y = temp
print ("the value of y is", y)

#(without using third variable)
x = 1305
y = 1905
x,y = y,x
print("The value of x is,x")
print("The value of y is,y")