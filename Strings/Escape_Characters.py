#Escape Characters: To insert characters that are illegal in a string, use an escape character.
#An escape character is a backslash \ followed by the character you want to insert.

#As print("Sahil "Sharma"") is illegal, so will use escape character

# Escape Character: \"
print("Sahil \"Sharma\"") #o/p: Sahil "Sharma"


#Single Quote: \'
print('It\'s Okay') #o/p: It's Okay


#Backslash: \\
print("This will insert one \\ backslash") #o/p: This will insert one \ backslash


#New Line: \n
print("Sahil\nSharma") #o/p: Sahil
                            #Sharma


#Tab: \t
print("Sahil\tSharma") #o/p: Sahil  Sharma


#Backspace: \b, it erases one character back to it
print("Sahil\bSharma") #o/p: SahiSharma


#Octal Value: \ooo OR \<int><int><int>, backslash followed by 3 integers result in octal value
print("\110\145\154\154\157") #Hello


#Hex Value: \xhh, backslash followed by an 'x' and a hex numeber represents a hex value
print("\x48\x65\x6c\x6c\x6f") #Hello