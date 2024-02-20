#!/usr/bin/env python3
""" module for filtered_logger """


def filter_datum(fields, redaction, message, separator):
    """
    Filters and redacts sensitive data from a message
    """
    for field in fields:  # for each field in fields
        start = message.find(field + "=")  # find the start of the field
        end = message.find(separator, start)  # find the end of the field
        if start != -1 and end != -1:  # if the field is found
            end += len(separator)  # add the length of the separator to the end
            message = message[:start] + field + "=" + \
                redaction + separator + message[end:]  # redact the field
    return message  # return the redacted message
