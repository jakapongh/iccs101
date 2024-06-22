from __future__ import annotations

class Country:
    def __init__(self, name: str, population: int, area: int):
        self.name = name
        self.population = population
        self.area = area

    def __str__(self):
        return f"{self.name} has a population of {str(self.population)} and is {str(self.area)} km^2"

    def __repr__(self):
        return f"Country(name={self.name}, population={self.population}, area={self.area})"

    def is_larger(self, country: Country):
        # Check that the country passed is actually of type Country
        if not isinstance(country, Country):
            raise TypeError('country is not a country')

        return self.area > country.area

    def population_density(self):
        # people per area
        return self.population / self.area


canada = Country('Canada', 34482779, 9984670)
usa = Country('United States of America', 313914040, 9826675)
print(canada.is_larger(usa))
print(canada.population_density())
print(canada)
print([canada])

