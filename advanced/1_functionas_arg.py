list=['car','bus','bike','train']

# Function as argument
def loop(x):
    print(x*3)

# Looping through the list
loop(list)

# Using function as argument
def map_simple(crazy,list):
    for item in list:
        # Calling the passed function
        crazy(item)

# Calling the function
map_simple(loop,list)

