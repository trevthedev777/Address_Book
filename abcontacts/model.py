# -*- coding: utf-8 -*-
# abcontacts/model.py

"""This module provides the model to manage the contacts table"""

from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel

# Create the Contact Model


class ContactsModel:
    def __init__(self):
        self.model = self._createModel()

    # Create the layout and functionality

    @staticmethod
    def _createModel():
        """Create and set up the model."""
        tableModel = QSqlTableModel()
        tableModel.setTable("contacts")
        # With this, you ensure that the changeson the model get saved into the databaseimmediately
        tableModel.setEditStrategy(QSqlTableModel.OnFieldChange)
        tableModel.select()
        # headers
        headers = ("ID", "Name", "Job", "Email", "Contact No.", "Address")

        for columnIndex, header in enumerate(headers):
            tableModel.setHeaderData(columnIndex, Qt.Horizontal, header)
        return tableModel

    def addContact(self, data):
        """Add a Contact to the database"""
        # gets the current number of rows in the data model.
        rows = self.model.rowCount()
        # inserts a new row at the end of the data model
        self.model.insertRows(rows, 1)

        #  inserts every item in data into the corresponding cell in the data model
        for column_index, field in enumerate(data):
            self.model.setData(self.model.index(rows, column_index + 1), field)

        # submits the changes to the database by calling .submitAll() on the model
        self.model.submitAll()
        # reloads the data from the database into the model
        self.model.select()

    # Delete Contact
    def deleteContact(self, row):
        """Removes a contact from the database"""
        self.model.removeRow(row)
        self.model.submitAll()
        self.model.select()

    # Clear All Contacts
    def clearContacts(self):
        """Remove all contacts in the database"""
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.removeRows(0, self.model.rowCount())
        self.model.submitAll()
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()


# Learning Object 6
# learning object 9.1
# Can not pyhsically deploy my app to a cloud based solution
