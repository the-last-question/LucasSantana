a=raw_input("digite a string:")
b=len(a)
c=0
for i in range(b):
    if a[i]==a[-(i+1)]:
        c=c+1
if c==b:
    print a,"palindromo"
else:
    print a,"nao palindromo"