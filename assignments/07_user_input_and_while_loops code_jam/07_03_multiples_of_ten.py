'''
Joseph Duran
Chapter 7
This program asks the user for a number and then reports whether the number is a multiple of 10.
3/10
'''
while True:
    chosen_number = input("Please enter a number?:")
    if int(chosen_number) % 10 == 0:
        print (f"{chosen_number} is a multiple of 10.")
    else:
        print (f"{chosen_number} is not a multiple of 10.")
