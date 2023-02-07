#!/usr/bin/env python3

from sys import argv

def main(argc: int, argv: list[str]) -> None:
    if argc < 3:
        raise ValueError("Missing pathname argument(s)!")

    set1 = set()
    set2 = set()

    with open(argv[1]) as f:
        for l in f.readlines():
            set1.add(l.strip())
    with open(argv[2]) as f:
        for l in f.readlines():
            set2.add(l.strip())

#   print(f"===== X is in {argv[1]}, but not in {argv[2]} =====")
    [print(x) for x in set1 if x not in set2]
#   print(f"===== X is in {argv[2]}, but not in {argv[1]} =====")
#   [print(x) for x in set2 if x not in set1]

if __name__ == "__main__":
    main(len(argv), argv)
