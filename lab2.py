# Practical tasks, variables
total = 100;
print("the total is ", total);

total = total + 99;
print("the total is now ", total);

total += 99;
print("the total is now ", total);

total = total * 100;

total *= 100;

total = - 1;
print("the total is ", total);

total = total + 4;
print("The total is ", total);

total = total / 2;
print("the total is ", total);

total = 98.2;
count = 5;

average = 98.2 / 5;
print("the average is ", average);

# Practical tasks, data types

type(1000);
type(100.111);
type("hello");
type(True)
type(100 / 5);

"ABC" * 10 # it extends the string by taking the string "ABC" and duplicating it ten times.

# Practical tasks, built-in functions
nam = "Chris";
num ="00000 000000";
adr = "222 roady road";

print(len(nam), nam);
print(num);
print(adr);

age = input("Enter the age");
age = int(age);
print("In one year your age will be", age + 1);

num1 = int(input("input number 1"));
num2 = int(input("input number 2"));
print(num1 * num2);

# Practical tasks, single double and triple quotes
comment = "i would have "thought" you knew better!"; # the string ends before "thought", an starts again after "thought" leaving it out of the string rather than printing the quotes as desired

print('this text includes characters such as \'\\\' \'\"\' and \"\'\" ');

print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ \n Hello There! \n \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\');

print("""This tex spans three lines.
and includes both single ('),
and double quotes (")""");

# Practical tasks, indexing and slicing
surname = "Palin";
initial = surname[2];
initial = surname[9]; # an error shows becuase the index value is greater than the string the vaule is being accessed from.

print(surname[1]);

surname = "Palin";
middle = surname[1:5];
print(middle);

print(surname[0:]);

# Practical task, lists
primes = [2, 3, 5, 7 ,13, 17, 19, 23, 29, 31, 37, 41, 43 ,47];
print(primes[0:4]);

names = ["Terry", "John", "Michael", "Eric", "Terry", "Graham"];
names[0] = "Terry, G.";
names[0:0] = ["Tim", "Bill", "Graeme"];

names[8:8] = ["JoJo", "Jim"];
print(names);

# nums = [1,2,3] * 5 = [5,10,15] wrong actual answer is [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2,3]
nums = [1,2,3]*5;
print(nums);

# Exercise tasks
prices = [2.65, 7.65, 8.25, 9.56];
prices.append(1,34)

prices.extend([9.62, 1.22, 3.86])
print(prices);

for x in prices:
    print(x);

primes = [2, 3, 5, 7, 11, 13, 17]

primes - [19, 17, 13, 11, 7, 5, 3, 2]

primes = [2, 3, 5, 7, 11, 13, 17]

primes = [2, 3, 5, 11, 13, 17, 19]

temps = [32, 46, 95, 10, 50]

temps.insert(0, 10)

temps.index(95)

temps.count(10)

Values = [n for n in range(100,200)]

# Portfolio tasks
name = input("What is your name");
print("hello " + name);

tempc = (float(input("Temperatutre in degree celsius: ")));
tempf = (tempc*9/5)+32;

print(str(tempf) + " degrees Fahreneit");

studNum = int(input("how mant students?: "));
grpSize = int(input("how large do you want the groups?: "));
grpNum = studNum // grpSize;

print("groups = ", grpNum, "remaining = ", studNum - (grpNum * grpSize));

sweetNum = int(input("how many sweets?: "));
studNum = int(input("how many students?: "));

sweetStud = sweetNum//studNum;
print("sweets per student = ", sweetStud, "remaining = ", sweetNum - (sweetStud * studNum));
