import country


class Continent:
    def __init__(self, name: str, countries: list[country.Country]):
        self.name = name
        self.countries = countries

    def __str__(self):
        accum = ""
        for c in self.countries:
            accum += str(c) + '\n'
        return accum

    def total_population(self):
        total = 0
        for c in self.countries:
            total += c.population

        return total


def main():
    canada = country.Country('Canada', 34482779, 9984670)
    usa = country.Country('United States of America',
                          313914040, 9826675)
    mexico = country.Country('Mexico', 112336538, 1943950)
    countries = [canada, usa, mexico]
    north_america = Continent('North America', countries)
    print("Continent name:", north_america.name)
    print("Total pop:", north_america.total_population())
    print("\nOutput of print(north_america):")
    print(north_america)


if __name__ == '__main__':
    main()
