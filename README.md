# NKS WebDev Console — Binaries

Public binary releases for [NKS WebDev Console](https://github.com/nks-hub/webdev-console). The main app repo is private; this repo exists so the WDC daemon's `wdc binaries install` flow can download cross-platform binaries over plain HTTPS without any GitHub authentication.

## What's published here

Each app is built from its upstream source by GitHub Actions and published as a release with the tag pattern `binaries-<app>-<version>`. The catalog API at `nks-wdc-catalog-api` resolves app+version+OS+arch to one of these release URLs.

| Tag pattern                  | Builds for                              |
|------------------------------|-----------------------------------------|
| `binaries-php-<X.Y.Z>`       | Windows x64, macOS arm64, Linux x64    |
| `binaries-apache-<X.Y.Z>`    | (planned)                               |
| `binaries-nginx-<X.Y.Z>`     | (planned)                               |
| `binaries-mariadb-<X.Y.Z>`   | (planned)                               |
| `binaries-mkcert-<X.Y.Z>`    | (planned)                               |

## How a release is triggered

```bash
git tag binaries-php-8.3.25
git push origin binaries-php-8.3.25
```

The matching workflow under `.github/workflows/` runs a 3-OS matrix and uploads the resulting tarballs/zips as release assets. Re-runs use the `-rN` suffix (e.g. `binaries-php-8.3.25-r2`) and are stripped before the version is resolved.

## Why a separate repo

The main `nks-hub/webdev-console` repo is private to keep the source code, plugin internals, and CI infrastructure under wraps. Release assets follow repo visibility on GitHub, so a private repo means anonymous `curl` returns 404 for download URLs — which would break every end user. Splitting binary publishing into this public repo decouples distribution from source visibility.

## License of binaries

Each binary keeps its upstream license: PHP under PHP-3.01, Apache under Apache-2.0, Nginx under BSD-2, MariaDB under GPL-2.0, etc. The build scripts in this repo are MIT.
