import time


def read_file_to_list(filename):
    file_list = []
    with open(filename, 'r') as f:
        for line in f:
            file_list.append(line.strip("\n\r"))
    return file_list


# parse out the file into a list of codes to has
def day15_parser(input_array):

    operation_list = []
    for line in input_array:
        operation_list = line.split(",")

    return operation_list


def calculate_hash(operation):

    box = 0
    label = ""
    for c in operation:
        ascii_v = ord(c)
        if ascii_v == 61:
            instruction = operation.split("=")[1]
            break
        # if "-"
        if ascii_v == 45:
            instruction = c
            break
        else:
            box = box + ascii_v
            box = box * 17
            box = box % 256
            label = label + c

    return box, label, instruction


def day15(operation_list):

    result = 0
    boxes = [[] for i in range(256)]
    # Read in our instructions
    for operation in operation_list:
        box, label, instruction = calculate_hash(operation)
        print(box, label, instruction)
        # remove lens from box is instruction is "-" and label matches
        if instruction == "-":
            boxes[box] = [x for x in boxes[box] if x[0] != label]
        else:
            labelFound = False
            for idx, slot in enumerate(boxes[box]):
                if slot[0] == label:
                    boxes[box][idx] = (label, int(instruction))
                    labelFound = True
            if not labelFound:
                boxes[box].append((label, int(instruction)))
    focus_power = 0
    for idx, box in enumerate(boxes):
        for slot, lens in enumerate(box):
            print(idx, slot, lens)
            focus_power += (idx + 1) * (slot + 1) * lens[1]


    return focus_power


def main():
    print("Advent of Code Day 15")
    start = time.time()

    input_array = read_file_to_list("InputFiles/input_day15.txt")

    print("Part 2")
    operation_list = day15_parser(input_array)
    print(f"Value is: {day15(operation_list)}")

    end = time.time()

    print(f"{end-start:.3f} seconds")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
