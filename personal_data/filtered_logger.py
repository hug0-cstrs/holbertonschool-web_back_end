#!/usr/bin/env python3
""" module for filtered_logger """

import re


def filter_datum(fields, redaction, message, separator):
    """ returns the log message obfuscated """
    regex = r'({}=)(.*?)(?={}|$)'.format('|'.join(fields), separator)
    return re.sub(regex, lambda x: '{}={}'.format(x.group(1),
                                                  redaction), message)
