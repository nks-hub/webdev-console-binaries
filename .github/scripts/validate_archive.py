#!/usr/bin/env python3
"""Refuse to publish a release asset that is not a real, intact archive.

Upstream hosts answer 200 with an HTML error page for files that rotated off
disk, so a successful download proves nothing. Every workflow runs this
before the upload step.

    validate_archive.py FILE... [--min-bytes N] [--require REGEX]...

For each FILE: size floor, magic bytes for the extension, full integrity read
(zip CRC / tar stream) and, with --require, at least one member path matching
every REGEX. Exits 1 on the first problem.
"""
import argparse
import os
import re
import sys
import tarfile
import zipfile

MAGIC = {
    ".zip": b"PK\x03\x04",
    ".xz": b"\xfd7zXZ\x00",
    ".gz": b"\x1f\x8b",
    ".tgz": b"\x1f\x8b",
    ".msi": b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1",
    ".exe": b"MZ",
}
HTML_START = (b"<!doc", b"<html", b"<head", b"<?xml", b"<!--")


class Invalid(Exception):
    pass


def member_names(path):
    lower = path.lower()
    if lower.endswith(".zip"):
        with zipfile.ZipFile(path) as z:
            bad = z.testzip()
            if bad:
                raise Invalid(f"corrupt zip member {bad}")
            return z.namelist()
    if lower.endswith((".tar.xz", ".tar.gz", ".tgz")):
        with tarfile.open(path, "r:*") as t:
            return [m.name for m in t]
    return None


def validate(path, min_bytes, require):
    size = os.path.getsize(path)
    if size < min_bytes:
        raise Invalid(f"only {size} bytes, expected at least {min_bytes}")

    with open(path, "rb") as f:
        head = f.read(8)
    if head.lstrip().lower().startswith(HTML_START):
        raise Invalid("content is an HTML/XML page, not an archive")

    ext = os.path.splitext(path)[1].lower()
    magic = MAGIC.get(ext)
    if magic and not head.startswith(magic):
        raise Invalid(f"bad magic bytes {head[:len(magic)].hex()} for {ext}")

    try:
        names = member_names(path)
    except (zipfile.BadZipFile, tarfile.TarError, EOFError, OSError) as exc:
        raise Invalid(f"unreadable archive: {exc}") from exc

    if names is not None:
        if not names:
            raise Invalid("archive is empty")
        for pattern in require:
            if not any(re.search(pattern, n) for n in names):
                raise Invalid(f"no member matches {pattern!r}")
    elif require:
        raise Invalid("--require needs a .zip/.tar.xz/.tar.gz archive")
    return size, len(names) if names is not None else 0


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("files", nargs="+")
    ap.add_argument("--min-bytes", type=int, default=100_000)
    ap.add_argument("--require", action="append", default=[])
    args = ap.parse_args(argv)

    failed = False
    for path in args.files:
        try:
            size, entries = validate(path, args.min_bytes, args.require)
            print(f"OK {path}: {size} bytes, {entries} entries")
        except (Invalid, FileNotFoundError) as exc:
            print(f"::error::{path}: {exc}")
            failed = True
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
