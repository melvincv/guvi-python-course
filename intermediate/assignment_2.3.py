'''
Write a function to loop through the given input numbers of size n and print them comma-separated.

Input:

A integer input n followed by the integer numbers (-10^9 ≤ numbers[i] ≤ 10^9) on each line upto n , where n is the size of the list.

Output:

Print the input numbers comma-separated.

Sample Input:

5
1
2
3
4
5

Sample Output:

1,2,3,4,5
'''

# Sample input
n = 5
numbers = [12, 34, 56, 78, 90]

# Function to print numbers comma-separated
def print_numbers():
    # Loop through the numbers and print them comma-separated
    for i in range(n):
        # Check if it's not the last number to avoid trailing comma
        if i != n - 1:
            # Print the number followed by a comma
            print(numbers[i], end=',')
        else:
            # Print the last number without a comma
            print(numbers[i])

print_numbers()