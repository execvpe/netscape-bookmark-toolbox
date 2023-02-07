# Netscape Bookmark (File) Toolbox

A collection of python scripts for parsing and converting Netscape bookmark files.

## Dependencies

All scripts should run using the default Python 3 libraries,
except `extract_urls.py` and `to_netscape_full.py` which require the HTML parser
[Beautiful Soup](https://en.wikipedia.org/wiki/Beautiful_Soup_(HTML_parser)).

If you are using Arch Linux, you can install the dependency using:
`pacman -S python-beautifulsoup4`

There should be a simillar way of installing the library if you are using another distribution.

## Usage

The term "**raw file**" denotes a file in which every line contains an URL.

Example:

```
https://google.com
https://en.wikipedia.org
https://github.com
...
```

### compare_lines.py

`compare_lines.py <raw file 1> <raw file 2>`

Compares files line-by-line and outputs lines which are present in
the first file, but not in the second.

### extract_urls.py

`extract_urls.py <Netscape bookmark file>`

Extracts all URLs from a Netscape bookmark file and print them on the
standard output (stdout).

### filter_200.py

`filter_200.py <raw file>`

Prints every URL which is reachable (server responded `200 OK`)
on the standard output.
If the request fails because of various reasons, the URL will be printed on the
standard error output stream (stderr) paired with the corresponding error code
in front of it. Discard any errors by appending `2> /dev/null`.

### rm_dups_and_sort.py

`rm_dups_and_sort.py <raw file> [raw file]...`

As the name suggests, this script removes duplicate URLs and sorts everything
before printing them on the standard output.

### to_netscape_basic.py

`to_netscape_basic.py <raw file>`

This script converts a raw file (URL on every line) back to the Netscape bookmark format.
Because the bookmark title have been discarded, the URL is used for this field.
**Timestamps and other metadata is discarded.**

*If you are unsatisfied with this behavior, scroll ahead.*

### to_netscape_today.py

`to_netscape_today.py <raw file>`

This script converts a raw file (URL on every line) back to the Netscape bookmark format.  
Because the timestamps (creation, modification) as well as the bookmark title have been discarded,
the **current time repectively the URL** is used for these fields.

*If you are unsatisfied with this behavior, scroll ahead.*

### to_netscape_full.py

`to_netscape_full.py <raw file> <netscape bookmark file> [netscape bookmark file]...`

This script converts a raw file (URL on every line) back to the Netscape bookmark format.  
The **Netscape bookmark files are being crawled for metadata** in the order given by the
command line arguments. The first match is used. If no match is found, timestamps are ignored
and the title will be the URL.

## Example (combined)

- Extract all the URLs in the bookmark file `bookmarks.html`
- Delete duplicates and sort the URLs.
- Check which of them are still reachable. Discard all errors.
- Export the URLs back to the Netscape bookmark format including metadata such as timestamps and title.

```
$ ./extract_urls.py bookmarks.html > bookmarks.raw
$ ./rm_dups_and_sort.py bookmarks.raw > unique.raw
$ ./filter_200.py unique.raw > reachable.raw 2> /dev/null
$ ./to_netscape_full.py reachable.raw bookmarks.html > export.html
```
