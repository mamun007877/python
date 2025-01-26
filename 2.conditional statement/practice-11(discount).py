'''
calulate the discounted amount
amount<=1000       10%
1000<amount<=5000  20%
5000<amount<=10000 30%
10000<amount       50%
'''

amount=float(input("Enter the amount: "))

if amount<=1000:
    discount=amount*0.10
elif 1000<amount<=5000:
    discount=amount*0.20
elif 5000<amount<=10000:
    discount=amount*0.30
elif 10000<amount:
    discount=amount*0.50

discounted_amount=amount-discount
print (f"discounted amount is {discounted_amount}")