#!/bin/bash
#
# Find 30 largest files in a tar package. Supports also gzip and bzip2 compressed
# files. Can be used for example for blacklisting unnecessary and space consuming
# stuff from backups.
#
# Tested and works with GNU tar version 1.26.
# May or may not work with other versions.
#
# This script is public domain. No warranties and no guarantees about fitness
# for any particular purpose.

tar_file="$1"
if [ ! -f "$tar_file" ]; then echo "Usage: `basename $0` tar_file"; exit 1; fi

if [ `echo "$tar_file"|grep 'tar.gz$'` ]; then tar_opts="-tzvf";
elif [ `echo "$tar_file"|grep 'tar.bz2$'` ]; then tar_opts="-tjvf";
else tar_opts="-tvf";
fi

tar $tar_opts "$tar_file"|cut -c 21-|sort -rn|head -30|awk '{ printf "%12d  %s\n", $1, $4}'

