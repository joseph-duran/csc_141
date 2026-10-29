'''Joseph Duran
Chapter 7
This program will show the user a list of pizza toppings and then ask them to choose toppings for their pizza.
5/10
'''
pizzas = True
while pizzas:
    topping = input("What topping would you like on your pizza?: ")
    if topping == "quit":
        pizzas = False
    else:
        print(f"Adding {topping} to your pizza.")
