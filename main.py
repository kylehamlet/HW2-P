# Author: kjh6064@psu.edu
# Kyle Hamlet, solo

def grade (gradepoint1,gradepoint2,gradepoint3):
  if gradepoint1 or gradepoint2 or gradepoint3 == "A":
    return 4.0
  elif gradepoint1 or gradepoint2 or gradepoint3 == "A-":
    return 3.67
  elif gradepoint1 or gradepoint2 or gradepoint3 == "B+":
    return 3.33
  elif gradepoint1 or gradepoint2 or gradepoint3 == "B":
    return 3.0
  elif gradepoint1 or gradepoint2 or gradepoint3 == "B-":
    return 2.67
  elif gradepoint1 or gradepoint2 or gradepoint3 == "C+":
    return 2.33
  elif gradepoint1 or gradepoint2 or gradepoint3 == "C":
    return 2.0
  elif gradepoint1 or gradepoint2 or gradepoint3 == "D":
    return 1.0
  else: 
    return 0.0

gradepoint1 = str(input("Enter your course 1 letter grade: "))
credit1 = float(input("Enter your course 1 credit: "))
gradepoint1 = grade(gradepoint1,0,0)
print(f"Grade point for course 1 is: {gradepoint1}")

gradepoint2 = str(input("Enter your course 2 letter grade: "))
credit2 = float(input("Enter your course 2 credit: "))
gradepoint2 = grade(gradepoint2,0,0)
print(f"Grade point for course 2 is: {gradepoint2}")


gradepoint3 = str(input("Enter your course 3 letter grade: "))
credit3 = float(input("Enter your course 3 credit: "))
gradepoint3 = grade(gradepoint3,0,0)
print(f"Grade point for course 3 is: {gradepoint3}")


GPA = (gradepoint1 * credit1 + gradepoint2 * credit2 + gradepoint3 * credit3) / (credit1 + credit2 + credit3)
print(f"Your GPA is: {GPA}")