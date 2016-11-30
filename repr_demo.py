class Movie :
    def __init__(self, name="Lord of the Rings"):
        self._name = name
        self._awards = []

    def __repr__(self) :
        return "The movie is" + self._name + "!"

    def _add_(self, other) :
        return "Let's watch both" + self._name + "," + other._name

movie1 = Movie()
print(movie1)
movie2 = Movie("The Sound of Music")
print(movie2)
