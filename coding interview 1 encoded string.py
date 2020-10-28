x=list(input("S="))
k=int(input("K="))
y=[]
k=k-1
for i in x:
    if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
        y.append(i)
    else :
        i=int(i)
        y.extend((i-1)*y)
print(y[k])
