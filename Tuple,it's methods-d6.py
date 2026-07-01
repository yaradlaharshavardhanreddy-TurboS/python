Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #tuple()
>>> a=(7,7.4,"True","Python","Harsha",9+6j)
>>> type(a)
<class 'tuple'>
>>> a.sort()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a.sort()
AttributeError: 'tuple' object has no attribute 'sort'
>>> a.index(9+6j)
5
>>> a.count()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a.count()
TypeError: tuple.count() takes exactly one argument (0 given)
>>> a.count("True")
1
>>> len(a)
6
