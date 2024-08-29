import math
import re
import time


def read_file_to_list(filename):
    file_list = []
    with open(filename, 'r') as f:
        for line in f:
            file_list.append(line.strip("\n\r"))
    return file_list


def day8(map_dict, path_list):

    steps = 0
    current_location = 'AAA'
    target_location = 'ZZZ'
    path_list_len = len(path_list)
    print(current_location)

    while current_location != target_location:

        next_move = path_list[steps % path_list_len]
        current_location = map_dict[current_location][next_move]
        steps += 1

    return steps


def day8_part2(map_dict, path_list):

    steps = []
    current_location = []
    # find the start locations and create a list of them for our "ghosts"
    for location in map_dict.keys():
        if location[2] == "A":
            current_location.append(location)
    print("-- Ghost Starts")
    print(current_location)
    path_list_len = len(path_list)

    # for each ghost, find the number of steps in its path
    for ghost in current_location:

        ghost_steps = 0
        while ghost[2] != "Z":
            next_move = path_list[ghost_steps % path_list_len]
            ghost = map_dict[ghost][next_move]
            ghost_steps += 1
        steps.append(ghost_steps)

    # Now find the lowest common multiple
    result = math.lcm(*steps)
    return result


# parse out the file into two parts - the directions and the map
def day8_parser(input_array):

    map_dict = {}
    path_list = [x for x in input_array[0]]

    for line in input_array[2:]:
        location = line.split("=")[0].strip()
        directions = line.split("=")[1].strip()[1:-1].split(",")
        map_dict[location] = {"L": directions[0], "R": directions[1].strip()}

    for i in map_dict.keys():
        print(i, map_dict[i])

    print()

    return map_dict, path_list


def main():
    print("Advent of Code Day 8")
    start = time.time()

    input_array = read_file_to_list("InputFiles/input_day8.txt")

    print("Part 1")
    map_dict, path_list = day8_parser(input_array)
    print(f"Value is: {day8(map_dict, path_list)}")

    # For part 2
    print("\n Part 2")
    print(f"Value is: {day8_part2(map_dict, path_list)}")
    end = time.time()

    print(f"{end-start:.3f} seconds")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
