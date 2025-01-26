import random
ran_num = random.randint(1,10)
# while True:
#     n=int(input("Enter your guesing number between 1-10: "))
#     if n==ran_num:
#         print("Congratulations! You guessed the correct number.")
#         break
#     elif n<ran_num:
#         print("Too low. Try again.")
#     else:
#         print("Too high. Try again.")
#another way of guessing
n=0
while n!=ran_num:
    n=int(input("Enter your guesing number between 1-10: "))
    if n<ran_num:
        print("Too low. Try again.")
    elif n>ran_num:
        print("Too high. Try again.")
    else:
        print("Congratulations! You guessed the correct number.")
