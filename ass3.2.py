hrs=input('Enter hours:')
rate=input('Enter rate per hour:')
hours=float(hrs)
ratef=float(rate)
if hours <= 40 :
    pay=hours*ratef
    print(pay)
else :
    pay=(40*ratef+(hours-40)*1.5*ratef)
    print(pay)
