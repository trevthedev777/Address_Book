# -*- coding: utf-8 -*-
# Address_book/main.py

"""This module provides RP Contacts application."""

import sys

from PyQt5.QtWidgets import QApplication

from .database import createConnection
from .views import Window


def main():
    """RP Contacts main function."""
    # Create The Application
    app = QApplication(sys.argv)
    # Connect tio the database before creating any window
    if not createConnection("contacts.sqlite"):
        sys.exit(1)
    # Create The Main Window if the connection succeeds
    win = Window()
    win.show()
    #  Run The Event Loop
    sys.exit(app.exec())
