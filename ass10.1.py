fname=input('Enter the file name:')
try:
  fh=open(fname)
except:
  print('File not found:',fname)
  quit()
counts={}
for line in fh:
  line=line.rstrip()
  if not line.startswith("From "):
    continue
  stuff=line.split()
  lst=stuff[5].split(:)
  counts[lst[0]]=counts.get(list[0],0)+1

print(sorted([k,v for v,k in counts.items()],reverse=true))
