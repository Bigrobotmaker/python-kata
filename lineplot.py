f = open("C:/Users/ben735/Desktop/CASE6.RSM")
thisdict ={}
f.readline()
f.readline()
f.readline()
f.readline()
x = f.readline()
x = x.split()
f.readline()
f.readline()
f.readline()
f.readline()
i = 0
while i < len(x):
    thisdict[x[i]]=[]
    i = i+1
print(thisdict)
i = 0
print()
b =[]
while True:
    b = f.readline().split()
    i = 0
    if len(x) != len(b):
            break
    while i < len(b):
        thisdict[x[i]].append(b[i])
        i = i+1
    
print(thisdict["TIME"])
print(len(thisdict))
  
