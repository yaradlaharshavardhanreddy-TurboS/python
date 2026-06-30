Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Formatting
a="vja"
print("city is ",a)
city is  vja


#---------------------

#format method
>>> 
>>> a=motu
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a=motu
NameError: name 'motu' is not defined
>>> b=patlu
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    b=patlu
NameError: name 'patlu' is not defined

>>> 
>>> 
>>> a="motu"
>>> b="patlu"
>>> 
>>> #using Formatting
>>> 
>>> print("Hello ",a+b)
Hello  motupatlu
>>> 
>>> #using format method
>>> 
>>> print("Hello {} {} ".format(a,b))
Hello motu patlu 
>>> 
>>> #----------------------------
>>> 
>>> #fstring
>>> 
>>> a="sita"
>>> b="ram"
>>> print(f"Hello {a}{b}")
Hello sitaram
>>> print(f"Hello {a} {b}")
Hello sita ram
>>> print(f"Hello {a} hello {b}")
Hello sita hello ram
>>> 
>>> 

>>> a=3
>>> b=7
>>> print(f"The product of {a} and {b} is a*b")
The product of 3 and 7 is a*b
>>> print(f"The product of {a} and {b} is",a*b)
The product of 3 and 7 is 21
>>> 
