for i in range(1,6):
    print("*" * i)

for i in range(5,0,-1):
    print("*" * i)

for i in range(1,11):
    print(i)

for i in range(10,0,-1):
    print(i)


for n in range(1,11):
    print(n)

count=1
total=0
while count<=10:
    total=total+count
    count=count+1
print(total)

for i in range(1,11):
    if i==5:
        continue
    print(i)

for i in range(1,21):
    if i%2==0:
        print(i)
 
for i in range(1,11):
    if i==5:
        break
    print(i)

num=int(input("Number:"))
for i in range(1,11):
    print(f"{num}*{i}={num*i}")
  

num=int(input("Number:"))
if num>0:
    print("Positive")
elif num<0:
    print("Negative")
else:
    print("Zero")

a = int(input("Number 1: "))
b = int(input("Number 2: "))
c = int(input("Number 3: "))

if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)


day=int(input("Day Number:"))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wedensday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case _:
        print("Invalid day")
    
a=int(input("Number 1:"))
b=int(input("Number 2:"))
op=input("Operator (+ _ * /):")

match op:
    case "+":
        print("Result:",a+b)
    case "-":
        print(a-b)
    case "*":
        print(a*b)
    case "/":
        print(a/b)
    case _:
        print("invalid operator")
    
total=0
for i in range(1,51):
    if i %2==0:
        total=total+i
print(total)
    
count=1
total=0
while count<=10:
    total=total+count
    count=count+1
print(total)


password=""
while password !="Python123":
    password=input("password:")
print("welcome")

for i in range(1,21):
    if i==11:
        break
    print(i)

for i in range(1,11):
    if i==5:
        continue
    print(i)

for i in range(1,51):
    if i %3==0:
        print(i)

for i in range(1,6,1):
    print("*" * i )

for i in range(5,0,-1):
    print("*" * i)    stringine number kond * aa string repeat aavum..


secret = 7
guess = 0

while guess != secret:
    guess = int(input("Guess: "))

print("“Omg, you found it!😱😮🫡")

fruits= ["Apple","Mango","Orange"]
print(fruits[0])

numbers={10,10,22,20,20,15,78}
print(numbers)
    