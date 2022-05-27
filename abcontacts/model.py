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
