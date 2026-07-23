# built-in functions

#print(dir())


#print(dir("__builtins__"))


#fromkeys()

'''
a = "codegana"

print(a)
print(list(a))
print(tuple(a))


print(set(a))

#print(dict(a))

b = dict.fromkeys(a)
print(b)


c = dict.fromkeys(a,"harsha")
print(c)


c["d"] = "python"
print(c)

'''

#eval()
'''
while True:
    a = int(input("Enter a value"))
    b = int(input("Enter b value"))
    print(a+b)


while True:
    a = float(input("Enter a value"))
    b = float(input("Enter b value"))
    print(a+b)


while True:
    a = input("Enter a value")
    b = input("Enter b value")
    print(a+b)


while True:
    a = complex(input("Enter a value"))
    b = complex(input("Enter b value"))
    print(a+b)




while True:
    a = bool(input("Enter a value"))
    b = bool(input("Enter b value"))
    print(a+b)

'''

# Here we have to mention what type of input we are going to pass
# but using eval we can use or type any data type it will work

'''
while True:
    a = eval(input("Enter a value"))
    b = eval(input("Enter b value"))
    print(a+b)

'''

#zip() - we can combine mutiple collections into once collection

'''
a = [10,20,30,40,50]
b= ["khushal","manoj","harsha","sumanth","trinadh"]

print(a+b)


'''
'''
b = zip(a,name)
print(b)
'''
'''

c = list(zip(a,b))
print(c)


c = tuple(zip(a,b))
print(c)


c = set(zip(a,b))
print(c)


c = dict(zip(a,b))
print(c)

'''


#enumerate()-> we can give counter to the collection


'''
names = ["nikitha","taruni","siri","kalyani","prameela"]
'''
#for i in range(len(names)):
 #   print(names[i])
'''

b = list(enumerate(names))
print(b)


b = list(enumerate(names,10))
print(b)


b = dict(enumerate(names,100))
print(b)


'''



#ASCII

#chr()

#ord()

print(chr(65))

print(chr(90))


print(ord("a"))

print(ord("z"))














































































