# -*- coding: utf-8 -*-
# Address_book/main.py

"""This module provides AB Contacts application."""

import sys

from PyQt5.QtWidgets import QApplication

from .views import Window


def main():
    """RP Contacts main function."""
    # Create The Application
    app = QApplication(sys.argv)
    # Create The Main Window
    win = Window()
    win.show()
    #  Run The Event Loop
    sys.exit(app.exec())
