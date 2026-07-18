
#task -attendance tracker



def attendance():
    n = int(input("Total no of students in class"))
    count = 0
    count1 = 0
    for i in range(n):
        i = input(f"Is the student{i+1} present/Absent").upper()
        if i=="P":
            count+=1
        elif i=="A":
            count1+=1




    print(f"Total no of students: {n}")

    print(f"Total no of students presenet:{count}")

    print(f"Total no of absentes :{count1}")


attendance()


        
