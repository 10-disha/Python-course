marks = int(input("enter your marks\n"))

if marks>=90:
    grade = "ex"
elif marks>=80:
    grade="A"   
elif marks>=70:
    grade="B"   
elif marks>=60:
    grade="C"            
elif marks>=50:
    grade="D"
else:
    grade="F"           


print("your grades are\n" + grade)    