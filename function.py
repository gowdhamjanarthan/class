def displayName(num): # p
    print(num)
displayName("gowtham")  # a

# arguments - you can pass values in function call
# parameters - you can receive values in function declaration

def addition(a,b):
    c = a + b
    print("The value of c is :", c )
addition(10,23)

def checkValue(x):
    if x > 0:
        print("x is positive")
    elif x == 0:
        print("x is Zero")
    else:
        print("x is Negative")
    
checkValue(0)
##def printValues():
##    data = [12,34,56,67]
##    for i in data

my_list = [1,2,3,4,5]

def printAllNumbers(num):
    sum=0
    for n in num:
        sum+=n
    return sum

print(printAllNumbers(my_list))


##def num(a,b):
##    for i in a+b:
##        i=a+b
##        print(i)
##num(2,2)

# local scope
def localScopeVar():
    x = 10
    print(x,"local scope - inside fn")
localScopeVar()
# print(x,"local scope - ourside fn")



# global scope

y = 350
def globalScopeVar():
    print(y,"value of y", "inside the fun")
globalScopeVar()
print(y,"value of y", "outside the fun")


num = 400  # global scope
def myNum():
    n1= 900  # local scope
    print(num,"this is the value of num")
    print(n1,"this is the value of n1","inside the fun")
myNum()
print(num,"this is the value of num","outside the fn")
print(n1,"this is the value of n1")

## return is a keyword - it returns the value of function call

# **kwargs

def displayTotal(stuId001,stuId003,stuId002):
    print(stuId003)

displayTotal(stuId001 = 300,stuId002 = 470,stuId003 = 450)

# *args
def displayDetails(*userDetails):
    print("The name of user is :", userDetails[0])
    
displayDetails("demo user 1",903873626)

def displayDetails(name,mobile):
    print("The name of user is :", name)
    print("The user mobile number is :", mobile)

displayDetails("demo user 1",903873626)
displayDetails(name = "demo user 2",mobile = 693783636)



##class A:
##    def __init__(self, num):
##        self.num = num
##    def print(self):
##        print(self.num)
##    def add_2(self):
##        self.num += 2
##
##class B(A):
##    def __init__(self, num):
##        self.num = num
##    def sub_2(self):
##        self.num -= 2
##        
##
##a = B(10)
##a.sub_2()
##a.add_2()
##a.print()
