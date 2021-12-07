#!/usr/bin/env python3
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Advent of code day N')
    parser.add_argument('-i', '--input', type=str,
                        default='input.txt',
                        help='Input file')

    return parser.parse_args()


def main():
    args = parse_args()


if __name__ == '__main__':
    main()
