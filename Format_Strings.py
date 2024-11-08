#F-Strings: preferred way of formatting strings.
#To specify a string as an f-string, simply put an f in front of the string literal, 
#and add curly brackets {} as placeholders for variables and other operations.

age=20
a=f"Sahil's age is {age} years"
print(a) #o/p: Sahil's age is 20 years


tomato=1000
t=f"Price of tomato is {tomato:.2f} rupees" # '.2f' which means fixed point number with 2 decimals
print(t) #o/p: Price of tomato is 1000.00 rupees


average=1000
ave=f"The average is {average/5}" #can be any mathematical operation
print(ave) #o/p: The average is 200.0