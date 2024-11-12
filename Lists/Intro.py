#Lists are used to store multiple items in a single variable.
#Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
#Lists are created using square brackets []
#fruits=['apple','banana','pineapple']

fruits=['apple','banana','pineapple']
print(fruits) # o/p: ['apple', 'banana', 'pineapple']


#List items are ordered, changable, allows duplicate values.
#List items are indexed, 1st item is at 0th index and similarly further.
print(fruits[0]) #o/p: apple
print(fruits[0],fruits[2]) #o/p: apple pineapple


#List Length
print(len(fruits)) #o/p: 3


#List can contain items of any data and also different data type
number=[1,2,3,4,5,6,7,8,9,10] #o/p: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(number)

boolean=[True, False, True] 
print(boolean) #o/p: [True, False, True]

mixed=[True, 18, "Sahil"]
print(mixed) #o/p: [True, 18, 'Sahil']


#Lists are objects with the data type 'list'
print(type(mixed)) #o/p: <class 'list'>