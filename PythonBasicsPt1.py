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
