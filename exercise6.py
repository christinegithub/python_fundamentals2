# Create a function that converts Fahrenheit temperatures to Celsius in a file called exercise6.py.

# Start with prompting the user for a temperature in Fahrenheit.
# Then call your function and pass in the user input as a parameter.

# Your function should:

# have one parameter: the temperature in Fahrenheit
# do the conversion with this formula: C = (F - 32) x 5/9
# ensure that the parameter you pass in is a number by converting it with int()
# Output the result in a full sentence using string interpolation.

fahrenheit = 0

def convert_celcius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

print("Please enter the temperature in Fahrenheit")

fahrenheit = int(input())

celcius = convert_celcius(fahrenheit)

print("That temperature in Celcius is {}".format(celcius))
