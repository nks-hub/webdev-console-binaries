#!/bin/bash
# Shim for the legacy ICU `icu-config` script that PHP 7.0/7.1 ext/intl still
# probes. ICU 60+ (Ubuntu 20.04+) dropped the script in favour of pkg-config,
# which the old autoconf macros in PHP ext/intl/config.m4 don't know about.
#
# PHP calls the following flags (see ext/intl/config.m4); each must return
# exactly what ICU 54's icu-config would have:
#   --version               : numeric "66.1" style version
#   --prefix                : install root (used only informatively)
#   --cflags                : full compile flags
#   --cxxflags / --cppflags : C++ variants (same content as cflags here)
#   --cppflags-searchpath   : -I paths ONLY (no -D, no warnings)
#   --ldflags               : full link line for icu-i18n + icu-uc
#   --ldflags-libsonly      : -l<lib> tokens only
#   --ldflags-searchpath    : -L paths only
#   --ldflags-system        : system libs (empty on modern glibc)
#   --ldflags-icuio         : icu-io specifically (for the io sub-library)
#
# Kept as a checked-in file (instead of an in-workflow heredoc) so edits don't
# have to navigate two layers of shell escaping inside `docker run ... bash -c`.
PCS="icu-i18n icu-uc"
case "$1" in
  --version) pkg-config --modversion icu-i18n ;;
  --prefix) echo /usr ;;
  --cflags|--cxxflags|--cppflags) pkg-config --cflags $PCS ;;
  --cppflags-searchpath) pkg-config --cflags-only-I $PCS ;;
  --ldflags) pkg-config --libs $PCS ;;
  --ldflags-libsonly) pkg-config --libs-only-l $PCS ;;
  --ldflags-searchpath) pkg-config --libs-only-L $PCS ;;
  --ldflags-system) echo "" ;;
  --ldflags-icuio) pkg-config --libs icu-io 2>/dev/null || echo "" ;;
  *) echo "" ;;
esac
