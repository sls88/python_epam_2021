"""Homework 8.2."""
import sqlite3
from types import TracebackType
from typing import Any, NoReturn, Tuple, Union


class TableData:
    """Wrap class TableData for database table.

    When initialized with database name and table acts as collection object (implements Collection protocol)
    example: instance = TableData(database_name='example.sqlite', table_name='presidents')
    """

    def __init__(self, *, database_name: str, table_name: str) -> None:
        self.database_name = database_name
        self.table_name = table_name
        self.save = None

    def __len__(self) -> int:
        """Give current amount of rows in table in database.

        example: len(instance)
        Returns:
            The return value. Amount of rows in table in database
        """
        self.cursor.execute(f"SELECT count(*) from {self.table_name}")
        return self.cursor.fetchone()[0]

    def __contains__(self, item: str) -> bool:
        """Check whether there is a database entry with the same name.

        example: 'name' in instance
        Args:
            item: name

        Returns:
            The return value. True if available
        """
        command = f"SELECT name from {self.table_name} where name=:name"
        self.cursor.execute(command, {"name": item})
        data = self.cursor.fetchone()
        return data is not None

    def __getitem__(self, item: str) -> Union[NoReturn, Tuple[Any]]:
        """Return database entry if the name exists and it is a string.

        example: instance['smth_name'] - give an entry from the database with the corresponding name, if any
        if specified i['name_column'] - return entries of the specified column
        Args:
            item: name

        Returns:
            The return value. Database entry
        """
        if not isinstance(item, str):
            raise ValueError("The name should be string")
        self.cursor.execute(f"PRAGMA table_info({self.table_name});")
        for column in self.cursor.fetchall():
            if column[1] == item:
                return self.save[column[0]]
        command = f"SELECT * from {self.table_name} where name=:name"
        self.cursor.execute(command, {"name": item})
        data = self.cursor.fetchone()
        if not data:
            raise KeyError("The name does not exist")
        return data

    def __iter__(self) -> "TableData":
        """Return an instance of the iterator.

        Returns:
            The return value. Instance of the iterator
        """
        return self

    def __next__(self) -> Union["TableData", NoReturn]:
        """Return the next entry of the table from the sorted by name, in alphabetical order.

        Returns:
            The return value. TableData instance
        """
        if not self.save:
            command = f"SELECT * from {self.table_name} order by name asc limit 1"
            self.cursor.execute(command)
            self.save = self.cursor.fetchone()
            return self
        command = f"SELECT * from {self.table_name} where name > :name order by name"
        self.cursor.execute(command, {"name": self.save[0]})
        next_ent = self.cursor.fetchone()
        if next_ent is None:
            self.save = None
            raise StopIteration
        self.save = next_ent
        return self

    def __enter__(self) -> "TableData":
        """Open connection to database.

        Returns:
            The return value. TableData instance
        """
        self._conn = sqlite3.connect(self.database_name)
        self.cursor = self._conn.cursor()
        return self

    def __exit__(
        self, exc_type: Exception, exc_val: Exception, exc_tb: TracebackType
    ) -> None:
        """Close connection to database.

        Args:
            exc_type: The type of the caught exception, or None.
            exc_val: The caught exception object, or None.
            exc_tb: The stack trace for the caught exception, or None.

        Returns:
            The return value. None
        """
        self._conn.close()
