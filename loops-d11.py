'''#loop()
#for,while,range,break,continue,pass
##for loop()
#list
a = [10,20,30,40,50]
for i in a:
    print(i)

a = [10,20,30,40,50]
for i in a:
    print(a)

a = [10,20,30,40,50]
for i in a:
    print(i,end="")

a = [10,20,30,40,50]
for i in a:
    print(i)
print(type(a))
print(type(i))



#tuple
a = (10,20,30,40,50)
for i in a:
    print(i)
print(type(a))
print(type(i))



#set
a = {10,20,30,40,50}
for i in a:
    print(i)
print(type(a))
print(type(i))



#for list to get data type
a =["harsha":red,"reddy":"vardhan","age":21]
for i in a:
    print(i)
print(type(a))
print(type(i))
#for dictionary
b = {"year":2026,"month":"july","date":9}
for i in a:
    print(i)
print(type(b))
print(type(i))
for i in b.keys():
    print(type(b))
    print(type(i))
    print(i)
for i in b.values:
     print(type(b))
    print(type(i))
    print(i)
for i in b.items():
    print(i)
    print(type(b))
    print(type(i))
#for string
a = "codegnan"
for i in a:
    print(i)
#for flaot
b = [4.5,6.7,8.9]
for i in b:
    print(i)
    print(type(b))
    print(type(i))
#for complex
a = [2 +8j,3+10j]
for i in b:
    print(i)
    print(type(b))
    print(type(i))
#for bool
a = [True,False]
for i in b:
    print(i)
    print(type(b))
    print(type(i))'''




#while loop()
#infinite execution
'''a = 10
while a>1:
    print(a)

a = 10
while a<1:
    print(a)

a= 10
while a>1:
    print(a)
    a = a-1


a =10
while a>1:
    print(a)
    a = a-1

a =10
while a>=1:
    print(a)
    a = a-1

a =20
while a>3:
    print(a)
    a = a-1'''

'''a =20
while a>3:
    a =a-1
print(a)


a =40
while a>5:
    a=a-1
print(a)

a =30
while a>1:
    print(a)
    a+=1

a =10
while a>2:
    print(a)
    a-=1'''



#range()
#start-stop-step
'''
for i in range(20):
    print(i)'''




#task 1    

'''for i in range(0,30,3):
    
    print(i)'''
    
    
#task2:
'''
for i in range(5,50,5):
    print(i)'''

#task3:
'''

for i in range(2,20,2):
    print(i)'''



#task4:
'''
while True:
    marks = int(input("Enter Student Marks:"))
    if 91<marks<=101:
        print("Garade-A")
        
    elif 81<marks<=91:
        print("Grade-B")
        
    elif 70<marks<=81:
        print("Grade-C")
        
    elif 50>marks<=71:
        print("Grade-D")

    elif marks<50:
        print("Grade- Fail")

    else:
        print("Enter correct marks")'''







#break


'''

break

prime prime a = 10

while a>1:

print (a) ama-1

a-10

while a > 1

print(a)

a = a - 1

if a=6:

break

10

while a > 1
a=10
while a>1:
    print(a)
    a=a-1'''

'''a=10
while a>1:
    print(a)
    a=a-1
    if a==6:
        break'''

'''a=10
while a>1:
    a=a-1
    if a==6:
        break
    print(a)'''

'''for i in range(20):
    if i==13:
        break
    print(i)'''

'''a="python"
if a=="h": 
    break
print(a)''' #error

'''a="python"
for i in a:
    if i=="h":
        break
    print(i)'''



#continue


#continue

'''a = 20
while a>5:
    print(a)
    a = a-1
    if a==10:
       continue'''

'''a =20
while a>5:
    a=a-1
    if a==10:
        continue
    print(a)'''

'''for i in range(15):
    if i==7:
        continue
    print(i)'''


'''a = "python"
for i in a:
    if i=="y":
        continue
    print(i)'''







# Task : ATM Application


card = input("Enter Card:")
account = 100000

if card =='c':
    
    print("Welcome Harsha Reddy")
    print("Please enter your password")
    pwd = input("Enter your ATM password:")

    

    if pwd=="1234":
            print("Login Successful")
            print('''Options : 1: Balance Enquiry
                               2: Withdraw Amount''')
            

    else:
        print("Invalid Password")
        
        
    option = int(input())
    
    if option==1:
        print("Your Account Balance is",account)
            

    elif option==2:
        print("Enter amount to withdraw")
        withdraw = int(input())
        print("Remining Amount within your account",account-withdraw)
            
                     
    else:
        
        print("Select a valid Option")
            
            

else:
    print("Enter VAlid Card")


























































































































































