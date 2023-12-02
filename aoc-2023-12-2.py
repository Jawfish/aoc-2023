from collections import Counter
import re


def parse_game(game):
    match = re.match(r"Game (\d+): (.*)", game)
    game_id = int(match.group(1))
    details = match.group(2)
    return game_id, details


def details_to_counters(details):
    counters_list = []
    for part in details.split(";"):
        counter = Counter()
        for color_info in part.split(","):
            count, color = color_info.strip().split()
            counter[color] += int(count)
        counters_list.append(counter)
    return counters_list


def game_is_valid(counters_list, valid_scores):
    for counter in counters_list:
        for color, count in counter.items():
            if count > valid_scores.get(color, 0):
                return False
    return True


def get_min_color(counters_list):
    max_counts = Counter()
    for counter in counters_list:
        for color, count in counter.items():
            max_counts[color] = max(max_counts.get(color, 0), count)
    return max_counts["red"], max_counts["green"], max_counts["blue"]


def main():
    valid_scores = {"red": 12, "green": 13, "blue": 14}
    sum_valid_game_ids = 0
    sum_power = 0

    with open("input") as file:
        for game in file:
            game_id, details = parse_game(game)
            counters_list = details_to_counters(details)
            r, g, b = get_min_color(counters_list)
            power = r * g * b
            sum_power += power
            if game_is_valid(counters_list, valid_scores):
                sum_valid_game_ids += game_id

    print(sum_valid_game_ids)
    print(sum_power)


if __name__ == "__main__":
    main()
