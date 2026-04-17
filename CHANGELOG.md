# Changelog

All notable releases produced by this repository's workflows. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); each section is keyed by the `binaries-<app>-<version>` tag.

## binaries-php-* (initial cross-platform builds)

### `binaries-php-{7.4.33, 8.0.30, 8.1.33, 8.2.30, 8.3.25, 8.4.20, 8.5.5}` — 2026-04-17

Initial NKS-built binaries for the WDC catalog. Configure flags chosen to match MAMP 8.2's bundled extension list and cover the union of WordPress, Drupal, Laravel, Symfony, and Nette runtime requirements.

- SAPIs: `cli`, `fpm`, `cgi`, `opcache` (Zend ext).
- DB: `mysqli`, `pdo_mysql`, `pdo_sqlite`, `sqlite3`, `pgsql`, `pdo_pgsql`.
- Net: `curl`, `openssl`, `soap`, `ftp`, `ldap`, `imap` (7.x–8.3 bundled; PECL on 8.4+).
- I18n: `mbstring`, `intl`, `iconv`, `gettext`, `xsl`, `tidy`.
- Image: `gd` with `jpeg`, `webp`, `freetype`, `xpm`.
- IPC + math: `bcmath`, `gmp`, `shmop`, `sysv{msg,sem,shm}`, `calendar`, `dba`, `pcntl`, `sockets`, `sodium`, `password_argon2`.
- Compressors: `zip`, `bz2`, `zlib`.
- PECL extensions installed and wired into `php.ini`: `apcu-5.1.28`, `redis-6.3.0`, `xdebug-3.4.7|3.5.1`, `imagick-3.7.0|3.8.1`, `mongodb-1.20.1|2.2.1`, `swoole-4.8.13|5.1.8|6.1.7|6.2.0`, `memcached-3.4.0` (≤8.4), `igbinary-3.2.16`, `yaml-2.2.5`, `oauth-2.0.10` (≤8.3), `imap-1.0.3` (8.4+).

PHP <8.1 on Linux is built inside `docker:ubuntu:20.04` so OpenSSL 1.1 and libxml2 2.9 are present (modern Ubuntu runners ship OpenSSL 3 and libxml2 2.13+ which break PHP 7.x source).

PHP 7.x macOS is intentionally not built — Homebrew's libxml2 2.13+ tightened const-correctness in `xmlError*` and `ext/libxml/libxml.c` won't compile against it. Building libxml2 from source on every CI run isn't worth the time.

## binaries-apache-2.4.66 — 2026-04-17

Comprehensive Apache HTTPD 2.4.66 build with `--enable-mods-shared=reallyall` plus explicit flags for: `md` (built-in ACME / Let's Encrypt), `remoteip` (for Cloudflare Tunnel deployments), `session` family, `macro`, `ratelimit`, `substitute`, `unique-id`, `log-forensic`, `dumpio`, `dav` family, `cache` family with `socache-{shmcb,memcache,redis}`, `lua`, `watchdog`, `buffer`, `reqtimeout`, `authn-socache`, `authnz-fcgi`, `http2` (via nghttp2), `brotli`. MPM: `event`. Windows is a mirror of the corresponding ApacheLounge VS17 build.

## binaries-nginx-1.27.3 — 2026-04-17

Nginx 1.27.3 source build with `http_ssl`, `http_v2`, `http_v3`, `http_realip`, `http_gzip_static`, `http_stub_status`, `stream`, `stream_ssl`, PCRE2 + JIT. Windows is the upstream nginx.org ZIP.

## binaries-mariadb-11.4.4 — 2026-04-17

Mirror of upstream MariaDB 11.4.4 LTS. Windows MSI from `archive.mariadb.org/winx64-packages/`, Linux glibc tarball from `bintar-linux-systemd-x86_64`. macOS arm64 not present in upstream archive — daemon should fall back to brew on Mac for the moment.

## binaries-mkcert-1.4.4 — 2026-04-17

Mirror of FiloSottile/mkcert v1.4.4 — Windows EXE, Linux x64 ELF, macOS arm64 Mach-O. Statically linked Go binary, no runtime deps.

## binaries-caddy-2.10.2 — 2026-04-17

Mirror of caddyserver/caddy v2.10.2 release tarballs/zip.

## binaries-cloudflared-2026.3.0 — 2026-04-17

Mirror of cloudflare/cloudflared 2026.3.0 single-binary releases. Includes both linux and macOS arm64 plus x64.

## binaries-mailpit-1.29.6 — 2026-04-17

Mirror of axllent/mailpit v1.29.6 release tarballs/zip.
