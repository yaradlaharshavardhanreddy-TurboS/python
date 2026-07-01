Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a=[2,5.6,"python",6+9j,True]
print(a)
[2, 5.6, 'python', (6+9j), True]
type(a)
<class 'list'>
#----------------------------

#append-to daa an data into a list
b=[2,5.6,"python",6+9j,True]
b.append(23)
b
[2, 5.6, 'python', (6+9j), True, 23]
b.append(25,11)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    b.append(25,11)
TypeError: list.append() takes exactly one argument (2 given)
#cannot add more than one data
#-------------------------------------

#extends
#can add more than one data in a form of list

a=[2,5.6,"python",6+9j,True,"Red"]
a.extends([23,"Harsha",147])
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a.extends([23,"Harsha",147])
AttributeError: 'list' object has no attribute 'extends'. Did you mean: 'extend'?
a.extend([23,"Harsha",147])
a
[2, 5.6, 'python', (6+9j), True, 'Red', 23, 'Harsha', 147]
#--------------------------------------

#insert-to add data at  certain index.

c=[2,5.6,"python",6+9j,True,"Red","Har"]
c.insert(2,"DSA")
c
[2, 5.6, 'DSA', 'python', (6+9j), True, 'Red', 'Har']

#-------------------------------------
#index-returns the index of the data we wanna find
d=[5,7.6,"ML",6+9j,True,"Red","Har"]
d.indec("ML")
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    d.indec("ML")
AttributeError: 'list' object has no attribute 'indec'. Did you mean: 'index'?
d.index("ML")
2


#------------------------------------------------
#copy-to copy data from a list.


ce=[17,10.6,"DSA",6+9j,True,"Red","Har"]
d=ce.copy()
d
[17, 10.6, 'DSA', (6+9j), True, 'Red', 'Har']
#-------------------------------------------------

#count--to count the occurences of a data in alist

d=[17,10.6,"DSA",6+9j,True,"Red","Har"]
d.count("Red")
1
#------------------------------------------------
#sort--to sort the data in a list into ascending to descending.
d=[17,10.6,21,27,26,95]
d.sort()
d
[10.6, 17, 21, 26, 27, 95]
>>> 
>>> #----------------------------------------------
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #reverse--printing the llist from last to first
>>> a=[7,8,14,91,27]
>>> a,reverse()
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a,reverse()
NameError: name 'reverse' is not defined. Did you mean: 'reversed'?
>>> a.reverse()
>>> a
[27, 91, 14, 8, 7]
>>> n=["java","python","c","c++"]
>>> n.reverse()
>>> n
['c++', 'c', 'python', 'java']
>>> #-------------------------------------------
>>> 
>>> #pop()--to remove a data froma list.if you want an exact index give that index inside pop() funtion.
>>> n=["java","python","c","c++"]
>>> n.pop()
'c++'
>>> n.pop(2)
'c'
>>> #-------------------------------------------
>>> #remove()--also remove data from the list but instead of index,we use data to remove from the list.
>>> 
>>> q=["java","python","c","c++"]
>>> q.remove("c")
>>> q
['java', 'python', 'c++']
>>> #-------------------------------------------
>>> 
>>> #length--returns the length of the list.
>>> q=["java","python","c","c++"]
>>> len(q)
4
>>> #-------------------------------------------
>>> #clear--clears the entire list
>>> q=["java","python","c","c++"]
>>> q.clear()
>>> q
[]
