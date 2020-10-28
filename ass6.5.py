text ="X-DSPAM-Confidence:    0.8475";
x=text.find('0')
res=float(text[x:x+6])
print(res)
