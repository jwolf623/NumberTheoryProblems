#First take a character as the input
#Then take a string in the input
#Then print out the number of times the character occurs in the string


letter=str(input())
phrase=str(input())
count=0
n=letter[0:1]
j=0                         #Back slicing index
k=1                         #Front slicing index

for letter in phrase:
    if n == phrase[j:k]:
        count+=1

    j+=1
    k+=1

print(count)

****************
L=[]
i=0
a=n[0:2]
b=n[2:5]
c=n[5:6]
d=n[7:9]
e=n[10:12]
f=n[13:15]
g=n[16:17]
print(a, b, c, d, e, f, g)

for i in range(0,7):
    n=float(input())
    
    n_parsed 
    L+=n_parsed

for num in L:
    if num < 0:
        L.remove(num)

L_sorted=sorted(L)

print(L_sorted)

