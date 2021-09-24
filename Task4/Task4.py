import sys
x = []
CountMin = 0
f = open(sys.argv[1], "r")
for line in f:
    y = line.split()
    x.append(int(y[0]))
mal = min(x)
bol = max(x)

for ch in range (mal,bol+1):
    counter=0
    for z in x:
        if ch > z:
            counter+=ch-z
        if ch < z:
            counter+=z-ch
    if CountMin == 0:
        CountMin = counter
    elif counter < CountMin:
        CountMin = counter

print(CountMin)
