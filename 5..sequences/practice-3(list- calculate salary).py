# calculate the salary, weekly working hours given in lis per hour cost is user input


list_hour=[int(input("enter the number of hours")) for i in range(5)]

cost_per_hour=float(input("enter the cost per hour: "))
salary=sum(list_hour)*cost_per_hour
print(salary)

# if hour is given in string 

list_hour=[int(i) for i in input("Enter the number of hours").split()]
wage=int(input("Enter the hour wages: "))
print(sum(list_hour)*wage)