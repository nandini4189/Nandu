#len()
'''a=[1,2,3,4,5,67,8,9]
print(len(a))'''

#min()
'''a=[2,34,5,6,7,8,0,2,3,4]
print(min(a))
'''

#max()
'''a=[2,34,5,6,7,8,0,2,3,4]
print(max(a))'''

#sorted()
'''a=[2,34,5,6,7,8,0,2,3,4]
print(sorted(a))'''

#sum()
'''a=[2,34,5,6,7,8,0,2,3,4]
print(sum(a))
'''
#type()
'''a={2,34,5,6,7,8,0,2,3,4}
print(type(a))
'''
#Upper()
'''a='this is python code'
print(a.upper())
'''
#lower()
'''a='this is python code'
print(a.lower())
'''

'''class Pet(object):
   def my_method(self):
      print("I am a Cat")
cat = Pet()
cat.my_method()
'''

'''def uma(*args):
    print(args)
uma(1,2,3,4,5,67,8,7)'''


'''#strip()
a= '       uma       '
a.strip()
print(a)
'''

'''#Replace()
a='umadevi'
print(a.replace('u','ra'))
'''

"""#)REplace()
a='umadevi is a good and active girl'
print(a.split())"""

# function define and  function call

'''def function_1():
    print('i like flowers')
    print('i like cricket')
function_1()
print('she is beatiful')
print('the values are 1,2,3..')'''

'''# function define and  function call
def printme(str):
    "hi"
    print(str)
    return;
printme('this is function calling')
printme('this second time function calling')
'''

'''my_string=["use database","drop table test"]
#print(my_string)
my_string.append('create table test as select * from test1')
#print(my_string)
my_string.append('select * from test')
print(my_string)
'''

'''def main():
    f= open("list.txt","w+")
    #f=open("list.txt","a+")
    for i in range(1):
         f.write('"use database" ,')
         f.write('"drop table test" ,')
         f.write('"create table test as select * from test1" ,')
         f.write('"select * from test" ,')

    f.close()
    #Open the file back and read the contents
    f=open("list.txt", "r")
    if f.mode == 'r':
      contents = f.read()
    print (contents)
    #or, readlines reads the individual line into a list
    fl =f.readlines()
    for x in fl:
        print(x)
if __name__== "__main__":
  main()
'''

'''with open('list.txt','r') as reader:
    print(reader.read())'''


'''# Python Function with arguments and Return value Example
def function(a,b):
    sum=a+b
    return sum
print('after calling the outside function:',function(20,30))


'''
'''#Python Function with No argument and No Return value Example
def add():
    a=20
    b=30
    sum=a+b
    print('the sum of two numbers:',sum)
add()
'''

'''#Python Function with no argument and with a Return value

def multi():
    a=20
    b=21
    multiplication=a*b
    return multiplication
print('after return value call the function:',multi())
'''


'''#Python Function with argument and No Return value

def multi(x,y):
    multi=x*y
    print('the multiplication is:',multi)
multi(2,4)


'''

'''# passing parameters and return result from the function.

def multi(x,y):
    multi=x*y
    print('the multiplication is:',multi)
multi(2,4)
def add(x,y):
    add=x+y
    print('the addition is:',add)
add(20,2)
def sub(a,b):
    sub=a-b
    print('the subtraction of two values:',sub)
sub(20,3)
def name(firstname,lastname):
    separator=','
    result=firstname+separator+lastname
    return result
print('the result string is:',name('uma','devi'))
print('the result string is:',name('rama','krishna'))

'''

#Math functions
#Floor()
'''import math
data =21.6
print('the floor value of 21.6 is:',math.floor(data))
'''

#ceil
'''import math
data =21.6
print('the ceil value of 21.6 is:',math.ceil(data))
'''

#pi value
'''import math
print('the pi value is:',math.pi)
'''

'''import math
data=24.6
print('the floor value:',math.floor(data))
print('the ceil value:',math.ceil(data))
print('the fabs value:',math.fabs(data))'''


'''def foo(y):
    y[0]='hello'

x=[5]
foo(x)
print (x[0])'''

'''def fun(x):
    x='this is uma'
    print(x)
bar='this is another one'
fun(x='hello')'''

'''#passed by reference

''''''student={'uma':100,'rama':101,'shan':102,'nandu':103}
def test(student):
    new={'sai':104,'bhagya':105}
    student.update(new)
   # print('inside the function',student)
    return
test(student)
print('outside the function:',student)
''''''
'''
#calling function multiple times

