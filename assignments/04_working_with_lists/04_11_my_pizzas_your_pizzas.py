'''
Joseph Duran
Chapter 4
This program shows my favorite pizza and my friends favorite pizza with a loop.
'''
pizzas = ["cheese", "pepperoni", "veggie", "hawaiian", "Neapolitan", "New York_Style"]

myfriend_pizzas = pizzas[:]  
pizzas.append('pepperoni')
myfriend_pizzas.append('hawaiian')




print("My favorite foods are:")
for pizza in pizzas:
    print(pizza)

print("My friends favorite pizzas are:")
for pizza in myfriend_pizzas:
    print(pizza)