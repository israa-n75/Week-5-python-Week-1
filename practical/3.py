a=int(input("a:"))
b=int(input("b:"))
if a > b :
    print(a,"a is greater")
elif b > a:
    print(b,"b is greater")
else:
    print("equal")
    

def add(a,b):
    print(a-b)
add(5,10)

def star():
    for i in range(1,6,1):
        print("*" *i)
star()

numbers = [1, 2, 3, 4, 5]
def odd_number():
    num =  [ ]
    for number in numbers:
        if number % 2 == 0:
            num.append(number)
    print(num)
odd_number()

numbers=[0,1,-5,10,-9,6,-2,2]
def seperate_numbers():
    positive=[]
    negative=[]
    for number in numbers:
        if number>0:
            positive.append(number)
        elif number<0:
            negative.append(number)
    print("Positive numbers:",positive)
    print("Negative numbers",negative)
seperate_numbers()




class Car:                        
    def __init__(self, brand, colour):
        self.brand = brand        
        self.colour = colour      

    def accelerate(self):        
        print(self.brand, "is moving")

car1 = Car("Toyota", "red")         
car1.accelerate()                   
print(car1.colour) 




class car:
    def __init__ (self,brand,colour):
        self.brand = brand
        self.colour = colour
    def accelerate(self):
        print(self.brand,"is moving")
    car1 = car("Toyota","red")
    car1.accelerate()
    print(car1.color)





class car:
    def __init__  (self,brand,colour):
        self.brand = brand
        self.colour = colour
    def accelerate(self):
        print(self.brand,"Is moving")
    car1=car("Toyota","Red")
    car1.accelerate()
    print(car1.colour)

class car:
    def __init__ (self,brand,colour):
        self.brand=brand
        self.colour=colour
    def accelerate(self):
        print(self.brand,"Is moving")
car1=car("Toyato","red")
car1.accelerate()
print(car1.colour)





class car:
    def __init__ (self,brand):
        self.brand=brand
    def accelerate(self):
        print(self.brand,"is moving")
car1=car("Porsche")
car2=car("BMW")
car1.accelerate()
car2.accelerate()




squares=[]
for i in range(1,6):
    squares.append(i*i)
print(squares)

square=[i*i for i in range(1,6)]
print(squares)



def greet(a,b):
    return(a+b)
print(greet(5,10))


def add(a,b):
    return(a*b)
print(add(10,5))


def greet(name):
    print("Hello",name)
greet("isra")
greet("jaza")


def is_even(n):
    return n%2==0
print(is_even(4))



def add(a, b):
    return a + b

result = add(10, 20)

numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def odd_number():
    num=[]
    for n in numbers:
        if n % 2 != 0:
            num.append(n)
    print(num)
odd_number()


numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def even_number():
    num=[]
    for number in numbers:
        if number % 2 == 0:
            num.apppend(number)
    print(num)


def square(n):
    return n * n
print(square(5))

square=lambda n:n*n
print(square(5))


squares=[i*i for i in range(1,6)]
print(squares)

numbers=[1,2,2,3,4,5,5,5,6,6]
unique_numbers=set(numbers)
print(unique_numbers)

square=lambda x:x*x
print(square(5))

square=[]
def square(x):
    return x*x
print(square(5))

add=lambda a,b:a+b
print(add(5,10))

def add(a,b):
    return a+b
print(5,10)


count=1
total=0
while count<=10:
    total=total+count
    count=count+1
print(total)

count=1
total=1
while count<=10:
    total=total*count
    count=count+1
print(total)


name="isra"
print(name,type(name))
