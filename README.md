# NKS WebDev Console — Binaries

[![Build PHP](https://github.com/nks-hub/webdev-console-binaries/actions/workflows/build-binaries.yml/badge.svg)](https://github.com/nks-hub/webdev-console-binaries/actions/workflows/build-binaries.yml)
[![Build Apache](https://github.com/nks-hub/webdev-console-binaries/actions/workflows/build-apache.yml/badge.svg)](https://github.com/nks-hub/webdev-console-binaries/actions/workflows/build-apache.yml)
[![Build Nginx](https://github.com/nks-hub/webdev-console-binaries/actions/workflows/build-nginx.yml/badge.svg)](https://github.com/nks-hub/webdev-console-binaries/actions/workflows/build-nginx.yml)
[![Latest release](https://img.shields.io/github/v/release/nks-hub/webdev-console-binaries?label=latest)](https://github.com/nks-hub/webdev-console-binaries/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Public binary releases for [NKS WebDev Console](https://github.com/nks-hub/webdev-console). The main app repo holds the daemon and Electron app; this repo exists so the WDC daemon's `wdc binaries install` flow can download cross-platform binaries over plain HTTPS without any GitHub authentication, and so binary lifetimes are decoupled from source-code releases.

## Catalog

Each app is built from its upstream source by GitHub Actions and published as a release with the tag pattern `binaries-<app>-<version>`. The catalog API at `nks-wdc-catalog-api` resolves `app + version + OS + arch` to one of these release URLs.

| Tag pattern                       | Built for                                  | Build mode                                       |
|-----------------------------------|--------------------------------------------|--------------------------------------------------|
| `binaries-php-<X.Y.Z>`            | Windows x64, macOS arm64, Linux x64        | source on Linux/Mac, repackaged php.net for Win |
| `binaries-apache-<X.Y.Z>`         | Windows x64, macOS arm64, Linux x64        | source on Linux/Mac, ApacheLounge for Win       |
| `binaries-nginx-<X.Y.Z>`          | Windows x64, macOS arm64, Linux x64        | source on Linux/Mac, nginx.org for Win          |
| `binaries-mariadb-<X.Y.Z>`        | Windows x64, Linux x64 (no upstream macOS) | mirror of mariadb.org tarballs/MSI              |
| `binaries-mkcert-<X.Y.Z>`         | Windows x64, macOS arm64, Linux x64        | mirror of FiloSottile/mkcert                    |
| `binaries-caddy-<X.Y.Z>`          | Windows x64, macOS arm64, Linux x64        | mirror of caddyserver/caddy                     |
| `binaries-cloudflared-<X.Y.Z>`    | Win/Linux/macOS x64+arm64                  | mirror of cloudflare/cloudflared                |
| `binaries-mailpit-<X.Y.Z>`        | Windows x64, macOS arm64, Linux x64        | mirror of axllent/mailpit                       |

## PHP build matrix

PHP binaries are compiled with a comprehensive extension set matching MAMP and the union of WordPress/Drupal/Laravel/Symfony/Nette requirements, plus PECL extensions installed afterward and wired into `php.ini`.

| PHP   | Win x64 | Linux x64 | macOS arm64 | Notes                                                |
|-------|---------|-----------|-------------|------------------------------------------------------|
| 8.5   | ✓       | ✓         | ✓           | OpenSSL 3, native build                              |
| 8.4   | ✓       | ✓         | ✓           | OpenSSL 3, native build                              |
| 8.3   | ✓       | ✓         | ✓           | OpenSSL 3, native build                              |
| 8.2   | ✓       | ✓         | ✓           | OpenSSL 3, native build                              |
| 8.1   | ✓       | ✓         | ✓           | OpenSSL 3, native build                              |
| 8.0   | ✓       | ✓         | ✓           | OpenSSL 1.1 (Linux via docker, Mac via brew)         |
| 7.4   | ✓       | ✓         | —           | OpenSSL 1.1 + libxml2 2.9 (Linux docker), mac N/A    |
| 7.0–7.3 | ✓     | —         | —           | upstream php.net repackage only                      |
| 5.6   | ✓       | —         | —           | upstream php.net repackage only                      |

PHP < 8.1 on Linux uses a `docker:ubuntu:20.04` build container so OpenSSL 1.1 and the older libxml2 are available; modern hosted runners only ship OpenSSL 3 and libxml2 2.13+ which break PHP 7.x's `ext/openssl` and `ext/libxml`.

### Bundled PHP extensions

Compiled in: bcmath, bz2, calendar, ctype, curl, dba, dom, exif, fileinfo, filter, ftp, gd (with jpeg/webp/freetype/xpm), gettext, gmp, hash, iconv, imap (7.x–8.3 — bundled; PECL on 8.4+), intl, json, ldap, libxml, mbstring, mysqli, mysqlnd, opcache, openssl, pcntl, pcre, PDO, pdo_mysql, pdo_pgsql, pdo_sqlite, pgsql, Phar, posix, readline, Reflection, session, shmop, SimpleXML, soap, sockets, sodium, SPL, sqlite3, sysvmsg, sysvsem, sysvshm, tidy, tokenizer, xml, xmlreader, xmlwriter, xsl, zip, zlib.

Installed via PECL after build: `apcu`, `redis`, `xdebug`, `imagick`, `mongodb`, `swoole`, `memcached` (≤8.4), `igbinary`, `yaml`, `oauth` (≤8.3), `imap` (8.4+ to fill the unbundling gap).

## How a release is triggered

Push a matching tag:

```bash
git tag binaries-php-8.3.25
git push origin binaries-php-8.3.25
```

The matching workflow under `.github/workflows/` runs the appropriate matrix and uploads the resulting tarballs/zips as release assets. Re-runs use the `-rN` suffix (e.g. `binaries-php-8.3.25-r2`) and are stripped before the version is resolved, so re-runs don't collide with the original release tag.

## License

[MIT](LICENSE) for the build scripts, workflow definitions, and documentation in this repository. Each binary keeps its upstream license — see [LICENSE](LICENSE) for the per-app summary.
