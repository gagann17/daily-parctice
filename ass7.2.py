fnmae=input("Enter the file name:")
try:
  fhand=open(fname)
except:
  print("file not found",fname)
  quit()
count=0
Avg=0

for line in fhand:
  line=line.rstrip()
  if not line.startswith("X-DSPAM-Confidence:"):
    continue
    count=count+1
    Avg=Avg+float(line[20:])
print("Average spam confidence: ",Avg/count)
