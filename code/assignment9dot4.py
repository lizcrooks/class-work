name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
emails = []

for line in handle:
    line = line.rstrip()
    if not line.startswith('From: ') : continue
    words = line.split()
    emails.append(words[1])
print emails

counts = dict()
for address in emails:
    counts[address] = counts.get(address,0) + 1

print counts

bigemail = None
bigcount = None
for address,count in counts.items():
    if bigcount == None or bigcount < count :
        bigemail = address
        bigcount = count

print bigemail, bigcount