#find user id and domain name from the email address
email=input("enter email address: ")

user_id, domain_name = email.split('@')

print(f"user id: {user_id} domain name: {domain_name}")

#another way

find_sep=email.find("@")
user_id=email[:find_sep:]
domain_name=email[find_sep+1::]
print(f"user id: {user_id} domain name: {domain_name}")