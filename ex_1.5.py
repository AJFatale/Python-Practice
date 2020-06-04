name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

count = None
mail = None
m = dict()

for l in handle:
    l = l.rstrip()
    if not l.startswith("From:"):
        continue
    w = l.split()
    m[w[1]]=m.get(w[1],0) + 1

#print(m)
#print(m.items())
for k,v in m.items():
    if count is None or count < v:
        count = v
        mail = k
        
    
print(mail,count)    