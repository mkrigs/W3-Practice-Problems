# Problem 1
string = "Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are"
print(string)
# Problem 2
import sys
print(sys.version)
print(sys.version_info)
# Problem 3
import datetime
print('Current date and time:')
print(datetime.datetime.now())
# Problem 4
import math
radius4 = 1.1
area = math.pi * radius4**2
print(area)
# Problem 5
firstName = 'Michael'
lastName = 'Krigbaum'
print(lastName, firstName)
# Problem 6
x = 3, 5, 7, 23
x_list = list(x)
x_tuple = tuple(x)
print(x_tuple, x_list)
# Problem 7
filename = 'abc.java'
f_extns = filename.split('.')
print(repr(f_extns[-1]))
# Problem 8
color_list = ["Red","Green","White","Black"]
print(color_list[0], color_list[-1])
# Problem 9
exam_st_date = (11, 12, 2014)
print(exam_st_date[0], '/', exam_st_date[1], '/', exam_st_date[2])
# Problem 10
a = '5'
n1 = int( "%s" % a)
n2 = int("%s%s" % (a,a))
n3 = int("%s%s%s" % (a,a,a))
print(n1 + n2 + n3)
# Problem 11
print(abs(5))
print(abs.__doc__)
# Problem 12
import calendar
year = 2033
month = 6
print(calendar.month(year, month))
# Problem 13
print("""
a string that you "don't" have to escape
This
is a  ....... multi-line
heredoc string --------> example
""")
# Problem 14
from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)
# Problem 15
radius15 = 6
volume15 = 4.0/3.0 * math.pi * radius15**3
print(volume15)
# Problem 16
num16 = 5
if num16 > 17:
    print((num16 - 17) * 2)
else:
    print(abs(num16 - 17))
# Problem 17
num17 = 1990
if abs(num17 - 1000) <= 100:
    print('within 100 of 1000')
elif abs(num17 - 2000) <= 1000:
    print('within 100 of 2000')
else:
    print('not within 100 of either 1000 or 2000')
# Problem 18
num18a = 2
num18b = 2
num18c = 2
if num18a == num18b == num18c:
    print(3 * (num18a + num18b + num18c))
else:
    print(num18a + num18b + num18c)
# Problem 19
def addIS(text):
    if len(text) > 2 and text[:2] == 'Is':
        return text
    else:
        return 'Is' + text
print(addIS('array'))
print(addIS('IsIndex'))
# Problem 20
def copiesString(text, num):
    for i in range(num):
        print(text)
copiesString('hi', 5)
# Problem 21
def oddOrEven(num):
    if num % 2 == 0:
        print('EVEN')
    else:
        print('ODD')
oddOrEven(6)
# Problem 22
def num4s(input):
    count = 0
    for i in input:
        if i == 4:
            count += 1
    print(count)
num4s([4,8,9,5,4,4])
# Problem 23
def first2Copies(text, num):
    for i in range(num):
        if len(text) > 2:
            print(text[:2])
        else:
            print(text)
first2Copies('text', 3)
first2Copies('hi', 3)
# Problem 24
def vowelCheck(letter):
    vowelList = ['a','e','i','o','u']
    if letter in vowelList:
        print('vowel')
    else:
        print('not vowel')
vowelCheck('i')
vowelCheck('g')
# Problem 25
def valueInData(num, list):
    if num in list:
        return True
    else:
        return False
print(valueInData(3,[1, 5, 8, 3]))
print(valueInData(-1, [1, 5, 8, 3]))
# Problem 26
def histogram(items):
    for n in items:
        output = ''
        times = n
        while times > 0:
            output += '*'
            times -= 1
        print(output)
histogram([2,3,6,5])
# Problem 27
def concatListIntoString(list):
    output = ''
    for i in list:
        listToString = str(i)
        output = output + listToString
    print(output)
concatListIntoString([5,'hi',5,5,5, 5.0,[5.8,2]])
# Problem 28
def printEven(list):
    for i in list:
        if i == 237:
            break
        else:
            if i % 2 == 0:
                print(i)

numbers28 = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958,743, 527
    ]
printEven(numbers28)
# Problem 29
def notInColorList(one, two):
    three = set([])
    for i in one:
        if i not in two:
            three.add(i)
    print(three)
color_list_1 = {"White", "Black", "Red"}
color_list_2 = {"Red", "Green"}
notInColorList(color_list_1, color_list_2)
# Problem 30
base = 5
height = 10
triangleArea = .5 * base * height
print(triangleArea)
# Problem 31
print(math.gcd(120, 48))
# Problem 32
print(math.lcm(120, 48))
# Problem 33
def sumIf2NotEqual(a,b,c):
    if a == b or b == c or a == c:
        if a == b and b == c:
            return a + b + c
        else:
            return 0
    else:
        return a + b + c
print(sumIf2NotEqual(5,5,5))
# Problem 34
def sumIfNotBetween(a, b):
    total = a + b
    if total >= 15 and total <= 20:
        return 20
    else:
        return total
print(sumIfNotBetween(5, 1))
# Problem 35
def problem35(a,b):
    if a == b or abs(a - b) == 5:
        return True
    else:
        return False
print(problem35(5, 9))
# Problem 36
def isInstance(a,b):
    if not (isinstance(a, int) and isinstance(b, int)):
        return 'Input two integers'
    return a + b
