#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters — make.fun entry.

Writes one Wi-Fi network name of at most 32 characters to
/output/entry.txt. The name is:

    MyExStillUsesThisWiFi

The breakup happened, but the ex never left the network: one character,
one situation, one story — and the punchline lands on the first read.
"""
import os
import sys

ENTRY = "MyExStillUsesThisWiFi"
MAX_CHARS = 32


def resolve_output_path():
    if len(sys.argv) > 1:
        return sys.argv[1]
    return "/output/entry.txt"


def main():
    text = ENTRY
    if not (1 <= len(text) <= MAX_CHARS):
        print(
            "entry must be 1-%d characters, got %d" % (MAX_CHARS, len(text)),
            file=sys.stderr,
        )
        return 1
    if not text.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    path = resolve_output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    os.replace(tmp, path)
    print("wrote %d characters to %s" % (len(text), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
