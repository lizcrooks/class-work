name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hours = []

for line in handle:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    atpos = line.find(':')
    time = line[atpos-2:atpos]
    hours.append(time)

counts = dict()
for time in hours:
    counts[time] = counts.get(time,0) + 1

lst = list()
for key, val in counts.items() :
    lst.append( (key, val) )
lst.sort()
for val, key in lst :
    print val, key
