fname=input('Enter the file name:')
try:
  fh=open(fname)
except:
  print('File not found:',fname)
  quit()
res=[]
for line in fh:
  line=line.rstrip()
  stuff=line.split()
  for word in stuff:
      if word in res:
          continue
    res.append(word)
print(res)
