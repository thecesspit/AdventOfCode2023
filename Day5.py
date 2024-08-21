import re
import time

def read_file_to_list(filename):
    file_list = []
    with open(filename, 'r') as f:
        for line in f:
            file_list.append(line.strip("\n\r"))
    return file_list

def day5_parser(input_array):

    card_dict = {}
    # Parse the file line by line
    for line in input_array:
        card_key = line.split(":")[0]
        card_winners = line.split(":")[1].split("|")[0].split(" ")
        card_numbers = line.split(":")[1].split("|")[1].split(" ")
        card_winners = [x for x in card_winners if x != ""]
        card_numbers = [x for x in card_numbers if x != ""]
        card_dict[card_key] = {"winners": card_winners, "numbers": card_numbers}
    return card_dict

def day5_parser(input_array):

    new_map = {}
    # split out the seed list from top of the file
    seed_line = input_array.pop(0)
    seed_list = []
    for seed in seed_line.split(" ")[1:]:
        seed_list.append(int(seed))
    # parse the rest of the file into maps
    map_name = "blank"
    map_values = []
    for line in input_array:
        # if blank line, write out our current map
        if line == "" and map_name != "blank":
            new_map[map_name] = [x for x in map_values if x]
            map_values = []
        # if line contains word map, start building the next map
        if line.find("map") > 0:
            map_name = line.split(" ")[0]
        else:
            values = line.split(" ")
            map_values.append([int(x) for x in values if x != ""])
    new_map[map_name] = [x for x in map_values if x]

    return seed_list, new_map

def seed_map_lookup(seed_map, value):
    # seed map is of form (range(start, end), change) - e.g ((50,98),2) => 51 -> 53
    destination = -1
    for item in seed_map:
        if value in seed_map[item][0]:
            destination = value + seed_map[item][1]
    if destination == -1:
        destination = value
    return destination


def day5(seed_list, seed_map):
    # Take a list of seeds and converted them through each level of the map to get the final location

    location_list = []
    for seed in seed_list:
        result_seed = seed
        seed_transforms = []
        for level in seed_map:
            for transform in level:
                if result_seed in transform[0]:
                    result_seed = result_seed + transform[1]
                    seed_transforms.append(result_seed)
                    break
        location_list.append(result_seed)
    return min(location_list)


def day5_part2(seed_list, seed_map):

    # for each pair in the seed_list create a temp seed list to pass back into day 5; and get the lowest location
    # then find the lowest location for all lowest

    location_list = []

    seed_pairs = int(len(seed_list)/2)
    for x in range(seed_pairs):
        seed_range = seed_list[x*2 + 1]
        seed_start = seed_list[x*2]
        print(f"Processing {seed_start} over {seed_range}")
        for seed in range(seed_start, seed_range):
            True
    return (location_list)


def seed_map_convertor(seed_map):
    # converts a seed map into a range / change
    new_seed_map = []
    for i in seed_map:
        new_list = []
        for item in seed_map[i]:
            # Python ranges don't include the last number
            new_list.append([range(item[1], item[1] + item[2]), item[0] - item[1]])
        new_seed_map.append(new_list)

    return new_seed_map


def main():
    print("Advent of Code Day 5")

    start = time.time()
    input_array = read_file_to_list("InputFiles/input_day5.txt")
    # input_array = read_file_to_list("InputFiles/input_day5_test.txt")

    print("Part 1")
    seed_list, parsed_map = day5_parser(input_array)
    converted_map = seed_map_convertor(parsed_map)
    # create an ugly list
    print("Seed List")
    print(seed_list)
    print("\n Seed/Location Map")
    for value, item in enumerate(converted_map):
        print(value, item)
    print(f"Minimum Location is: {day5(seed_list, converted_map)}")
    print("\n Part 2")
    print(f"Minimum Location is: {day5_part2(seed_list, parsed_map)}")
    end = time.time()

    print(f"{end-start:.3f} seconds")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
