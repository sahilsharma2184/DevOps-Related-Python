#If you need to specify the data type of the variable, it can be done through casting
x=str(5) #x is '5'
y=int(3) #y is 
z=float(6) #z is 6.0
print(x,y,z) #o/p: 5 3 6.0
#############################

#get the type of variable using type() function
a="Sahil" #is same as 'Sahil' i.e. double quotes are same as single quotes, both are strings
b=9.8
print(type(a))
print(type(b))
#############################

p=int(1) #1
q=int(9.7) #9
r=int("3") #3
print(p,q,r) # 1 9 3

#############################
s=float(1) #1.0
t=float(8.6) #8.6
u=float("3") #3.0
v=float("4.6") #4.6
print(s,t,u,v) #1.0 8.6 3.0 4.6

#############################
w=str("srmap") #'srmap'
h=str("9.6") #'9.6'
i=str("7") #'7'
print(w,h,i) #srmap 9.6 7