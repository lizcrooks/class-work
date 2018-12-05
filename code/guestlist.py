guests = ['Emily Dickinson', 'Shakespeare', 'Queen Elizabeth I']
message = ("Would you, " + guests[0] + " please do me the honor of attending this dinner party?")
guests[0] = 'Elizabeth Taylor'
guests.insert(0, 'Cary Grant')
guests.insert(-2, 'Humphrey Bogart')
guests.append('Galileo')
message = "I can only invite two people for dinner."
print(message)
absent_guest = guests.pop()
message = ("I am sorry I cannot invite you to dinner " + absent_guest + ".")
print(message)
absent_guest = guests.pop()
message = ("I am sorry I cannot invite you to dinner " + absent_guest + ".")
print(message)
absent_guest = guests.pop()
message = ("I am sorry I cannot invite you to dinner " + absent_guest + ".")
print(message)
absent_guest = guests.pop()
message = ("I am sorry I cannot invite you to dinner " + absent_guest + ".")
print(message)
message = ("Would you, " + guests[0] + " still do me the honor of attending this dinner party?")
print(message)
message = ("Would you, " + guests[1] + " still do me the honor of attending this dinner party?")
print(message)
del guests[0]
del guests[0]
print(guests)
len(guests)
print(len(guests))



