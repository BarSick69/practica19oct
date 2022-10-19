from random import randint
x=[]
y=[]
for i in range(0,5):
    x.append(randint(0,200))
    y.append(randint(0,200))
x=set(x)
y=set(y)
print("X:",x)
print("Y:",y)
print("XUY:",x.union(y))
print("X intersectie Y",x.intersection(y))
print("X\\Y:",x-y)
print("(X\\Y)U(Y\\X)",(x-y).union(y-x))
print("(X\Y)intersectie(Y\X):",(x-y).intersection(y-x))
