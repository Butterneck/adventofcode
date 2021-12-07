#!/usr/bin/env python3
import argparse
from collections import defaultdict

def parse_args():
    parser = argparse.ArgumentParser(description='Advent of code day N')
    parser.add_argument('-i', '--input', type=str,
                        default='input.txt',
                        help='Input file')

    return parser.parse_args()


def fish_population(starting_fishes: [int], days: int, reproduction_time: int, warming_time: int):
    born_at = defaultdict(lambda: 0)

    for fish in starting_fishes:
        born_at[str(fish)] += 1
    for day in range(days):
        born_at[str(day)] = born_at[str(day)] + born_at[str(day - reproduction_time)] + born_at[str(day - (reproduction_time + warming_time))]

    return sum(born_at.values()) + len(starting_fishes)


def main():
    args = parse_args()

    total = 0
    days_remaining = 80
    reproduction_time = 7
    warming_time = 2

    with open(args.input, "r") as f:
        starting_fishes = [ el for el in f.readline().replace("\n", "").split(",") ]
        print("After 80 days: ", fish_population(starting_fishes, 80, reproduction_time, warming_time))
        print("After 256 days: ", fish_population(starting_fishes, 256, reproduction_time, warming_time))


if __name__ == '__main__':
    main()
