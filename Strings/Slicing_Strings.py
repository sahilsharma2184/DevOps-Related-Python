#Slicing: return a range of characters by using the slice syntax
#Specify the start index and the end index, separated by a colon, to return a part of the string
#Get the characters from starting index position (included) to ending index position (not included)
#Indexing starts from 0
a="Sahil Sharma"
print(a[1:5]) #ahil
print(a[:5]) #Sahil
print(a[6:]) #Sharma
print(a[-6:-2])#Shar, in negative indexing starting is done from end of string by -1