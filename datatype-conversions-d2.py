Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Datatypes Convesion
#int
int(7)
7
int(7.23)
7
int("python")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("python")
ValueError: invalid literal for int() with base 10: 'python'
int(4+7j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(4+7j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0

#float
float(7)
7.0
float(7.23)
7.23
float("python")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float("python")
ValueError: could not convert string to float: 'python'
float(4+9j)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    float(4+9j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
#int and float Data Conversion is not posssible for String and Complex data

#String
str("23")
'23'
str("2.32")
'2.32'
str("python")
'python'
str("5+6j")
'5+6j'
str("True")
'True'
str("False")
'False'

#String can data convert all datatypes


#Complex
complex(5)
(5+0j)
comple(2.32)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    comple(2.32)
NameError: name 'comple' is not defined. Did you mean: 'compile'?
complex(2.32)
(2.32+0j)
complex(string)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    complex(string)
NameError: name 'string' is not defined. Did you forget to import 'string'?
>>> complex(6+2j)
(6+2j)
>>> comple(True)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    comple(True)
NameError: name 'comple' is not defined. Did you mean: 'compile'?
>>> complex(False)
0j
>>> complex(False)
0j
>>> 
>>> comple(True)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    comple(True)
NameError: name 'comple' is not defined. Did you mean: 'compile'?
>>> complex(True)
(1+0j)
>>> 
>>> #complex can data convert all except String
>>> 
>>> 
>>> #boolean
>>> 
>>> bool(2)
True
>>> bool(6.32)
True
>>> bool(python)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    bool(python)
NameError: name 'python' is not defined
>>> bool(4+9j)
True
>>> bool(True)
True
>>> bool(False)
False
>>> 
>>> 
>>> #Boolean can data convert all except String
>>> 
>>> 
>>> #Note:In Boolean The String data can convert,there hs been a mistake i  missed " "
