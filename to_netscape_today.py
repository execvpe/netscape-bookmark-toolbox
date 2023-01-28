#!/usr/bin/env python3

from sys import argv
from time import time

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

def netscape_add(url: str, date: int, title: str) -> None:
    print(f'    <DT><A HREF="{url}" ADD_DATE="{date}" LAST_MODIFIED="{date}">{title}</A>')

def netscape_end() -> None:
    print("</DL>")

def main(argc: int, argv: list[str]) -> None:
    if argc < 2:
        raise ValueError("Missing pathname argument(s)!")

    now = int(time())
    netscape_begin()

    with open(argv[1]) as f:
        for l in f.readlines():
            l = l.strip()
            netscape_add(l, now, l)

    netscape_end()

if __name__ == "__main__":
    main(len(argv), argv)
