score=input('What is the score?:')
try:
  scr = float(score)
except:
  print('Please add a numeric value')

if scr > 1.0 or scr < 0.0 :
  print('Enter a valid grade point')
elif scr >= 0.9 :
  print('A')
elif scr >= 0.8 :
  print('B')
elif scr >= 0.7 :
  print('C')
elif scr >= 0.6 :
  print('D')
else :
  print('F')
