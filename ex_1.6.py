name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

count = None
mail = None
m = dict()

for l in handle:
    l = l.rstrip()
    if not l.startswith("From "):
        continue
    x = l.split()[5]
    w = x.split(':')
    m[w[0]]=m.get(w[0],0) + 1

    
 #   print(x)
#print(m.items())

for k,v in sorted(m.items()):                                         
    print(k,v)
#l = list()
#for k,v in lst:
 #   l.append((v,k))
#print(l)
   
          