'''
#max()

print(max(4,5,7,8,10,20))

#sum()

a = 3,4,5,8,9,10,20

print(sum(a))

'''

#map()

'''
a = [2,5,7,8,10,14,16,18,19,20]
b = [1,3,5,7,9,11,15,17,21,24]

c = list(map(max,a,b))
print(c)

c = list(map(min,a,b))
print(c)
'''


'''
a = input("data1")
b = input("data2")
print(a+b)


a,b = input("enter he names").split(",")


a,b = [int(x) for x in input("names").split(",")]
print(a+b)


a,b = int(input()).split(",")
print(a+b)

a = map(int,input("enter the values").split(","))
print(a+b)


a = list(map(int,input("enter the values").split(",")))
print(a)
print(type(a))


a = tuple(map(int,input("enter the values").split(",")))
print(a)
print(type(a))

a = set(map(int,input("enter the values").split(",")))
print(a)
print(type(a))


a = list(map(eval,input("enter the values").split(",")))
print(a)
print(type(a))

'''


#dict
'''


a = {}

key = input()
pairs = input()

a[key]= "pairs"

print(a)


'''


#dict()

'''

a = input("enter the key and value pairs")

b = dict(i.split(":") for i in a.split(","))

print(b)

'''














































































































































