#!/usr/bin/env python3

from sys import argv

def main(argc: int, argv: list[str]) -> None:
    if argc < 3:
        raise ValueError("Missing pathname argument(s)!")

    set1 = set()

    with open(argv[1]) as f:
        for l in f.readlines():
            set1.add(l.strip())
    with open(argv[2]) as f:
        for l in f.readlines():
            set1.add(l.strip())

    for e in sorted(set1):
        print(e)

if __name__ == "__main__":
    main(len(argv), argv)
