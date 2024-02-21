#!/usr/bin/env python3
""" Module of Authentication
"""

from typing import List, TypeVar

from flask import request


class Auth:
    """ Class to manage the API authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method for validating if endpoint requires auth """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        if not path.endswith('/'):
            path = path + '/'

        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Method that handles authorization header """
        if request is None:
            return None

    def current_user(self, request=None) -> TypeVar("User"):
        """ Validates current user """
        return None
