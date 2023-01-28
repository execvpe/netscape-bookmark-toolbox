#!/usr/bin/env python3

from bs4 import BeautifulSoup
from sys import argv

def main(argc: int, argv: list[str]) -> None:
    if argc < 2:
        raise ValueError("Missing pathname argument!")

    with open(argv[1]) as f:
        soup = BeautifulSoup(f, features="html.parser")
        for e in soup.findAll("a"):
            print(e["href"])

if __name__ == "__main__":
    main(len(argv), argv)
