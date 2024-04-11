# FORK this starter file and save it to your own Repl.it account.


# Declare and initialize the 12 variables here:

date = "Monday 2019-03-18"

time =  "10:05:34 AM"

astronautCount =  7

astronautCount = int(input("Enter the number of astronauts: "))

astronautStatus = "ready"

averageAstronautMassKg = 80.7

crewMassKg = astronautCount * averageAstronautMassKg

fuelMassKg = 760000

shuttleMassKg = 74842.31

totalMassKg = crewMassKg + fuelMassKg + shuttleMassKg

fuelTempCelsius = -225

fuelLevel = 100

weatherStatus = "clear"




# Write code to generate the LC04 report here:
print(
    "-------------------------------------\n" +
"> LC04 - LAUNCH CHECKLIST\n" +
"-------------------------------------\n" +
"Date: " + date + "\n" +
"Time: " + time + "\n\n" +
"-------------------------------------\n" +
"> ASTRONAUT INFO\n" +
"-------------------------------------\n" +
"* count: " + str(astronautCount) + "\n" +
"* status: " + astronautStatus +"\n\n" +
"-------------------------------------\n" +
"> FUEL DATA\n" +
"-------------------------------------\n" +
"* Fuel temp celsius: " + str(-225) + "C\n" +
"* Fuel level: " + str(100) + "%\n\n" +
"-------------------------------------\n" +
"> MASS DATA\n" +
"-------------------------------------\n" +
"* Crew mass: " + str(crewMassKg) + "kg\n" +
"* Fuel mass: " + str(fuelMassKg) + "kg\n" +
"* Shuttle mass: " + str(shuttleMassKg) + "kg\n" +
"* Total mass: " + str(totalMassKg) + "kg\n\n" +
"-------------------------------------\n" +
"> FLIGHT PLAN\n" +
"-------------------------------------\n" +
"* weather: " + weatherStatus + "\n\n" +
"-------------------------------------\n" +
"> OVERALL STATUS\n" +
"-------------------------------------\n" +
"* Clear for takeoff: YES"
)



# When done, have your TA check your code.




# BONUS: Use input to prompt the user to enter the number of astronauts going on the mission.