'''Joseph Duran
Chapter 7
This program will show a list of the pastrami sandwiches.
6/10
'''

deli_orders = ['pastrami', 'turkey', 'ham', 'pastrami', 'roast beef', 'veggie', 'pastrami'] 
print("Sorry, we are out of pastrami today.")
while  'pastrami' in deli_orders:
    deli_orders.remove('pastrami')
print(f"Available sandwiches: {deli_orders}")