grade = input("Enter a grade: ")
grade = int(input("Enter your grade: "))
if grade>=90:
    print("A")
elif grade>=80:
    print("B")
elif grade>=70:
    print('C')
elif grade>=65:
    print("D")
elif grade>=0:
    print("F")
else:
    print("ERROR: Grades cannot be 66negative numbers or words. Fuck off.")