# identical operator - check whether two variables refer
#                 to the same object or not - is , is not
# membership operator - in, not in  -- it returns boolean

# membership operator - in , not in
myString = "Hello"
print("e" in myString)  # True
print("h" in myString)  # False - because py is a case sensitive
print("w" not in myString,"not in") # True

numbersData = [45,2,56,32,435] #list
print(2 in numbersData)  # True
print(2 not in numbersData) # False


# identical operator - is , is not

a = 3
b = 3
c = a 

print(a is b,"is ")
print(id(a))
print(id(b))

print(a is not c,"sdnjhfjdk")


# it returns False because
# both lists “my_list1” and “my_list2” refer to
# different memory locations,
# even though they contain the same elements.

my_list1 = [1, 2, 3]
my_list2 = [1, 2, 3]
print(my_list1 is my_list2)
print(id(my_list1))
print(id(my_list2))

print(my_list1  is not my_list2)

