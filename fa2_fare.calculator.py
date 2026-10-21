# Travel Fare Calculator
FARE_RATE = 14

# Validate students name
def name_strip():
    while True:
        name = input("Enter passenger name:").strip()
        if name == "":
            print("Must not be empty. Please try again.")
        else:
            return name
    
# Validate distance travelled
def distance_digit():
    while True:
        distance = float(input("Enter distance(km): "))
        if distance <= 0:
            print("Must be greater than 0. Please try again")
        else:
            return distance
    
    
# Validate passengers
def passengers_positive():
    while True:
        passengers = int(input("Enter amount of passengers: "))
        if passengers <= 0:
            print("Must be a positive number. Please try again")
        else:
            return passengers
    
passengername = name_strip()
distancetravelled = distance_digit()
numpassengers = passengers_positive()

total_fare = distancetravelled * FARE_RATE * numpassengers

print("\nPassenger:", passengername)
print("Total Fare: PHP", round(total_fare, 2))

# Validation rules
# 1. Passenger name -- Must not be empty
# 2. Distance -- Number greater than 0
# 3. Passengers -- Positive whole number
