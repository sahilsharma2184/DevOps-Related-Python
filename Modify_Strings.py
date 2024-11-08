#Upper Case
a="Sahil Sharma"
print(a.upper()) #o/p: SAHIL SHARMA


#Lower Case
print(a.lower()) #o/p: sahil sharma


#Remove Whitespaces: remove space before and after the actual text using strip()
b=" Sahil "
print(b.strip()) #o/p: 'Sahil'


#Replace String: replace() function replaces a string with another string
c="SRM AP"
print(c.replace("AP", "Andhra Pradesh")) #o/p: SRM Andhra Pradesh


#Split String: split() returns a list where the text b/w specified separator becomes the list items
d="Sahil$Sharma"
print(d.split('$')) #o/p: ['Sahil', 'Sharma']