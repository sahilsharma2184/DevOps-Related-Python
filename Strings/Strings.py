"""
Strings in python are surrounded by either single quotation marks, or double quotation marks.
-> 'hello' is the same as "hello"
"""


print("Sahil") #This and below string, both will be treated same irrespective of the quotations, o/p: Sahil
print('Sahil') #o/p: Sahil


#Quotes Inside Quotes
print("Sahil 'Sharma'") #o/p: Sahil 'Sharma'
print('Sahil "Sharma"') #o/p: Sahil "Sharma"
#Note: quotes can be used inside a string as long as they don't match the quotes surrounding the string
#print("Sahil "Sharma"") and print('Sahil 'Sharma'') both are invalid


#Assigning string to a variable
a="Sahil"
b='Sharma'
print(a+b) #o/p: SahilSharma
print(a,b) #o/p: Sahil Sharma


#Multi-line Stings can be assigned using three quotes """<string>""" or '''<string>'''
c="""Sahil
Sharma
SRMAP"""
print(c) #o/p:  Sahil
                #Sharma  
                #SRMAP


#Strings are Arrays
"""
Python are arrays of bytes representing unicode characters.
Python does not have a character data type, a single character is simply a string with a length of 1.
Square brackets can be used to access elements of the string.
The counting starts from 0...till (length of the string - 1)
"""
d="Sahil Sharma" #0='S' , 1='a' , 2='h'...likewise
print(d[2]) #o/p: h
 

#Looping through a String
for i in d: #d="Sahil Sharma"
    print(i)
#o/p below
"""
S
a
h
i
l

S
h
a
r
m
a"""


#String Length, using len() function the length of the string can be calculated
print(len(d)) #d="Sahil Sharma", o/p: 12, len() starts counting from 1


#Check String: To check if a certain phrase or character is present in a string, we can use the keyword 'in' , is a bool data type
print("S" in d) #True
print("Reddy" in d) #False


#Check if NOT: To check if a certain phrase or character is NOT present in a string, we can use the keyword 'not in', is a bool data type
print("Reddy" not in d) #True
print("S" not in d)#False

