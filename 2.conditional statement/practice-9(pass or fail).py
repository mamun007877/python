#check if a student has passed or failed by taking three subject
math_mark=int(input("Number of mathematical course:"))

english_mark=int(input("Number of English course:"))

science_mark=int(input("Number of Science course:"))
if math_mark>=33 and english_mark>=33 and science_mark>=33:
    print("You have passed all subjects")
else:
    print("You have failed at least one subject")