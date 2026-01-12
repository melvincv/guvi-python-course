toys=["ball", "doll", "car", "blocks", "puzzle"]

# Create a new list with toys that contain the letter "o"
newtoy=[x for x in toys if "o" in x]
print(newtoy)  # Output: ['ball', 'doll', 'blocks']

# Create a new list excluding the toy "doll"
newtoy=[x for x in toys if x!="doll"]
print(newtoy)  # Output: ['ball', 'car', 'blocks', 'puzzle']

# Create a new list with all toy names in uppercase
newtoy=[x.upper() for x in toys]
print(newtoy)  # Output: ['BALL', 'DOLL', 'CAR', 'BLOCKS', 'PUZZLE']

# Create a new list replacing "car" with "truck"
newtoy=[x if x!="car" else "truck" for x in toys]
print(newtoy)  # Output: ['ball', 'doll', 'truck', 'blocks', 'puzzle']