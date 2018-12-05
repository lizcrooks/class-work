temp = input('Enter the temperatures in degrees Farenheit? ')
farenheit = float(temp)
Celsius = (int(farenheit) - 32) * (5/9)
print("The temperature " + str(farenheit) + " degrees Farenheit " + "is " + str(Celsius) + " degrees Celsius")