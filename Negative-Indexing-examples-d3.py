Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=" Simple is better than Complex"
>>> a[-23]
' '
>>> a[-21]
's'
>>> a[-21]+a[-20]+a[-19]+a[-18]+a[-17]+a[-16]
's bett'
>>> a[-21]+a[-22]+a[-23]+a[-24]+a[-25]+a[-26]
'si elp'
>>> a[-21]+a[-20]+a[-19]+a[-18]+a[-17]+a[-16]
... 
's bett'
>>> a[-27]
'm'
>>> a[-29]
'S'
>>> a[-29]+a[-28]+a[-27]+a[-26]+a[-25]+a[-24]
... 
'Simple'
>>> a[-12]+a[-11]+a[-10]+a[-9]
'than'
>>> a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'Complex'
>>> 
>>> 
>>> b="I Love Python"
>>> 
>>> b[-11]+b[-10]+b[-9]+b[-8]
'Love'
>>> b[-6]+b[-5]+b[-4]+b[-3]+b[-2]+b[-1]
'Python'
>>> 
>>> 
>>> 
