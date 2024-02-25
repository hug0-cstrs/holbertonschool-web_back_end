#!/usr/bin/env python3
"""Basic auth"""
from base64 import b64decode, binascii
from typing import TypeVar

from api.v1.auth.auth import Auth
from models.user import User


class BasicAuth(Auth):
    """ Basic Auth class """

    def extract_base64_authorization_header(
        self,
        authorization_header: str
    ) -> str:
        """
            Extract header in base64
        """
        if authorization_header is None\
           or type(authorization_header) != str\
           or not authorization_header.startswith('Basic ')\
           and not authorization_header.endswith(' '):

            return None

        return authorization_header.split(' ')[1]

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str
    ) -> str:
        """
        returns the decoded value of
        a Base64 string base64_authorization_header:
        """
        if base64_authorization_header is None\
           or type(base64_authorization_header) != str:
            return None
        try:
            decode_bytes = b64decode(base64_authorization_header)
        except binascii.Error as error:
            return None
        return decode_bytes.decode('utf-8')

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """
            Basic - User credentials
        """
        if decoded_base64_authorization_header is None or\
           type(decoded_base64_authorization_header) != str or\
           ':' not in decoded_base64_authorization_header:

            return (None, None)

        credentials_user = decoded_base64_authorization_header.split(':', 1)

        return (credentials_user[0], credentials_user[1])

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str
    ) -> TypeVar('User'):
        """Basic - User object"""
        if user_email is None or type(user_email) != str:
            return None
        if user_pwd is None or type(user_pwd) != str:
            return None
        try:
            usr_found = User.search({'email': user_email})
        except Exception:
            return None
        for user in usr_found:
            if user.is_valid_password(user_pwd):
                return user

    def current_user(
            self, request=None
    ) -> TypeVar('User'):
        """Basic - Overload current_user - and BOOM!"""
        authorization = self.authorization_header(request)
        if not authorization:
            return None
        extract = self.extract_base64_authorization_header(authorization)
        if not extract:
            return None
        decode_base64 = self.decode_base64_authorization_header(extract)
        if not decode_base64:
            return None
        email, pwd = self.extract_user_credentials(decode_base64)
        if not email or not pwd:
            return None
        user = self.user_object_from_credentials(email, pwd)
        return user
