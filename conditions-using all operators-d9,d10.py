#conditions
#if-conditins by using comparison operators
#<.>,<=.>=,!=,==

'''a=10
b=20
if a<b:
    print("less")'''

'''a=10
b=20
if a>b:
    print("less")'''

'''a=10
b=20
if a<=b:
    print("less")'''

'''a=10
b=20
if a>=b:
    print("less")'''

'''a=10
b=20
if a!=b:
    print("less")'''

'''a=10
b=20
if a==b:
    print("less")'''

'''a=int(input("enter a"))
b=int(input("enter b"))
if a<b:
    print("less")'''

'''a=int(input("enter a"))
if a<15:
    print("less")'''

'''a="python"
if a=="python":
    print("match")'''


#-----------------------------------------------
#if-condition by using logical operators
#logical-- and, or, not

'''a=3
b=6
if a<b and b>a:
    print("true")'''


'''a=3
b=6
if a<=b and b>=a:
    print("true")'''



'''a=3
b=6
if a!=b and b==a:
    print("true")   '''


'''a=3
b=6
if a<b or b>a:
    print("true")'''


'''
a=3
b=6
if a<=b or b>=a:
    print("true")'''



'''a=3
b=6
if a!=b or b==a:
    print("true")'''


'''a=3
b=6
if not a<b and b>a:
    print("true")'''



'''a=3
b=6
if a<b or b>a:
    print("true")    '''



#--------------------------------------------------------

#if-condition by using identify operators
#identify -- is , is not

'''a=4
if type(a) is int:
    print("is is int")'''
    


'''a=4
if type(a) is not int:
    print("is is int")'''


'''a=4.3
if type(a) is float:
    print("is is float")'''


'''a=4.3
if type(a) is  not float:
    print("is is float")'''


'''a="course"
if type(a) is str:
    print("is is string")'''

'''a="course"
if type(a) is not  str:
    print("is is string")
                            '''

'''a= 7+2j
if type(a) is complex:
    print("is is complex")'''


'''a= 7+2j
if type(a) is not complex:
    print("is is complex")'''


'''a= True
if type(a) is bool:
    print("is is bool")'''


'''
a= True
if type(a) is not bool:
    print("is is bool")'''


#---------------------------------------------------

#if-condition by using membership operators
# membership  in,not in

'''a=2,3,4,5,6,7,8
if 8 in a:
    print("true")'''

'''a=2,3,4,5,6,7,8
if 8 not in a:
    print("true")'''

'''a=int(input())
if 30 in a:
    print("true")   Traceback (most recent call last):
  File "C:/Users/hp/Desktop/Python-037/conditions-using all operators.py", line 176, in <module>
    if 30 in a:
TypeError: argument of type 'int' is not a container or iterable

#error because we cannot say what user can give '''




'''a=2,3,4,5,6,7,8
b=int(input("enter value"))
if b  in a:
    print("true")'''





'''a=2,3,4,5,6,7,8
b=int(input("enter value"))
if b  not in a:
    print("true")'''


#-----------------------------------------------

#if-else conditions by using comparision operators
# <.>,<=,>=,!=,==

'''a=4
b=7
if a<b:
    print("true")
else:
    print("false")'''

'''a=4
b=7
if a>b:
    print("true")
else:
    print("false")'''

'''a=4
b=7
if a<=b:
    print("true")
else:
    print("false")'''


'''a=4
b=7
if a>=b:
    print("true")
else:
    print("false")'''

'''a=4
b=7
if a!=b:
    print("true")
else:
    print("false")'''

'''a=4
b=7
if a==b:
    print("true")
else:
    print("false")'''



    
'''a=int(input("enter a"))
b=int(input("enter b"))
if a<b:
    print("true")
else:
    print("false") '''                                               


#-------------------------------------------

#if-else conditions by using logical operators

# and , or ,not

'''a=4
b=7
if a<b and b>a:
    print("true")
else:
    print("false")'''

