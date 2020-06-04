fname = input("Enter file name: ")
if len(fname) < 1 : 
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

for l in fh:
    l = l.rstrip()
    if not l.startswith("From:"):
        continue
    lst = l.split()
    print(lst[1])
  #  print(l.rstrip())

#print("There were", count, "lines in the file with From as the first word")
