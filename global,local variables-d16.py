#Gobal and local variables

#A Varaible inside and outside the function is called local variable
#A variable is defined inside the function and is accessible to the entire global space is called global variable
#A variable is inside the function is called global variable


#first case of global variable
'''a=4
def check1():
    print("inside the value is:",a)
check1()
print("outside value is:",a)'''

#second case of global variable
'''a=2
def check2():
    a=5
    a=a**2
    print("inside value is:",a)
check2()
print("outside value is:",a)'''

#third case of both global and local variables
'''a=6
def check3():
    a=8
    print("inside value is:",a)
    a=10
    print("updated value is",a+5)
    b=13
    b=b+a
    print("value of b is:",b)
check3()
print("a value is",a)
print("b value is",b)'''#it will not print beacause b is not declared outside the function



#usage of global key word --> when use want to access the global variable inside the function directly
#and carry forward the updated value even outside the function then we need to use goblal keyword


#usage of global keyword
'''a=4
def final():
    global a,b
    print("inside value is",a)
    a=15
    print("update value is",a)
    b=20
    b=b+a
    print("value of b is",b)
final()
print("a value is",a)
print("b value is",b)'''
