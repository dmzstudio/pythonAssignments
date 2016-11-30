infile = open("data.txt", "r")
continentfile = open("continent.txt", "r")

catalogue = dict()

line = infile.readline()
line = infile.readline()

continentline = continentfile.readline()
continentline = continentfile.readline()

while line != "" and continentline != "":
    value_list = []
    line = line.split("|")
    continentline = continentline.split(",")
    continentline[1] = continentline[1].rstrip("\n")
    line[1] = "".join(line[1].split(","))
    line[2] = "".join(line[2].split(",")).rstrip("\n")
    value_list.append(continentline[1])
    value_list.append(line[1])
    value_list.append(line[2])
    catalogue[line[0]] = value_list
    line = infile.readline()
    continentline = continentfile.readline()

for el in catalogue:
    print(el)
print()

addCountryList = list()
print("Add a country")
addCountryName = input("Enter the country name: ")
if addCountryName in catalogue:
    print("Sorry, that country is already in the list.")
else:
    addContinentName = input("Enter the continent name: ")
    addPopulationValue = input("Enter the country's population: ")
    addAreaValue = input("Enter the country's area: ")
    addCountryList.append(addContinentName)
    addCountryList.append(addPopulationValue)
    addCountryList.append(addAreaValue)
    catalogue[addCountryName] = addCountryList
    print(addCountryList)
    print()
    print("Adding the country was successful!")
    print(addCountryName, catalogue.get(addCountryName))

print()
for el in catalogue:
    print(el)
print()


# Delete a country
print()
deleteCountryName = input("Enter the country you want to delete: ")
if deleteCountryName in catalogue :
    del catalogue[deleteCountryName]
    print(deleteCountryName, "was deleted.")
else :
    print("That country wasn't found on the list.")
    print()

# Find a country
print()
findCountry = input("Enter the country to search: ")
if findCountry in catalogue :
    print(catalogue[findCountry])
    print()
else :
    print("Country not found.")
    print()


# Filter countries by continent
print()
findContinent = input("Enter the continent you want: ")
if findContinent in catalogue.values():
    print(key)


print()
print(catalogue)


# setPopulationOfASelectedCountry
countryName = input("Enter name of country: ")
if countryName in catalogue:
    newPop = input("Enter the new population: ")


# findCountryWithLargestPop


# findCountryWithSmallestPop


# 
