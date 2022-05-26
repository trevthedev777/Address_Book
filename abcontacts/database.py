# -*- coding: utf-8 -*-
# abcontacts/database.py

"""This module provides a database connection"""

# Import PyQt Classes
from PyQt5.QtWidgets import QMessageBox
# QSqlQuery to execute and manipulate SQL statements.
from PyQt5.QtSql import QSqlDatabase, QSqlQuery


def _createContactsTable():
    """Create the contacts table in the database"""
    createTableQuery = QSqlQuery()
    return createTableQuery.exec(
        """
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            name VARCHAR(40) NOT NULL,
            job VARCHAR(50),
            email VARCHAR(40) NOT NULL
        )
        """
    )


# argument holds the name or path to the physical SQLite database file on the system
def createConnection(databaseName):
    """Create and open a database connection"""

    # Create the Database Connection
    connection = QSqlDatabase.addDatabase("QSQLITE")
    # sets the filename or the path to the database
    connection.setDatabaseName(databaseName)

    if not connection.open():
        # If connection is unsuccessful
        QMessageBox.warning(
            None,
            "abcontact",
            f"Database Error: {connection.lastError().text()}",
        )
        return False

    #  This ensures that the application creates the contacts table before doing any operations on the database
    _createContactsTable()
    # If connection is successful
    return True
