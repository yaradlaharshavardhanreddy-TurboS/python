#Generators: no tuple comprehension in the above cases if we remove those braces and we keep peranthesis when outcome is generator
#[expr for var in callection/range]

#in list
'''a=[i for i in range(16)]
print(a)
print(type(a))'''


#(expr for i in range in collection/range)
'''a=(i for i in range(16))
print(a)
print(*a)
print(type(a))'''

'''b=list(a)
print(b)'''

#print(tuple(a))
#print(set(a))

#generators main definition: A generator is also a function which can be used as an iterator (loop) by producing group of values, where we can use yield key word
#yield vs return: return will terminate the function where as yield can pass the function and go on with every successive iteration
'''a,b=[int(x) for x in input("Enter the values:").split(",")]
def check(a,b):
    while a<b:
        #yield a
        a=a+1
        yield a
print(*check(a,b))'''


'''a,b=[int(x) for x in input("Enter the values:").split(",")]
def check(a,b):
    while a<b:
        a=a+1
        #return a in this it will print only first value and stop
    return a
    #return a in this it will print only last value and stop 
print(check(a,b))'''


#yield v/s return
def mygen():
    return "vja"
    return "hyd"
    return"vzg"
    #return "vja","hyd","vzg"
print(*mygen())

'''def mygen():
    yield "python"
    yield "java"
    yield "DSA"
print(*mygen())'''

#next()
'''d=mygen()
print(next(d))
print(next(d))
print(next(d))'''
