
#Method-1-Using Temp

a = int(input())

b = int(input())

temp = a

a = b

b = temp

print(a,b)


#Method-2-Using No Temp


a = int(input())

b = int(input())

a,b = b,a

print(a,b)


#Method-3-Using Arithemtic Operators


a = int(input())

b = int(input())

c = b-a

a = a+c

b = b-c

print(a,b)


#Method-4-Using Formatting

#for int

a = int(input())

b = int(input())

a = a+b

b = a-b

a = a-b

print("after swapping a=%d b=%d" %(a,b))




#for float

a = float(input())

b = float(input())

a = a+b

b = a-b

a = a-b

print("after swapping  a=.2%f b=.2%f"%(a,b))


#for string

a = input()

b = input()

a,b = b,a

print("after swapping  a=%s b=%s" %(a,b))





























        
