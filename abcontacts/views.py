# -*- coding: utf-8 -*-

"""This module provides views to manage the contacts table."""

# Classes to Import
from PyQt5.QtWidgets import (
    QAbstractItemView,  # To provide access to the table view selection behavior policy
    QHBoxLayout,
    QMainWindow,
    QPushButton,  # Create Add, Del, Del All Button
    QTableView,   # To provide the table-like view that displays the contacts list
    QVBoxLayout,
    QWidget,
)

# Import the model
from .model import ContactsModel


# Generate the APPs Main Window
class Window(QMainWindow):

    """Main Window."""

    def __init__(self, parent=None):
        """Initializer"""

        super().__init__(parent)
        self.setWindowTitle("book")
        self.resize(550, 250)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)
        self.contactsModel = ContactsModel()

        self.setupUI()

    def setupUI(self):
        """Setup the main window's GUI"""

        # Create the table view widget
        self.table = QTableView()
        self.table.setModel(self.contactsModel.model)

        # Allows that the whole row is selected
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.resizeColumnsToContents()

        # Create Buttons
        self.addButton = QPushButton("Add...")
        self.deleteButton = QPushButton("Delete")
        self.clearAllButton = QPushButton("Clear All")

        # GUI Layout
        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.deleteButton)
        layout.addStretch()
        layout.addWidget(self.clearAllButton)
        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)
