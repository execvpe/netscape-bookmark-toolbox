#!/usr/bin/env python3

from bs4 import BeautifulSoup
from sys import argv, stderr

soups = []

def netscape_begin() -> None:
    print(
"""
<!DOCTYPE NETSCAPE-Bookmark-file-1>
<!-- This is an automatically generated file.
     It will be read and overwritten.
     DO NOT EDIT! -->
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<meta http-equiv="Content-Security-Policy"
      content="default-src 'self'; script-src 'none'; img-src data: *; object-src 'none'"></meta>
<TITLE>Bookmarks</TITLE>
<H1>All hyperlinks / URLs</H1>

<DL><p>
""")

def netscape_add(tag: str) -> None:
    print(f'    <DT>{tag}')

def netscape_end() -> None:
    print("</DL>")

def find_tag(url: str) -> str:
    global soups
    for s in soups:
        for e in s.findAll("a", href=True):
            if e["href"] != url:
                continue
            return repr(e)

    return None

def main(argc: int, argv: list[str]) -> None:
    if argc < 3:
        raise ValueError("Missing pathname argument(s)!")

    netscape_begin()

    global soups
    for p in argv[2:]:
        with open(p) as f:
            soups.append(BeautifulSoup(f, features="html.parser"))

    with open(argv[1]) as f:
        for url in f.readlines():
            url = url.strip()
            tag = find_tag(url)
            if tag == None:
                print(f"The URL {url} was not found in the given bookmark files!", file=stderr)
                continue
            netscape_add(tag)

    netscape_end()

if __name__ == "__main__":
    main(len(argv), argv)
