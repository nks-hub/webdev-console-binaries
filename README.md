# @nks-hub/webdev-console-binaries

[![Build](https://github.com/nks-hub/webdev-console-binaries/actions/workflows/build-binaries.yml/badge.svg)](https://github.com/nks-hub/webdev-console-binaries/actions)
[![Latest release](https://img.shields.io/github/v/release/nks-hub/webdev-console-binaries?label=latest)](https://github.com/nks-hub/webdev-console-binaries/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Cross-platform](https://img.shields.io/badge/Cross--platform-Win%20%2B%20macOS%20%2B%20Linux-22c55e)](https://github.com/nks-hub/webdev-console-binaries/releases)

> Public binary releases for [NKS WebDev Console](https://github.com/nks-hub/webdev-console). Cross-platform PHP, Apache, Nginx, MariaDB, Redis, mkcert, Caddy, cloudflared and Mailpit binaries built from upstream sources by GitHub Actions, ready for the WDC daemon's `wdc binaries install` flow over plain anonymous HTTPS.

---

## Why?

The WDC daemon's `BinaryDownloader` runs `HttpClient.GetAsync(url)` without GitHub authentication on every end-user machine. Hosting binaries in the private source-code repo would 404 for everyone. This separate public repo decouples binary distribution from source-code visibility — install URLs work anonymously, source code stays private.

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

## Features

- 🐘 **PHP 5.6 → 8.5** — twelve minor versions, comprehensive ext set (opcache, gd, intl, pdo_mysql/pgsql/sqlite, ldap, gettext, tidy, sodium, ...) plus PECL: apcu, redis, xdebug, imagick, mongodb, swoole, memcached, igbinary, yaml, oauth, imap.
- 🅰️ **Apache 2.4** — full module catalog: mod_md (built-in ACME / Let's Encrypt), mod_remoteip, http2, brotli, dav, cache, lua, ratelimit, session_crypto, socache_redis…
- 🌐 **Nginx, Caddy** — modern web server alternatives with HTTP/2 + HTTP/3 support.
- 🛢️ **MariaDB 11.4 LTS** — Linux + Windows MSI mirror.
- 🔴 **Redis** — TLS-enabled source build for Linux + macOS, community fork mirror for Windows.
- 🔒 **mkcert + cloudflared** — local CA + Cloudflare Tunnel daemon mirrors.
- 📧 **Mailpit** — local SMTP testing.
- 🐳 **Docker fallback** for legacy PHP — `ubuntu:20.04` container with OpenSSL 1.1 + libxml2 2.9 lets PHP 7.x build on modern Linux runners.

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

## Release Catalog

<!-- RELEASE_TABLE_START -->
| Tag | Name | Published | Assets | Description |
| --- | --- | --- | ---: | --- |
| [binaries-mysql-9.6.0](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-mysql-9.6.0) | MySQL 9.6.0 (cross-platform binaries) | 2026-04-22 | 3 | Mirror of [MySQL 9.6.0](https://dev.mysql.com/downloads/mysql/) for use with NKS WebDev Console's `wdc binaries install mysql@9.6.0` flow... |
| [binaries-mysql-8.4.8](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-mysql-8.4.8) | MySQL 8.4.8 (cross-platform binaries) | 2026-04-22 | 3 | Mirror of [MySQL 8.4.8](https://dev.mysql.com/downloads/mysql/) for use with NKS WebDev Console's `wdc binaries install mysql@8.4.8` flow... |
| [binaries-mariadb-12.3.1](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-mariadb-12.3.1) | MariaDB 12.3.1 (cross-platform binaries) | 2026-04-18 | 4 | Mirror of [MariaDB 12.3.1](https://mariadb.org/download/?t=mariadb&p=mariadb&r=12.3.1) for use with NKS WebDev Console's `wdc binaries in... |
| [binaries-mariadb-11.8.3](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-mariadb-11.8.3) | MariaDB 11.8.3 (cross-platform binaries) | 2026-04-18 | 4 | Mirror of [MariaDB 11.8.3](https://mariadb.org/download/?t=mariadb&p=mariadb&r=11.8.3) for use with NKS WebDev Console's `wdc binaries in... |
| [binaries-php-8.0.30](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-php-8.0.30) | PHP 8.0.30 (cross-platform binaries) | 2026-04-17 | 2 | Self-contained PHP 8.0.30 binaries for use with |
| [binaries-php-7.4.33](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-php-7.4.33) | PHP 7.4.33 (cross-platform binaries) | 2026-04-17 | 4 | Self-contained PHP 7.4.33 binaries for use with |
| [binaries-php-7.3.33](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-php-7.3.33) | PHP 7.3.33 (cross-platform binaries) | 2026-04-17 | 2 | Self-contained PHP 7.3.33 binaries for use with |
| [binaries-php-7.2.34](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-php-7.2.34) | PHP 7.2.34 (cross-platform binaries) | 2026-04-17 | 2 | Self-contained PHP 7.2.34 binaries for use with |
| [binaries-php-7.1.33](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-php-7.1.33) | PHP 7.1.33 (cross-platform binaries) | 2026-04-17 | 2 | Self-contained PHP 7.1.33 binaries for use with |
| [binaries-php-8.4.20](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-php-8.4.20) | PHP 8.4.20 (cross-platform binaries) | 2026-04-17 | 3 | Self-contained PHP 8.4.20 binaries for use with |
| [binaries-php-8.3.25](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-php-8.3.25) | PHP 8.3.25 (cross-platform binaries) | 2026-04-17 | 3 | Self-contained PHP 8.3.25 binaries for use with |
| [binaries-php-8.2.30](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-php-8.2.30) | PHP 8.2.30 (cross-platform binaries) | 2026-04-17 | 3 | Self-contained PHP 8.2.30 binaries for use with |
| [binaries-php-8.1.33](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-php-8.1.33) | PHP 8.1.33 (cross-platform binaries) | 2026-04-17 | 3 | Self-contained PHP 8.1.33 binaries for use with |
| [binaries-php-8.5.5](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-php-8.5.5) | PHP 8.5.5 (cross-platform binaries) | 2026-04-17 | 3 | Self-contained PHP 8.5.5 binaries for use with |
| [binaries-nginx-1.27.3](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-nginx-1.27.3) | Nginx 1.27.3 (cross-platform binaries) | 2026-04-17 | 3 | Self-contained Nginx 1.27.3 binaries for use |
| [binaries-cloudflared-2026.3.0](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-cloudflared-2026.3.0) | cloudflared 2026.3.0 (cross-platform binaries) | 2026-04-17 | 6 | Mirror of upstream **cloudflared 2026.3.0** for use with NKS WebDev Console's `wdc binaries install` flow. File naming follows the catalo... |
| [binaries-php-7.0.33](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-php-7.0.33) | PHP 7.0.33 (cross-platform binaries) | 2026-04-17 | 1 | Self-contained PHP 7.0.33 binaries for use with |
| [binaries-apache-2.4.66](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-apache-2.4.66) | Apache HTTPD 2.4.66 (cross-platform binaries) | 2026-04-17 | 3 | Self-contained Apache HTTPD 2.4.66 binaries for |
| [binaries-redis-7.4.2](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-redis-7.4.2) | Redis 7.4.2 (cross-platform binaries) | 2026-04-17 | 3 | Self-contained Redis 7.4.2 binaries for use with NKS WebDev Console's `wdc binaries install redis@7.4.2` flow. Linux/macOS built from ups... |
| [binaries-php-5.6.40](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-php-5.6.40) | PHP 5.6.40 (cross-platform binaries) | 2026-04-17 | 1 | Self-contained PHP 5.6.40 binaries for use with |
| [binaries-mailpit-1.29.6](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-mailpit-1.29.6) | mailpit 1.29.6 (cross-platform binaries) | 2026-04-17 | 3 | Mirror of upstream **mailpit 1.29.6** for use with NKS WebDev Console's `wdc binaries install` flow. File naming follows the catalog's `$... |
| [binaries-caddy-2.10.2](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-caddy-2.10.2) | caddy 2.10.2 (cross-platform binaries) | 2026-04-17 | 3 | Mirror of upstream **caddy 2.10.2** for use with NKS WebDev Console's `wdc binaries install` flow. File naming follows the catalog's `${a... |
| [binaries-mariadb-11.4.4](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-mariadb-11.4.4) | MariaDB 11.4.4 (cross-platform binaries) | 2026-04-17 | 4 | Mirror of [MariaDB 11.4.4](https://mariadb.org/download/?t=mariadb&p=mariadb&r=11.4.4) for use with NKS WebDev Console's `wdc binaries in... |
| [binaries-mkcert-1.4.4](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-mkcert-1.4.4) | mkcert 1.4.4 (cross-platform binaries) | 2026-04-17 | 3 | Mirror of [FiloSottile/mkcert 1.4.4](https://github.com/FiloSottile/mkcert/releases/tag/v1.4.4) for use with NKS WebDev Console's `wdc bi... |
<!-- RELEASE_TABLE_END -->

## PHP build matrix

| PHP   | Win x64 | Linux x64 | macOS arm64 | Notes                                                        |
|-------|---------|-----------|-------------|--------------------------------------------------------------|
| 8.5   | ✅      | ✅        | ✅          | OpenSSL 3, native build                                      |
| 8.4   | ✅      | ✅        | ✅          | OpenSSL 3, native build                                      |
| 8.3   | ✅      | ✅        | ✅          | OpenSSL 3, native build                                      |
| 8.2   | ✅      | ✅        | ✅          | OpenSSL 3, native build                                      |
| 8.1   | ✅      | ✅        | ✅          | OpenSSL 3, native build                                      |
| 8.0   | ✅      | ✅        | ❌          | OpenSSL 1.1 (Linux docker); macOS libxml2 + icu4c@78 ABI break |
| 7.4   | ✅      | ✅        | ❌          | OpenSSL 1.1 via docker; macOS skipped                        |
| 7.1–7.3 | ✅    | ✅        | ❌          | docker ubuntu:20.04 (OpenSSL 1.1); macOS skipped             |
| 7.0   | ✅      | ❌        | ❌          | ICU 66+ namespace alias break; Windows-only                  |
| 5.6   | ✅      | ❌        | ❌          | EOL; Windows-only via php.net                                |

## How a release is triggered

```bash
git tag binaries-php-8.3.25
git push origin binaries-php-8.3.25
```

The matching workflow under `.github/workflows/` runs the appropriate matrix and uploads the resulting tarballs/zips as release assets. Re-runs use the `-rN` suffix (`binaries-php-8.3.25-r2`) and are stripped before the version is resolved, so retries don't collide with the original tag.

## Requirements

- WDC daemon ≥ 0.1.6 (catalog client expects `nks-hub-binaries` source field)
- Anonymous HTTPS access to `github.com` (releases) — no auth needed

## Contributing

Issues and PRs welcome. New binary requests should open an [issue](https://github.com/nks-hub/webdev-console-binaries/issues/new/choose) describing the upstream source, target platforms, and intended consumer (which WDC plugin will use it).

## Support

- [GitHub Issues](https://github.com/nks-hub/webdev-console-binaries/issues)
- [NKS WebDev Console](https://github.com/nks-hub/webdev-console) — main project

## License

[MIT](LICENSE) for the build scripts, workflow definitions, and documentation in this repository. Each published binary keeps its upstream license — see [LICENSE](LICENSE) for the per-app summary.

## Links

- [NKS WebDev Console](https://github.com/nks-hub/webdev-console) — main daemon project
- [GitHub Releases](https://github.com/nks-hub/webdev-console-binaries/releases) — published binaries
- [WDC Catalog API](https://github.com/nks-hub/webdev-console) — version resolver service
- [SECURITY.md](SECURITY.md) — disclosure policy
- [CHANGELOG.md](CHANGELOG.md) — release history

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/nks-hub">NKS Hub</a>
</p>
