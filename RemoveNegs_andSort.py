L=[]
i=0

while i < 8:
    n=int(input())
    L.append(n)
    i+=1

for num in L:
    if num < 0:
        L.remove(num)

L_sorted=sorted(L)

print(L_sorted)
