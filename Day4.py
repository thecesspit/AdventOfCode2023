import re
import time

def read_file_to_list(filename):
    file_list = []
    with open(filename, 'r') as f:
        for line in f:
            file_list.append(line.strip("\n\r"))
    return file_list

def day4_parser(input_array):

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

def day4_card_checker(card_dict):
    # For each card, count the number of winning numbers and return a score.
    winnings = 0

    for card, value in card_dict.items():
        card_winnings = 0
        print(card, value)
        for winner in value["winners"]:
            if winner in value["numbers"]:
                card_winnings += 1
        if card_winnings == 1:
            winnings += card_winnings
        if card_winnings > 1:
            winnings += pow(2,(card_winnings - 1))

    return winnings


def day4_card_checker_advance(card_dict):
    # for each card, count the number of winners and add cards to the array
    card_count = [1 for x in range(1, len(card_dict)+1) if True]
    result = 0

    for card, value in card_dict.items():
        card_winnings = 0
        card_number = int("".join(c for c in card if c.isdigit()))
        for winner in value["winners"]:
            if winner in value["numbers"]:
                card_winnings += 1
        print(f"Card Number {card_number} = {card_winnings}")
        if card_winnings > 0:
            for i in range(card_winnings):
                card_count[card_number+i] += card_count[card_number-1]
    for i in card_count:
        result += i
    return result


def main():
    print("Advent of Code Day 4")

    start = time.time()
    input_array = read_file_to_list("InputFiles/input-day4.txt")

    test_input_array = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
                        "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
                        "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
                        "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
                        "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
                        "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]

    parsed_cards = day4_parser(input_array)
    print("Part 1")
    print(day4_card_checker(parsed_cards))
    print("Part 2")
    print(day4_card_checker_advance(parsed_cards))
    end = time.time()

    print(f"{end-start:.3f} seconds")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
