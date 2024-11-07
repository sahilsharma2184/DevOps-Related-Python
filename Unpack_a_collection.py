#a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking
collection=["Sahil","Sharma",10512]
x,y,z=collection
print(x+y+z) #You can also use the + operator to output multiple variables but can't be used with number and string data type, like here as '+' is a mathematical operator, best practice is to use with ','