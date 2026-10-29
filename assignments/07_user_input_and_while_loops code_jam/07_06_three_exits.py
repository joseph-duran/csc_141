'''
Joseph Duran
Chapter 7
This program will show the user three different ways to exit a while loop.
5/10'''

while True:
    user_input = input("Type 'exit' to exit the loop, or type 'break' to break the loop, or type 'quit' to quit the program: ")
    if user_input == "exit":
        print("Exiting the loop using 'exit'.")
        break
    elif user_input == "break":
        print("Breaking the loop using 'break'.")
        break
    elif user_input == "quit":
        print("Quitting the program using 'quit'.")
        break
    else:
        print("You entered:", user_input)