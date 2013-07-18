#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Unit tests for billing_reference.py
#
# Public domain. No warranty whatsoever and
# no guarantees about fitness for any purpose.

import unittest
from billing_reference import ReferenceNumber

class BillingReferenceTest(unittest.TestCase):
    def test_generator_with_too_short_bill_ids(self):
        self.assertEquals(13, ReferenceNumber(1).get())
        self.assertEquals(291, ReferenceNumber(29).get())
    
    def test_generator(self):
        self.assertEquals(2820, ReferenceNumber(282).get())
        self.assertEquals(2956, ReferenceNumber(295).get())
        self.assertEquals(26343, ReferenceNumber(2634).get())
        self.assertEquals(2313232, ReferenceNumber(231323).get())
        self.assertEquals(3243556567550, ReferenceNumber(324355656755).get())
        self.assertEquals(3400158640913006, ReferenceNumber(340015864091300).get())
    
    def test_formatting(self):
        self.assertEquals(u"26", ReferenceNumber(2).format())
        self.assertEquals(u"563", ReferenceNumber(56).format())
        self.assertEquals(u"4556", ReferenceNumber(455).format())
        self.assertEquals(u"26343", ReferenceNumber(2634).format())
        self.assertEquals(u"1 23136", ReferenceNumber(12313).format())
        self.assertEquals(u"23 13232", ReferenceNumber(231323).format())
        self.assertEquals(u"86409 13009", ReferenceNumber(864091300).format())
        self.assertEquals(u"3 40015 86409 13006", ReferenceNumber(340015864091300).format())

if __name__ == '__main__':
    unittest.main()
