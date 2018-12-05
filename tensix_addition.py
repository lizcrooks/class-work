print("Enter 'q' to quit whenever.")
while True:

    try:
        x = input("Tell me a number: ")
        if x == 'q':
            break
        x = int(x)

        y = input("Tell me another number: ")
        if y == 'q':
            break
        y = int(y)

    except ValueError:
        print("Sorry, I do honestly need a number.")

    else:
        sum = x + y
        print("The sum of " + str(x) + " and " + str(y) + " is " + str(sum) + ".")