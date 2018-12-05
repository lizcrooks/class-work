filename = 'programming_poll.txt'

results = []
print("Enter quit when you are done.")
while True:
    result = input("\nWhat's a reason you like programming?")
    results.append(result)

    continue_poll = input("Want to give another reason? (yes/no) ")
    if continue_poll != 'yes':
        break
        
    with open(filename, 'a') as file_object:
        for result in results:
            file_object.write(result + "\n")
            