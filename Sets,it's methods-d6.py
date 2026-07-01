Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#sets{}
a=[5,8.9,"pooja",5+9j,True,False}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
a={5,8.9,"pooja",5+9j,True,False}
type(a)
<class 'set'>
print(a)
{False, True, (5+9j), 5, 8.9, 'pooja'}

#subset

a={1,2,3,4,5,6,7,8,9,}
b={2,4,6,}
a.issubset()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a.issubset()
TypeError: set.issubset() takes exactly one argument (0 given)
a.issubset(b)
False
a.issubset(a)
True
b.issubset(a)
True
b.issuperset(a)
False
a.issuperset(b)
True

#-----------------------------------------

#union
a={1,2,3,4,5,6,7,8,9,10,10,11}
b={10,9,15,21}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 15, 21}
c={1,2,3,4,5,6,7,8,9}
c={1,2,3,4,5,6,7,8,9,10,9,10}
print(c)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
#------------------------------------------

#intersection()
c={1,2,3,4,5,6,7,8,9,10,10,11}
b={10,9,15,21}
c.intersection(b)
{9, 10}
#------------------------------------

#update()
c={1,2,3,4,5,6,7,8,9,10,10,11}
d={12,15,18,1,2,3,4,}
d.update(c)
d
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 18}
c.update(d)
c
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 18}
#-----------------------------------------------

#diffrence()
={4,5,6,7,10,12,17}
SyntaxError: invalid syntax
>>> f={4,5,6,7,10,12,17}
>>> g={15,17,19,25.4,5}
>>> f.diffrence(g)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    f.diffrence(g)
AttributeError: 'set' object has no attribute 'diffrence'. Did you mean: 'difference'?
>>> f.difference(g)
{4, 6, 7, 10, 12}
>>> g.difference(f)
{25.4, 19, 15}
>>> #-----------------------------------------------
>>> 
>>> a={3,4,5,6,7,10,11}
>>> b={1,3,5,7,9,1,15}
>>> a.symmetric_difference(b)
{1, 4, 6, 9, 10, 11, 15}
>>> #Symmetric_diffrence
>>> 
>>> #---------------------------------------------
>>> 
>>> a={3,4,5,6,7,10,11}
>>> b={1,3,5,7,9,1,15}
>>> a.intersection_update(a)
>>> a
{3, 4, 5, 6, 7, 10, 11}
>>> a.intersection_update(b)
>>> a
{3, 5, 7}
>>> b.intersection_update(a)
>>> b
{3, 5, 7}
>>> #intersecction_update()
>>> 
>>> #------------------------------------------------
>>> 
>>> #symmetrc_diffrence_update
>>> 
>>> #diffrence_update
>>> 
>>> a={3,4,6,8,9}
>>> b={4,5,7,9,10}
>>> a.difference_update(b)
>>> a
{3, 6, 8}
>>> b.difference_update(a)
>>> b
{4, 5, 7, 9, 10}
>>> 
>>> #----------------------------------------------


#symmetrc_diffrence_update

d={3,4,6,8,9}
e={4,5,7,9,10}
SyntaxError: multiple statements found while compiling a single statement
d={3,4,6,8,9}

e={4,5,7,9,10}

d.symmetric_difference_update(e)
d
{3, 5, 6, 7, 8, 10}
e.symmetric_difference_update(d)
e
{3, 4, 6, 8, 9}
#---------------------------------------

#pop()

g={1,2,3,4,5,7,9,10}
g.pop()
1
#remove()
g.remove(5)
g
{2, 3, 4, 7, 9, 10}


#----------------------------------


g={1,2,3,4,5,7,9,10}
g.discard(9)
g
{1, 2, 3, 4, 5, 7, 10}
o=g.copy()
o
{1, 2, 3, 4, 5, 7, 10}
#copy

#discard

#clear
g={1,2,3,4,5,7,9,10}
g.clear()
g
set()

#add
g={1,2,3,4,5,7,9,10}
g
{1, 2, 3, 4, 5, 7, 9, 10}
g.add(12)
g
{1, 2, 3, 4, 5, 7, 9, 10, 12}

len(g)
9

#length()

#disjoint()
g={1,2,3,4,5,7,9,10}
j={1,2,3,4,5,7,9,10}
g.isdisjoint(j)
False
#note: in sets count(),index() are not valid since it is unordered
