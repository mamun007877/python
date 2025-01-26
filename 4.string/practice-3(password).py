#check if the password and confirm password are same
#case sensitive
password = input("Password: ")
confirm_password = input("Confirm Password: ")

if password == confirm_password:
    print("Passwords match.")
else:
    if password.casefold()==confirm_password.casefold():
        print("Passwords are the same but case is different and try again.")
    else:
        print("Passwords do not match.")

#not case sensitive

password = input("Password: ").casefold()
confirm_password = input("Confirm Password: ").casefold()

if password == confirm_password:
    print("Passwords match.")
else:
    print("Passwords do not match.")