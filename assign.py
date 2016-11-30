"""
David Moriarty
CS1026A - Assignment 4
"""

CONTINENTDATA = 'continent.txt'
DATA = 'data.txt'

class Country :

    def __init__(self, name, population, area, continent) :
        self._name = name
        self._population = population
        self._area = area
        self._continent = continent

    def __repr__(self) :
        return "self._name + self._continent"

    def setPopulation(self, newPop) :
        self._population = newPop

    def getName(self) :
        return self._name

    def getArea(self) :
        return self._area

    def getPopulation(self) :
        return self._population

    def getContinent(self) :
        return self._continent

    def getPopDensity(self) :
        return self._population / self._area



class CountryCatalogue :

    def __init__(self, filename) :
        cDictionary = {}
        self._filename = INFILE = open('continent.txt', encoding='utf-8', "r", errors='ignore')
        for line in INFILE:
            data = line.split(",")
            cDictionary[data[0]] = data[1].rstrip()

    def filterCountriesByContinent(self) :


    def printCountryCatalogue(self) :


    def findCountry(self) :


    def deleteCountry(self) :


    def addCountry(self, newCountry) :
        self._newCountry = input(newCountry)


    def setPopulationOfASelectedCountry(self) :


    def saveCountryCatalogue(self, filename) :


    def findCountryWithLargestPop(self) :


    def findCountryWithSmallestPop(self) :


    def findMostPopulousContinent(self) :


    def filterCountriesByPopDensity(self) :
