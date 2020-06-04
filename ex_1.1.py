fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    m=line.rstrip()
    print(m.upper())