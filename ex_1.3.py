fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    l = line.split()
    for w in range(len(l)):
        if l[w] not in lst:
            lst.append(l[w])
lst.sort()
print(lst)
