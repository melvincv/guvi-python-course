x="  Hello from Melvin, who lives in India  "

y='''
This is a multi-line string.
It can span multiple lines.
You can include line breaks and indentation.
'''

print(y)

# String is an Array, print the first character
print("print the 3 character of the string x:")
print(x[2])

# Length of the string
print(len(x))

# Check if "lives" is in the string x
print("lives" in x)

# Slicing a string
print(x[2:5])  # From index 2 to 4
print(x[2:])   # From index 2 to end
print(x[:5])  # From start to index 4
print(x[-5:-2])  # From index -5 to -3

# Print a blank line
print()

print(x.upper())  # Convert to uppercase
print(x.lower())  # Convert to lowercase   
print(x.strip())  # Remove whitespace from both ends
print(x.replace("India", "USA"))  # Replace substring
print(x.split(","))  # Split string into a list by spaces

# Concatination
a = "Hello"
b = "World"
c = a + " " + b
print(c)

print()

text = "python is easy python is powerful"

print(text.find("python"))   # index of first match
print(text.count("python"))  # 2
print("easy" in text)  # True
