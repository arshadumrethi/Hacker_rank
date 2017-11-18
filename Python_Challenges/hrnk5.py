#Attempt number 1 which did not work
# n = int(raw_input())
# for n in range(1, 21):
#     i = int()
#     i = i > 0
#     if i < n:
#         print i^2
#     else:
#         break

#Attempt number 2 which worked
n = int(raw_input())
i = 0 #setting i as zero
numbers = [] #setting an empty list where the numbers will be stored.

while i < n:
    numbers.append(i) #Filling up the list with numbers less than n starting with 0.
    i += 1 #Adding each consecutive number i < n to the list.

for num in numbers:
    print num**2 #printing the square of each number in the list.


#Another script that works but not for all test cases.
# for i in range(int(raw_input())):
#     print i**2
