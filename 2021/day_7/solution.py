#!/usr/bin/env python3
import argparse
from collections import defaultdict
from math import floor, ceil

def parse_args():
    parser = argparse.ArgumentParser(description='Advent of code day N')
    parser.add_argument('-i', '--input', type=str,
                        default='input.txt',
                        help='Input file')

    return parser.parse_args()


def get_most_occurent(data):
    occurrencies = defaultdict(lambda: 0)
    most_occurrent = None
    for el in data:
        occurrencies[str(el)] += 1
        if not most_occurrent or occurrencies[str(el)] > most_occurrent:
            most_occurrent = occurrencies[str(el)]

    return most_occurrent


def calculate_total_fuel_consumption(destination_point: int, data: [int]):
    return sum(abs(destination_point - int(el)) for el in data)


def calculate_total_fuel_consumption_two(destination_point: int, data: [int]):
    return sum(calculate_single_fuel_consumption_two(abs(destination_point - int(el))) for el in data)


def calculate_single_fuel_consumption_two(distance):
    return floor(distance / 2) * (distance + 1) + ceil(distance/2) * (distance % 2)


def handle(data: [int]):
    destination_point = get_most_occurent(data)
    fuel_consumption = 0

    while True:
        # fuel_consumption = calculate_total_fuel_consumption(destination_point, data)
        fuel_consumption = calculate_total_fuel_consumption_two(destination_point, data)
        # fuel_consumption_left = calculate_total_fuel_consumption(destination_point - 1, data)
        fuel_consumption_left = calculate_total_fuel_consumption_two(destination_point - 1, data)
        # fuel_consumption_right = calculate_total_fuel_consumption(destination_point + 1, data)
        fuel_consumption_right = calculate_total_fuel_consumption_two(destination_point + 1, data)

        if fuel_consumption < fuel_consumption_left and fuel_consumption < fuel_consumption_right:
            break
        elif fuel_consumption > fuel_consumption_left:
            destination_point -= 1
        elif fuel_consumption > fuel_consumption_right:
            destination_point += 1


    print(destination_point)
    print(fuel_consumption)


def main():
    args = parse_args()
    with open(args.input, "r") as f:
        data = f.readlines()[0].replace("\n", "").split(",")
        handle(data)


if __name__ == '__main__':
    main()
