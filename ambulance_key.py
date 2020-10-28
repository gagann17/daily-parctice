n1=input()
n1=int(n1)
lst1=[]
while len(lst1)<n1:
    i=input()
    lst1.append(i)
n2=input()
n2=int(n2)
lst2=[]
while len(lst2)<n2:
    j=input()
    lst2.append(j)
lst1.extend(lst2)
a=input()
b=input()
x=lst1.index(a)
y=lst1.index(b)
del lst1[x:y+1]
print(*lst1,sep="\n")

    