'''list={12,3,4,5,6,7,8,9,0,2,44}
def test(list):
    new={50,45,11,1,2}
    list.update(new)
    print('inside function is:',list)
    return
test(list)
print('the outside function is:',list)
new={30,31,32,33,34,43}
list.update(new)
print('updated list:',list)
test(list)
print('here the values are updated :',list)
prev={101,102,103,2,3,4,5,6,7,8,90}
list.update(prev)
print('update the list:',list)'''
'''
print('apple',end=', ')
print('banana',end=',')
print('mango',end=',')
print('strawberry',end=' ')
'''


#Built-in functions
# All()
'''k=[2,3,4,5]
print(all(k))'''

'''k=[0,False]
print(all(k))
'''
'''k=[0,1,2,'uma',False,True]
print(all(k))

'''
# bin()
'''x=100
y=bin(x)
print(y)'''

#bool()

'''test=[0]
print('this is boolean:','is',bool(test))
'''
'''test='uma'
print('this is boolean:',bool(test))'''

'''test=None
print('none is boolean :',bool(test))
'''

#callable()
'''
x='uma'
print(callable(x))'''

#exec()
'''x=100
exec('print(x==100)')
exec('print(x+1)')
'''

#any()

'''a=[2,3,4,5,False]
print(any(a))
'''
'''a=['uma',1,2,3,5,True]
print(any(a))
'''
#ascii()
'''a='she is beautiful uma is beautiful girl'
print(ascii(a))'''


'''#float()

# for integers
print (float (9))

# for floats
print (float (8.19))

# for string floats
print (float ("-24.27"))

# for string floats with whitespaces
print (float ("     -17.19\n"))

# string float error
print (float ("xyz"))

'''

#format()

# integer
'''print (format (231, "d"))

# float arguments
print (format (123.4567898, "f"))

# binary format
print (format (12, "b"))
'''

'''student=['uma','devi','ram']
fset=frozenset(student)
print('the student name of:',fset)'''


'''class student:
    id=110
    name='umadevi'
    email='umareddy@gmail.com'
    def getinfo(self):
        print(self.id,self.name,self.email)
s=student()
s.getinfo()
delattr(student,'course')
s.getinfo()'''

'''attr=dir()
print(attr)'''

'''val=id('umadevi')
val2=id(1293)
val3=id(2.456790)
print(val)
print(val2)
print(val3)'''


'''
def function1():
    x='uma'
    y='devi'
    s=x+' '+y
    print('the concatenation string:',s)
def function2():
    a='rama'
    b='krishna'
    c=a+' '+b
    print('the argument string:',c)
def function3():
    x=20
    y=30
    z=x+y
    print('the addition of values:',z)
function1(function2(function3()))
#function3()

'''
'''def fun1():
    print('this is outer function')
    def fun2():
        print('this is inner function')
    fun2()
fun1()

'''

'''def func2():
    print("func2")

def func1():
    func2()

def func():
    func1()

if __name__ == '__main__':
    func()
'''

'''def what(obj):
    print('the')
    return obj

@what
class Huh(object):
    def __init__(self):
        print('hell')
    print('what')

Huh()


'''
'''def outer(num1):
    def inner_increment(num1):
        return num1+10
    num2=inner_increment(num1)
    print(num1,num2)
    inner_increment(10)
    def inner_inner_increment(num1):
        return num1+100
    num2=inner_inner_increment(num1)
    print(num1,num2)
    inner_inner_increment(100)
outer(10)
'''

'''x=[10,20,30,40,30]
y=x[2]+20
print((x))
print(y)
'''

'''#cloning
x=[10,20,40,50]
y=x[:]
y[2]=550
print(y)
print(x)
'''
#aliasing
'''x=[10,20,30,50,60]
y=x
print(x)
print(y)'''

#Cloning
'''x=[10,20,30,50,60]
y=x
y[2]=200
print(y)

'''
# By using slice operator
'''x=[10,20,40,50]
y=x[:]
y[1]=1000
print(x)
print(y)
'''
'''#By using copy of function
x=[10,20,40,50]
y=x.copy()
y[1]=1000
print(x)
print(y)
'''

'''l=eval(input('enter values in the list:'))
s=set(l)
print(s)

'''


'''rec={}
n=int(input('enter number of students:'))
i=1
while i<=n:
    name=input('enter student name:')
    marks=input('enter % of marks:')
    rec[name]=marks
    i=i+1
print('name of student','\t','% of marks')
for x in rec:
    print('\t',x,'\t\t',rec[x])
'''

