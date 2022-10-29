a={1,2,3,"A","B","C"}
a=list(a)
combinatii=[]
for i in range(0,len(a)):
    combinatii.append(a[i])
l=len(a)
for j in range(0,l):
        for k in range(0,l):
            if(j!=k):
                if(set({a[j],a[k]}) not in combinatii):
                    combinatii.append(set({a[j],a[k]}))

for j in range(0,len(a)):
        for k in range(0,len(a)):
            if(j!=k):
                for r in range(0,len(a)):
                    numb=[j,k,r]
                    numbset=set(numb)
                    if(len(numbset)==len(numb)):
                        if(r!=k and r!=j):
                            if(set({a[j],a[k],a[r]})not in combinatii):
                                combinatii.append(set({a[j],a[k],a[r]}))

for j in range(0,l):
        for k in range(0,l):
            for n in range(0,l):
                for r in range(0,l):
                    numb=[j,k,n,r]
                    numbset=set([j,k,n,r])
                    if(len(numbset)==len(numb)):
                        if(set({a[j],a[k],a[n],a[r]})not in combinatii):
                            combinatii.append(set({a[j],a[k],a[n],a[r]}))
for j in range(0,l):
    for k in range(0,l):
            for n in range(0,l):
                for r in range(0,l):
                    for o in range(0,l):
                        numb=[j,k,n,r,o]
                        numbset=set([j,k,n,r,o])
                        if(len(numbset)==len(numb)):
                            if(set({a[j],a[k],a[n],a[r],a[o]})not in combinatii):
                                combinatii.append(set({a[j],a[k],a[n],a[r],a[o]}))
for j in range(0,l):
    for k in range(0,l):
            for n in range(0,l):
                for r in range(0,l):
                    for o in range(0,l):
                        for x in range(0,l):
                            numb=[j,k,n,r,o,x]
                            numbset=set([j,k,n,r,o,x])
                            if(len(numbset)==len(numb)):
                                if(set({a[j],a[k],a[n],a[r],a[o],a[x]})not in combinatii):
                                    combinatii.append(set({a[j],a[k],a[n],a[r],a[o],a[x]}))
print(combinatii)
print(len(combinatii))


