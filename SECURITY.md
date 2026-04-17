# Security Policy

## Reporting a vulnerability

If you discover a security issue with one of the binaries published here, **do not open a public GitHub issue**. Email `info@nks-hub.cz` with:

- the affected `binaries-<app>-<version>` tag (or "all"),
- a clear description of the issue,
- reproduction steps if known.

A maintainer will respond within 5 working days.

## What this repo guarantees

Each release on this repo is the byte-exact output of a [GitHub Actions workflow](.github/workflows/) running on `windows-2022`, `macos-14`, or `ubuntu-24.04` runners hosted by GitHub. The workflow source code, the runner OS, and the upstream source/binary URLs are all auditable from the release page → "Built from" link → workflow run.

Workflows that **mirror** an upstream binary (mkcert, caddy, cloudflared, mailpit, MariaDB) re-upload the upstream artifact verbatim under our naming convention. The integrity of the file is whatever the upstream provides — verify the upstream checksum out-of-band if the use case warrants it.

Workflows that **build from source** (PHP, Apache, Nginx) compile from `https://www.php.net/distributions/`, `https://archive.apache.org/dist/httpd/`, and `https://nginx.org/download/` respectively. Source tarballs are not signature-verified in the workflow yet — see "Future hardening" below.

## What this repo does NOT guarantee

- **Reproducibility:** builds are not bit-for-bit reproducible. The same tag re-run will produce a functionally equivalent but not byte-identical binary (timestamps, build paths embedded, etc.).
- **Signature/SBOM:** binaries are not currently signed and we do not ship Software Bill of Materials. This is on the roadmap.
- **Provenance attestations:** we do not currently produce SLSA or in-toto attestations.

## Future hardening (roadmap)

In rough priority order:

1. `SHA256SUMS` file uploaded as a release asset, signed with a long-lived ed25519 key whose public key lives in this repo.
2. GPG-verify upstream PHP/Apache/Nginx source tarballs in the workflow before configure.
3. SLSA Level 3 provenance via [slsa-framework/slsa-github-generator](https://github.com/slsa-framework/slsa-github-generator).
4. Reproducible builds (deterministic timestamps via `SOURCE_DATE_EPOCH`, fixed build paths).
5. cosign-sign release artifacts.

Pull requests advancing any of the above are welcome.
