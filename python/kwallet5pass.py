#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Simple utility for setting and getting passwords to/from KDE Wallet.
# This version is for KDE 5 and uses DBus to access the wallet.
#
# See kwalletpass.py for KDE 4 compatible version.
#
# Note that the error handling is very rudimentary.
# There are cases which aren't handled.
#
# Public domain. No warranty whatsoever and
# no guarantees about fitness for any purpose.

import dbus
import getopt
import os.path
import sys

from getpass import getpass


class EmptyPassword(RuntimeError):
    pass


class PasswordMismatch(RuntimeError):
    pass


class KWallet5Pass:
    def __init__(self, wallet_name):
        self._app_name = self.__class__.__name__

        self._session_bus = dbus.SessionBus()
        proxy_object = self._session_bus.get_object("org.kde.kwalletd5", "/modules/kwalletd5")
        self._kwalletd = dbus.Interface(proxy_object, "org.kde.KWallet")
        self._wallet_handle = self._open(wallet_name)

    def _open(self, wallet_name):
        return self._kwalletd.open(wallet_name, 0, self._app_name)

    def get(self, folder, key):
        return str(self._kwalletd.readPassword(self._wallet_handle, folder, key, self._app_name))

    def set(self, folder, key, value):
        self._kwalletd.writePassword(self._wallet_handle, folder, key, value, self._app_name)


def prompt_for_password():
    password = getpass("Enter password: ")
    if len(password) == 0:
        raise EmptyPassword()
    passwd_again = getpass("Retype password: ")
    if password != passwd_again:
        raise PasswordMismatch()
    return password


def exit_with_usage():
    print("To set a password: python3 {} [-w wallet_name] set <folder> <key> [password]".format(sys.argv[0]))
    sys.exit("To get a password: python3 {} [-w wallet_name] get <folder> <key>".format(sys.argv[0]))


if __name__ == "__main__":
    wallet_name = "kdewallet"  # default in many cases
    try:
        options, args = getopt.getopt(sys.argv[1:], "w:")
        for key, value in options:
            if key == "-w":  # allow overriding of wallet name
                wallet_name = value
        operation = args[0]
        folder = args[1]
        key = args[2]
        password = args[3] if len(args) > 3 else None

        if operation not in ("get", "set"):
            exit_with_usage()

        kwallet = KWallet5Pass(wallet_name)
        if "get" == operation:
            print(kwallet.get(folder, key))
        else:
            if not password:
                password = prompt_for_password()
            kwallet.set(folder, key, password)
            print("Password set successfully")
    except EmptyPassword:
        sys.exit("Cannot set empty password.")
    except PasswordMismatch:
        sys.exit("Passwords do not match.")
    except dbus.exceptions.DBusException as e:
        print("DBus error encountered. Maybe KWallet service is not available.")
        sys.exit("Message: " + str(e))
    except getopt.GetoptError:
        exit_with_usage()
    except IndexError:
        exit_with_usage()

