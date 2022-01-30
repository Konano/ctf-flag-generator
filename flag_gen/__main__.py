import math
import secrets
import argparse

char_map = [
    ['A', 'a', '4', '@'],
    ['B', 'b', '8'],
    ['C', 'c'],
    ['D', 'd'],
    ['E', 'e', '3'],
    ['F', 'f'],
    ['G', 'g', '6', '9'],
    ['H', 'h'],
    ['I', 'i', '1'],
    ['J', 'j'],
    ['K', 'k'],
    ['L', 'l', '1'],
    ['M', 'm'],
    ['N', 'n'],
    ['O', 'o', '0'],
    ['P', 'p'],
    ['Q', 'q'],
    ['R', 'r'],
    ['S', 's', '5', '$'],
    ['T', 't', '7'],
    ['U', 'u'],
    ['V', 'v'],
    ['W', 'w'],
    ['X', 'x'],
    ['Y', 'y'],
    ['Z', 'z', '2'],
]


def leet_change(c):
    if c.isalpha():
        c = c.upper()
        char_set = char_map[ord(c) - ord('A')]
        new_c = secrets.choice(char_set)
        return new_c, math.log2(len(char_set))
    else:
        return c, 0


def leet(s):
    entropy = 0
    new_string = []
    for c in s.replace(' ', '_'):
        new_char, e = leet_change(c)
        new_string.append(new_char)
        entropy += e
    return ''.join(new_string), entropy


def main():
    global args
    parser = argparse.ArgumentParser()
    parser.add_argument("string", help="origin flag string")
    args = parser.parse_args()
    new_string, entropy = leet(args.string)
    print(new_string)
    print(f"Entropy: {entropy:.2f} bits")


if __name__ == "__main__":
    main()
