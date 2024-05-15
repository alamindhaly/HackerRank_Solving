i = 4
d = 4.0
s = 'HackerRank '

i2 = int(input())
d2 = float(input())
s2 = input()

print(i + i2)

# Print the sum of the double variables on a new line.
print("{:.1f}".format(d + d2))

#"{:.1f}": This is a string format specification.
# It tells Python to format the value as a floating-point number with one digit after the decimal point (1f).
# The colon (:) indicates the start of the format specifier, and .1 specifies that there should be one digit after the decimal point.

# .format(d + d2): This part of the line applies the format() method to the string "{:.1f}".
# The format() method replaces the placeholder {:.1f} with the result of the expression d + d2,
# which is the sum of the two double variables d and d2.

#So, when you run print("{:.1f}".format(d + d2)), it will print the sum of d and d2 formatted as a floating-point number with one digit after the decimal point.

# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.

print(s + s2)
