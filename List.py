l=[1,2,3,4,5,6,7,8,9]
print(l[5:8])
k=["Lucky","tinku","Meenu", 5,6]
print(k[0:7])
h=[1,2,3,4,"Hello",[7,8,9,10]]
print(h[0:5])
print(h[5][0:5])
print(h[0: ])
j=[1,2,3,4,5,6,7,8,9,10]
print(j[0::2])
print(j[-1::-1])
print(j[-1::-2])
print(type(j))
print(h[5][-1::-1],h[5::-1])
print(j[-3],j[7])
g=[1,2,3,4,5,6,7,8,9,10]
b=len(g)
print(b)
for v in range(b-1,-1,-1):
    print(v,g[v])
