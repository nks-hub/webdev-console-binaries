[![Build](https://github.com/nks-hub/webdev-console-binaries/actions/workflows/build-binaries.yml/badge.svg)](https://github.com/nks-hub/webdev-console-binaries/actions)
[![Latest Release](https://img.shields.io/github/v/release/nks-hub/webdev-console-binaries?label=release)](https://github.com/nks-hub/webdev-console-binaries/releases)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Cross-platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-blue)](https://github.com/nks-hub/webdev-console-binaries/releases)
[![Releases](https://img.shields.io/github/v/tag/nks-hub/webdev-console-binaries?label=tags)](https://github.com/nks-hub/webdev-console-binaries/tags)

# NKS WebDev Console — Binaries

Public binary releases for [NKS WebDev Console](https://github.com/nks-hub/webdev-console). Cross-platform PHP, Apache, Nginx, MariaDB, MySQL, PostgreSQL, Redis, mkcert, Caddy, cloudflared and Mailpit binaries built from upstream sources by GitHub Actions — ready for the WDC daemon's `wdc binaries install` flow over plain anonymous HTTPS.

## Features

- ✅ **Cross-platform matrix** — Windows x64, macOS arm64, Linux x64 for every supported app
- ✅ **PHP 5.6 → 8.5** — twelve minor versions with comprehensive extension set (opcache, gd, intl, pdo_mysql/pgsql/sqlite, ldap, gettext, tidy, sodium, …) plus PECL: apcu, redis, xdebug, imagick, mongodb, swoole, memcached, igbinary, yaml, oauth, imap
- ✅ **Apache 2.4** — full module catalog: mod_md (ACME / Let's Encrypt), mod_remoteip, http2, brotli, dav, cache, lua, ratelimit, session_crypto, socache_redis…
- ✅ **MariaDB + MySQL** — official upstream mirrors plus source-built macOS arm64 (upstream doesn't ship arm64 pre-built tarballs)
- ✅ **PostgreSQL** — runtime-only Windows package from EnterpriseDB binaries, Linux/macOS source builds with initdb/start/query/dump smoke tests
- ✅ **Nginx, Caddy** — modern web server alternatives with HTTP/2 + HTTP/3 support
- ✅ **Redis** — TLS-enabled source build for Linux + macOS, community fork mirror for Windows
- ✅ **mkcert + cloudflared** — local CA + Cloudflare Tunnel daemon mirrors
- ✅ **Mailpit** — local SMTP testing catcher
- ✅ **Docker fallback** for legacy PHP — `ubuntu:20.04` container with OpenSSL 1.1 + libxml2 2.9 lets PHP 7.x build on modern Linux runners
- ✅ **Anonymous HTTPS download** — no GitHub auth needed, works over plain `curl -L`
- ✅ **SHA-256 verified** — upstream manifests checked before publishing

## Requirements

- WDC daemon ≥ 0.1.6 (catalog client expects `nks-hub-binaries` source field)
- Anonymous HTTPS access to `github.com` (releases) — no authentication needed

## Why a separate repo?

The WDC daemon's `BinaryDownloader` runs `HttpClient.GetAsync(url)` without GitHub authentication on every end-user machine. Hosting binaries in the (previously) private source-code repo would 404 for everyone. This separate public repo decouples binary distribution from source-code visibility — install URLs work anonymously.

## Quick Start

The catalog API at [`wdc.nks-hub.cz`](https://github.com/nks-hub/wdc-catalog-api) resolves `app + version + OS + arch` to the right release URL automatically. The daemon never constructs URLs by hand.

```bash
# From the WDC daemon CLI:
wdc binaries install php@8.3.25
wdc binaries install apache@2.4.66
wdc binaries install mariadb@11.4.4
wdc binaries install postgresql@18.3
```

Manual download via `curl` works the same way:

```bash
curl -L -o php.tar.xz \
  https://github.com/nks-hub/webdev-console-binaries/releases/download/binaries-php-8.3.25/php-8.3.25-linux-x64.tar.xz
```

## Build Matrix

### PHP

| PHP     | Win x64 | Linux x64 | macOS arm64 | Notes                                                         |
|---------|---------|-----------|-------------|---------------------------------------------------------------|
| 8.5     | ✅      | ✅        | ✅          | OpenSSL 3, native build                                       |
| 8.4     | ✅      | ✅        | ✅          | OpenSSL 3, native build                                       |
| 8.3     | ✅      | ✅        | ✅          | OpenSSL 3, native build                                       |
| 8.2     | ✅      | ✅        | ✅          | OpenSSL 3, native build                                       |
| 8.1     | ✅      | ✅        | ✅          | OpenSSL 3, native build                                       |
| 8.0     | ✅      | ✅        | ❌          | OpenSSL 1.1 (Linux docker); macOS libxml2 + icu4c@78 ABI break |
| 7.4     | ✅      | ✅        | ❌          | OpenSSL 1.1 via docker; macOS skipped                         |
| 7.1–7.3 | ✅      | ✅        | ❌          | docker ubuntu:20.04 (OpenSSL 1.1); macOS skipped              |
| 7.0     | ✅      | ❌        | ❌          | ICU 66+ namespace alias break; Windows-only                   |
| 5.6     | ✅      | ❌        | ❌          | EOL; Windows-only via php.net                                 |

### Other apps

| Tag pattern                    | Platforms                            | Build mode                                     |
|--------------------------------|--------------------------------------|------------------------------------------------|
| `binaries-apache-<X.Y.Z>`      | Win x64, macOS arm64, Linux x64      | source on Linux/Mac, ApacheLounge on Win       |
| `binaries-nginx-<X.Y.Z>`       | Win x64, macOS arm64, Linux x64      | source on Linux/Mac, nginx.org on Win          |
| `binaries-mariadb-<X.Y.Z>`     | Win x64, Linux x64, macOS arm64      | upstream mirror + brew-bottle relocated macOS  |
| `binaries-mysql-<X.Y.Z>`       | Win x64, Linux x64, macOS arm64      | dev.mysql.com mirror + brew-bottle relocated   |
| `binaries-postgresql-<X.Y>`     | Win x64, Linux x64, macOS arm64      | EnterpriseDB runtime subset + source Linux/macOS |
| `binaries-redis-<X.Y.Z>`       | Win x64, macOS arm64, Linux x64      | source with TLS on Linux/Mac, fork on Win      |
| `binaries-mkcert-<X.Y.Z>`      | Win x64, macOS arm64, Linux x64      | mirror of FiloSottile/mkcert                   |
| `binaries-caddy-<X.Y.Z>`       | Win x64, macOS arm64, Linux x64      | mirror of caddyserver/caddy                    |
| `binaries-cloudflared-<X.Y.Z>` | Win/Linux/macOS x64+arm64            | mirror of cloudflare/cloudflared               |
| `binaries-mailpit-<X.Y.Z>`     | Win x64, macOS arm64, Linux x64      | mirror of axllent/mailpit                      |

## Release Catalog

<!-- RELEASE_TABLE_START -->
| Tag | Name | Published | Assets | Description |
| --- | --- | --- | ---: | --- |
| [binaries-postgresql-18.3](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-postgresql-18.3) | PostgreSQL 18.3 (cross-platform binaries) | 2026-05-04 | 3 | PostgreSQL 18.3 binaries for NKS WebDev Console's `wdc binaries install postgresql@18.3` flow. |
| [binaries-mysql-9.6.0](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-mysql-9.6.0) | MySQL 9.6.0 (cross-platform binaries) | 2026-04-22 | 3 | Mirror of [MySQL 9.6.0](https://dev.mysql.com/downloads/mysql/) for use with NKS WebDev Console's `wdc binaries install mysql@9.6.0` flow... |
| [binaries-mysql-8.4.8](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-mysql-8.4.8) | MySQL 8.4.8 (cross-platform binaries) | 2026-04-22 | 3 | Mirror of [MySQL 8.4.8](https://dev.mysql.com/downloads/mysql/) for use with NKS WebDev Console's `wdc binaries install mysql@8.4.8` flow... |
| [binaries-mariadb-12.3.1](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-mariadb-12.3.1) | MariaDB 12.3.1 (cross-platform binaries) | 2026-04-18 | 4 | Mirror of [MariaDB 12.3.1](https://mariadb.org/download/?t=mariadb&p=mariadb&r=12.3.1) for use with NKS WebDev Console's `wdc binaries in... |
| [binaries-mariadb-11.8.3](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-mariadb-11.8.3) | MariaDB 11.8.3 (cross-platform binaries) | 2026-04-18 | 4 | Mirror of [MariaDB 11.8.3](https://mariadb.org/download/?t=mariadb&p=mariadb&r=11.8.3) for use with NKS WebDev Console's `wdc binaries in... |
| [binaries-php-8.0.30](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-php-8.0.30) | PHP 8.0.30 (cross-platform binaries) | 2026-04-17 | 2 | Self-contained PHP 8.0.30 binaries for use with |
| [binaries-php-7.4.33](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-php-7.4.33) | PHP 7.4.33 (cross-platform binaries) | 2026-04-17 | 4 | Self-contained PHP 7.4.33 binaries for use with |
| [binaries-php-7.3.33](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-php-7.3.33) | PHP 7.3.33 (cross-platform binaries) | 2026-04-17 | 2 | Self-contained PHP 7.3.33 binaries for use with |
| [binaries-php-7.2.34](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-php-7.2.34) | PHP 7.2.34 (cross-platform binaries) | 2026-04-17 | 2 | Self-contained PHP 7.2.34 binaries for use with |
| [binaries-php-7.1.33](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-php-7.1.33) | PHP 7.1.33 (cross-platform binaries) | 2026-04-17 | 2 | Self-contained PHP 7.1.33 binaries for use with |
| [binaries-php-8.4.20](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-php-8.4.20) | PHP 8.4.20 (cross-platform binaries) | 2026-04-17 | 4 | Self-contained PHP 8.4.20 binaries for use with |
| [binaries-php-8.3.25](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-php-8.3.25) | PHP 8.3.25 (cross-platform binaries) | 2026-04-17 | 5 | Self-contained PHP 8.3.25 binaries for use with |
| [binaries-php-8.2.30](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-php-8.2.30) | PHP 8.2.30 (cross-platform binaries) | 2026-04-17 | 5 | Self-contained PHP 8.2.30 binaries for use with |
| [binaries-php-8.1.33](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-php-8.1.33) | PHP 8.1.33 (cross-platform binaries) | 2026-04-17 | 5 | Self-contained PHP 8.1.33 binaries for use with |
| [binaries-php-8.5.5](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-php-8.5.5) | PHP 8.5.5 (cross-platform binaries) | 2026-04-17 | 4 | Self-contained PHP 8.5.5 binaries for use with |
| [binaries-nginx-1.27.3](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-nginx-1.27.3) | Nginx 1.27.3 (cross-platform binaries) | 2026-04-17 | 3 | Self-contained Nginx 1.27.3 binaries for use |
| [binaries-cloudflared-2026.3.0](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-cloudflared-2026.3.0) | cloudflared 2026.3.0 (cross-platform binaries) | 2026-04-17 | 6 | Mirror of upstream **cloudflared 2026.3.0** for use with NKS WebDev Console's `wdc binaries install` flow. File naming follows the catalo... |
| [binaries-php-7.0.33](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-php-7.0.33) | PHP 7.0.33 (cross-platform binaries) | 2026-04-17 | 2 | Self-contained PHP 7.0.33 binaries for use with |
| [binaries-apache-2.4.66](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-apache-2.4.66) | Apache HTTPD 2.4.66 (cross-platform binaries) | 2026-04-17 | 3 | Self-contained Apache HTTPD 2.4.66 binaries for |
| [binaries-redis-7.4.2](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-redis-7.4.2) | Redis 7.4.2 (cross-platform binaries) | 2026-04-17 | 3 | Self-contained Redis 7.4.2 binaries for use with NKS WebDev Console's `wdc binaries install redis@7.4.2` flow. Linux/macOS built from ups... |
| [binaries-php-5.6.40](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-php-5.6.40) | PHP 5.6.40 (cross-platform binaries) | 2026-04-17 | 2 | Self-contained PHP 5.6.40 binaries for use with |
| [binaries-mailpit-1.29.6](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-mailpit-1.29.6) | mailpit 1.29.6 (cross-platform binaries) | 2026-04-17 | 3 | Mirror of upstream **mailpit 1.29.6** for use with NKS WebDev Console's `wdc binaries install` flow. File naming follows the catalog's `$... |
| [binaries-caddy-2.10.2](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-caddy-2.10.2) | caddy 2.10.2 (cross-platform binaries) | 2026-04-17 | 3 | Mirror of upstream **caddy 2.10.2** for use with NKS WebDev Console's `wdc binaries install` flow. File naming follows the catalog's `${a... |
| [binaries-mariadb-11.4.4](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-mariadb-11.4.4) | MariaDB 11.4.4 (cross-platform binaries) | 2026-04-17 | 4 | Mirror of [MariaDB 11.4.4](https://mariadb.org/download/?t=mariadb&p=mariadb&r=11.4.4) for use with NKS WebDev Console's `wdc binaries in... |
| [binaries-mkcert-1.4.4](https://github.com/nks-hub/webdev-console-binaries/releases/tag/binaries-mkcert-1.4.4) | mkcert 1.4.4 (cross-platform binaries) | 2026-04-17 | 3 | Mirror of [FiloSottile/mkcert 1.4.4](https://github.com/FiloSottile/mkcert/releases/tag/v1.4.4) for use with NKS WebDev Console's `wdc bi... |
<!-- RELEASE_TABLE_END -->

## Development

### Triggering a release

```bash
git tag binaries-php-8.3.25
git push origin binaries-php-8.3.25
```

The matching workflow under `.github/workflows/` runs the appropriate matrix and uploads the resulting tarballs/zips as release assets. Re-runs use the `-rN` suffix (`binaries-php-8.3.25-r2`) and are stripped before the version is resolved, so retries don't collide with the original tag.

### Workflow architecture

Each app has a dedicated workflow (`build-php.yml`, `build-apache.yml`, `build-mariadb.yml`, …). Workflows trigger on matching tags via pattern (`binaries-<app>-*`) or manual dispatch. The `mirror` job fetches upstream pre-built assets; parallel per-platform jobs build from source where upstream doesn't ship a compatible binary (macOS arm64 for MariaDB/MySQL uses `brew install` + `install_name_tool` rpath relocation via `dylibbundler`).

## Contributing

Contributions are welcome! New binary requests should open an [issue](https://github.com/nks-hub/webdev-console-binaries/issues/new/choose) describing the upstream source, target platforms, and intended consumer (which WDC plugin will use it).

1. Fork the repository
2. Create your feature branch (`git checkout -b feat/new-app-build`)
3. Add or modify a workflow under `.github/workflows/`
4. Test with a pre-release tag (`binaries-<app>-<version>-rc1`)
5. Open a Pull Request

## Support

- 📧 **Email:** dev@nks-hub.cz
- 🐛 **Bug reports:** [GitHub Issues](https://github.com/nks-hub/webdev-console-binaries/issues)
- 🔗 **Main project:** [nks-hub/webdev-console](https://github.com/nks-hub/webdev-console)
- 🔒 **Security:** [SECURITY.md](SECURITY.md) — disclosure policy
- 📜 **History:** [CHANGELOG.md](CHANGELOG.md) — release notes

## License

[MIT](LICENSE) for the build scripts, workflow definitions, and documentation in this repository. Each published binary retains its upstream license — see [LICENSE](LICENSE) for the per-app summary.

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/nks-hub">NKS Hub</a>
</p>
