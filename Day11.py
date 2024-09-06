import time


def read_file_to_list(filename):
    file_list = []
    with open(filename, 'r') as f:
        for line in f:
            file_list.append(line.strip("\n\r"))
    return file_list


def print_map_grid(map_grid):
    for line in map_grid:
        for char in line:
            print(char, end="")
        print("")


def find_galaxies(map_grid):

    # Find all the galaxies in a map_grid
    galaxies = []
    for y, row in enumerate(map_grid):
        for x, item in enumerate(row):
            if item == "#":
                galaxies.append((x, y))
    # Returns a list of tuples with the x/y co-ords of the galaxies in the map grid
    return galaxies


def expand_galaxies(galaxies, age):

    # first find the size of the galaxy by looking for the highest x and y in the galaxies list
    galaxy_width = max([x[0] for x in galaxies])
    galaxy_height = max([x[1] for x in galaxies])

    print(f"Galaxy width {galaxy_width}, Height {galaxy_height}, Age {age}")
    # now go through all the possible rows and columns and work out which ones are empty
    empty_col = []
    for x in range(galaxy_width + 1):
        empty = True
        for galaxy in galaxies:
            if empty and x == galaxy[0]:
                empty = False
        if empty:
            empty_col.append(x)
    print("Empty Columns: ", empty_col)

    empty_row = []
    for y in range(galaxy_height + 1):
        empty = True
        for galaxy in galaxies:
            if empty and y == galaxy[1]:
                empty = False
        if empty:
            empty_row.append(y)
    print("Empty Rows: ", empty_row)

    # Next for each galaxy pair add + age for every row/column less than it
    new_galaxies = []
    for galaxy in galaxies:
        lower_empty_cols = len([x for x in empty_col if x < galaxy[0]])
        lower_empty_rows = len([x for x in empty_row if x < galaxy[1]])
        new_galaxy = (lower_empty_cols * age + galaxy[0], lower_empty_rows * age + galaxy[1])
        new_galaxies.append(new_galaxy)
    print("Expanded Galaxy List: :", new_galaxies)

    return new_galaxies


def expand_map(map_grid, age):

    columns = len(map_grid[0])
    rows = len(map_grid)
    new_map_grid = [[0 for i in range(rows)] for j in range(columns)]
    for y, line in enumerate(map_grid):
        for x, item in enumerate(line):
            new_map_grid[x][y] = item

    # do the inserts
    map_grid = []
    for line in new_map_grid:
        map_grid.append(line)
        if "#" not in line:
            for x in range(age):
                map_grid.append(line)

    return map_grid


def map_distances(galaxy_list):

    total_distance = 0

    # for each galaxy, find its distance from all the other galaxies
    for start in galaxy_list:
        distance = 0
        for destination in galaxy_list:
            distance += abs(start[0] - destination[0]) + abs(start[1] - destination[1])
        total_distance += distance

    return total_distance/2


def day11(map_grid, age):

    galaxies = find_galaxies(map_grid)
    # new version
    galaxies = expand_galaxies(galaxies, age)

    result = map_distances(galaxies)

    return result

# parse out the file into two parts - the directions and the map
def day11_parser(input_array):

    map_grid = []
    for line in input_array:
        map_grid.append([x for x in line])

    return map_grid


def main():
    print("Advent of Code Day 11")
    start = time.time()

    input_array = read_file_to_list("InputFiles/input_day11.txt")

    print("Part 1")
    map_grid = day11_parser(input_array)
    print(f"Value is: {day11(map_grid, 1)}")

    # For part 2
    print("\n Part 2")
    map_grid = day11_parser(input_array)
    print(f"Value is: {day11(map_grid, 999999)}")
    end = time.time()

    print(f"{end-start:.3f} seconds")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
