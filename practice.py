a="10"
b="20"
a=int(a)
b=int(b)
print(a+b)

a=input("Enter Your num:")
b=input("Enter Your sec num:")
a=int(a)
b=int(b)
print( "sum:",a+b)

a=int (input("Enter Your First Number:"))
b=int (input("Enter Your Second Number:"))
print("Sum:",a+b)
print("Difference:",a-b)
print("Product:",a*b)
print("Division:",a/b)

name=input("Enter Your Name:")
age=int(input("Enter Your Age :"))
print("Hello ",name + " , Next Year You Will Be",age+1)

length=int(input("Enter Length:"))
width=int(input("Enter Width:"))
print("Area=",length*width)

#Type conversion    
# int(): text or float to whole number
a = int("25")
b = int(7.9)

# float(): text or int to decimal number
c = float("3.5")
d = float(10)

# str(): number to text
e = str(20)
f = str(4.5)

# bool(): value to True / False
g = bool(1)
h = bool(0)
i = bool("hello")
j = bool("")

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))
print(f, type(f))
print(g, type(g))
print(h, type(h))
print(i, type(i))
print(j, type(j))



######################arithmetic###############################

a=17
b=5
print(a + b)   
print(a - b)    
print(a * b)    
print(a / b)    
print(a // b)  
print(a % b)    
print(a ** b)   


n=int(input("Number:"))
if n%2==0:
    print("Odd")
else:
    print("Even")

age=18
is_student=True
if age>=18 and is_student:
    print("Entry Allowed") 
else:
    print("Not Allowed")

age=18
is_student=True
if age>=20 or is_student:
    print("Entry Allowed") 
else:
     print("Not Allowed")


marks=int(input("Marks:"))
if marks>=80:
    print("Grade:A")
elif marks>=65:
    print("Grade:B")
elif marks>=50:
    print("Grade:C")
else :
    print("Grade:Fail")

age=20
has_id=True

if age>=18 and has_id:
    print("Entry Allowed")
else:
    ("Not allowed")


a=int(input("A:"))
b=int(input("B:"))
print("sum:",a+b)
print("difference:",a-b)
print("product:",a*b)

name=input("Name:")
age=int(input("Age:"))
print(f"Hello {name} ,You are {age} years old ")


num=int(input("Num:"))
if num % 2 == 0:
    print("Even")
else :
    print("Odd") 

marks=int(input("Num:"))
if marks>=90:
    print("Grade A")

elif marks>=70:
    print("Grade B")

elif marks>= 50:
    print("Grade C")

else:
    print("Fail")


day=2
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wedensday")
    case _:
        print("invalid dat")

for  i in range(1,6,1):
    print("*" *i)

for i in "Isra":
    print(i)

for fruits in ["apple","banana"]:
    print(fruits)

for num in range(10,0,-1):
    print(num)

total=0
for i in range(1,11):
    total=total+i
print(total)

for num in [10, 20, 25,  30, 35, 40]:
    if num% 2 == 0:
        print(num)


count=1
while count<=10:
    print(count)
    count=count+1

count=1
while count<=10:
    print(count)
    count=count+1


total=0
count=1
while count<=10:
    total=total+count
    count=count+1
print(total)


num=int(input("Num:"))
count=1
while count<=10:
    print(f"{num} * {count} = {count*num} ")
    count=count+1

for i in range(1,6):
    if i==3:
        pass
    print(i)


num=int(input("Num:"))
if num % 2 == 0:
    print("Even")
else:
    print("odd")

numbers=[2,4,6,8,10]
print(numbers[0:3])

nums=[10,20,30]
print(len(nums))

squares=[]
for i in range(1,6):
    squares.append(i*i)
print(squares)

doubled = []

for num in range(1,6):
    doubled.append(num * 2)

print(doubled)

doubled=[num*2 for num in range(1,6)]
print(doubled)
   

numbers=[1,2,3,4,5]
def odd_number():
    num=[]
    for number in numbers:
        if number% 2 ==0:
            num.append(number)
    print(num)
odd_number()

