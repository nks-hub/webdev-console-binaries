# @nks-hub/webdev-console-binaries

[![Build PHP](https://github.com/nks-hub/webdev-console-binaries/actions/workflows/build-binaries.yml/badge.svg)](https://github.com/nks-hub/webdev-console-binaries/actions/workflows/build-binaries.yml)
[![Build Apache](https://github.com/nks-hub/webdev-console-binaries/actions/workflows/build-apache.yml/badge.svg)](https://github.com/nks-hub/webdev-console-binaries/actions/workflows/build-apache.yml)
[![Build Nginx](https://github.com/nks-hub/webdev-console-binaries/actions/workflows/build-nginx.yml/badge.svg)](https://github.com/nks-hub/webdev-console-binaries/actions/workflows/build-nginx.yml)
[![Latest release](https://img.shields.io/github/v/release/nks-hub/webdev-console-binaries?label=latest)](https://github.com/nks-hub/webdev-console-binaries/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Cross-platform](https://img.shields.io/badge/Cross--platform-Win%20%2B%20macOS%20%2B%20Linux-22c55e)](https://github.com/nks-hub/webdev-console-binaries/releases)

> Public binary releases for [NKS WebDev Console](https://github.com/nks-hub/webdev-console). Cross-platform PHP, Apache, Nginx, MariaDB, Redis, mkcert, Caddy, cloudflared and Mailpit binaries built from upstream sources by GitHub Actions, ready for the WDC daemon's `wdc binaries install` flow over plain anonymous HTTPS.

---

## Why?

The WDC daemon's `BinaryDownloader` runs `HttpClient.GetAsync(url)` without GitHub authentication on every end-user machine. Hosting binaries in the private source-code repo would 404 for everyone. This separate public repo decouples binary distribution from source-code visibility — install URLs work anonymously, source code stays private.

## Features

- 🐘 **PHP 5.6 → 8.5** — twelve minor versions, comprehensive ext set (opcache, gd, intl, pdo_mysql/pgsql/sqlite, ldap, gettext, tidy, sodium, ...) plus PECL: apcu, redis, xdebug, imagick, mongodb, swoole, memcached, igbinary, yaml, oauth, imap.
- 🅰️ **Apache 2.4** — full module catalog: mod_md (built-in ACME / Let's Encrypt), mod_remoteip, http2, brotli, dav, cache, lua, ratelimit, session_crypto, socache_redis…
- 🌐 **Nginx, Caddy** — modern web server alternatives with HTTP/2 + HTTP/3 support.
- 🛢️ **MariaDB 11.4 LTS** — Linux + Windows MSI mirror.
- 🔴 **Redis** — TLS-enabled source build for Linux + macOS, community fork mirror for Windows.
- 🔒 **mkcert + cloudflared** — local CA + Cloudflare Tunnel daemon mirrors.
- 📧 **Mailpit** — local SMTP testing.
- 🐳 **Docker fallback** for legacy PHP — `ubuntu:20.04` container with OpenSSL 1.1 + libxml2 2.9 lets PHP 7.x build on modern Linux runners.

## Quick Start

The catalog API at `nks-wdc-catalog-api` resolves `app + version + OS + arch` to the right release URL automatically. The daemon never has to construct a URL by hand.

```bash
# From the WDC daemon CLI:
wdc binaries install php@8.3.25
wdc binaries install apache@2.4.66
wdc binaries install mariadb@11.4.4
```

Manual download via `curl` works the same way:

```bash
curl -L -o php.tar.xz \
  https://github.com/nks-hub/webdev-console-binaries/releases/download/binaries-php-8.3.25/php-8.3.25-linux-x64.tar.xz
```

## What's published

| Tag pattern                       | Built for                                  | Build mode                                       |
|-----------------------------------|--------------------------------------------|--------------------------------------------------|
| `binaries-php-<X.Y.Z>`            | Win x64, macOS arm64, Linux x64            | source on Linux/Mac, php.net repackage on Win    |
| `binaries-apache-<X.Y.Z>`         | Win x64, macOS arm64, Linux x64            | source on Linux/Mac, ApacheLounge on Win         |
| `binaries-nginx-<X.Y.Z>`          | Win x64, macOS arm64, Linux x64            | source on Linux/Mac, nginx.org on Win            |
| `binaries-mariadb-<X.Y.Z>`        | Win x64, Linux x64                         | mirror of `archive.mariadb.org`                  |
| `binaries-redis-<X.Y.Z>`          | Win x64, macOS arm64, Linux x64            | source with TLS on Linux/Mac, fork on Win        |
| `binaries-mkcert-<X.Y.Z>`         | Win x64, macOS arm64, Linux x64            | mirror of FiloSottile/mkcert                     |
| `binaries-caddy-<X.Y.Z>`          | Win x64, macOS arm64, Linux x64            | mirror of caddyserver/caddy                      |
| `binaries-cloudflared-<X.Y.Z>`    | Win/Linux/macOS x64+arm64                  | mirror of cloudflare/cloudflared                 |
| `binaries-mailpit-<X.Y.Z>`        | Win x64, macOS arm64, Linux x64            | mirror of axllent/mailpit                        |

## PHP build matrix

| PHP   | Win x64 | Linux x64 | macOS arm64 | Notes                                                        |
|-------|---------|-----------|-------------|--------------------------------------------------------------|
| 8.5   | ✅      | ✅        | ✅          | OpenSSL 3, native build                                      |
| 8.4   | ✅      | ✅        | ✅          | OpenSSL 3, native build                                      |
| 8.3   | ✅      | ✅        | ✅          | OpenSSL 3, native build                                      |
| 8.2   | ✅      | ✅        | ✅          | OpenSSL 3, native build                                      |
| 8.1   | ✅      | ✅        | ✅          | OpenSSL 3, native build                                      |
| 8.0   | ✅      | ✅        | ❌          | OpenSSL 1.1 (Linux docker); macOS libxml2 2.13+ ABI break    |
| 7.4   | ✅      | ✅        | ❌          | OpenSSL 1.1 + libxml2 2.9 via docker; macOS skipped          |
| 7.1–7.3 | ✅    | ✅        | ❌          | docker ubuntu:20.04 (OpenSSL 1.1, libxml2 2.9)               |
| 7.0   | ✅      | ❌        | ❌          | ICU 66+ namespace alias break; Windows-only                  |
| 5.6   | ✅      | ❌        | ❌          | EOL; Windows-only via php.net                                |

## Requirements

- WDC daemon ≥ 0.1.6 (catalog client expects `nks-hub-binaries` source field)
- Anonymous HTTPS access to `github.com` (releases) — no auth needed

## How a release is triggered

```bash
git tag binaries-php-8.3.25
git push origin binaries-php-8.3.25
```

The matching workflow under `.github/workflows/` runs the appropriate matrix and uploads the resulting tarballs/zips as release assets. Re-runs use the `-rN` suffix (`binaries-php-8.3.25-r2`) and are stripped before the version is resolved, so retries don't collide with the original tag.

## License

[MIT](LICENSE) for the build scripts, workflow definitions, and documentation in this repository. Each published binary keeps its upstream license — see [LICENSE](LICENSE) for the per-app summary.

---

Made by [NKS Hub](https://github.com/nks-hub) — part of the [NKS WebDev Console](https://github.com/nks-hub/webdev-console) project.
