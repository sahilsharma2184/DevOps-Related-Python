#When you compare two values, the expression is evaluated and Python returns the Boolean answer either True or False
print(9>8) #o/p: True
print(9==8) #o/p: False
print(9<8) #o/p: False


#Printing a message based on whether the condition is True or False
a=10
b=20
if a>b:
    print("a is big")
else:
    print("b is big") #o/p: b is big


#Evaluate Values and Variables
#Note: Any string is True except empty strings
#Note: Any number is True except 0
#Note: Any list, tuple, dictionary are True except empty ones
print(bool(5)) #o/p: True
print(bool("Sahil")) #o/p: True
c=10
d="Sharma"
print(bool(c)) #o/p: True
print(bool(d)) #o/p: True
print(bool(["apple","banana","guava"])) #True


#False Values:  False values are empty values, such as (), [], {}, "", the number 0, and the value 'None'
print("Below are all False values")
print(bool(False)) #o/p: False
print(bool(None)) #o/p: False
print(bool("")) #o/p: False
print(bool(())) #o/p: False
print(bool({})) #o/p: False
print(bool([])) #o/p: False