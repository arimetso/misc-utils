#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Urldecode strings in (somewhat of) unix style.
# Parameters are checked and decoded first.
# If no parameters are found read from standard input.
#
# Public domain. No warranty whatsoever. No guarantees
# about fitness for any purpose.

import fileinput
import urllib
import sys

if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        print urllib.unquote(arg)
else:
    for line in fileinput.input():
        print urllib.unquote(line.strip())

