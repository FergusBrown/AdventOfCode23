
def part1(line: str) -> int:
    nums = [int(c) for c in line if c.isnumeric()]
    return nums[0] * 10 + nums[-1]

def part2(line: str) -> int:
    word_map = [
        ("one", "1"),
        ("two", "2"),        
        ("three", "3"),
        ("four", "4"),
        ("five", "5"),
        ("six", "6"),
        ("seven", "7"),
        ("eight", "8"),
        ("nine", "9"),
        ("zero", "0"),
    ]

    for tup in word_map:
        line = line.replace(tup[0], tup[0] + tup[1] + tup[0])

    return part1(line)

if __name__ == "__main__":
    with open('input') as f:
        total1 = 0
        total2 = 0
        for l in f.readlines():
            total1 += part1(l)
            total2 += part2(l)

        print(total1)
        print(total2)

        