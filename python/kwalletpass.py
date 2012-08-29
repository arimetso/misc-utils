#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple utility for setting and getting passwords to/from KDE Wallet.
#
# Note that the error handling is very rudimentary.
# There are cases which aren't handled.
#
# Public domain. No warranty whatsoever and
# no guarantees about fitness for any purpose.

from PyKDE4.kdeui import KWallet
from PyQt4 import QtGui
from getpass import getpass

import sys

def exit_with_usage():
    print "To set a password: python {} set <folder> <key> [password]".format(sys.argv[0])
    sys.exit("To get a password: python {} get <folder> <key>".format(sys.argv[0]))

try:
    args = sys.argv[1:]
    op = unicode(args[0], "UTF-8")
    folder = unicode(args[1], "UTF-8")
    key = unicode(args[2], "UTF-8")
    if "set" == op and len(args) > 3:
        password = unicode(args[3], "UTF-8")
    else:
        password = None
except IndexError, err:
    exit_with_usage()

# Basic input checks for operation and folder names
if op not in { "get", "set" }:
    exit_with_usage()
if len(folder) == 0 or len(key) == 0:
    exit_with_usage()

# Password must not be empty. If it wasn't in the command line, ask it
if "set" == op and (password == None or len(password) == 0):
    password = getpass("Enter password:")
    if len(password) == 0:
        sys.exit("Cannot set an empty password.")

# Just a blank application to keep QEventLoop from complaining
application = QtGui.QApplication([])

# Open the wallet
wallet = KWallet.Wallet.openWallet(KWallet.Wallet.LocalWallet(), 0)

# The folder we're getting from should exist
if "get" == op and not wallet.hasFolder(folder):
    sys.exit("Folder {} not found.".format(folder))

if not wallet.hasFolder(folder):
    wallet.createFolder(folder)
wallet.setFolder(folder)

if "get" == op:
    status, password = wallet.readPassword(key)
    print unicode(password)
else:
    wallet.writePassword(key, password)
