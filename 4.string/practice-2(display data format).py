'''
display data in given format(25 letters)
prodcut name........price
chicken pizza.........300

'''
item=input("Please enter the item you want to display: ")
price=input("Please enter the price: ")
print(f"{item}{"."*(25-(len(price)+len(item)))}{price}")