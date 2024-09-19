import time


def read_file_to_list(filename):
    file_list = []
    with open(filename, 'r') as f:
        for line in f:
            file_list.append(line.strip("\n\r"))
    return file_list


# parse out the file into a list of codes to has
def day18_parser(input_array):
    dig_list = []
    for line in input_array:
        parts = line.split(" ")
        dig_list.append({'direction': parts[0],
                         'distance': int(parts[1]),
                         'colour': parts[2].strip("()")})
    return dig_list


def print_trench(trench_list, just_size=False):
    trench_size = 0
    for row in trench_list:
        for item in row:
            if not just_size:
                print(item, end="")
        trench_size += len([x for x in row if x == "#"])
        if not just_size:
            print("\n", end="")

    return trench_size


# dig the trench, but record this time as a series of co-ords
def dig_trench_points(dig_list):

    current_x = 2
    current_y = 2
    trench_points = [(current_x, current_y)]
    perimeter = 0

    for dig in dig_list:
        if dig['direction'] == 'U':
            current_y += dig['distance']
        if dig['direction'] == 'D':
            current_y -= dig['distance']
        if dig['direction'] == 'L':
            current_x -= dig['distance']
        if dig['direction'] == 'R':
            current_x += dig['distance']
        trench_points.append((current_x, current_y))
        perimeter += dig['distance']
    # then put the last point onto the list

    return trench_points, perimeter


def shoelace_trench_size(trench_points, perimeter):
    result = 0

    # for each point the area is based on the the current point and the next point - (x1*y2 - y1*x2)
    # see: https://en.wikipedia.org/wiki/Shoelace_formula
    for i in range(len(trench_points)-1):
        x1 = trench_points[i][0]
        y1 = trench_points[i][1]
        x2 = trench_points[i+1][0]
        y2 = trench_points[i+1][1]
        result += (x1 * y2) - (y1 * x2)
    # total size is this calculated value divided by 2 PLUS the perimeter divided by two (as the points are centred in the vector).
    # there's +2 to the perimter needed, but not sure why....
    result = abs(result)/2 + (perimeter+2) / 2
    return result


def dig_trench(trench_list, dig_list, start_x, start_y):
    current_x = start_x
    current_y = start_y

    # now for each row in the digging list, dig out our trench
    for instruction in dig_list:

        # Dig Right
        if instruction["direction"] == "R":
            right_gap = (current_x + 1) - len(trench_list[0]) + instruction["distance"]
            # if overflowing the grid to the right, add extra columns
            if right_gap > 0:
                for row in trench_list:
                    for x in range(right_gap + 1):
                        row.append(".")
            # then dig right
            for excavation in range(instruction["distance"]):
                trench_list[current_y][current_x + excavation + 1] = "#"
            current_x += instruction["distance"]

        # Dig Left
        if instruction["direction"] == "L":
            # if overflowing the grid to the left, add extra columns
            left_gap = instruction["distance"] - current_x
            if left_gap > 0:
                for row in trench_list:
                    for x in range(left_gap):
                        row.insert(0, ".")
                current_x += left_gap
            # then dig left
            for excavation in range(instruction["distance"]):
                trench_list[current_y][current_x - excavation - 1] = "#"
            current_x -= instruction["distance"]

        # Dig Down
        if instruction["direction"] == "D":
            down_gap = (current_y + 1) - len(trench_list) + instruction["distance"]
            # if overflowing the grid downwards, add extra rows
            if down_gap > 0:
                for i in range(down_gap):
                    new_row = ["." for x in range(len(trench_list[0]))]
                    trench_list.append(new_row)
            # then dig down
            # print_trench(trench_list)
            for excavation in range(instruction["distance"]):
                trench_list[current_y + excavation + 1][current_x] = "#"
            current_y += instruction["distance"]

        # Dig Up
        if instruction["direction"] == "U":
            up_gap = instruction["distance"] - current_y
            # if overflowing the grid upwards, add extra rows
            if up_gap > 0:
                for i in range(up_gap):
                    new_row = ["." for x in range(len(trench_list[0]))]
                    trench_list.insert(0, new_row)
                current_y = current_y + up_gap
            # then dig up
            for excavation in range(instruction["distance"]):
                trench_list[current_y - excavation - 1][current_x] = "#"
            current_y -= instruction["distance"]
    return trench_list


