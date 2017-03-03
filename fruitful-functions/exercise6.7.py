'''
Exercise 6.7.
-------------
 A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a
function called is_power that takes parameters a and b and returns True if a is a power of b . Note:
you will have to think about the base case.'''

def isPower(a, b):
    #recursive solutions
    print(a, b)
    if a == b:
        return True
    if a % b == 0 and isPower(a // b, b):
        return True
    else:
        return False 


