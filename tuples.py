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


# task

#Task 1:
my_Tuple = ("apple","banana","cherry")
print(my_Tuple)

#Task 2:
my_Tuple = ("apple","banana","cherry")
print(my_Tuple[1])

#Task 3:
my_Tuple = ("apple","banana","cherry")
convert = list(my_Tuple)
convert[1] = "orange"
my_Tuple = tuple(convert)
print(my_Tuple)

#Task 4:
x = (1,2,3)
y = ("a","b","c")
x += y
print(x)

#Task 5:
my_Tuple = ("apple","banana","cherry")
if "apple" in my_Tuple:
    print("yes")
else:
    print("no")

#Task 6:
my_Tuple = ("apple","banana","cherry")
print(my_Tuple.index("cherry"))

#Task 7:
my_Tuple = ("apple","banana","cherry")
print(my_Tuple.count("banana"))

#Task 8:
singleELE = ("hello",)
print(type(singleELE))

#Task 9:
my_Num = (1,2,3,4)
convert = list(my_Num)
convert.reverse()
my_Num = tuple(convert)
print(my_Num)

#Task 10:
myTuple = ("a","b","c")
print(myTuple[-1])

#Task 11:
Tuple = ("a","b","c","d")
print(Tuple[1:3])

#Task 12:
myNumb = ("x","y")
multiply = myNumb*3
print(multiply)

#Task 13:
my_Tuple = ("apple","banana","cherry")
print(len(my_Tuple))

#Task 14:
Num1 = (1,2,3)
Num2 = (4,5,6)
if Num1 == Num2:
    print("Yes")
else:
    print("No")

#Task 15:
my_data = (10,20,30,40,50,23)
Max = max(my_data)
print(Max)

#Task 16:
myData = (-10,-20,-30,-40,-50)
Min = min(myData)
print(Min)

#Task 17:
Bool = (True,True,False)
All = all(Bool)
print(All)

#Task 18:
Bool = (True,True,False)
Any = any(Bool)
print(Any)

#Task 19:
NumbTuple = (5,2,8,1,9)
conv = list(NumbTuple)
conv.sort()
NumbTuple = tuple(conv)
print(NumbTuple)

#Task 20:
Data1 = (1,2,3)
Data2 = (4,5,6)
Data3 = Data1 + Data2
print(Data3)


# task - gowdham


#tuples Question.txt
#1)create a tuple with three elements: "apple", "banana", "cherry".
fruit=("apple", "banana", "cherry")
print(fruit)

#2)access the second element of the tuple created in the previous question.
fruit=("apple", "banana", "cherry")
print(fruit[1])

#3)replace "banana" with "orange" in the tuple.
fruit=("apple", "banana", "cherry")
rearange=list(fruit)
rearange[1]="orange"
fruit=tuple(rearange)
print(fruit)

#4)concatenate two tuples:(1,2,3)and ("a","b","c").
z=(1,2,3)
x=("a","b","c")
z+=x
print(z)

#5)check id "apple" exists in the tuple.
fruit=("apple", "banana", "cherry")
if "apple"in fruit:
    print("yes")
else:
     print("no")

#6)find the index of "cherry" in the tuple.
fruit=("apple", "banana", "cherry")
print(fruit.index("cherry"))

#7)count the occurrence of "banana" om the tuple.
fruit=("apple", "banana", "cherry")
print(fruit.count("banana"))

#8)create a tuple with a single element"hello".
single=("hello",)
print(single)

#9)reverse the tuple:(1,2,3,4,5)
num=(1,2,3,4,5)
rearange=list(num)
rearange.reverse()
num=tuple(rearange)
print(num)

#10)access the last element of the tuple:('a','b','c','d')
a=('a','b','c','d')
print(a[-1])

#11)slice the tuple ('a','b','c','d') to get ('b','c').
a=('a','b','c','d')
slice=a[1:3]
print(slice)

#12)repeat the tuples ('x','y') three times.
tuples=('x','y')
repeat =tuples*3
print(repeat)

#13)find the length of the tuples("apple", "banana", "cherry")
a=("apple", "banana", "cherry")
print(len(a))

#14)cheack if two tuples(1,2,3)and(1,2,3)are equal.
a=(1,2,3)
b=(1,2,3)
if a==b :
    print("a=b answer is true")
else:
    print("a not equal to b anwer is fals")

#15)find the maximum elements from the tuple(10,20,30,40,50,23).
a=(10,20,30,40,50,23)
new=max(a)
print(new)

#16)find the minimum elemennts from the tuple(-10,-20,-30,-40,-50).
a=(-10,-20,-30,-40,-50)
new=min(a)
print(new)

#17)cheack if all elements of the tuples(true,true,false)are true.

a = (True, True, False)
allflase = all(a)
print(allflase)

#18)cheack if any elements of the tuples(true,true,false)is true.
a = (True, True, False)
anyfalse=any(a)
print(anyfalse)

#19)sort the tuples (5,2,8,1,9) in ascending order.
a=(5,2,8,1,9)
sorted=tuple(sorted(a))
print(sorted)

#20)merge two tuples(1,2,3)and (4,5,6)into a single tuple.
a=(1,2,3)
b=(4,5,6)
combaine=a+b
print(combaines)
