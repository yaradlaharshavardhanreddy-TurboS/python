Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Slicing
a="codegnan"
a[0:3]
'cod'
#Here it is

a[0:4]
'code'


a="work until you succeed"
a[6:10]
'ntil'
a[6:11]
'ntil '
a[5:10]
'until'
a[12:15]
'ou '
a[11:14]
'you'
>>> a[:4]
'work'
>>> a[15:22]
'succeed'
>>> 
>>> b="codegnan i solutions"
>>> b="codegnan it solutions"
>>> b[12:20]
'solution'
>>> 
>>> 
>>> #Negative Slicing
>>> 
>>> a="Vijayawada is a royal city"
>>> a[-10:]
'royal city'
>>> a[-10:-5]
'royal'
>>> a[-15]
'i'
>>> a[-16]
' '
>>> a[-25]
'i'
>>> a[-26]
'V'
>>> a[-26:-16]
'Vijayawada'
>>> a[-4:]
'city'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> b="Vizagis city of dreams"
>>> b="Vizag is city of dreams"
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> b[-15:-20]
''
>>> b[-14:-19]
''
