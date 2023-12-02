from dataclasses import dataclass
import re 

@dataclass
class CubeData:
    colour: str
    max_allowed: int
    min_needed: int = 0

def colour_val(set: str, colour: str) -> int:
    if m := re.search("(\d+) " + colour, set):
        return int(m.group(1))
    else:
        return 0

if __name__ == "__main__":
    with open('input') as f:
        part1 = 0
        part2 = 0
        for l in f.readlines():

            cube_data = [
                CubeData("red", 12),
                CubeData("green", 13),
                CubeData("blue", 14),
            ]
            
            possible = True
            for set in l.split(';'):
                for c in cube_data:
                    c.min_needed = max(c.min_needed, colour_val(set, c.colour))
                    possible &= c.min_needed <= c.max_allowed

            if possible:
                game_match = re.search('Game (\d+):', l)
                part1 += int(game_match.group(1))

            power = 1
            for c in cube_data:
                power *= c.min_needed
            
            part2 += power

        print(part1)
        print(part2)

        