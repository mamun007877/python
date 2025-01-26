# re-arrange lowercase to upper case
lower_case = ""
upper_case = ""
string1=input("Please enter a string: ")
for i in string1:
    if i.islower():
        lower_case += i
    else:
        upper_case += i
re_arrange=lower_case+upper_case
print(re_arrange)