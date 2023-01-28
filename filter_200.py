#!/usr/bin/env python3

from requests import get
from sys import argv, stderr

def get_statuscode(url: str) -> int:
    try:
        r = get(url, verify=True, timeout=3,
                headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0"})
        return int(r.status_code)
    except:
        return -1

def main(argc: int, argv: list[str]) -> None:
    if argc < 2:
        raise ValueError("Missing pathname argument(s)!")

    with open(argv[1]) as f:
        for l in f.readlines():
            l = l.strip()
            code = get_statuscode(l)
            if code == 200:
                print(l)
            else:
                print(f"[{code}] {l}", file=stderr)

if __name__ == "__main__":
    main(len(argv), argv)
