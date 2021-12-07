def part_1():
    depth_increases: int = 0
    previous_line: int = 0
    with open('input.txt', 'r') as f:
        for line in f:
            line = int(line)
            depth_increases = depth_increases + 1 if previous_line and line > previous_line else depth_increases
            previous_line = line

    print(depth_increases)


def part_2():
    depth_increases: int = 0
    previous_line: int = 0
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    for i in range(len(lines) - 2):
        window = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
        depth_increases = depth_increases + 1 if previous_line and window > previous_line else depth_increases
        previous_line = window

    print(depth_increases)

def main():
    part_1()
    part_2()    

if __name__ == '__main__':
    main()
