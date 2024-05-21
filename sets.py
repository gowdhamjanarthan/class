# set is used to store multiple items in a single variable
# it unchangable, unordered, unindexed
# it returns random order
# it doesn't allow duplicate values
# False and True is 0 and 1 is considered the same value

my_set = { "item1","item2","item2",False,1,0,True}
print(my_set)
print(type(my_set))
print(len(my_set))

setWithCons = set((12,4,6,23))
print(type(setWithCons))

for num in setWithCons:
    print(num)

print(121 in setWithCons)
print(121 not in setWithCons)

# add()

setWithCons.add(400)
print(setWithCons,"after adding the item")

# to add one set into another set - update()

setWithCons.update(my_set)
print(setWithCons,"after update the set")
# clear()
demo_set = {"aaa","bbb"}
demo_set.clear()
print(demo_set,"After clear the set")

# copy()
copySet = setWithCons.copy()
print(copySet,"set copied")

# difference()  - it returns new set, 

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = {"cherry","microsoft"}

diff_Result = set1.difference(set2,set3)
print(diff_Result,"difference")

# difference_update() - removes items from sets, and returns the first set items

##set1.difference_update(set2)
##print(set1,"difference_update_set")


# discard()
set3.discard("cherry")
print(set3,"after discard")

# intersection() - returns the common element in both sets
intersection_set = set1.intersection(set2)
print(intersection_set,"intersection_set")

# intersection_update() - it removes the elements which is not present in the both sets

set1.intersection_update(set2)
print(set1,"intersection_Update_set")


# isdisjoint() - it returns true when the element is not present in the another set
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y)

print(z)

# issubset() - it returns true, when the element of one set is present in another set

n1 = {23,4,6}
n2 = {5,23,94,4,2}
Result = n1.issubset(n2)
print(Result,"issubset result")

# pop() - it removes elements in random order

n1.pop()
print(n1,"pop()")