'''x=100  # Global Variable
def fun1():
    print(x)
def func2():
    print(x)
fun1()
func2()

'''
# Factorial of a number
'''def factorial(n):
    if n==1:
        return 1
    else:
        return n* factorial(n-1)
num=4
print('the factorial value of number is:',factorial(num))

'''


# Local variable
'''def fun1():
    a=100
    print(a)
def fun2():
    b=200
    print(b)
fun1()
fun2()
'''


#Lambda Functions::

'''f=lambda x:x+x
print(f(5))
'''


# Even_numbers list::
'''my_list=[2,4,33,22,44,55,66,2,3,1,2,65,39,4]
result=list(filter(lambda x:(x % 2==0),my_list))
print(result)


'''

'''list=[2,3,4,6,78,9,0,2,22,44,56,1,2,3,4]
new_list=list(map(lambda x:x*2,list))
print(new_list)
'''
'''li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(map(lambda x: x*2 , li))
print(final_list)'''

'''sequences = [10,2,8,7,5,4,3,11,0, 1]
filtered_result = map (lambda x: x*x, sequences)
print(list(filtered_result))'''

'''from functools import reduce
seq=[4,5]
result=reduce(lambda x, y: x+y,seq)
print(result)
'''
'''with open ("Sanky_data.xlsx", "r+") as f:
    old = f.read ()  # read everything in the file
    f.seek (0)  # rewind
    f.write ("new line\n" + old)  #

'''

'''text_file=open('file.txt','w')
text_file.write('this is my string i want to add this in my file')
text_file.close()

'''

'''# Built-in module functions::

# importing built-in module math
import math

# using square root(sqrt) function contained in math module
print(math.sqrt (25))
print (math.pi)

# 2 radians = 114.59 degreees
print (math.degrees (2))

# 60 degrees = 1.04 radians
print (math.radians (60))

# Sine of 2 radians
print (math.sin (2))

# Cosine of 0.5 radians
print (math.cos (0.5))

# Tangent of 0.23 radians
print (math.tan (0.23))

# 1 * 2 * 3 * 4 = 24
print (math.factorial (4))

# importing built in module random
import random

# printing random integer between 0 and 5
print (random.randint (0, 5))

# print random floating point number between 0 and 1
print (random.random ())

# random number between 0 and 100
print (random.random () * 100)

List = [1, 4, True, 800, "python", 27, "hello"]

# using choice function in random module for choosing
# a random element from a set such as a list
print (random.choice (List))

# importing built in module datetime
import datetime
from datetime import date
import time

# Returns the number of seconds since the
# Unix Epoch, January 1st 1970
print (time.time ())

# Converts a number of seconds to a date object
print (date.fromtimestamp (454554))

'''
'''import mymodule
module={'s.no':1,
       'name':'uma',
       'age':26,
       'sal':50000,
        'country':'India'}
a=mymodule.module('s.no','name','age','sal','country')
print(a)


'''


'''import platform

x = dir(platform)
print(x)


'''



'''from math import  sqrt,factorial
print(sqrt(16))
print(factorial(5))'''

'''import math
print(dir(math))'''

'''import datetime
from datetime import date
import time
print(time.time ())

# Converts a number of seconds to a date object
print(date.fromtimestamp (454554))
'''

'''import math as m
print('tha math value of pi is :',m.pi)'''

'''from math import *
print('the squareroot value is:',sqrt(25))
print('the pi value is:',pi)
print('the sin value is:',sin(100))
print('the cos value is:',cos(200))
print('the factorial of value is:',factorial(5))'''

'''import sys
sys.path
'''
''''import math
#this is got executed---1. only once during a session
import math
import math'''

'''from math import *
print('the squareroot value is:',sqrt(25))
print('the pi value is:',pi)
print('the sin value is:',sin(100))
print('the cos value is:',cos(200))
print('the factorial of value is:',factorial(5))

'''

'''def SayHello(name):
    print("hello "+ name)
    return

'''

'''def sum(x,y):
    x = 10
    y = 2
    print(sum(x+y))
def average(x,y):
    return(x+y)/2
def power(x,y):
    return(x**y)
'''

'''def printLine(text):
  print(text, 'is awesome.')

printLine('Python')

'''
'''def greetPerson(*name):
  print('Hello', name)

greetPerson('Frodo', 'Sauron')
'''
'''def Foo(x):
  if (x==1):
    return 1
  else:
    return x+Foo(x-1)

print(Foo(4))

'''

numbers = [1, 3, 6]
newNumbers = tuple(map(lambda x: x , numbers))
print(newNumbers)