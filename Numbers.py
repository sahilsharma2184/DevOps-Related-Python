"""
There are three numeric types in Python:

-> int or integer is a whole number, positive or negative, without decimals, of unlimited length

-> float or "floating point number" is a number, positive or negative, containing one or more decimals. 
Float can also be scientific numbers with an "e" to indicate the power of 10.

-> Complex numbers are written with a "j" as the imaginary part

Variables of numeric types are created when you assign a value to them
"""
import random

x=5 #int
y=3.5 #float
z=1j #complex
print(type(x))
print(type(y))
print(type(z))
print()

a=1
b=9522319652841
c=-4515485196418541
print(type(a))#int 
print(type(b))#int
print(type(c))#int
print()

p=5.6
q=8.9
r=9.0
print(type(p))#float
print(type(q))#float
print(type(r))#float
print()

h=35e3
i=12E4
j=-87.5e100
print(type(h))#float
print(type(i))#float
print(type(j))#float
print()

l=3+5j
m=5j
n=-6j
print(type(l))#complex
print(type(m))#complex
print(type(n))#complex
print()

############################################################

print("Type Conversion, convert from one type to another with the int(), float(), and complex() methods")
u=5
v=5.5
w=5j

print("convert int to float")
uif=float(u)
print(uif)
print(type(uif))
print()

print("convert int to complex")
uic=complex(u)
print(uic)
print(type(uic))
print()

print("convert float to int")
vfi=int(v)
print(vfi)
print(type(vfi))
print()

print("convert float to complex")
vfc=complex(v)
print(vfc)
print(type(vfc))
print()

#Note: convert complex numbers can't be converted into another number type.

############################################################
