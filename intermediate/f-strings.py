name="Melvin"
role="AI Consultant"

# Using f-strings to format strings in Python
print(f"My name is {name} and I work as an {role}.")  # Embedding variables
print(f"{name.upper()} works as an {role.lower()}.")  # Using methods

# f-strings with expressions
price = 500
gst = 18

print(f"Total price: {price + (price * gst / 100)}")

# Formatting numbers
score = 92.45678
print(f"Score: {score:.2f}")

