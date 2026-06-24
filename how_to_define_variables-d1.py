Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#variables  how to define variables and rules to follow:


print(3+3)
6
#Assing a value to a varriable\
a=11
print(a)
11
#ex
b=10
c=1
print(b+c)
11
#Assing strings to a variable
Name="Harsha Reddy"
print(NAme)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print(NAme)
NameError: name 'NAme' is not defined. Did you mean: 'Name'?
print(Name)
Harsha Reddy
#can assign any numbers after only an letter
#ex
a123456789="Cat"
>>> print(a123456789)
Cat
>>> #variable name does not allow special charchters except
>>> #underscore
>>> @Abc="red"
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> _red="cart"
>>> print(_red)
cart
>>> 
>>> #Should not use keywords as variables
>>> 
>>> if=23
SyntaxError: invalid syntax
>>> print=12
>>> print(print)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print(print)
TypeError: 'int' object is not callable
>>> 
>>> 
>>> #single line v=multiple variable
>>> 
>>> #method1
>>> a,b=3,4
>>> print(a,b)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    print(a,b)
TypeError: 'int' object is not callable
>>> z,x=3,2
>>> print(z,x)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    print(z,x)
TypeError: 'int' object is not callable
>>> a=10;b=20
>>> print(a+b)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    print(a+b)
TypeError: 'int' object is not callable
>>> h=10;g=20
>>> print(h+g)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    print(h+g)
TypeError: 'int' object is not callable
