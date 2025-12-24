# String Methods in Python
x="Hello from Melvin, who lives in India"

print(x.capitalize())	# Converts the first character to upper case
print(x.casefold())	# Converts string into lower case
print(x.center(50))	# Returns a centered string
print(x.count('l'))	# Returns the number of times a specified value occurs in a string
print(x.encode())	# Returns an encoded version of the string
print(x.endswith('a'))	# Returns true if the string ends with the specified value
print(x.expandtabs())	# Sets the tab size of the string
print(x.find('l'))	# Searches the string for a specified value and returns the position of where it was found
print(x.format())	# Formats specified values in a string
print(x.format_map({}))	# Formats specified values from a dictionary in a string
print(x.index('l'))	# Searches the string for a specified value and returns the position of where it was found
print(x.isalnum())	# Returns True if all characters in the string are alphanumeric
print(x.isalpha())	# Returns True if all characters in the string are in the alphabet
print(x.isascii())	# Returns True if all characters in the string are ascii characters
print(x.isdecimal())	# Returns True if all characters in the string are decimals
print(x.isdigit())	# Returns True if all characters in the string are digits
print(x.isidentifier())	# Returns True if the string is an identifier
print(x.islower())	# Returns True if all characters in the string are lower case
print(x.isnumeric())	# Returns True if all characters in the string are numeric
print(x.isprintable())	# Returns True if all characters in the string are printable
print(x.isspace())	# Returns True if all characters in the string are whitespaces
print(x.istitle())	# Returns True if the string follows the rules of a title
print(x.isupper())	# Returns True if all characters in the string are upper case
print(x.join(['a','b']))	# Converts the elements of an iterable into a string
print(x.ljust(50))	# Returns a left justified version of the string
print(x.lower())	# Converts a string into lower case
print(x.lstrip())	# Returns a left trim version of the string
print(x.maketrans('a','b'))	# Returns a translation table to be used in translations
print(x.partition(' '))	# Returns a tuple where the string is parted into three parts
print(x.replace('l','L'))	# Returns a string where a specified value is replaced with a specified value
print(x.rfind('l'))	# Searches the string for a specified value and returns the last position of where it was found
print(x.rindex('l'))	# Searches the string for a specified value and returns the last position of where it was found
print(x.rjust(50))	# Returns a right justified version of the string
print(x.rpartition(' '))	# Returns a tuple where the string is parted into three parts
print(x.rsplit())	# Splits the string at the specified separator, and returns a list
print(x.rstrip())	# Returns a right trim version of the string
print(x.split())	# Splits the string at the specified separator, and returns a list
print(x.splitlines())	# Splits the string at line breaks and returns a list
print(x.startswith('H'))	# Returns true if the string starts with the specified value
print(x.strip())	# Returns a trimmed version of the string
print(x.swapcase())	# Swaps cases, lower case becomes upper case and vice versa
print(x.title())	# Converts the first character of each word to upper case
print(x.translate(str.maketrans('l','L')))	# Returns a translated string
print(x.upper())	# Converts a string into upper case
print(x.zfill(50))	# Fills the string with a specified number of 0 values at the beginning