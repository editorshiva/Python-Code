marks = int(input("Enter your Marks\n"))
if ( marks>=90):
    grade="S"
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
print("Your grade is " + grade)