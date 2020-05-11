# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class UserDefinition(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, username: str=None, password: str=None, firstname: str=None, lastname: str=None):  # noqa: E501
        """UserDefinition - a model defined in Swagger

        :param username: The username of this UserDefinition.  # noqa: E501
        :type username: str
        :param password: The password of this UserDefinition.  # noqa: E501
        :type password: str
        :param firstname: The firstname of this UserDefinition.  # noqa: E501
        :type firstname: str
        :param lastname: The lastname of this UserDefinition.  # noqa: E501
        :type lastname: str
        """
        self.swagger_types = {
            'username': str,
            'password': str,
            'firstname': str,
            'lastname': str
        }

        self.attribute_map = {
            'username': 'username',
            'password': 'password',
            'firstname': 'firstname',
            'lastname': 'lastname'
        }
        self._username = username
        self._password = password
        self._firstname = firstname
        self._lastname = lastname

    @classmethod
    def from_dict(cls, dikt) -> 'UserDefinition':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UserDefinition of this UserDefinition.  # noqa: E501
        :rtype: UserDefinition
        """
        return util.deserialize_model(dikt, cls)

    @property
    def username(self) -> str:
        """Gets the username of this UserDefinition.


        :return: The username of this UserDefinition.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this UserDefinition.


        :param username: The username of this UserDefinition.
        :type username: str
        """

        self._username = username

    @property
    def password(self) -> str:
        """Gets the password of this UserDefinition.


        :return: The password of this UserDefinition.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password: str):
        """Sets the password of this UserDefinition.


        :param password: The password of this UserDefinition.
        :type password: str
        """

        self._password = password

    @property
    def firstname(self) -> str:
        """Gets the firstname of this UserDefinition.


        :return: The firstname of this UserDefinition.
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname: str):
        """Sets the firstname of this UserDefinition.


        :param firstname: The firstname of this UserDefinition.
        :type firstname: str
        """

        self._firstname = firstname

    @property
    def lastname(self) -> str:
        """Gets the lastname of this UserDefinition.


        :return: The lastname of this UserDefinition.
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname: str):
        """Sets the lastname of this UserDefinition.


        :param lastname: The lastname of this UserDefinition.
        :type lastname: str
        """

        self._lastname = lastname