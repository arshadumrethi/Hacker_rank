# n = int(raw_input())
# rand = range(1,n+1)
# var = ', '.join(str(rand))
# print var

from __future__ import print_function
print(*range(1, input() + 1), sep="")

Input  = input()
Answer = ''

for i in range(1,Input+1):
    Answer += str(i)

print Answer
