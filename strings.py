print("working")
print("My name is 'vidhya' ")
print('My name is "vidhya" ')


multi = """jdgfud dfkgidlg fgkdshgf kg
kdgfjkdg dfkgdfi
kfdjgdkf kdfgd"""
print(multi,"multi")

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a.splitlines(),"splitlines")
print(a)

name = "hello, world"
print(name[7])  # w - space included
for nameData in name:
    print(nameData,"nameData")

print(len(name),"length")  # space included

txt = "The best things in life are free!"
print("free" not in txt)


#slice  - extract a specific part of a string
# start position is included
# end position is not included
print(name[1:5],"slice")
print(name[1:],"slice without end")
print(name[:6],"slice without start")

# uppercase

print(name.upper(),"upper case")

#lowercase
print(name.lower(),"lower case")

# strip

demoVar = "  code clash  "
print(demoVar.strip(),"strip")

# replace
print(demoVar.replace("code", "coding"))

# split - it returns in list items
print(name.split(","))
studentsName = "Gowtham and sashreeik"
print(studentsName.split("and"))

str1 = "ocean"
str2 = "academy"
numberData = 35
str3 = str1 + " " + str2
print(str3)

# f-string
str4 = f"{str3} {numberData}"
print(str4,"str4")

#capitalize()
print(str3.capitalize())

#Split () 

# casefold() - lower case
print(str3.casefold())

txt = "I love apples, apple are my favorite fruit"
print(txt.count("apple",15,25))

# endswith
print(txt.endswith("g"))

# startswith
print(txt.startswith("I"))

# find - it returns the index of the first occurence.

txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x)

# title() - it converts each word 1st letter into caps

print(str3.title(),"title")

# swapcase()

names = "Demo NamES"
print(names.swapcase(),"swapcase")

# splitlines - it returns your data into list
