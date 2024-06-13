
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
