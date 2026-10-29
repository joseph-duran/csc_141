'''Joseph Duran
Chapter 7
This program will show a list of deli items and then ask the user to choose items for their sandwich.
7/10
'''
sandwich_orders = ['turkey', 'ham', 'roast beef', 'veggie', 'chicken salad']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I am making your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")