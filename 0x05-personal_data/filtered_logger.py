#!/usr/bin/env python3
"""
logging file
"""
from typing import List
import re
import logging
import os
import mysql.connector

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Function that return the log message obfuscated"""
    for i in fields:
        message = re.sub(fr'{i}=.*?{separator}',
                         f'{i}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Constructor method"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format method to filter values in incoming log records
            using filter_datum"""
        formato = filter_datum(self.fields, self.REDACTION,
                               super().format(record), self.SEPARATOR)
        return formato


def get_logger() -> logging.Logger:
    """ Get logger method"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Get DB method that return connector to the database"""
    cnx = mysql.connector.connect(
                     user=os.environ.get('PERSONAL_DATA_DB_USERNAME'),
                     password=os.environ.get('PERSONAL_DATA_DB_PASSWORD', ''),
                     host=os.environ.get('PERSONAL_DATA_DB_HOST', 'localhost'),
                     database=os.environ.get('PERSONAL_DATA_DB_NAME', 'root'))
    return cnx
