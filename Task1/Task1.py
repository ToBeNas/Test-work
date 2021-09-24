import sys
n = int(sys.argv[1])
m = int(sys.argv[2])

num = 1
path = "1"

while True:
    num+=m-1
    if num > n:
        num -= n
    if num !=1:
        path += str(num)
    if num == 1:
        break
print (path)