import re

points: dict = {}
points_with_overlaps: int = 0

def update_passing_points(x1: int, y1: int, x2: int, y2: int):
    global points
    global points_with_overlaps
    if x1 == x2 and y1 == y2:
        key = str(x1) + "," + str(y1)
        current_value = points.get(key)
        points[key] = current_value + 1 if current_value else 1
        points_with_overlaps = points_with_overlaps + 1 if points[key] == 2 else points_with_overlaps
    if x1 == x2:
        # Vertical line
        for i in range(min(y1, y2), max(y1, y2) + 1):
            key = str(x1) + "," + str(i)
            current_value = points.get(key)
            points[key] = current_value + 1 if current_value else 1
            points_with_overlaps = points_with_overlaps + 1 if points[key] == 2 else points_with_overlaps
    elif y1 == y2:
        # Horizonal line
        for i in range(min(x1, x2), max(x1, x2) + 1):
            key = str(i) + "," + str(y1)
            current_value = points.get(key)
            points[key] = current_value + 1 if current_value else 1
            points_with_overlaps = points_with_overlaps + 1 if points[key] == 2 else points_with_overlaps
    else:
        # Diagonal line
        dx = 1 if x2 > x1 else -1
        dy = 1 if y2 > y1 else -1
        for i in range(abs(x2 - x1) + 1):
            key = str(x1 + i * dx) + "," + str(y1 + i * dy)
            current_value = points.get(key)
            points[key] = current_value + 1 if current_value else 1
            points_with_overlaps = points_with_overlaps + 1 if points[key] == 2 else points_with_overlaps


def main():
    r = r"(\d+),(\d+) -> (\d+),(\d+)"

    # Load input file line by line
    # For every line determine passing points and update max value to avoid matrix scanning at the end
    with open('input.txt', 'r') as f:
        for line in f:
            x1, y1, x2, y2 = re.match(r, line).groups()
            update_passing_points(int(x1), int(y1), int(x2), int(y2))

    print(points_with_overlaps)


if __name__ == '__main__':
    main()