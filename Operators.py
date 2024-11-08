#Operators are used to perform operations on variables and values like '+' operator is used to add two values
""" 
Python divides the operators in the following groups:
    ->Arithmetic operators
    ->Assignment operators
    ->Comparison operators
    ->Logical operators
    ->Identity operators
    ->Membership operators
    ->Bitwise operators
"""


#Arithmetic Operators

#Addition: '+'
print(10+5) #o/p: 15

#Subtraction: '-'
print(10-5) #o/p: 5

#Multiplication: '*'
print(10*5) #o/p: 50

#Division: '/', finds the quotient
print(10/2) #o/p: 5.0

#Modulus: '%', finds the remainder
print(10%5) #o/p: 0

#Exponentiation: '**', means raised to the power
print(2**5) #same as 2*2*2*2*2 => o/p: 32

#Floor Division: '//', rounds off the quotient to the nearest whole number, takes floor value i.e. 8.5 means 8, similarly 9.5 means 9
#For negative results, "rounding down" means going further into the negatives. 
# For example:
#In -7 // 3, the result is closer to -3 than to -2. Python rounds towards the more negative integer, so we get -3.
print(7//3) #o/p: 2
print(-7//3) #o/p: -3