import re

def day1(input_array):
    result = 0
    # replace number strings with digits
    letters_to_numbers = {"one": "1",
                          "two": "2",
                          "three": "3",
                          "four": "4",
                          "five": "5",
                          "six": "6",
                          "seven": "7",
                          "eight": "8",
                          "nine": "9"}
    # create regexp string to search on using the keys TODO: I am sure this could be made easier to look at
    re_string = "(?=("
    for item in list(letters_to_numbers.keys()):
        re_string += item + "|"
        re_string += letters_to_numbers[item] + "|"
    re_string = re_string[:-1]
    re_string += "))"

    # Use our regexp string on each line in the array to do a replace
    for idx, i_str in enumerate(input_array):
        match_list = re.findall(re_string, i_str)

        # Now calculate the values
        if match_list[0].isdigit():
            first_digit = int(match_list[0])
        else:
            first_digit = int(letters_to_numbers[match_list[0]])
        if match_list[-1].isdigit():
            second_digit = int(match_list[-1])
        else:
            second_digit = int(letters_to_numbers[match_list[-1]])

        line_answer = first_digit * 10 + second_digit
        print(line_answer)
        result = result + line_answer

    return result


def read_file_to_list(filename):
    file_list = []
    with open(filename, 'r') as f:
        for line in f:
            file_list.append(line.strip("\n\r"))
    return file_list


def main():
    print("Advent of Code Day 1")

    input_array = read_file_to_list("InputFiles/input-day1.txt")

    test_input_array = ["two1nine",
                        "eightwothree",
                        "abcone2threexyz",
                        "xtwone3four",
                        "4nineeightseven2",
                        "zoneight234",
                        "7pqrstsixteen",
                        "oneight",
                        "twonethreeight"]

    print(day1(input_array))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
