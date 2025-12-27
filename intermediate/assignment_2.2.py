'''
Write a function to print the input string with double quotes.

Input:

A string 'input_str' containing the input string to be printed. The input string can contain alphanumeric characters, spaces, and special characters.

Output:

Print the input string with double quotes around it.

Sample Input:

Hello, World!

Sample Output:

"Hello, World!"
'''

def print_with_quotes(input_str):
    print("\"" + input_str + "\"")

print_with_quotes("Hello, World!")