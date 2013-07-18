#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Generator and formatter for Finnish billing reference numbers.
# (i.e. viitenumero, http://fi.wikipedia.org/wiki/Tilisiirto)
#
# Converts a bill id to a reference number by calculating and
# appending the required checksum to the original id. Formatting
# follows the guidelines published by Finanssialan Keskusliitto:
#
# http://www.fkl.fi/en/material/publications/Publications/Bank_Transfer_Guidelines_2011.pdf
#
# Public domain. No warranty whatsoever and
# no guarantees about fitness for any purpose.

import getopt
import sys

MULTIPLIERS = [ 7, 3, 1 ]

class ReferenceNumber(object):
    def __init__(self, bill_id):
        self._reference = self._generate_ref(bill_id)

    def get(self):
        return self._reference

    def format(self):
        return " ".join(self._group(self._reference))

    def __unicode__(self):
        return unicode(self._reference)

    def _generate_ref(self, bill_id):
        checksum = 0
        index = 0
        source = int(bill_id)
        while source > 0:
            checksum += (source % 10) * MULTIPLIERS[index % len(MULTIPLIERS)]
            source = source / 10
            index = index + 1
        return int(bill_id) * 10 + (10 - checksum) % 10

    def _group(self, reference):
        remaining = unicode(reference)
        first_group_len = len(remaining) % 5
        if first_group_len > 0:
            yield remaining[:first_group_len]
            remaining = remaining[first_group_len:]
        while len(remaining) > 0:
            group = remaining[:5]
            remaining = remaining[5:]
            yield group

def exit_with_usage():
    sys.exit("Usage: %s [-f] bill_id" % sys.argv[0])

if __name__ == "__main__":
    formatted_output = False
    try:
        options, args = getopt.getopt(sys.argv[1:], "f")
        for key, value in options:
            if "-f" == key:
                formatted_output = True

        reference = ReferenceNumber(args[0])
        if formatted_output:
            print reference.format()
        else:
            print reference.get()
    except getopt.GetoptError:
        exit_with_usage()
    except IndexError:
        exit_with_usage()

