guestname = input("Enter your name: ")

with open('guest_name.txt', 'w') as file_object:
    file_object.write("The guest's name is " + guestname)