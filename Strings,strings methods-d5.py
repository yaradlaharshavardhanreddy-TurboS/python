Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#String Methods

#1) len()--length method

a="Data Science"
len(a)
12

b=""
len(b)
0

c=" "
len(c)
1

#--------------------------------------

#count()

a="twinkle twinkle little star"

a.count("t")
5
a.count("twinkle")
2
a.count("w")
2

#--------------------------------------


#find()--find a string

a="coded"
a.find("a")
-1
a.find("d")
2
a.find("x")
-1

#--------------------------------------

#escape sequences

#\n-->new line
#\t-->tab space

a="name:harsha reddy\nmobile no:9494639719\tmailid:reddy@gmail.com\nbranch:cse"
print(a)
name:harsha reddy
mobile no:9494639719	mailid:reddy@gmail.com
branch:cse




#--------------------------------------

#replace()--replace method



a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'




#--------------------------------------



#upper
a="Harsha Reddy"
a.upper()
'HARSHA REDDY'

#lower()

a="HARSHA REDDY"
a.lower()
'harsha reddy'


#capitalize()


#can make the intial charchter to upper case.

a="python code"
a.captialize()
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    a.captialize()
AttributeError: 'str' object has no attribute 'captialize'. Did you mean: 'capitalize'?
a.captitalize()
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    a.captitalize()
AttributeError: 'str' object has no attribute 'captitalize'. Did you mean: 'capitalize'?
a.captialize()
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    a.captialize()
AttributeError: 'str' object has no attribute 'captialize'. Did you mean: 'capitalize'?
a.capitalize()
'Python code'




#title()
#makes all intial charchters in a sentence ccaptial

a="I am in class"
a.title()
'I Am In Class'


#--------------------------------------


#isupper()
a="HARSHa"
a.isupper()
False
a.islower()
False
a="HARSHA"
a.isupper()
True


#isdigit()

d="1234"
d.isdigit()
True


#isallpha()

a="hatsareinco"
a.isaplha()
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    a.isaplha()
AttributeError: 'str' object has no attribute 'isaplha'. Did you mean: 'isalpha'?
a.isalpha()
True


#isalnum()
a="13apper"
a.isalnum()
True



#-------------------------------------------











... 
... 
>>> 

... 
>>> 
>>> #startswith()
>>> a="hello python"
>>> a.startswith("h")
True
>>> a.endswith("n")
True
>>> 
>>> #-------------------------------------------------
>>> 
>>> 
>>> #strip()
>>> #lstrip(),rstrip()
>>> 
>>> a="              pooja           "
>>> a.strip()
'pooja'
>>> a.lstrip()
'pooja           '
>>> a.rstrip()
'              pooja'
>>> 
>>> 
>>> #-----------------------------------------------------
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #split()-splits the string
>>> 
>>> a="python java c c++"
>>> a.split()
['python', 'java', 'c', 'c++']
>>> b="i am in vja"
>>> b.split()
['i', 'am', 'in', 'vja']
>>> 
>>> #------------------------------------------------------
>>> 
>>> 
>>> #join
>>> 
>>> a="vja","hyd","vzg"
"".join(a)
'vjahydvzg'

" ".join(a)
'vja hyd vzg'
"p".join(a)
'vjaphydpvzg'


#--------------------------------------------------------

#comcatneation

fname="harsha"
lname="reddy y"
print(fname+" "+lname)
harsha reddy y
print((fname+" "+lname).title())
Harsha Reddy Y


