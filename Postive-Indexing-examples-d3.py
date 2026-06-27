Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> q="I am Learning Python Course"
>>> 
>>> q[13]
' '
>>> a[11]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a[11]
NameError: name 'a' is not defined
>>> q[11]
'n'
>>> q[14]+a[15]+a[16]+a[17]+a[18]+a[19]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    q[14]+a[15]+a[16]+a[17]+a[18]+a[19]
NameError: name 'a' is not defined
>>> q[14]+q[15]+q[16]+q[17]+q[18]+q[19]
'Python'
>>> q[5]
'L'
>>> q[5]+q[6]+q[7]+q[8]
'Lear'
>>> q[5]+q[6]+q[7]+q[8]+q[9]
'Learn'
>>> q[21]
'C'
>>> q[21]+q[22]+q[23]+q[24]+q[25]+q[26]
'Course'
>>> 
>>> 
>>> 
>>> s="Time is Very Precious
SyntaxError: unterminated string literal (detected at line 1)
>>> s="Time is Very Precious"
>>> 
>>> 
>>> s[13]
'P'
>>> s[13]+s[14]+s[15]+s[16]+s[17]+s[18]+s[19]+s[20]
'Precious'
>>> s[8]+s[9]+s[10]+s[11]
'Very'
>>> s[0]+s[1]+s[2]+s[3]
'Time'
