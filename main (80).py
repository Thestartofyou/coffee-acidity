# Define the pH range for different acidity levels
LOW_ACIDITY_RANGE = (6.0, 6.9)
MEDIUM_ACIDITY_RANGE = (6.9, 7.5)
HIGH_ACIDITY_RANGE = (7.5, 8.0)

# Define the pH value of the coffee
coffee_pH = float(input("Enter the pH value of the coffee: "))

# Determine the acidity level of the coffee based on its pH value
if LOW_ACIDITY_RANGE[0] <= coffee_pH < LOW_ACIDITY_RANGE[1]:
    acidity_level = "low"
elif MEDIUM_ACIDITY_RANGE[0] <= coffee_pH < MEDIUM_ACIDITY_RANGE[1]:
    acidity_level = "medium"
elif HIGH_ACIDITY_RANGE[0] <= coffee_pH <= HIGH_ACIDITY_RANGE[1]:
    acidity_level = "high"
else:
    acidity_level = "invalid pH value"

# Display the acidity level of the coffee
print("The acidity level of the coffee is:", acidity_level)
