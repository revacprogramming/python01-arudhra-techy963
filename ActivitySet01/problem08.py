fname = raw_input("Enter file name: ")
f = open(fname)
count = 0
total = 0
for line in f:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
        
    t=line.find("0")
    number= float(line[t:])
    count = count + 1
    total = total + number

average = total/count

print ("Average spam confidence:",average)