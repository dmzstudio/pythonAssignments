data_file = open("data.txt", "r")
cont_file = open("continent.txt", "r")

cDictionary = dict()
catalogue = dict()

data_lines = data_file.readline()
data_lines = data_file.readlines()

cont_lines = cont_file.readline()
cont_lines = cont_file.readlines()

for line in cont_lines:
    Type = line.split(",")
    countryData = Type[0]
    continentData = Type[1]
    cDictionary[countryData] = continentData
    cont_lines = cont_file.readlines()


for line in data_lines :
    for line in cont_lines :
        catalogueList = []

        Type = line.split("|")
        countryData = Type[0]
        popData = Type[1]
        areaData = Type[2]

        Type = line.split(",")
        continentData = Type[1]

        line[1] = "".join(line[1].split(","))
        line[2] = "".join(line[2].split(",")).rstrip("\n")

        catalogueList.append(continentData)
        catalogueList.append(popData)
        catalogueList.append(areaData)

        catalogue[countryData] = catalogueList


print()
for el in catalogue:
    print(el)
print()

addCountryList = []
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
for element in catalogue:
    if findContinent in catalogue.get(element):
        print (element.key())

print()
print(catalogue)


# setPopulationOfASelectedCountry
countryName = input("Enter name of country: ")
if countryName in catalogue:
    newPop = input("Enter the new population: ")
