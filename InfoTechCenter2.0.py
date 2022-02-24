import random

# Weather Branch

def weather():
    weatherForecast = ["Icy","Snowy","Raining","Windy","Foggy","Sunny"]
    weatherConditions = random.choice(weatherForecast)
    return weatherConditions

# Calling weather Function to determine weather
weatherAlert = weather()

def vehicleResponceSystem():
    if weatherAlert == "Icy":
        print("\nVRS has changed your alarm 30 minutes earlier based on the NWS forecast of",weatherAlert)
        print("Your VRS will only allow your car to go 30MPH")
    elif weatherAlert == "Snowy":
        print("\nVRS has changed your alarm 15 minutes earlier based on the NWS forecast of",weatherAlert)
        print("Your VSR will only allow you car to go 50MPH")
    elif weatherAlert == "Raining":
        print("\nVRS has changed your alarm 5 minutes earlier based on the NWS forecast of",weatherAlert)
        print("Your VRS will only allow your car to go 60MPH")
    elif weatherAlert == "Windy":
        print("\nVRS has changed your alarm 5 minutes earlier based on the NWS forecast of",weatherAlert)
        print("Your VRS will only allow your car to go 70MPH")
    elif weatherAlert == "Foggy":
        print("\nVRS has changed your alarm 5 minutes earlier based on the NWS forecast of",weatherAlert)
        print("Your VRS will only allow your car to go 60MPH")
    else:
        print("\nVRS has changed your alarm 0 minutes earlier based on the NWS forecast of",weatherAlert)
        print("Your VRS will allow your car to go 100MPH")
vehicleResponceSystem()