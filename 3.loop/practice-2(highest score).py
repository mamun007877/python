'''
Highest Score

Instructions

You are going to write a program that calculates the highest score from a List of scores.
e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

Important you are not allowed to use the max or min functions. The output words must match the example. i.e

The highest score in the class is: x

Example Input
78 65 89 86 55 91 64 89
In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]
Example Output
The highest score in the class is: 91


Hint
Think about the logic before writing code. How can you compare numbers against each other to see which one is larger?

'''
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
#way-1
max_score=student_scores[0]
for i in student_scores:
    if i>max_score:
        max_score=i
print(f"The highest score in the class is:{max_score}")

#way-2 using max function
print(f"The highest score in the class is: {max(student_scores)}")
