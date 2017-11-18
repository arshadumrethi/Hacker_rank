a = int(input())
b = int(input())
m = int(input())

while a in range(11) and b in range(11):
    print pow(a,b)
    break

while a in range(11) and b in range(11) and m in range(2,1001):
    print pow(a,b,m)
    break
