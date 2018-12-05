# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
try:
    fh = open(fname)
except:
    print 'File cannot be opened', fname
    
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    atpos = line.find(':')
    spam = line[atpos+1:]
    confidence = float(spam)
    total = total + confidence
    average = total / count
print "Average spam confidence:", average
