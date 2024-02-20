#!/usr/bin/env python3
""" module for filtered_logger """


def filter_datum(fields, redaction, message, separator):
    """ returns the log message obfuscated """
    for field in fields:
        message = message.replace(field + separator,
                                  field + redaction + separator)
    return message
