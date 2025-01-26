# find sum of given number as input, find sum of positive and negative number, find max,min value,convert dec to bin
# import math
# n_times=int(input("enter the number of times"))
# sum=0
# positive_sum=0
# negative_sum=0
# max=-math.inf
# min=math.inf
# for i in range(n_times):
#     num=int(input("enter the number"))
#     sum+=num
#     if num>0:
#         positive_sum+=num
#     else:
#         negative_sum+=num
#     if num>max:
#         max=num
#     if num<min:
#         min=num
# print(f"sum ={sum}\npositive_sum ={positive_sum}\nnegative_sum ={negative_sum}\nmax ={max}\nmin ={min}")

#convert dec to bin
bin=""
dec=int(input("enter the number: "))
while dec>0:
    bin+=str(dec%2)
    dec=dec//2

print(f"binary representation of {dec} is {bin[::-1]}")

