'''
Chapter 5
Joseph Duran
This progame will show you the who has access to the program. 
5/10
'''




users =["Admin", "Chase", "Rick", "Adam"]

for users in users:
    if 'Admin' in users:
        print("Hello Admin, would you like to see a status report")
else:
    print("You're just some regular person")

    