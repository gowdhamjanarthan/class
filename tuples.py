myTuple = ("Bat","Ball",1j,False) # holds all data types in a single variable
print(myTuple)
print(type(myTuple))

#Tuple constructor:
construct = tuple(("item 1","item2","item3"))
print(construct)

Tup_le = ("item 1","item2","item3","item3") # can hold duplicate values

#Accessing tuples:
print(myTuple[2]) # Index
print(myTuple[-1]) # Negative Index
print(myTuple[2: ]) # Range

#Adding elements to a Tuple:
myTuple = ("Bat","Ball",1j,False)
converTuple = list(myTuple)
converTuple[0] = "Stumps" # Replacing
converTuple.append("Pitch") # Adds to the end of the tuple
myTuple = tuple(converTuple)
print(myTuple)

#Adding one tuple to another:
x = ("Umpire","Players")
myTuple += x
print(myTuple)

#looping a Tuple

#For loop:
myTuple = ("Bat","Ball",1j,False)
n = 0
for x in myTuple:
    if n < len(myTuple):
        print(myTuple[n])
        n += 1

#While loop:
myTuple = ("Bat","Ball",1j,False)
n = 0
while n < len(myTuple):
        print(myTuple[n])
        n += 1


# count  - The count() method returns
#           the number of times a specified
#           value appears in the tuple.

my_Tuples = (23,54,2,56,2,45)
print(my_Tuples.count(54))
print(my_Tuples.index(56))
