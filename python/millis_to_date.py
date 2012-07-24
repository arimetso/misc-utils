#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Convert milliseconds from Unix epoch (Jan 1 1970 00:00:00.000) to a human-readable date.
# Works for example for Java System.currentTimeMillis() timestamps.
#
# Public domain. No warranty whatsoever. No guarantees about fitness for any purpose.

from datetime import datetime, timedelta
import sys

if len(sys.argv) < 2:
    sys.exit("Usage: {} milliseconds".format(sys.argv[0]))

unix_epoch = datetime(1970, 1, 1, 0, 0, 0, 0)
date = unix_epoch + timedelta(milliseconds=int(sys.argv[1]))

print date
