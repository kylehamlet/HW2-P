# Author: kjh6064@psu.edu
# Kyle Hamlet, solo

def getGradePoint (gradepoint):
  if gradepoint == "A":
    return 4.0
  elif gradepoint == "A-":
    return 3.67
  elif gradepoint == "B+":
    return 3.33
  elif gradepoint == "B":
    return 3.0
  elif gradepoint == "B-":
    return 2.67
  elif gradepoint == "C+":
    return 2.33
  elif gradepoint == "C":
    return 2.0
  elif gradepoint == "D":
    return 1.0
  else: 
    return 0.0

credits = 0
GPC = 0
count = 0
x = 1
while count != 3:
  gradepoint = str(input(f"Enter your course {x} letter grade: "))
  credit = float(input(f"Enter your course {x} credit: "))
  test = getGradePoint(gradepoint)
  print(f"Grade point for course {x} is: {test}")
  gradepoint_calc = getGradePoint(gradepoint)*credit
  credits += credit
  GPC += gradepoint_calc
  x += 1
  count += 1

GPA = (GPC/credits)
print(f"Your GPA is: {GPA}")