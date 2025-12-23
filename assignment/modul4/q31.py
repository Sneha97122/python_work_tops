text = "  hello python programming  "

print( text)

#count the lenth
print("length():",len(text))

# convert to uppercase
print("Upper():", text.upper())

# convert to lowercase
print("Lower():", text.lower())

# capitalize first letter
print("Capitalize():", text.capitalize())

#for title
print("title():",text.title())

# remove spaces
print("Strip():", text.strip())

# replace substring
print("Replace():", text.replace("python", "java"))

# find position of a word
print("Find():", text.find("python"))

#startwith particuler char
print("startwith():",text.startswith("python"))

#endwith particuler cher
print("endwith():",text.endswith("lo"))

# split string
print("Split():", text.split())

# count characters
print("Count():", text.count("o"))

#string is alpha or not
print("isalpha():",text.isalpha())

#string is only number
print("isdigit():",text.isdigit())

#string is combination of alphabets and numbers
print("isalnum():",text.isalnum())

# Pads the string with zeros
print("zfill():",text.zfill(3))


