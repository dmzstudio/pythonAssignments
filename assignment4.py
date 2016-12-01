"""
David Moriarty
CS1026A - Assignment 4
"""

cont_file = "continent.txt"
data_file = "data.txt"


class Country() :

    def __init__(self, name, population, area, continent) :
        self._name = name
        self._population = population
        self._area = area
        self._continent = continent

    def getName(self) :
        return self._name

    def getPopulation(self) :
        return self._population

    def getArea(self) :
        return self._area

    def getContinent(self) :
        return self._continent

    def getPopDensity(self) :
        populationDensity = self._population / self._area
        return populationDensity

    def setPopulation(self, newPop) :
        self._population = newPop

    def __repr__(self) :
        return "%s in %s" % ( (self._name).title(), (self._continent).title() )


class CountryCatalogue() :

    def continent(file) :
        cDictionary = {}
        cont_data = open(cont_file, 'r', encoding='utf-8', errors='ignore')

        readlines = cont_data.readline()
        readlines = cont_data.readlines()

        for line in readlines :
            Type = line.split(",")
            countryData = Type[0]
            continentData = Type[1]
            cDictionary[countryData] = continentData

        cont_data.close()
        return cDictionary

    def data(file) :
        catalogue = {}

        cont_data = open(cont_file, 'r', encoding='utf-8', errors='ignore')
        data = open(data_file, 'r', encoding='utf-8', errors='ignore')

        readlines = cont_data.readline()
        readlines = cont_data.readlines()
        line = data.readline()
        line = data.readlines()

        while line != "" and readlines != "":
            catalogueList = []
            line = line.split("|")
            readlines = readlines.split(",")
            readlines[1] = readlines[1].rstrip("\n")
            line[1] = "".join(line[1].split(","))
            line[2] = "".join(line[2].split(",")).rstrip("\n")
            catalogueList.append(readlines[1])
            catalogueList.append(line[1])
            catalogueList.append(line[2])
            catalogue[line[0]] = catalogueList
            line = data.readlines()
            readlines = cont_data.readlines()

        cont_data.close()
        data.close()
        return catalogue


    def __init__(self, catalogue, cDictionary) :
        self._catalogue =  data(data)
        self._cDictionary = continent(cond_data)


    def addCountry(self, addCountry) :
        addCountryList = []
        addCountryName = input("Enter the country name: ")

        if addCountryName in catalogue :
            print("That country is already in the list.")
            addCountryName = input("Enter the country name: ")
        else :
            addContinentName = input("Enter the continent name: ")
            addPopulationValue = input("Enter the country's population: ")
            addAreaValue = input("Enter the country's area: ")
            addCountryList.append(addContinentName)
            addCountryList.append(addPopulationValue)
            addCountryList.append(addAreaValue)
            catalogue[addCountryName] = addCountryList
            print(addCountryList)
            print()
            print("Successfully added the country.")
            print(addCountryName, catalogue.get(addCountryName))


    def deleteCountry(self) :
        deleteCountryName = input("Enter the country you want to delete: ")
        if deleteCountryName in catalogue :
            del catalogue[deleteCountryName]
            print(deleteCountryName, "was deleted.")
        else :
            print("That country wasn't found.")
            print()


    def findCountry(self) :
        findCountry = input("Enter the country you want to lookup: ")
        if findCountry in catalogue :
            print(catalogue[findCountry])
            print()
        else :
            print("Country not found.")
            print()


    def filterByContinent(self) :
        filterContinent = input("Enter the continent you want: ")
        for element in cDictionary :
            if filterContinent in cDictionary.get(element) :
                print(element)
            else :
                print("There are no contries from that continent.")

    def setPopulationOfCountry(self, newPop) :
        countryName = input("Enter the name of the country: ")
        if countryName in catalogue :
            newPop = input("Enter the updated population: ")
            catalogue[line[1]] = newPop


    # def findCountryWithLargestPop(self) :
    #
    # def findCountryWithSmallestPop(self) :
    #
    # def findMostPopulousContinent(self) :
    #
    # def filterCountriesByPopDensity(self) :
    #
    # def printCountryCatalogue(self) :
    #
    # def saveCountryCatalogue(self, filename) :
