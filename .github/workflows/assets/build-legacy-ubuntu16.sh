#!/bin/bash
# Builds PHP 5.6 / 7.0 inside ubuntu:16.04 (OpenSSL 1.0.2, ICU 55) with the
# workspace bind-mounted at /work. Expects /work/php-src.tar.xz (already
# checksum-verified by the caller). Usage: build-legacy-ubuntu16.sh VER MM
set -e
VER=$1; MM=$2
export DEBIAN_FRONTEND=noninteractive
apt-get update -q
apt-get install -y -q build-essential autoconf libxml2-dev libsqlite3-dev libssl-dev libcurl4-openssl-dev \
  libbz2-dev libfreetype6-dev libjpeg-dev libpng-dev libxslt1-dev libgmp-dev libreadline-dev pkg-config \
  xz-utils ca-certificates libicu-dev patchelf file
[ -e /usr/include/gmp.h ] || ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/include/gmp.h
cd /tmp && tar xf /work/php-src.tar.xz && cd php-$VER
for p in /work/.github/workflows/assets/patches/$MM/*.patch; do [ -e "$p" ] || continue; echo "Applying $p"; patch -p1 --forward < "$p"; done
P=/work/install/php-$VER
./configure --prefix=$P \
  --enable-fpm --enable-mbstring --enable-bcmath --enable-soap \
  --enable-intl --enable-pcntl --enable-sockets --enable-exif \
  --with-openssl --with-curl --enable-zip --with-zlib --with-bz2 \
  --with-mysqli=mysqlnd --with-pdo-mysql=mysqlnd --with-pdo-sqlite --with-sqlite3 \
  --with-readline --with-xsl --with-gmp > /tmp/configure-$VER.log 2>&1 || { tail -30 /tmp/configure-$VER.log; exit 1; }
make -j8 > /tmp/make-$VER.log 2>&1 || { tail -40 /tmp/make-$VER.log; exit 1; }
make install > /tmp/install-$VER.log 2>&1
mkdir -p $P/lib
ldd $P/bin/php $P/sbin/php-fpm $P/bin/php-cgi | grep -oE '/[^ ]+\.so[^ ]*' | sort -u \
  | grep -vE '/(libc|libm|libdl|libpthread|librt|libresolv|libutil|ld-linux[^/]*)\.so' \
  | xargs -r cp -Lv -t $P/lib/
for f in $P/bin/php $P/bin/php-cgi $P/bin/phpdbg $P/sbin/php-fpm; do [ -e $f ] && patchelf --set-rpath '$ORIGIN/../lib' $f; done
for f in $P/lib/*.so*; do patchelf --set-rpath '$ORIGIN' $f || true; done
$P/bin/php -v
echo BUILD_OK
