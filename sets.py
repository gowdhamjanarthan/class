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

