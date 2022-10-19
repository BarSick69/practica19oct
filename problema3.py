
from random import randint
#union(), intersection() și difference(),
x=set({})
y=set({})
z=set({})
a=set({})
for i in range(0,10):
    x.add(randint(0,200))
    y.add(randint(0,200))
    z.add(randint(0,200))
for i in range(0,201):
    a.add(i)
print("a)")
print("X:",x)
print("Y:",z)
print("Y:",y)
r1=a-(x.union(y).union(z))
r2=(a-x).intersection(a-y).intersection(a-z)
if(r1==r2):
    print("A")
else:
    print("F")
print("b)")
r1=a-(x.intersection(y).intersection(z))
r2=(a-x).union(a-y).union(a-z)
if(r1==r2):
    print("A")
else:
    print("F")