'''a=4
b=7
if a<=b and b>=a:
    print("true")
else:
    print("false")'''


'''a=4
b=7
if a!=b and b==a:
    print("true")
else:
    print("false")'''

'''a=4
b=7
if a<b or a>b:
    print("true")
else:
    print("false")'''


'''a=4
b=7
if a<=b or a>=b:
    print("true")
else:
    print("false")'''

'''a=4
b=7
if a!=b or a==b:
    print("true")
else:
    print("false")'''

'''a=int(input("enter a"))
b=int(input("enter b"))
if a<b and a>b:
    print("true")
else:
    print("false")'''


'''a=int(input("enter a"))
b=int(input("enter b"))
if a<b or a>b:
    print("true")
else:
    print("false")'''


#------------------------------------


#if-else conditions by using indentify operators

# is , is not

'''a=4
if type(a) is int:
    print("true")
else:
    print("false")'''


'''
a=4
if type(a) is not int:
    print("true")
else:
    print("false")'''

'''a=4.3
if type(a) is float:
    print("true")
else:
    print("false")'''

'''a=4.3
if type(a) is not float:
    print("true")
else:
    print("false")'''


'''a="python"
if type(a) is str:
    print("true")
else:
    print("false")'''

'''a="python"
if type(a) is not str:
    print("true")
else:
    print("false")'''

'''a=2+8j
if type(a) is complex:
    print("true")
else:
    print("false")'''


'''a=2+8j
if type(a) is not  complex:
    print("true")
else:
    print("false")'''


'''a=True
if type(a) is bool:
    print("true")
else:
    print("false")'''


'''a=True
if type(a) is not bool:
    print("true")
else:
    print("false")'''

#-------------------------------------------------------

#if-else conditions by using membership operators

'''a=2,3,4,5,6,7,8
if 8 in a:
    print("true")
else:
    print("false")'''

'''a=2,3,4,5,6,7,8
if 8 not in a:
    print("true")
else:
    print("false")
    '''

'''a=int(input())
if 30 in a:
    print("true")   Traceback (most recent call last):
  File "C:/Users/hp/Desktop/Python-037/conditions-using all operators.py", line 176, in <module>
    if 30 in a:
TypeError: argument of type 'int' is not a container or iterable

#error because we cannot say what user can give '''




'''a=2,3,4,5,6,7,8
b=int(input("enter value"))
if b  in a:
    print("true")
else:
    print("false")'''





'''a=2,3,4,5,6,7,8
b=int(input("enter value"))
if b  not in a:
    print("true")

else:
    print("fasle")'''


#--------------------------------------------

#if-else-else conditions by using comparision operators

'''a=4
b=6
if a<b:
    print("less")
else:
    print("greater")'''


'''a=4
b=6
if a>b:
    print("less")
elif a<b:
    print("greater")'''
#----------------------------------------------------------

#if-else-else conditions by using logical operators

'''a=18
b=5
if a<b and b>a:
    print("b is greater")

elif a==b or a<=b:
    print("they are not equal")

elif not(a==b):
    print("a is greater")
    
else:
    print("cannot be determined")'''




#-----------------------------------------------------------

#if-else-else conditions by using identify operators

#identify
'''a = 5
if type(a)is int:
    print("it is int")

elif type(a)is not int :
    print("false")'''


'''a = 5.3
if type(a)is float:
    print("it is floatt")

elif type(a)is float:
    print("false")'''


'''a = "Python"
if type(a)is str:

    print("it is string")

elif type(a)is str:
    print("false")'''

'''a = 5+7j
if type(a)is complex:
    print("it is complex")

else:
    print("false")'''


'''a = True
if type(a)is bool:
    print("it is Boolean")

elif ype(a)is bool:
    print("false")'''


#---------------------------------------------

#if-else-else conditions by using membership operators
    
'''a=2,3,4,5,6,7,8
if 8 in a:
    print("true")
elif 8 not in a:
    print("false")'''

