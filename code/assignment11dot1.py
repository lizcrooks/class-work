import re
hand = open('regex_sum_348093.txt')
total = list()
for line in hand:
    x = line.rstrip()
    y = re.findall('([0-9]+)' , x) 
    if len(y) > 0 :
        total = total +(y) 
        numlist = [int(value) for value in total]
        totalnum = sum(numlist)
print totalnum