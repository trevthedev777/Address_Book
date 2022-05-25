# -*- coding: utf-8 -*-

"""This module provides views to manage the contacts table."""

from PyQt.QtWidgets import (
    QHBoxlayout,
    QMainWindow,
    QWidget,
)


class Window(QMainWindow):

    """Main Window."""

    def __init__(self, parent=None):
        """Initializer"""
        super().init(parent)
        self.setWindowTitle("RP Contacts")
        self.resize(550, 250)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setlayout(self.layout)
