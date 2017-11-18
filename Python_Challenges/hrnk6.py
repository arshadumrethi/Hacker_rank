# n = int(raw_input())
#
# def leap(n):
#     if n % 400 == 0:
#         print "leap"
#     elif n % 100 == 0:
#         print "False"
#
#
# leap(n)

def is_leap(year):
    leap = False
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    else:
        return False

print is_leap(input())
