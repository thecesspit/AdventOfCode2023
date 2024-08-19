import re
import time

def read_file_to_list(filename):
    file_list = []
    with open(filename, 'r') as f:
        for line in f:
            file_list.append(line.strip("\n\r"))
    return file_list

def day2_parser(input_array):

    game_dict = {}
    # Parse the file line by line
    for line in input_array:
        game_key = line.split(":")[0]
        game_split = line.split(":")[1].split(";")
        game_list = []
        for game in game_split:
            game_result = {}
            for cubes in game.split(","):
                game_result[cubes.split(" ")[2]] = int(cubes.split(" ")[1])
            game_list.append(game_result)
        game_dict[game_key] = game_list
    return game_dict

def day2_limitchecker(game_dict, limits):
    # Now for each game, see if the cubes are over our limits
    limit_result = 0
    for key, game in game_dict.items():
        passed = True
        for result in game:
            for limit in limits.keys():
                if (limit in result) and (limits[limit] < result[limit]):
                    passed = False
                    break
        if passed:
            limit_result += int(key.split(" ")[1])

    return limit_result

def day2b_power(game_dict):
    test_result = 0

    # Now for each game, see if the cubes are over our limits
    for key, game in game_dict.items():
        game_max = {'red':  0, 'green': 0, 'blue': 0}
        power = 1
        for result in game:
            for colour in game_max.keys():
                if (colour in result) and (game_max[colour] < result[colour]):
                    game_max[colour] = result[colour]
        for value in game_max.values():
            power = power * value
        test_result += power

    return test_result


def main():
    print("Advent of Code Day 1")

    start = time.time()
    input_array = read_file_to_list("InputFiles/input-day2.txt")

    test_input_array = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
                        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
                        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
                        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
                        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]

    limits = {'red': 12, 'green': 13, 'blue': 14}
    parsed_games = day2_parser(input_array)
    print("Part 1")
    print(day2_limitchecker(parsed_games, limits))
    print("Part 2")
    print(day2b_power(parsed_games))
    end = time.time()

    print(f"{end-start:.3f} seconds")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
