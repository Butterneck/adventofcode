#!/usr/bin/env python3
import argparse
from collections import defaultdict
import re

def parse_args():
    parser = argparse.ArgumentParser(description='Advent of code day N')
    parser.add_argument('-i', '--input', type=str,
                        default='input.txt',
                        help='Input file')

    return parser.parse_args()


def handle_instruction(instruction: str, current_pos: dict):
    if match := re.match(r"^forward (\d+)$", instruction):
        current_pos["horizontal_pos"] += int(match.group(1))
    if match := re.match(r"^up (\d+)$", instruction):
        current_pos["depth_pos"] -= int(match.group(1))
    if match := re.match(r"down (\d+)$", instruction):
        current_pos["depth_pos"] += int(match.group(1))

    return current_pos


def handle_instruction_with_aim(instruction: str, current_pos: dict):
    if match := re.match(r"^forward (\d+)$", instruction):
        current_pos["horizontal_pos"] += int(match.group(1))
        current_pos["depth_pos"] += current_pos["aim"] * int(match.group(1))
    if match := re.match(r"^up (\d+)$", instruction):
        current_pos["aim"] -= int(match.group(1))
    if match := re.match(r"down (\d+)$", instruction):
        current_pos["aim"] += int(match.group(1))

    return current_pos


def main():
    args = parse_args()
    current_pos = defaultdict(lambda: 0)
    with open(args.input) as f:
        for line in f:
            # current_pos = handle_instruction(line, current_pos)
            current_pos = handle_instruction_with_aim(line, current_pos)

    print(current_pos)
    print(current_pos["horizontal_pos"] * current_pos["depth_pos"])


if __name__ == '__main__':
    main()
