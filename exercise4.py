# Define a function that accepts a string as an argument and
# returns False if the word is less than 8 characters long (or True otherwise).

word = ''

def char_count(word):
    if len(word) < 8:
        return False
    else:
        return True

print(char_count('bitmaker'))

print(char_count('new'))

print(char_count('chocolate'))
