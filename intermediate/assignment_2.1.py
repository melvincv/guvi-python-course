'''
Write a function to print the length of the given input string.

Input:

A string 'input_str' containing the input string to find the length of. The input string can contain alphanumeric characters, spaces, and special characters.

Output:

Print the length of the input string.

Sample Input:

Hello, World!

Sample Output:

13
'''

def string_length(input_str):
    print(len(input_str))

string_length("Hello, World!")