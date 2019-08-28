
string1 = 'lohit'
string2 = "agarwalla"
string3 = "India's Kohinoor"
string4 = 'colour of sky is "blue"'
print( string1 + ". " + string2 + ". " + string3 + ". " + string4 )

new = '''this is a tripple quoted sentence, here we can use use both single and double quote inside it 'fds "fds "fds ' '''
print(new)

new_string = new[0:4]
new_string2 = new[:4] #same as above.
new_string3 = new[:] #copies the whole string
print(new_string3)

print(string1.upper())
print(string3.lower())
print(len(string2))
print(string2.find('ll'))
print(string4.replace('blue','sky blue'))
print(string4.title()) #converts the first letter of string to capital and all other letters to small letters.
print('hit' in string1) # in operator is used to check if a string is in the given string. it returns a boolean value