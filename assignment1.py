"""
Created by: David Moriarty
COMPSCI 1026A 003
CS1026: Assignment 2
"""

## This is a program for a car rental company.
# It prompts each user to input a list of information, and then processes
# the information and displays the results.
# It then computes the amount owing from the data requested from the user.


# Import modules
from sys import exit
import os


# Instructions for user.
print()
print("*"*46)
print()
print(" "*5, "Welcome! Please fill out this form!", " "*5)
print()
print("*"*46)
print()


# Input for name of user, capitalizes first and last name.
name = input("Enter your full name: ").title()
print()

# Input for age of user.
age = int(input("Enter your age: "))

# Classification code name and code.
bName = "Budget"
bCode = "[ B ]"
dName = "Daily"
dCode = "[ D ]"
wName = "Weekly"
wCode = "[ W ]"


# Titles
nameTitle = "Name: "
ageTitle = "Age: "
codeTitle = "Classification Code: "
numOfDaysTitle = "Number of Days Rented: "
startOdometerTitle = "Start Odometer Reading: "
finalOdometerTitle = "Final Odometer Reading: "
kmDrivenTitle = "Kilometers Driven: "


# Display the three classification codes.
print()
print("Classification codes")
print("-"*46)
print("%-37s %6s" % (bName, bCode))
print("%-37s %6s" % (dName, dCode))
print("%-37s %6s" % (wName, wCode))
print("-"*46)
print()

# Input for classification code. Converts lowercase input to uppercase.
classCode = input("Enter the classification code: ").upper()
print()

# Check for invalid classification code entry.
if not (classCode == "B" or classCode == "D" or classCode == "W"):
    # Display error message, invalid code, customer name, and age.
    print("Error: Invalid classification code [", classCode, "] was entered.")
    print()
    print("%-8s %20s" % (nameTitle, name))
    print()
    print("%-8s %20.0f" % (ageTitle, age))
    print()

    # Exit program.
    exit(0)
print()

# Input for number of days of rental term.
numOfDays = int(input("Enter how many days you want the car for: "))
print()

# Input for starting odometer reading.
startOdometer = int(input("Enter the initial odometer reading: "))
print()

# Input for final odometer reading.
finalOdometer = int(input("Enter the final odometer reading: "))

# After all inputs are submitted, this clears the screen.
os.system('cls' if os.name == 'nt' else 'clear')

# Thank you message.
print()
print("*"*46)
print(" "*15, "Thank you!", " "*15)
print("*"*46)
print()

