# -*- coding: utf-8 -*-

"""This module provides views to manage the contacts table."""

# Classes to Import
from tkinter import dialog
from PyQt5 import Qt
from PyQt5.QtWidgets import (
    QAbstractItemView,  # To provide access to the table view selection behavior policy
    QDialog,  # Create Dialog Boxes
    QDialogButtonBox,
    QFormLayout,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QMessageBox,
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

# Dialog Box


class AddDialog(QDialog):
    """Add Contact Dialog"""

    def __init__(self, parent=None):
        """Initializer"""
        super().__init__(parent=parent)
        self.setWindowTitle("Add Contact")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.data = None  # The data the user provides

        self.setupUI()

    def setupUI(self):
        """Setup the Add Contact dialog's GUI"""
        # Create line edits for data fields
        self.nameField = QLineEdit()
        self.nameField.setObjectName("Name")
        self.jobField = QLineEdit
        self.jobField.setObjectName("Job")
        self.emailField = QLineEdit()
        self.emailField.setObjectName("Email")
        self.numberField = QLineEdit()
        self.numberField.setObjectName("Contact No.")
        self.addressField = QLineEdit()
        self.addressField.setObjectName("Address")

        # Layout the data Fields
        layout = QFormLayout()
        layout.addRow("Name:", self.nameField)
        layout.addRow("Job:", self.jobField)
        layout.addRow("Email:", self.emailField)
        layout.addRow("Contact No.:", self.numberField)
        layout.addRow("Address:", self.addressField)
        self.layout.addLayout(layout)

        # Add Buttons to GUI
        self.addButton = ("Add...")
        self.addButton.clicked.connect(self.openAddDialog)

        # Add standard buttons to the dialog and connect them
        self.buttonsBox = QDialogButtonBox(self)
        self.buttonsBox.setOrientation(Qt.Horizontal)
        self.buttonsBox.setStandardButtons(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )
        self.buttonsBox.accepted.connect(self.accept)
        self.buttonsBox.rejected.connect(self.reject)
        self.layout.addWidget(self.buttonsBox)

    # Form Validation
    def accept(self):
        """Accept the data provided through the dialog"""
        self.data = []

        # checks if the user has provided data for each field in the dialog.
        for field in (self.nameField, self.jobField, self.emailField, self.numberField, self.addressField):
            # If not, then the dialog shows an error message that warns the user about the missing data
            if not field.text():
                QMessageBox.critical(
                    self,
                    "Error!",
                    f"You must provide a contact's {field.objectName()}"
                )
                # Reset .data
                self.data = None
                return

            self.data.append(field.text())

        if not self.data:
            return

        super().accept()

    def openAddDialog(self):
        """Open The Add Contact Dialog"""
        dialog = AddDialog(self)
        if dialog.exec() == QDialog.Accepted:
            self.contactsModel.addContact(dialog.data)
            self.table.resizeColumnsToContents()
