#!/bin/bash
#
# Generate simple self-signed SSL certificate using JDK keytool.
#
# Public domain. No warranty whatsoever. No guarantees about fitness for any purpose.

keystore_file=keystore.dat

test -f "$keystore_file" && echo "`basename $0`: $keystore_file already exists." && exit 1
keytool -keystore "$keystore_file" -storepass "pas5W0rd" -alias "devkey" -genkey -keyalg "RSA" -validity 3650 -keypass "pas5W0rd"

