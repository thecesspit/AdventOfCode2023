import re
import time


def read_file_to_list(filename):
    file_list = []
    with open(filename, 'r') as f:
        for line in f:
            file_list.append(line.strip("\n\r"))
    return file_list


def day7(hand_list):

    result = 0
    # first for each hand, rank it from 5 of a kind to high card
    for idx, hand in enumerate(hand_list):
        counts = []
        current_hand = hand['hand']
        for card in current_hand:
            if card != "-" and card != "1":
                counts.append(current_hand.count(card))
                current_hand = current_hand.replace(card, "-")
        # now find the number of jacks (1s) in the hand, and add that to the highest count
        if "1" in current_hand:
            if not counts:
                # five of a kind of jacks
                counts = [5]
            else:
                number_of_jacks = current_hand.count("1")
                counts[counts.index(max(counts))] = counts[counts.index(max(counts))] + number_of_jacks

        hand_list[idx]['count'] = counts

    # now covert the counts into a hand_rank
    for idx, hand in enumerate(hand_list):
        if 5 in hand['count']:
            hand['rank'] = 6
            hand['rank_l'] = "5 Of a Kind"
        elif 4 in hand['count']:
            hand['rank'] = 5
            hand['rank_l'] = "4 Of a Kind"
        elif 3 in hand['count'] and 2 in hand['count']:
            hand['rank'] = 4
            hand['rank_l'] = "Full House"
        elif 3 in hand['count']:
            hand['rank'] = 3
            hand['rank_l'] = "Triple"
        elif hand['count'].count(2) == 2:
            hand['rank'] = 2
            hand['rank_l'] = "Two Pair"
        elif 2 in hand['count']:
            hand['rank'] = 1
            hand['rank_l'] = "One Pair"
        else:
            hand['rank'] = 0
            hand['rank_l'] = "High Card"
    sorted_hand_list = sorted(hand_list, key=lambda k: (k['rank'], k['hand']), reverse=True)
    for idx, hand in enumerate(sorted_hand_list):
        print(hand)
        result = result + (len(sorted_hand_list) - idx) * hand['bid']
    return result


def day7_part2(hand_list):

    result = 1
    print(hand_list)

    return result


def day7_parser(input_array):

    hand_list = []
    # A hand has two parts - the cards and the bid/
    # Read in the Boats and time for each race
    for line in input_array:
        hand = line.split(" ")[0]
        raw_hand = hand
        bid = line.split(" ")[1]
        hand = hand.replace("A", "Z")
        hand = hand.replace("K", "Y")
        hand = hand.replace("Q", "X")
        hand = hand.replace("J", "W")
        hand_list.append({'hand': hand, 'bid': int(bid), 'raw_hand': raw_hand})

    return hand_list

def day7_parser2(input_array):

    hand_list = []
    # A hand has two parts - the cards and the bid/
    # Read in the Boats and time for each race
    for line in input_array:
        hand = line.split(" ")[0]
        raw_hand = hand
        bid = line.split(" ")[1]
        hand = hand.replace("A", "Z")
        hand = hand.replace("K", "Y")
        hand = hand.replace("Q", "X")
        hand = hand.replace("J", "1")
        hand_list.append({'hand': hand, 'bid': int(bid), 'raw_hand': raw_hand})

    return hand_list


def main():
    print("Advent of Code Day 7")
    start = time.time()

    print("Part 1")
    input_array = read_file_to_list("InputFiles/input_day7.txt")
    hand_list = day7_parser(input_array)
    print(f"Value is: {day7(hand_list)}")

    # For part 2
    print("\n Part 2")
    input_array_2 = read_file_to_list("InputFiles/input_day7.txt")
    hand_list_2 = day7_parser2(input_array_2)
    print(f"Value is: {day7(hand_list_2)}")
    end = time.time()

    print(f"{end-start:.3f} seconds")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
