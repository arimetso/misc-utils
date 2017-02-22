#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Simple client for org.freedesktop.Notifications service,
# https://developer.gnome.org/notification-spec/
#
# Public domain. No warranty whatsoever and
# no quarantees about fitness for any purpose.

import dbus
import getopt
import sys


SERVICE = "org.freedesktop.Notifications"
PATH = "/org/freedesktop/Notifications"
ICON = ""


class DbusNotifications:
    """
    Simple client for org.freedesktop.Notifications service.
    """
    def __init__(self):
        self._app_name = self.__class__.__name__
        self._session_bus = dbus.SessionBus()
        proxy_object = self._session_bus.get_object(SERVICE, PATH)
        self._notify = dbus.Interface(proxy_object, SERVICE)

    def notify(self, summary, body):
        """
        Send a desktop notification. Summary is a single-line overview
        of the notification and body is a multi-line body of text. Some
        markup is allowed in body, see the documentation in:
        https://developer.gnome.org/notification-spec/
        """
        actions = ("default", "OK")
        hints = dict()
        expires = 360000
        self._notify.Notify(self._app_name, 0, ICON, summary, body, actions, hints, expires)


if __name__ == "__main__":
    notifications = DbusNotifications()
    notifications.notify("Lounas", "Lounas!")
