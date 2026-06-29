Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Striding

a="Data Science"
a[::]
'Data Science'
a[::1]
'Data Science'
a[::2]
'Dt cec'

b="Cloud Computing"
>>> a[::5]
'DSc'
>>> b[::5]
'C u'
>>> a[::4]
'D e'
>>> b[::4]
'Cdmi'
>>> b[::8]
'Cm'
>>> b[2:]
'oud Computing'
>>> b[:9]
'Cloud Com'
>>> b[3:11]
'ud Compu'
>>> b[::2]
'CodCmuig'
>>> b[::6]
'CCi'
>>> 
>>> 
>>> a=
SyntaxError: invalid syntax
>>> c="Machine Learning"
>>> c[3:14:2]
'hn eri'
>>> a[5:15:4]
'Sn'
>>> c[5:15:4]
'nei'
>>> c[2:12:3]
'cnLr'
>>> c[0:10:1]
'Machine Le'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #Negative Strinding
>>> d="Python Course"
>>> d[-1:-10:-2]
'ero o'
>>> d[-3:-13:-4]
'r t'
>>> d[-5:-11:-3]
'on'
