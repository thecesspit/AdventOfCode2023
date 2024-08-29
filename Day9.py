import time


def read_file_to_list(filename):
    file_list = []
    with open(filename, 'r') as f:
        for line in f:
            file_list.append(line.strip("\n\r"))
    return file_list


def pyramid_analysis(analysis):

    # Create the analysis pyramid
    analysis_pyramid = [analysis]
    current_analysis = analysis
    while current_analysis:
        new_analysis = []
        for idx, x in enumerate(current_analysis):
            if idx+1 < len(current_analysis):
                new_analysis.append(current_analysis[idx+1] - x)
        current_analysis = new_analysis
        analysis_pyramid.append(current_analysis)
        # check we have all 0's in the list
        if not [x for x in current_analysis if x != 0]:
            current_analysis = []
    return analysis_pyramid


def day9(analysis_list):

    result = 0

    for analysis in analysis_list:
        analysis_pyramid = pyramid_analysis(analysis.copy())

        # Now work back up the pyramid to add a value to each row
        analysis_pyramid = [x for x in reversed(analysis_pyramid)]

        for idx, fill_in in enumerate(analysis_pyramid):
            if idx == 0:
                analysis_pyramid[idx].append(fill_in[-1])
            else:
                analysis_pyramid[idx].append(fill_in[-1] + analysis_pyramid[idx-1][-1])
        result = result + analysis_pyramid[-1][-1]

    return result


def day9_part2(analysis_list):
    result = 0

    for analysis in analysis_list:
        analysis_pyramid = pyramid_analysis(analysis)

        # Now work back up the pyramid to add a value to each row
        analysis_pyramid = [x for x in reversed(analysis_pyramid)]

        for idx, fill_in in enumerate(analysis_pyramid):
            if idx == 0:
                analysis_pyramid[idx].insert(0, fill_in[0]),
            else:
                analysis_pyramid[idx].insert(0, fill_in[0] - analysis_pyramid[idx-1][0])
        print(analysis_pyramid)
        result = result + analysis_pyramid[-1][0]

    return result


# parse out the file into two parts - the directions and the map
def day9_parser(input_array):

    analysis_list = []
    for line in input_array:
        line_list = line.split()
        analysis_list.append([int(x) for x in line_list])

    return analysis_list


def main():
    print("Advent of Code Day 9")
    start = time.time()

    input_array = read_file_to_list("InputFiles/input_day9.txt")

    print("Part 1")
    analysis_list = day9_parser(input_array)
    print(f"Value is: {day9(analysis_list)}")

    # For part 2
    print("\n Part 2")
    print(f"Value is: {day9_part2(analysis_list)}")
    end = time.time()

    print(f"{end-start:.3f} seconds")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
