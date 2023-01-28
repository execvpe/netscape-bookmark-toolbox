#!/usr/bin/env python3

from bs4 import BeautifulSoup
from sys import argv

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

def netscape_add(url: str, creation: int, modification: int, title: str) -> None:
    s = f'    <DT><A HREF="{url}"'

    if creation != None:
        s += f' ADD_DATE="{creation}"'
    if modification != None:
        s += f' LAST_MODIFIED="{modification}"'

    s += f'>{title}</A>'

    print(s)

def netscape_end() -> None:
    print("</DL>")

def find_metadata(url: str) -> tuple[int, int, str]:
    global soups
    for s in soups:
        for e in s.findAll("a", href=True):
            if e["href"] != url:
                continue

            try:
                creation = int(e["add_date"])
            except KeyError:
                creation = None

            try:
                modification = int(e["last_modified"])
            except KeyError:
                modification = None

            title = e.get_text(strip=True)

            return (creation,
                    modification,
                    title if len(title) > 0 else url)

    return None, None, url

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
            creation, modification, title = find_metadata(url)

            netscape_add(url, creation, modification, title)

    netscape_end()

if __name__ == "__main__":
    main(len(argv), argv)
