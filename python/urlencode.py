#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Urlencode strings in (somewhat of) unix style.
# Parameters are checked and encoded first.
# If no parameters are found read from standard input.
#
# Public domain. No warranty whatsoever. No guarantees
# about fitness for any purpose.

import fileinput
import sys
import urllib

if len(sys.argv) > 1:
    for index in range(1, len(sys.argv)):
        print urllib.urlencode({ 'url': sys.argv[index] })[4:]
else:
    for line in fileinput.input():
        print urllib.urlencode({ 'url': line.strip() })[4:]

