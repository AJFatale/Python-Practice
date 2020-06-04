fname = input("Enter file name: ")
fh = open(fname)
count = 0
s = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    
    c = line.find(":")
    v = line[c+2:]
    s = s + float(v)
    count =count + 1
    
    
print(s/count)
