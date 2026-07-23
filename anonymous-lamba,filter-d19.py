
# anonyomous
'''
def cal(x):

    return 2*x+5

x = int(input("Enter x"))

print(cal(x))


'''



#syntax

'''
#a = lambda arg:exp
a = int(input())
b = lambda x:2*x+5
print(b(a))

'''



#task 1:

'''
a = int(input())
b = int(input())

c = lambda a,b:a*b

print(c(a,b))
'''

#task 2:
'''

s = input("Enter a string")
c = lambda s:s.upper()
print(c(s))

'''


#task 3:

'''
s = input("Enter a string")
c = lambda s:s.title()
print(c(s))
'''


#task 4:

'''

fname = input("Enter a string")
lname = input("Enter a string")

fullname = lambda fname,lname:(fname + " "+ lname).title()

print(fullname(fname,lname))

'''



#task 5:

'''

fname,lname = [x for x in input("enter the names").split(",")]

fullname = lambda fname,lname:(fname+"  "+lname).title()
print(fullname(fname,lname))

'''

#filter

'''

a = list(map(int,input().split()))

for i in range(len(a)):
    if a[i]%2 == 0:
        print(a[i],end = " ")


'''


# even numbers
'''
a = list(map(int,input().split()))
b = list(filter(lambda x:x%2 == 0,a))
print(b)


'''
#non empty print
'''

a =[[],(),set(),{}," ",None,5,8.9,"python",8+9j,True,False]

b = list(filter(None,a))

print(b)

'''








































































