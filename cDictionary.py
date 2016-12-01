ilename = "continent.txt"

readfile = open(filename, "r")

readlines = readfile.readline()
readlines = readfile.readlines()

cDictionary = {}

for line in readlines :
    Type = line.split(",")
    countryData = Type[0]
    continentData = Type[1]
    cDictionary[countryData] = continentData


# Filter countries by continent
filterContinent = input("Enter the continent you want: ")
for element in cDictionary :
    if filterContinent in cDictionary.get(element) :
        print(element)


readfile.close()
