# Eliya Statema
# 3/6/25
# Population

def main():
    data = []
    while True:
        add_more = input("Add state data (y/n)? ")
        if add_more == "y":
            year = int(input("Enter the year: "))
            state = input("Enter the state name: ")
            population = int(input("Enter the population: "))
            data.append([year, state, population])
        else:
            break

    target_year = int(input("Enter the year to calculate population for: "))
    total_population = sum_population_for_year(data, target_year)
    print(f"The total population for the year {target_year} is {total_population}.")

def sum_population_for_year(data, target_year):
    total_population = 0
    for year in data:
        if year[0] == target_year:
             total_population += year[2]
    return total_population

if __name__ == '__main__':
    main()