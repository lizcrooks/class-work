filename = 'guestbook.txt'

print("Enter done when you are finished.")
while True:
    name = input("What's your name? ")
    if name == 'done':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(name + "\n")
        print("Hello " + name + ", your name is now in the guest book.")