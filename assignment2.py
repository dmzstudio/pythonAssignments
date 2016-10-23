"""
Created by: David Moriarty
COMPSCI 1026A 003
CS1026: Assignment 2
"""

import math
import os

## This program reads geometrical shape names input by the user, and calculates the volume of those shapes.
## This program is able to calculate the volume of three geometrical shapes: Cubes, Pyramids, and Ellipsoids.
## The program will keep asking for more shapes until the user enters the sentinnel value 'quit'.
## Once 'quit' is entered, it will display a the list of volumes that were calculated, unless the user didn't perform any calculations.


# Information panel at top of the program.
print()
print('.'*60)
print()
print("This program calculates the volume of 3D shapes.")
print("Enter 'QUIT' to stop the program.")
print()
print('.'*60)
print()

# Lists for each of the shapes.
cubeVolumeList = []
pyramidVolumeList = []
ellipsoidVolumeList = []
count = 0

# Function to clear the screen.
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Function to calculate the volume of cubes.
def cubeVolume():
    print()
    print("Enter the side length of the cube: ")
    sideLength = int(input("> "))
    cube_volume = (sideLength**3)
    return cube_volume, sideLength

# Function to calculate the volume of pyramids.
def pyramidVolume():
    print()
    print("Enter the base length of the pyramid: ")
    pyramidBase = int(input("> "))
    print("Enter the height of the pyramid: ")
    pyramidHeight = int(input("> "))
    pyramid_volume = (1/3 * pyramidBase ** 2 * pyramidHeight)
    return pyramid_volume, pyramidBase, pyramidHeight

# Function to calculate the volume of ellipsoids.
def ellipsoidVolume():
    print()
    print("Enter the first radius of the ellipsoid: ")
    radius1 = int(input("> "))
    print()
    print("Enter the second radius of the ellipsoid: ")
    radius2 = int(input("> "))
    print()
    print("Enter the third radius of the ellipsoid: ")
    radius3 = int(input("> "))
    ellipsoid_volume = (4/3 * math.pi * radius1 * radius2 * radius3)
    ellipsoid_volume = round(ellipsoid_volume, 2)
    return ellipsoid_volume, radius1, radius2, radius3

# Function that displays all the volumes stored in their lists.
def volumeListDisplay(cubesVolumeList, pyramidVolumeList, ellipsoidVolumeList):

    print("You calculated {} cube(s).".format(len(cubesVolumeList)))
    print("Cubes: ", ", ".join(map(str, cubesVolumeList)))
    print()

    print("You calculated {} pyramid volume(s).".format(len(pyramidVolumeList)))
    print("Pyramids: ", ", ".join(map(str, pyramidVolumeList)))
    print()

    print("You calculated {} ellipsoid volume(s).".format(len(ellipsoidVolumeList)))
    print("Ellipsoids: ", ", ".join(map(str, ellipsoidVolumeList)))
    print()


def shapeInput():
    print("Enter the shape you would like to calculate the volume for: cube, pyramid, ellipsoid, or enter 'quit' to exit the program: ")
    print()
    shapeInput = input("> ").lower()
    return shapeInput


# While loop that keeps asking for user input until they enter 'quit'.
quit = False
while quit == False:
    # The conditional statements detect which shape is entered.
    userInput = shapeInput()

    # If the incorrect shape is entered, it will continue asking for a user to enter a shape.
    if userInput != "cube" and userInput != "pyramid" and userInput != "ellipsoid" and userInput != "quit":
        userInput = shapeInput()


    # If the shape entered is one of the right shapes, it detects which shape is entered and calls the right function to ask for the needed values to calculate the volume of that shape, and then stores the volume in the right list.

    if userInput== "cube":
        cube_volume, sideLength = cubeVolume()
        cubeVolumeList.append(cube_volume)
        print("The volume of a cube with a side length of %s is %s:" % (sideLength, cube_volume))

    elif userInput == "pyramid":
        pyramid_volume, pyramidBase, pyramidHeight = pyramidVolume()
        pyramidVolumeList.append(pyramid_volume)
        print("The volume of a pyramid with a base of %s and a height of %s is %s:" % (pyramidBase, pyramidHeight, pyramid_volume))

    elif userInput == "ellipsoid":
        ellipsoid_volume, radius1, radius2, radius3 = ellipsoidVolume()
        ellipsoidVolumeList.append(ellipsoid_volume)
        print("The volume of an ellipsoid with radii %s, %s, and %s is %s:" % (radius1, radius2, radius3, ellipsoid_volume))

    # If the sentinnel 'quit' is entered, it will exit the program.
    if userInput == "quit":
        clear()
        count = count -1

        # Prints a notice that the user has exited the program.
        print("-"*60)
        print()
        print("You have come to the end of your session.")
        print()
        print("-"*60)
        print()

        quit = True

    count = count + 1


# If the user didn't perform any volume calculations.
if count == 0:
    print("You didn't perform any calculations.")
    print()

# If the user performed volume calculations, it will display all the volumes calculated by shape.
else:
    print("The volumes you calculated for each shape in this session were:")
    print()
    volumeListDisplay(cubeVolumeList, pyramidVolumeList, ellipsoidVolumeList)