def outfill_trench(trench_list):
    filled = False
    while not filled:
        # assume filled in until we start finding edges
        filled = True
        # any space in side the trench needs to be filled in
        for y in range(len(trench_list)):
            # first, lets fill in the bit definitely outside - the . at start and end of the row with "*"'s
            # any more *'s found after a start are also outside so we can fill in trailing ... there to.
            start, end = True, True
            for x in range(len(trench_list[0])):
                start_cell = trench_list[y][x]
                end_cell = trench_list[y][-(x + 1)]
                if start_cell == "#":
                    start = False
                if start_cell == "*":
                    start = True
                if start_cell == "." and start:
                    trench_list[y][x] = "*"
                    filled = False
                if end_cell == "#":
                    end = False
                if end_cell == "*":
                    end = True
                if end_cell == "." and end:
                    trench_list[y][-(x + 1)] = "*"
                    filled = False
        # repeat column by column
        for x in range(len(trench_list[0])):
            # first, lets fill in the bit definitely outside - the . at start and end of the row with "*"'s
            start, end = True, True
            for y in range(len(trench_list)):
                start_cell = trench_list[y][x]
                end_cell = trench_list[-(y + 1)][x]
                if start_cell == "#":
                    start = False
                if start_cell == "*":
                    start = True
                if start_cell == "." and start:
                    trench_list[y][x] = "*"
                    filled = False
                if end_cell == "#":
                    end = False
                if end_cell == "*":
                    end = True
                if end_cell == "." and end:
                    trench_list[-(y + 1)][x] = "*"
                    filled = False
    return trench_list


def infill_trench(trench_list):
    # for every ., replace with #
    for y in range(len(trench_list)):
        for x in range(len(trench_list[0])):
            if trench_list[y][x] == ".":
                trench_list[y][x] = "#"
    return trench_list


def day18(dig_list, just_size=False):
    lava_capacity = 0
    # first create a small grid to work from, with [y][x] co-ordinates
    trench_list = [["." for x in range(6)] for y in range(6)]
    # start our dig at 2,2
    current_x = 2
    current_y = 2
    trench_list[current_y][current_x] = "#"

    # now dig the trench based on the instructions
    trench_list = dig_trench(trench_list, dig_list, current_x, current_y)
    print_trench(trench_list, just_size)

    # now infill the trench with lava
    trench_list = outfill_trench(trench_list)
    trench_list = infill_trench(trench_list)
    lava_capacity = print_trench(trench_list, just_size)
    print(f"Trench Size is {lava_capacity}\n")

    return lava_capacity


def colour_convert(dig_list):
    direction_list = "RDLU"
    for idx, instruction in enumerate(dig_list):
        dig_list[idx]["distance"] = int(dig_list[idx]["colour"][1:-1], 16)
        dig_list[idx]["direction"] = direction_list[int(dig_list[idx]["colour"][-1])]
    return dig_list


def main():
    print("Advent of Code Day 18")
    start = time.time()

    input_array = read_file_to_list("InputFiles/input_day18.txt")

    print("Part 1")
    dig_list = day18_parser(input_array)
    print(f"Calculated with grid Value is: {day18(dig_list, False)}")

    trench_points, perimeter = dig_trench_points(dig_list)
    print(f"Calculated with points: {shoelace_trench_size(trench_points, perimeter)}")

    print("Part 2")
    big_dig_list = colour_convert(dig_list)
    trench_points_colour, perimeter = dig_trench_points(big_dig_list)
    print(f"Value is: {shoelace_trench_size(trench_points_colour, perimeter)}")
    end = time.time()

    print(f"{end - start:.3f} seconds")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