# CONSTANTS
WEEK = (numOfDays // 7) + 1
KM_DRIVEN = finalOdometer - startOdometer
AVG_KM_DAY = (KM_DRIVEN / numOfDays)
AVG_KM_WEEK = (KM_DRIVEN / WEEK)
YOUNG_DRIVER_SURCHARGE = (numOfDays * 10)
BUDGET_BASE_CHARGE = (20 * numOfDays)
BUDGET_KM_CHARGE = KM_DRIVEN * 0.30
DAY_BASE_CHARGE = (50 * numOfDays)
DAY_KM_SURCHARGE = (KM_DRIVEN - 100*numOfDays) * 0.30
WEEK_BASE_CHARGE = (200 * WEEK)
WEEK_KM_SURCHARGE_A = (50 * WEEK)
WEEK_KM_SURCHARGE_B = (100 * WEEK)
WEEK_KM_OVER_2000 = (KM_DRIVEN - 2000*WEEK) * 0.30

# Process customer information and display results.
print()
print("-"*46)
print("Customer information")
print("-"*46)
print()

print("%-22s %20s" % (nameTitle, name))
print("%-36s %6.0f" % (ageTitle, age))
print("%-36s %6s" % (codeTitle, classCode))
print("%-36s %6.0f" % (numOfDaysTitle, numOfDays))
print("%-36s %6.0f" % (startOdometerTitle, startOdometer))
print("%-36s %6.0f" % (finalOdometerTitle, finalOdometer))
print("%-36s %6.0f" % (kmDrivenTitle, KM_DRIVEN))
print()


# Title for list of charges.
print()
print("-"*46)
print("List of charges")
print("-"*46)
print()


# Conditional statement that computes what to charge the customer based on:
# 1. If the user is under 25, it adds the young driver surcharge.
# 2. Which code they select.
# 3. Number of days of the rental term.
# 4. Start odometer reading.
# 5. Final odometer reading.
# 6. It calculates the total km driver, then calculates the km surcharge.
# 7. Calculates the total charges.

# If driver under 25, it adds the surcharge to the charges printout.
if age < 25 :
    if classCode == "B" or classCode == "D" or classCode == "W" :
        youngDriverSurchargeTitle = "Young Driver Surcharge: "
        print("%-36s $%6.2f" % (youngDriverSurchargeTitle, YOUNG_DRIVER_SURCHARGE))

# 1: Code 'B' (Budget)
if classCode == "B" :
    # a. base charge: $20.00/day
    budgetBaseChargeTitle = "Base Charge: "
    print("%-36s $%6.2f" % (budgetBaseChargeTitle, BUDGET_BASE_CHARGE))

    # b. km charge: $0.30/km
    budgetKmChargeTitle = "Extra Km Surcharge: "
    print("%-36s $%6.2f" % (budgetKmChargeTitle, BUDGET_KM_CHARGE))

    print()

    # c. total charges
    if age < 25 :
        budgetTotalCharge = (YOUNG_DRIVER_SURCHARGE + BUDGET_BASE_CHARGE + BUDGET_KM_CHARGE)
    else :
        budgetTotalCharge = (BUDGET_BASE_CHARGE +  BUDGET_KM_CHARGE)

    budgetTotalChargeTitle = "Total Charges: "
    print("%-36s $%6.2f" % (budgetTotalChargeTitle, budgetTotalCharge))

# 2: Code 'D' (Daily)
elif classCode == "D" :
    # a. base charge: $50.00/day
    dailyBaseChargeTitle = "Base Daily Charge: "
    print("%-36s $%6.2f" % (dailyBaseChargeTitle, DAY_BASE_CHARGE))

    # b. kms charge: if <= 100km = $0
    if AVG_KM_DAY <= 100 :
        dailyKmCharge = 0
    # else = $0.30/km
    elif AVG_KM_DAY >= 100 :
        dailyKmCharge = DAY_KM_SURCHARGE

    dailyKmChargeTitle = "Extra Km Surcharge: "
    print("%-36s $%6.2f" % (dailyKmChargeTitle, dailyKmCharge))

    print()

    # c. total charges
    if age < 25 :
        dailyTotalCharge = (YOUNG_DRIVER_SURCHARGE + DAY_BASE_CHARGE + dailyKmCharge)
    else :
        dailyTotalCharge = (DAY_BASE_CHARGE + dailyKmCharge)

    dailyTotalChargeTitle = "Total Charges: "
    print("%-36s $%6.2f" % (dailyTotalChargeTitle, dailyTotalCharge))

# 3: Code 'W' (weekly)
elif classCode == "W" :
    # a. base charge: $200.00/week or fraction of a week
    weekBaseChargeTitle = "Base Weekly Charge: "
    print("%-36s $%6.2f" % (weekBaseChargeTitle, WEEK_BASE_CHARGE))

    # b. km surcharge:
    # if avg km/wk <= 1000 = $0
    if AVG_KM_WEEK <= 1000 :
        weeklyKmCharge = 0

    # if avg km/wk > 1000 and < 2000 = $50/wk
    elif AVG_KM_WEEK > 1000 and AVG_KM_WEEK < 2000 :
        weeklyKmCharge = WEEK_KM_SURCHARGE_A

    # if avg km/wk > 2000/wk = $100/wk + $0.30/km over the 2000 km/wk.
    elif AVG_KM_WEEK >= 2000 :
        weeklyKmCharge = (WEEK_KM_SURCHARGE_B + WEEK_KM_OVER_2000)

    # weekly km surcharge
    weekKmTitle = "Extra Km Surcharge: "
    print("%-36s $%6.2f" % (weekKmTitle, weeklyKmCharge))

    print()

    # c. total charges
    if age < 25 :
        weeklyTotalCharge = (YOUNG_DRIVER_SURCHARGE + WEEK_BASE_CHARGE + weeklyKmCharge)
    else :
        weeklyTotalCharge = (WEEK_BASE_CHARGE + weeklyKmCharge)

    weekTotalTitle = "Total Charges: "
    print("%-36s $%6.2f" % (weekTotalTitle, weeklyTotalCharge))
