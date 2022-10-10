# Boolean expressions
10 < 100;
100 != 100;
50 >= 50;

age = 20;
age < 18;
age < 21;
age < 32;

"a" < "b";
"b" < "a";
"John" < "Terry";

"john" < "Terry";
# because the the "j" in john is lower case as opposed to the previous experession

5 < 10.2;
5 < "Monty";
5 < "5";

# logical operatiors within expressions
age = 30;
age >= 18 and age <=65;
age < 18 or age >65;
not age > 18;

age = 30;
(age >= 18 and age <= 65) and (not age == 30);

5 < age <= 30;
age > 20 < 40;

names = ["Terry", "John", "Michael", "Eric", "Terry", "Graham"];
"Michael" in names;
"Terry" not in names;

message = "Hello there, my name is John";
"there, m" in message;

# If statements
age = input("enter age: ");
if age >= 18 and age <= 30:
    print("you are still young!");

if age >= 18 and age <= 30:
    print("you are still young!");
elif age <= 30:
    print("old");
elif age >= 18:
    print("young");

name = input("Enter your name: ");
if name is True:
    print("Your name is", name);
else:
    print("Name not entered");

# The Ternary Operator
print("you are an adult" if age >= 18 else "you are not an adult yet!");

# Using while and for loops
names = ["Chris", "Dio", "Ken", "Jimbo"];
for n in names:
    print(n);

for m in range(2, 10, 2):
    print(m, "to the power of", m, "=", m ** m);

numbers = [10, 20, 30, 90, 200, 30, 22, 11];
total = 0

for n in numbers:
    total += n;
    print(total)
    if n > 100:
        break
else:
    print("hey")

# Exercises
num = int(input("enter a number between 1 and 10: "));
if num in range(1,10):
    print("It is in the range");

num1 = int(input("enter a number: "));
num2 = int(input("enter a number: "));
print(("the value", num1, "is larger than the value", num2) if num1>num2 else ("the value", num2, "is larger than", num1));

if num1 or num2 == 0:
    print("error");
else:
    print(num1 / num2);

n = 0;
while n < 100:
    n += 1;
    print("Chris");

# Portfolio tasks
name = input("What is your name: ");
if name != "":
    print("hello " + name);
else:
    print("Hello stranger");

badPas = ['password', 'letmein', 'sesame', 'hello', 'justinbieber'];

Pas1 = input("enter password: ");
Pas2 = input("confirm password: ");

while Pas1 != Pas2 or (8 > len(Pas1) > 12) or Pas1 in badPas:
    print("error. Try again");
    Pas1 = input("enter password: ");
    Pas2 = input("confirm password: ");
else:
    Pas1 == Pas2;
    print("password set");


num = int(input("enter number: "));
while -12 > num > 12:
    num = int(input("enter number: "));

if num < 0:
    num = str(num).replace("-", "");
    x = -1;
    y = 12;
    z = 0;
else:
    x = 1;
    y = 1;
    z = 13;

for n in range(y, z, x):
    n *= int(num);
    print(n);




