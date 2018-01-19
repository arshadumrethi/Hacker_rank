from __future__ import print_function

n = int(input())
i = 0
while 1:
    i+=n*(n-1)
    nfound=0
    for j in range(2,n):
        if (i%j != 0):
            nfound=1
            break
    if(nfound==0):
        if(i==0):
            i=1
        print(i)
        break
