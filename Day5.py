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


def day5(seed_list, seed_map):
    # Take a list of seeds and converted them through each level of the map to get the final location

    location_list = []
    for seed in seed_list:
        result_seed = seed
        seed_transforms = []
        for level in seed_map:
            for transform in level:
                if transform[0] < result_seed < transform[1]:
                    result_seed = result_seed + transform[2]
                    seed_transforms.append(result_seed)
                    break
        location_list.append(result_seed)
    return min(location_list)


def day5_part2(seed_range_list, seed_map):

    # for each pair in the seed_list create a temp seed list to pass back into day 5; and get the lowest location
    # then find the lowest location for all lowest

    location_list = []
    work_list = []
    # Initialize our list of seeds:
    for seed in seed_range_list:
        seed.append(0)
    print("Seed Range is")
    print(seed_range_list)
    work_list = seed_range_list

    # loop around until our seed work list empty:
    while work_list:
        t_found = False
        current_work = work_list.pop()
        level = current_work[2]
        print(f"Work {current_work}")
        if level == 7:
            location_list.append(current_work)
        else:
            for transform in seed_map[level]:
                modifier = transform[2]
                if current_work[0] == 1054656969 :
                    True
                if current_work[0] >= transform[0] and current_work[1] <= transform[1]:
                    # seed range is entirely within the transform
                    work_list.append([current_work[0] + modifier, current_work[1] + modifier, level + 1])
                    t_found = True
                    break
                if transform[0] <= current_work[0] < transform[1] < current_work[1]:
                    # Transform starts inside the transform and ends out side it, we need to split our seed
                    # first take the section inside and modify it
                    work_list.append([current_work[0] + modifier, transform[1] + modifier, level + 1])
                    # then take the section outside as a new work item at this level:
                    work_list.append([transform[1] + 1, current_work[1], level])
                    t_found = True
                    break
                if transform[1] > current_work[1] >= transform[0] > current_work[0]:
                    # Transform starts outside the transform and ends inside it, we need to split our seed
                    # first take the section inside and modify it
                    work_list.append([transform[0] + modifier, current_work[1] + modifier, level + 1])
                    # then take the section outside as a new work item at this level:
                    work_list.append([current_work[0], transform[0] - 1, level])
                    t_found = True
                    break
                if current_work[0] < transform[0] and current_work [1] > transform[1]:
                    # work is bigger than the transform
                    # take the section inside
                    work_list.append([transform[0] + modifier, transform[1] + modifier, level + 1])
                    work_list.append([current_work[0], transform[0] - 1, level])
                    work_list.append([transform[1] + 1, current_work[1], level])
                    t_found = True
                    break
            if not t_found:
                # No transform find, so we can move forward to the next level
               work_list.append([current_work[0], current_work[1], level + 1])
    print(location_list)
    result = min([item[0] for item in location_list])

    return result


def seed_range_convertor(seed_list):
    # take a list of seeds and convert them into the range they represent for the Day 2 problem
    seed_range_list = []

    seed_pairs = int(len(seed_list)/2)
    for x in range(seed_pairs):
        seed_range = seed_list[x*2 + 1]
        seed_start = seed_list[x*2]
        seed_range_list.append([seed_start, seed_start + seed_range])

    return seed_range_list


def seed_map_convertor(seed_map):
    # converts a seed map into a lower, upper and change
    new_seed_map = []
    for i in seed_map:
        new_list = []
        for item in seed_map[i]:
            # Python ranges don't include the last number
            new_list.append([item[1], item[1] + item[2] - 1, item[0] - item[1]])
        new_seed_map.append(new_list)

    return new_seed_map


def main():
    print("Advent of Code Day 5")

    start = time.time()
    input_array = read_file_to_list("InputFiles/input_day5.txt")
    # input_array = read_file_to_list("InputFiles/input_day5_test.txt")

    print("Part 1")
    seed_list, parsed_map = day5_parser(input_array)
    # Convert our seed map to a range with modifier for all integers in that range.
    converted_map = seed_map_convertor(parsed_map)
    print("Seed List")
    print(seed_list)
    print("\nSeed/Location Map")
    for value, item in enumerate(converted_map):
        print(value, item)
    print(f"Minimum Location is: {day5(seed_list, converted_map)}")

    # For part 2
    print("\n Part 2")
    seed_range_list = seed_range_convertor(seed_list)
    print(f"Minimum Location is: {day5_part2(seed_range_list, converted_map)}")
    end = time.time()

    print(f"{end-start:.3f} seconds")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
