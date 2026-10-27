"""Self-check for validate_archive.py. Run: python .github/scripts/test_validate_archive.py"""
import io
import os
import tarfile
import tempfile
import zipfile

from validate_archive import Invalid, validate

HTML = b"<html><head><title>Oops... requested URL was not found</title></head></html>"


def write(dirname, name, data):
    path = os.path.join(dirname, name)
    with open(path, "wb") as f:
        f.write(data)
    return path


def make_zip(members):
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        for name, data in members.items():
            z.writestr(name, data)
    return buf.getvalue()


def make_tar_xz(members):
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w:xz") as t:
        for name, data in members.items():
            info = tarfile.TarInfo(name)
            info.size = len(data)
            t.addfile(info, io.BytesIO(data))
    return buf.getvalue()


def rejects(path, **kw):
    try:
        validate(path, kw.pop("min_bytes", 1), kw.pop("require", []))
    except Invalid:
        return True
    return False


with tempfile.TemporaryDirectory() as d:
    good_zip = make_zip({"Apache24/bin/httpd.exe": os.urandom(4096)})
    ok = write(d, "ok.zip", good_zip)
    assert validate(ok, 1000, [r"(^|/)bin/httpd\.exe$"]) == (len(good_zip), 1)

    assert rejects(write(d, "html.zip", HTML)), "HTML saved as .zip must fail"
    assert rejects(ok, min_bytes=10**9), "size floor"
    assert rejects(write(d, "trunc.zip", good_zip[: len(good_zip) // 2])), "truncated zip"
    assert rejects(ok, require=[r"bin/mysqld\.exe$"]), "missing required member"

    tx = write(d, "ok.tar.xz", make_tar_xz({"bin/httpd": os.urandom(4096)}))
    assert validate(tx, 1000, [r"(^|/)bin/httpd$"])[1] == 1
    assert rejects(write(d, "html.tar.xz", HTML)), "HTML saved as .tar.xz"
    assert rejects(write(d, "empty.zip", make_zip({}))), "empty archive"
    assert rejects(write(d, "page.exe", HTML)), "HTML saved as .exe"

    elf = write(d, "mkcert-1.4.4-linux-x64", b"\x7fELF" + os.urandom(4096))
    assert validate(elf, 1000, []) == (4100, 0)
    assert rejects(write(d, "tool-1.2.3-linux-x64", HTML)), "HTML saved as a raw binary"
    assert rejects(write(d, "text-1.2.3-linux-x64", b"just text" * 100)), "non-executable raw file"

print("validate_archive: all checks passed")
