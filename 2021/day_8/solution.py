#!/usr/bin/env python3
import argparse
import re
from collections import defaultdict

def parse_args():
    parser = argparse.ArgumentParser(description='Advent of code day N')
    parser.add_argument('-i', '--input', type=str,
                        default='input.txt',
                        help='Input file')

    return parser.parse_args()


def parse_line(line: str):
    regex = r"(\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) \| (\w+) (\w+) (\w+) (\w+)"
    groups = re.match(regex, line).groups()
    return groups[:10], groups[10:]


def part_one(input_file: str):
    occurrencies = defaultdict(lambda: 0)
    with open(input_file) as f:
        for line in f:
            patterns, output_values = parse_line(line)
            for output_value in output_values:
                if len(output_value) == 2: occurrencies["1"] += 1
                elif len(output_value) == 3: occurrencies["7"] += 1
                elif len(output_value) == 4: occurrencies["4"] += 1
                elif len(output_value) == 7: occurrencies["8"] += 1

    print(sum(occurrencies.values()))


def get_known_patterns(patterns: [str]) -> dict:
    """Returns patterns for 1, 4, 7"""
    known_patterns = defaultdict(lambda: "")
    for pattern in patterns:
        if len(pattern) == 2: known_patterns["1"] = pattern
        elif len(pattern) == 4: known_patterns["4"] = pattern
        elif len(pattern) == 3: known_patterns["7"] = pattern
        # Exit early if possible
        if len(known_patterns.keys()) == 3:
            break
    return known_patterns


def decode_len_five(element: str, known_patterns: dict) -> str:
    # 2, 3, 5 have pattens of len 5
    if set(element).issuperset(set(known_patterns["1"])): return "3"
    elif len(set(element).intersection(set(known_patterns["4"]))) == 2: return "2"
    else: return "5"


def decode_len_six(element: str, known_patterns: dict) -> str:
    # 0, 6, 9 have patterns of len 6
    if set(element).issuperset(set(known_patterns["4"])): return "9"
    elif set(element).issuperset(set(known_patterns["7"])): return "0"
    else: return "6"

def decode_line(patterns: [str], output: [str]) -> str:
    """Returns decoded output as array of int"""
    known_patterns = get_known_patterns(patterns)
    decoded_output = ""

    for el in output:
        if len(el) == 2: decoded_output += "1"
        elif len(el) == 3: decoded_output += "7"
        elif len(el) == 4: decoded_output += "4"
        elif len(el) == 5: decoded_output += decode_len_five(el, known_patterns)
        elif len(el) == 6: decoded_output += decode_len_six(el, known_patterns)
        elif len(el) == 7: decoded_output += "8"

    return decoded_output


def part_two(input_file: str):
    total_sum = 0
    with open(input_file) as f:
        for line in f:
            patterns, output = parse_line(line)
            print("patterns: ", patterns)
            print("output: ", output)
            decoded_output = decode_line(patterns, output)
            print("decoded_output: ", decoded_output)
            total_sum += int(decoded_output)

    print("total sum: ", total_sum)



def main():
    args = parse_args()
    part_one(args.input)
    part_two(args.input)


if __name__ == '__main__':
    main()
