r=input()
r=int(r)
c=input()
lst=[]
lst1=[]
i=0
while len(lst)<r:
    lst.append(tuple(map(int,input().split(' '))))
while i<len(lst):
    if i==0:
        x=int(lst[i][1])-0
        lst1.append(x)
    else :
        x=int(lst[i][1])-int(lst[i-1][1])
        lst1.append(x)
    i+=1
m=max(lst1)
n=lst1.index(m)
k=97
for j in range(26):
    if lst[n][0]==j:
        print(chr(k))
        quit()
    k+=1
