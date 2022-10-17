# Importing and using functions
from math import log2

result = math.sqrt(2401)
print(result)

result = math.log2(1024)
print(result)


# Defining functions
def displayTwice(msg):
    """Function that prints a given value for "msg" twice"""
    print(msg)
    print(msg)


displayTwice("hello")

help(displayTwice)


def findMax(a,b):
    """Finds the maximum of two values."""
    if ( a > b ):
        max = a
    else:
        max = b
    return max


print(findMax(2,20))

print(findMax(4,1))

print(findMax(19,100))


# Default Arguments
def calc(a, b):
    print(a*b)


calc(4)


# Keyword arguments
def someFunc(x, y, z):
    print("x is", x, "\ny is", y, "\nz is", z)


someFunc(z=6, y=1, x=8)

print("hello", "bye", sep="-")
print("Bye", "bye", sep="=")
print("hello again", "hello", sep="~")


# Arbitary length argument lists
def calcAve(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total/len(numbers)


print(calcAve(6,3,3))


#Lambda expression
hypot = lambda a,b : math.sqrt(a * a + b * b)

print(type(hypot(2,2)))

to_seconds = lambda hours = 0, minutes = 0: print((hours*3600)+(minutes*60))

to_seconds(2)

def do_something(prefix="Message", prompt, answer=False):
    print(prompt, prefix, answer)

do_something("hi")


# Portfolio
def inRange(a):
    if a in range(1,100):
        return True
    else:
        return False


print(inRange(99))


def charNum(msg = ""):
    upNum = 0
    loNum = 0
    for x in msg:
        if x.islower():
            loNum+=1
        elif x.isupper():
            upNum+=1
        num = ("upper case letters:", upNum, "\nLower case letters:", loNum)
    return num

print(charNum("HiYA"))

name = input("What is your name: ").lower()

if name != "":
    print("hello " + name.replace(name[0], name[0].upper()))
else:
    print("Hello stranger")

def cutStr(msg):
    a = len(msg)
    if a > 1:
        return msg[0:a-1]
    else:
        return msg

print(cutStr("HELLO HOW ARE YOU!"))

def cToF(a):
    return (a*9/5)+32

def fToC(a):
    return (a-32)*5/9

def cToF(a):
    degc=a.upper()
    if "C" in a:
        numc = a[0:len(a)-1]
        numf = (int(numc)*9/5)+32
        return str(numf)+"F"
    else:
        return "input number in format <temperature>C"

import statistics


def minMaxMean(*temps):
    print(min(temps))
    print(max(temps))
    print(statistics.mean(temps))
minMaxMean(12,19,243,2,44,2)