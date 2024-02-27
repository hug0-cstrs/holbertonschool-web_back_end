#!/usr/bin/env python3
""" Auth module """

import uuid

import bcrypt
from db import DB
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import User


def _hash_password(password: str) -> str:
    """ _hash_password: returns a salted hash of the input password
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """ _generate_uuid: returns a string representation of a new UUID
    """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ register_user: returns a User object
        """
        try:
            # Check if user already exists
            self._db.find_user_by(email=email)
            raise ValueError(f'User {email} already exists')
        except NoResultFound:
            # Add user to the database
            return self._db.add_user(email, _hash_password(password))

    def valid_login(self, email: str, password: str) -> bool:
        """ valid_login: returns a boolean
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode('utf-8'),
                                  user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """ create_session: returns the session ID as a string
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def valid_login(self, email: str, password: str) -> bool:
        """Credentials validation"""
        exists = True
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            exists = False

        if exists:
            byte_obj = bytes(password, 'utf-8')
            if bcrypt.checkpw(byte_obj, user.hashed_password):
                return True

        return False
