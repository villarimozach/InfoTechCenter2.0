# Code Name - Hornet


#Import Libraries Here
#Print to one line with time delay between prints
from time import sleep
import random


#Welcome Branch
print("\033[1;34m Welcome To InfoTechCenter  \n")
sleep(1)
print("\033[1;34m Hornet's Operating System Booting Up  \n")


#Gas Branch

# Gas Level Function
sleep(1)
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Haft Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    #print(currentGasLevel)
    return currentGasLevel

# Variable calls the value of gasLevelGauge Function
gasLevelIndicator = gasLevelGauge()

# Create If-ELIF-ELSE statements using the comparative Operator == Equal to in order to display gas level messages to display gas level messages
def gasLevelAlert():
    gasStations = ["Shell","BP","Citgo","Circle K","Mobil","Speedway","Marathon","Love's","Meijer","Costco","Sunoco"]
    miles = round(random.uniform(1,25), 1)
    if gasLevelIndicator == "Empty":
        print("***WARNING***\nYOU ARE ON EMPTY!!!\nCalling Emergency Contact")
    elif gasLevelIndicator == "Low":
        print("***WARNING***\nYour gas tank is extremely LOW\nThe closest gasoline station is " + random.choice(gasStations) + " which is " + str(miles) + " miles away!!!")
    elif gasLevelIndicator == "Quarter Tank":
        print("You are on a QUARTER TANK of gas\nStart planing a visit to the gas station!!!")
    elif gasLevelIndicator == "Haft Tank":
        print("You are on a HAFT TANK of gas\nYou have 125 more miles to empty!!!")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("You are on a THREE QUARTER TANK of gas\nYou have 205 more miles to empty!!!")
    else:
        print("You have a FULL TANK of gas, Congratulations.\nYou have 310 more miles to empty!!!")


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

 # Call Functions Here
gasLevelGauge()
gasLevelAlert()
vehicleResponceSystem()

