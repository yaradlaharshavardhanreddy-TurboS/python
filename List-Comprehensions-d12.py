

#List Comprehensions

#syntax:

#  variable =[exp for var in collection/range]
'''
a = ["codegnan","python","java"]

a = [i.upper() for i in a]
print(a)
'''


'''
a = ["vja","hyd","vzg"]

b= [i.title() for i in a]

print(b)'''


'''
a = [1,2,3,5,6,8,12,13]

b= [i*i for i in a]

print(b)

'''


#if-usageg in list comprehension

'''n = 21

# b = [print(i,end=" ") for i in range(n)]

b = [i for i in  range(n) if i%2==0]
print(b)



b = [i*i for i in range(21) if i%2==0]

print(b)

'''


x = ["apple","banana","grapes","mango","kiwi","dragon","berry"]


'''
b = [x[i] for i in range(len(x)) if "a" in x[i]]

print(b)'''
'''

b = [i for i in a if "a" in i]
print(b)

b = [i for i in a if "a" not in i]
print(b)'''

'''

b = [i*i if i%2==0 else i*5 for i in range(30)]
print(b)

'''
'''

a = [1,2,3,4,5]
b = [5,4,3,2,1]

c = [a[i]+b[i] for i in range(len(a))]

print(c)
 
'''


















