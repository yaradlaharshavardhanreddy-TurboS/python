Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dict{}

a={"name":"harsha","mailid":"reddy@123"."mobile no":"9494719729"}
SyntaxError: invalid syntax
a={"name":"harsha","mailid":"reddy@123","mobile no":"9494719729"}
type(a)
<class 'dict'>
print(a)
{'name': 'harsha', 'mailid': 'reddy@123', 'mobile no': '9494719729'}

#keys()

a.keys()
dict_keys(['name', 'mailid', 'mobile no'])

#values()

a.values()
dict_values(['harsha', 'reddy@123', '9494719729'])


#--------------------------------------------------

#items()

a.items()
dict_items([('name', 'harsha'), ('mailid', 'reddy@123'), ('mobile no', '9494719729')])

#update()

a.update({"course":"python","institue":"codegnan","mentor":"pooja mam"})
a
{'name': 'harsha', 'mailid': 'reddy@123', 'mobile no': '9494719729', 'course': 'python', 'institue': 'codegnan', 'mentor': 'pooja mam'}

#----------------------------------------------------

#setdefault()

b={"year":2026,"month":"july"}
b.setdefault("date",2)
2
b
{'year': 2026, 'month': 'july', 'date': 2}

#pop()
b
{'year': 2026, 'month': 'july', 'date': 2}
b={"year":2026,"month":"july","date":21}
b.pop("month")
'july'

#popitem()
b.popitem()
('date', 21)
b
{'year': 2026}

#--------------------------------------------

#get

d={"year":2026,"month":"july","date":21}
d.get("year")
2026

#--------------------------------------------

#copy()
a=d.copy()
a
{'year': 2026, 'month': 'july', 'date': 21}

#clear()
>>> d.clear()
>>> d
{}
>>> 
>>> d.update({"name":"pooja"})
>>> d
{'name': 'pooja'}
>>> #----------------------------------------------
>>> 
>>> 
>>> #len()
>>> len(d)
1
>>> 
>>> d
{'name': 'pooja'}
>>> #-----------------------------------------------
>>> 
>>> a={"idnos":[10,20,30],"names":["harsha","trinadh","sai"],"marks":[99,98,97]}
>>> a
{'idnos': [10, 20, 30], 'names': ['harsha', 'trinadh', 'sai'], 'marks': [99, 98, 97]}
>>> type(a)
<class 'dict'>
>>> len(a)
3
>>> a.keys()
dict_keys(['idnos', 'names', 'marks'])
>>> a.values()
dict_values([[10, 20, 30], ['harsha', 'trinadh', 'sai'], [99, 98, 97]])
>>> a.items()
dict_items([('idnos', [10, 20, 30]), ('names', ['harsha', 'trinadh', 'sai']), ('marks', [99, 98, 97])])
>>> 
>>> a.get("idnos")
[10, 20, 30]
>>> 
>>> 
>>> #------------------------------------------------
>>> 
>>> a.update({40,"reddy",100})
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    a.update({40,"reddy",100})
ValueError: dictionary update sequence element #0 has length 5; 2 is required
>>> a.update([40,"reddy",100])
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    a.update([40,"reddy",100])
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
