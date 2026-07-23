
# ASCII
'''

for i in range(65,91):
    print(chr(i),end = " ")

print()

for i in range(97,123):
    print(chr(i),end = " ")

'''


'''
s = input()

for i in s:
  print(f"{i}-{ord(i)} ")

'''
'''
while True:
    w = float(input("Enter your weight in kg sir/madam"))

    h = float(input("Enter your heigt in m sir/madam"))

    bmi = w/(h)**2f


    if bmi<18.5:
        print(f"Your bmi is {round(bmi,2)} You are in underweight category ")

    elif bmi>18.5 and bmi<=29.5:
        print(f"Your bmi is {round(bmi,2)} You are in healthy category ")

    elif bmi>30:
        print(f"Your bmi is {round(bmi,2)} You are in obese category ")

    else:
        print(f"Please enteer valid height and weight")

'''
'''

def cal(x):

    return 2*x+5

x = int(input("Enter x"))

print(cal(x))


'''

'''

#syntax
#a = lambda arg:exp
a = int(input())
b = lambda x:2*x+5
print(b(a))


'''








































