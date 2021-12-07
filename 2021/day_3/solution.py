#!/usr/bin/env python3
import argparse
from collections import defaultdict

def parse_args():
    parser = argparse.ArgumentParser(description='Advent of code day N')
    parser.add_argument('-i', '--input', type=str,
                        default='input.txt',
                        help='Input file')

    return parser.parse_args()


def part_one(input_file: str):
    zeroes = defaultdict(lambda: 0)
    ones = defaultdict(lambda: 0)

    with open(input_file) as f:
        for line in f:
            for i, char in enumerate(line):
                if char == "0":
                    zeroes[i] += 1
                elif char == "1":
                    ones[i] += 1

        gamma = "".join([ "0" if zeroes[i] > ones[i] else "1" for i in range(len(zeroes.keys())) ])
        epsilon = "".join([ "0" if gamma[i] == "1" else "1" for i in range(len(gamma)) ])

        power_consumption = int(gamma, 2) * int(epsilon, 2)
        print(power_consumption)


def fi(lines: [str], a: str, b: str):
    available = lines
    element = ""

    for i in range(len(lines[0])):
        ones_count = 0
        zeroes_count = 0

        for line in available:
            if line[i] == "1":
                ones_count += 1
            elif line[i] == "0":
                zeroes_count += 1

        if ones_count >= zeroes_count:
            element += a
        elif zeroes_count > ones_count:
            element += b

        available = [ el for el in available if el.startswith(element) ]

        if len(available) == 1:
            break

    return available[0]


def part_two(input_file: str):
    with open(input_file) as f:
        lines = f.readlines()

    oxygen = fi(lines, "1", "0")
    co2 = fi(lines, "0", "1")

    print(int(oxygen, 2) * int(co2, 2))

def main():
    args = parse_args()
    part_one(args.input)
    part_two(args.input)

if __name__ == '__main__':
    main()
