x = 1

def findfactors(num):
    facs = []
    for i in range(1, num):
        if num % i == 0:
            facs.append(i)
    return facs

while x < 10000:
    facs = findfactors(x)
    facsum = sum(facs)
    if facsum == x:
        print(x)
        x += 1
    else:
        x += 1