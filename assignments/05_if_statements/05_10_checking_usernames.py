'''
Joseph Duran
Chapter 5
This program will show you if the user name is taken or not.
6/10'''




current_users = ('Demi Boyer', 'Crystal Cox', 'Evelynn Lawson', 'Maddox Lyons')
new_users = ('Zeke Peck', 'Crystal Cox', 'Lane Castro', 'Maddox Lyons')
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry {new_user} this user name is taken")