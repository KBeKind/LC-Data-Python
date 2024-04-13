# Exercise #1: Construct for loops that accomplish the following tasks:

    # a. Print the numbers 0 - 20, one number per line.
for num in range(21):
    print(num)

    # b. Print only the ODD values from 3 - 29, one number per line.
for oddNum in range(3, 30, 2):
    print(oddNum)

    # c. Print the EVEN numbers 12 to -14 in descending order, one number per line.
for evenNum in range(12, -15, -2):
    print(evenNum)

    # d. Challenge - Print the numbers 50 - 20 in descending order, but only if the numbers are multiples of 3. (Your code should work even if you replace 50 or 20 with other numbers).
for num in range(50, 20, -1):
    if num % 3 == 0:
        print(num)



# Define three variables for the LaunchCode shuttle - one for the starting fuel level, another for the number of astronauts aboard, and the third for the altitude the shuttle reaches.
startingFuelLevel = 0
numberOfAstronauts = 0
maxAltitude = 0

# Exercise #4: Construct while loops to do the following:
# a. Query the user for the starting fuel level. Validate that the user enters a positive, integer value greater than 5000 but less than 30000.

while startingFuelLevel <= 5000 or startingFuelLevel >= 30000:
    startingFuelLevel = int(input("Enter the starting fuel level: "))
    if startingFuelLevel <= 5000 or startingFuelLevel >= 30000:
        print("Invalid Entry: Starting fuel level must be more than 5000 and less than 30000")


# b. Use a second loop to query the user for the number of astronauts (up to a maximum of 7). Validate the entry.

while numberOfAstronauts <=0 or numberOfAstronauts > 7:
    numberOfAstronauts = int(input("Enter the number of astronauts: "))
    if numberOfAstronauts <=0 or numberOfAstronauts > 7:
        print("Invalid Entry: Number of astronauts must be more than 0 and less than 8")


# c. Use a final loop to monitor the fuel status and the altitude of the shuttle. Each iteration, decrease the fuel level by 100 units for each astronaut aboard. Also, increase the altitude by 50 kilometers.
currentFuelLevel = startingFuelLevel
while currentFuelLevel >= 100:
    maxAltitude += 50
    currentFuelLevel -= 100

# Exercise #5: Print the result with the phrase, The shuttle gained an altitude of ___ km and has ___ kg of fuel left. Fill in the blanks with the altitude and fuel level values.
print("The shuttle gained an altitude of " + str(maxAltitude) + " km and has " + str(currentFuelLevel) + "kg of fuel left.")

# If the altitude is 2000 km or higher, add “Orbit achieved!” Otherwise add, “Failed to reach orbit.”
if maxAltitude >= 2000:
    print("Orbit achieved!")
else:
    print("Failed to reach orbit.")