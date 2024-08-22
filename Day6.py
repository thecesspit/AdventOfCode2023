import re
import time


def read_file_to_list(filename):
    file_list = []
    with open(filename, 'r') as f:
        for line in f:
            file_list.append(line.strip("\n\r"))
    return file_list


def day6(boat_list):

    result = 1
    print(boat_list)
    winners = []
    for boat in boat_list:
        winner = 0
        t = boat['time']
        d = boat['distance']
        for x in range(t):
            speed = x
            my_distance = speed * (t - x)
            if my_distance > d:
                winner += 1
        winners.append(winner)
    print(winners)

    for i in winners:
        result = result * i

    return result


def day6_part2(input_array):

    result = 0

    return result


def day6_parser(input_array):

    boat_list = []
    # Read in the Boats and time for each race
    boat = 0
    for item in input_array[0].split(" ")[1:]:
        if item:
            boat_list.append({'boat': boat, 'time': int(item)})
            boat += 1
    boat = 0

    # read in the distance record for each race
    for item in input_array[1].split(" ")[1:]:
        if item:
            boat_list[boat]['distance'] = int(item)
            boat += 1

    return boat_list


def main():
    print("Advent of Code Day 6")

    start = time.time()



    print("Part 1")
    input_array = read_file_to_list("InputFiles/input_day6.txt")
    boat_list = day6_parser(input_array)
    print(f"Value is: {day6(boat_list)}")


    # For part 2
    print("\n Part 2")
    input_array_2 = read_file_to_list("InputFiles/input_day6_part2.txt")
    boat_list_2 = day6_parser(input_array_2)
    print(f"Value is: {day6(boat_list_2)}")
    end = time.time()

    print(f"{end-start:.3f} seconds")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
