#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
            add_user: returns a user object
            and save the user to the database
        """

        user = User()
        user.email = email
        user.hashed_password = hashed_password
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """
            find_user_by: returns the first row found
            in the users table as filtered by the method's input arguments
        """
        if not kwargs:
            raise InvalidRequestError
        user = self._session.query(User).filter_by(**kwargs).first()
        if user is None:
            raise NoResultFound
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        update_user: updates the user's attributes as passed
        in the method's arguments
        """
        # Find the user by the provided user_id
        try:
            user = self.find_user_by(id=user_id)
        except (InvalidRequestError, NoResultFound):
            return

        # Update the user's attributes based on the provided arguments
        for k, v in kwargs.items():
            if hasattr(user, k):  # check if the user object has the attribute
                # Ensure that the user object has the attribute
                setattr(user, k, v)
            else:
                raise ValueError

        # Commit the changes to the database
        self._session.commit()

        # Return None
        return None