'''a=2,3,4,5,6,7,8
if 8 not in a:
    print("true")
elif 8 in a:
    print("false")
    '''

'''a=int(input())
if 30 in a:
    print("true")   Traceback (most recent call last):
  File "C:/Users/hp/Desktop/Python-037/conditions-using all operators.py", line 176, in <module>
    if 30 in a:
TypeError: argument of type 'int' is not a container or iterable

#error because we cannot say what user can give '''




'''a=2,3,4,5,6,7,8
b=int(input("enter value"))
if b  in a:
    print("true")
elif b not in :
    print("false")'''





'''a=2,3,4,5,6,7,8
b=int(input("enter value"))
if b  not in a:
    print("true")

elif b in a:
    print("fasle")'''

#--------------------------------------------------


#multiple-if conditions by using comparision operators

'''a=20
b=40
if a<b:
    print("less")

if b>a:
    print("greater")

if a!=b:
    print("not equal")'''


'''a=20
b=40
if a==b:
    print("less")

if b>=a:
    print("greater")

if a<=b:
    print("not equal")
'''

'''a=20
b=40
if a<b:
    print("less")

if b==a:
    print("greater")

if a>=b:
    print("not equal")

else:
    print("true")'''

#--------------------------------------------
#if-else-else conditions by using logical operators

'''a=20
b=40
if a<b and b>a:
    print("less")

if b>=a or b<=a:
    print("greater")

if not (a!=b or a==b):
    print("not equal")
else:
    print("True")'''

#-------------------------------------------

#if-else-else conditions by using identify operators

'''a=20
if type(a) is int:
    print("it is int")

if type(a) is not float:
    print("it is only int")

else:
    print("True")'''


'''a=20.0
if type(a) is float:
    print("it is float")

if type(a) is not float:
    print("it is only int")

else:
    print("True")'''


'''a="python"
if type(a) is str:
    print("it is String")

if type(a) is not str:
    print("it is only int")

else:
    print("True")'''



'''a=5+4j
if type(a) is complex:
    print("it is complex")

if type(a) is not complex:
    print("it is only int")

else:
    print("True")'''

'''a=True
if type(a) is bool:
    print("it is bool")

if type(a) is not bool:
    print("it is only int")

else:
    print("True")'''


#--------------------------------------------
#if-else-else conditions by using membership operators


'''a=2,3,4,5,6,7,8
if 8 in a:
    print("true")
if 8 not in a:
    print("false")'''

'''a=2,3,4,5,6,7,8
if 8 not in a:
    print("true")
if 8 in a:
    print("false")
    '''

'''a=int(input())
if 30 in a:
    print("true")   Traceback (most recent call last):
  File "C:/Users/hp/Desktop/Python-037/conditions-using all operators.py", line 176, in <module>
    if 30 in a:
TypeError: argument of type 'int' is not a container or iterable

#error because we cannot say what user can give '''




'''a=2,3,4,5,6,7,8
b=int(input("enter value"))
if b  in a:
    print("true")
if b not in :
    print("false")'''





'''a=2,3,4,5,6,7,8
b=int(input("enter value"))
if b  not in a:
    print("true")

if b in a:
    print("fasle")'''


#--------------------------------------------------



'''a=4
b=9
if a<b:
    print("less")
    if b>a:
        print("greater")'''


'''a=4
b=9
if a>b:
    print("less")
    ifb>a:
    print("greater")'''


'''
a=7
b=11
if a!=b:
    print("true")
    if b==a:
        print("greater")'''


'''a=7
b=11
if a!=b:
    print("true")
    if b==a:
        print("greater")
    else:
        print("false")'''


'''a=13
b=15
if a==b:
    print("true")
    if b>a:
        print("greater")

else:
    print("false)'''


'''a=7
b=11
if a!=b:
    print("true")

    if b==a:
        print("greater")
    elif a<b:
        print("less")
    else:
        print("false")'''

#-------------------------------------------------------
































