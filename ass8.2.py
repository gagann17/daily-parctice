fname=input('Enter the file name:')
try:
  fh=open(fname)
except:
  print("File no found",fname)
  quit()
count=0
for line in fh:
  line=line.rstrip()
  if not line.startswith("From "):
    continue
  stuff=line.split()
  count=count+1
  print(stuff[1])
