#!/usr/bin/env python3
""" Module of Basic Authentication"""

from api.v1.auth.auth import Auth
from base64 import b64decode


class BasicAuth(Auth):
    """ Class to manage the API authentication """
    pass

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Method that returns the Base64 part of the Authorization header
        for a Basic Authentication
        """
        if (authorization_header is None or
                not isinstance(authorization_header, str) or
                not authorization_header.startswith("Basic ")):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ Method that returns the decoded value of a Base64 string
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            encoded = base64_authorization_header.encode('utf-8')
            decoded64 = b64decode(encoded)
            decoded = decoded64.decode('utf-8')
        except BaseException:
            return None

        return decoded

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ Method that returns the user email and password from
        the Base64 decoded value
        """
        if (decoded_base64_authorization_header is None or
                not isinstance(decoded_base64_authorization_header, str) or
                ":" not in decoded_base64_authorization_header):
            return (None, None)
        return tuple(decoded_base64_authorization_header.split(":", 1))
