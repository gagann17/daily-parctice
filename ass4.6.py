def computepay(h,r):
    if h > 40:
        return 40*r+(h-40)*1.5*r
    else :
        return h*r
hours=input('Enter hours:')
rate=input('Enter rate:')

try:
    hrs = float(hours)
    ratef = float(rate)
except:
    print("Enter a valid numeric value")

x=computepay(hrs,ratef)
print('Pay',x)
