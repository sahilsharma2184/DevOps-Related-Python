#Variables that are created outside of a function are known as global variables. Global variables can be used by everyone, both inside of functions and outside.
x="sahil" #global variable
def fun():
    x="sharma" #local variable
    print("User is "+x)
fun() #o/p: User is sharma
#If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
print(x) #o/p: sahil

#################################################################

#To create a global variable inside a function, you can use the global keyword
def funtush():
    global y
    y="SRM"
funtush()
print("Value of y is",y) #o/p: Value of y is SRM

#################################################################

#Also, use the global keyword if you want to change a global variable inside a function.
z="University"
def vsc():
    global z
    z="College"
vsc()
print("Value of z is",z) #o/p: College