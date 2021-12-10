#!/usr/bin/env python3
import argparse
from math import floor

def parse_args():
    parser = argparse.ArgumentParser(description='Advent of code day N')
    parser.add_argument('-i', '--input', type=str,
                        default='input.txt',
                        help='Input file')

    return parser.parse_args()


def get_opening_char(char: str) -> str:
    if char == ")": return "("
    elif char == "]": return "["
    elif char == "}": return "{"
    elif char == ">": return "<"


def parse_line(line: str, opening_chars: [str], closing_chars: [str]) -> (str, [str]):
    """Returns the first illegal character along with the unclosed characters"""
    opened_chunks = []
    for char in line:
        if char in opening_chars: opened_chunks.append(char)
        elif char in closing_chars and get_opening_char(char) != opened_chunks.pop(): return char, opened_chunks
    return None, opened_chunks


def get_syntax_error_score(line: str, opening_chars: [str], closing_chars: [str]) -> int:
    illegal_char, opened_chunks = parse_line (line, opening_chars, closing_chars)
    if illegal_char:
        if illegal_char == ")": return 3
        elif illegal_char == "]": return 57
        elif illegal_char == "}": return 1197
        elif illegal_char == ">": return 25137
    else: return 0


def part_one(input_file: str, opening_chars: [str], closing_chars: [str]) -> None:
    with open(input_file) as f:
        print(sum([ get_syntax_error_score(line, opening_chars, closing_chars) for line in f ]))


def get_unmatched_char_score(char: str) -> int:
    if char == "(": return 1
    if char == "[": return 2
    if char == "{": return 3
    if char == "<": return 4



def part_two(input_file: str, opening_chars: [str], closing_chars: [str]) -> None:
    final_scores = []
    with open(input_file) as f:
        for line in f:
            illegal_char, opened_chunks = parse_line(line, opening_chars, closing_chars)
            if illegal_char is None:
                line_score = 0
                for chunk in opened_chunks[::-1]:
                    line_score = line_score * 5 + get_unmatched_char_score(chunk)
                final_scores.append(line_score)

    final_scores.sort()
    print(final_scores[floor(len(final_scores) / 2)])


def main():
    args = parse_args()
    opening_chars = ["(", "[", "{", "<"]
    closing_chars = [")", "]", "}", ">"]
    part_one(args.input, opening_chars, closing_chars)
    part_two(args.input, opening_chars, closing_chars)


if __name__ == '__main__':
    main()