print(isInstance(5, '0'))
# Problem 37
name37, age37, address37 = 'Mike', '23', 'Columbus'
print('Name: {}\nAge: {}\nAddress: {}'.format(name37, age37, address37))
# Problem 38
x38 = 4
y38 = 3
print((x38 + y38)**2)
# Problem 39
def futureValue(amt, int, yrs):
    new_amount = amt
    intAdjusted = int/100.0
    for i in range(yrs):
        new_amount = new_amount + (new_amount * intAdjusted)
    print(round(new_amount, 2))
futureValue(10000, 3.5, 7)
# Problem 40
def distanceFormula(point1, point2):
    distance = math.sqrt(((point2[0] - point1[0])**2) + ((point2[1] - point1[1])**2))
    print(distance)
point1 = (5, 7)
point2 = (9, 20)
distanceFormula(point1, point2)
# Problem 41
import os.path
print(os.path.isfile('PythonBasicsPt1.py'))
print(os.path.isfile('main.txt'))
# Problem 42
import struct
print(struct.calcsize("P") * 8)
# Problem 43
import platform
import os
print("Name of the operating system:",os.name)
print("\nName of the OS system:",platform.system())
print("\nVersion of the operating system:",platform.release())
# Problem 44
import site;
print(site.getsitepackages())
# Problem 45
from subprocess import call
call(["ls", "-l"])
# Problem 46
import os
print("Current File Name : ",os.path.realpath(__file__))
# Problem 47
import multiprocessing
print(multiprocessing.cpu_count())
# Problem 48
n = "246.2458"
print(float(n))
print(int(float(n)))
# Problem 49
from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir('/Users/mk/Desktop') if isfile(join('/Users/mk/Desktop', f))]
print(files_list)
# Problem 50
for i in range(0, 10):
    print('*', end="")
# Problem 51
import cProfile
def sum():
    print(1+2)
cProfile.run('sum()')
# Problem 53
import os
# Access all environment variables
print('*----------------------------------*')
print(os.environ)
print('*----------------------------------*')
# Access a particular environment variable
print(os.environ['HOME'])
print('*----------------------------------*')
print(os.environ['PATH'])
print('*----------------------------------*')
# Problem 54
import getpass
print(getpass.getuser())
# Problem 57
import time
def sum_of_n_numbers(n):
    start_time = time.time()
    s = 0
    for i in range(1,n+1):
        s = s + i
    end_time = time.time()
    return s,end_time-start_time
n = 5
print("\nTime to sum of 1 to ",n," and required time to calculate is :",sum_of_n_numbers(n))
# Problem 58
def sumNPositiveInts(num):
    sum_num = (num * (num + 1) / 2)
    print(sum_num)
sumNPositiveInts(5)
# Problem 59
def heightInCM(feet, inches):
    cms = (feet * 30.48) + ((inches/12) * 30.48)
    print(cms)
heightInCM(5, 6)
# Problem 60
def hypotenuse(a, b):
    hypo = math.sqrt((a**2) + (b**2))
    print(hypo)
hypotenuse(3,4)
# Problem 61
def inchesYardsMiles(feet):
    inches = feet * 12
    yards = feet / 3
    miles = feet / 5280
    print('Inches: {}\nYards: {}\nMiles: {}'.format(inches, yards, miles))
inchesYardsMiles(52)
# Problem 62
def convertToSeconds(days, hours, mins, secs):
    seconds = (days * 86400) + (hours * 3600) + (mins * 60) + secs
    print(seconds)
convertToSeconds(5, 12, 25, 30)
# Problem 65
def secsToDHMS(seconds):
    days = seconds // 86400
    remainder = seconds % 86400
    hours = remainder // 3600
    remainder = remainder % 3600
    minutes = remainder // 60
    remainder = remainder % 60
    seconds = remainder
    print('Days: {}\nHours: {}\nMinutes: {}\nSeconds: {}'.format(days, hours, minutes, seconds))
secsToDHMS(476730)
# problem 66
def BMI(height, weight):
    bmi = (weight/(height**2)) * 703
    print(bmi)
BMI(72, 200)
# Problem 67
def pressureConversion(kPa):
    psi = kPa * 0.1450377377
    mmHg = kPa * (760/101.325)
    atm = kPa * 0.00986923
    print("PSI: {}\nmmHg: {}\nATM: {}".format(psi, mmHg, atm))
pressureConversion(500)
# Problem 68
num = 5245
x  = num //1000
x1 = (num - x*1000)//100
x2 = (num - x*1000 - x1*100)//10
x3 = num - x*1000 - x1*100 - x2*10
print("The sum of digits in the number is", x+x1+x2+x3)
# Problem 69
x, y, z = 2, 4, 5
a1 = min(x, y, z)
a3 = max(x, y, z)
a2 = (x + y + z) - a1 - a3
print("Numbers in sorted order: ", a1, a2, a3)
# Problem 73
x1 = 5.6
y1 = 7.8
x2 = 3.6
y2 = 4.7

x_m_point = (x1 + x2)/2
y_m_point = (y1 + y2)/2
print();
print("The midpoint of line is :")
print( "The midpoint's x value is: ",x_m_point)
print( "The midpoint's y value is: ",y_m_point)
# Problem 83
def elementsGTnum(list, num):
    for i in list83:
        if i < num:
            return False
        else:
            return True
list83 = [25, 65,78,43,567]
print(elementsGTnum(list83, 40))


