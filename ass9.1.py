fname=imput('Enter the file name:')
try:
  fh=open(fname)
except:
  print('File not found:',fname)
  quit()
counts={}
for line in fh:
  if not line.startswith("From "):
    continue
  line=line.rstrip()
  words=line.split()
  counts[words[1]]=counts.get(words[1],0)+1
bigword=None
bigcount=None

for word,count in counts;
  if bigcount is None or count>bigcount:
    bigword=word
    bigcount=count

print(bigword,bigcount)
