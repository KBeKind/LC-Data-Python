# Assign the variables for exercise 1 here:

engine_indicator_light = "red blinking"

space_suits_on = True

shuttle_cabin_ready = True

crew_status = space_suits_on and shuttle_cabin_ready

computer_status_code = 200

shuttle_speed = 15000

# BEFORE running the code, predict what will be printed to the console by the following statements:

if engine_indicator_light == "green":
    print("engines have started")
elif engine_indicator_light == "green blinking":
    print("engines are preparing to start")
else:
    print("engines are off")

    # 3) Write conditional expressions to satisfy the following safety rules:

    # a) If crew_status is true, print "Crew Ready" else print "Crew Not Ready".

if crew_status:
    print("Crew Ready")
else:
    print("Crew Not Ready")

    # b) If computer_status_code is 200, print "Please stand by. Computer is rebooting." Else if computer_status_code is 400, print "Success! Computer online." Else print "ALERT: Computer offline!"

if computer_status_code == 200:
    print("Please stand by. Computer is rebooting.")
elif computer_status_code == 400:
    print("Success! Computer online.")
else:
    print("ALERT: Computer offline!")

    # c) If shuttle_speed is > 17,500, print "ALERT: Escape velocity reached!" Else if shuttle_speed is < 8000, print "ALERT: Cannot maintain orbit!" Else print "Stable speed".

if shuttle_speed > 17500:
    print("ALERT: Escape velocity reached!")
elif shuttle_speed < 8000:
    print("ALERT: Cannot maintain orbit!")
else:
    print("Stable speed")

# 4) PREDICT: Do the code blocks shown in the Section D produce the same result?

print("Yes")
# print("Yes" or "No")


engine_indicator_light = 'not red blinking'
fuel_level = 18000
engine_temperature = 2500

# 5) Implement the following checks using if/else statements:

# a) If fuel_level is above 20000 AND engine_temperature is at or below 2500, print "Full tank. Engines good."

# b) If fuel_level is above 10000 AND engine_temperature is at or below 2500, print "Fuel level above 50%.  Engines good."

# c) If fuel_level is above 5000 AND engine_temperature is at or below 2500, print "Fuel level above 25%. Engines good."

# d) If fuel_level is at or below 5000 OR engine_temperature is above 2500, print "Check fuel level. Engines running hot."

# e) If fuel_level is below 1000 OR engine_temperature is above 3500 OR engine_indicator_light is red blinking print "ENGINE FAILURE IMMINENT!"

# f) Otherwise, print "Fuel and engine status pending..."

if fuel_level < 1000 or engine_temperature > 3500 or engine_indicator_light == "red blinking":
    print("ENGINE FAILURE IMMINENT!")
elif fuel_level <= 5000 or engine_temperature > 2500:
    print("Check fuel level. Engines running hot.")
elif fuel_level > 20000 and engine_temperature <= 2500:
    print("Full tank. Engines good.")
elif fuel_level > 10000 and engine_temperature <= 2500:
    print("Fuel level above 50%. Engines good.")
elif fuel_level > 5000 and engine_temperature <= 2500:
    print("Fuel level above 25%. Engines good.")
else:
    print("Fuel and engine status pending...")

# 6) a) Create the variable command_override, and set it to be true or false. If command_override is false, then the shuttle should only launch if the fuel and engine check are OK. If command_override is true, then the shuttle will launch regardless of the fuel and engine status.

command_override = True

# 6) b) Code the following if/else check:

# If fuel_level is above 20000 AND engine_indicator_light is NOT red blinking OR command_override is true print "Cleared to launch!" Else print "Launch scrubbed!"

if (fuel_level > 20000 and engine_indicator_light != "red blinking") or command_override:
    print("Cleared to launch!")
else:
    print("Launch scrubbed!")
