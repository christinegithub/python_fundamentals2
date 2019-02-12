# Define a function called is_even that accepts a number as an argument and
# returns a boolean (true/false) indicating whether that number is even or not
# (HINT: use the % operator).
# Try calling it with different numbers.

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


print(is_even(46))

print(is_even(5333333))

print(is_even(-5))

print(is_even(-100))
