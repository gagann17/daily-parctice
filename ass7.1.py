fname=input('Enter the file name:')
try:
  fhand=open(fname)
except:
  print('File name not found:',fname)
  quit()
for line in fhand:
  line=line.rstrip()
  print(line.upper())
