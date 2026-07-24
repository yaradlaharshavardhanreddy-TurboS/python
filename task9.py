
# task - marks analysis report

n = int(input("Enter the no of students"))
b = []
for i in range(1,n+1):
    print(f" enter the student{i} marks")
    i = int(input())
    b.append(i)

print(f"....................Marks Analysis Report...................")

print(f"total no of students in class {n}")

print(f"highest marks in the class is {max(b)}")

print(f"lowest marks in the class is {min(b)}")

print(f"total marks in the class is {sum(b)}")

print(f"average marks in the class is {(sum(b)/n)}")




