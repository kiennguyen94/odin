# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class KeyValueDefinition(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, key: str=None, value: str=None):  # noqa: E501
        """KeyValueDefinition - a model defined in Swagger

        :param key: The key of this KeyValueDefinition.  # noqa: E501
        :type key: str
        :param value: The value of this KeyValueDefinition.  # noqa: E501
        :type value: str
        """
        self.swagger_types = {
            'key': str,
            'value': str
        }

        self.attribute_map = {
            'key': 'key',
            'value': 'value'
        }
        self._key = key
        self._value = value

    @classmethod
    def from_dict(cls, dikt) -> 'KeyValueDefinition':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The KeyValueDefinition of this KeyValueDefinition.  # noqa: E501
        :rtype: KeyValueDefinition
        """
        return util.deserialize_model(dikt, cls)

    @property
    def key(self) -> str:
        """Gets the key of this KeyValueDefinition.


        :return: The key of this KeyValueDefinition.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key: str):
        """Sets the key of this KeyValueDefinition.


        :param key: The key of this KeyValueDefinition.
        :type key: str
        """

        self._key = key

    @property
    def value(self) -> str:
        """Gets the value of this KeyValueDefinition.


        :return: The value of this KeyValueDefinition.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str):
        """Sets the value of this KeyValueDefinition.


        :param value: The value of this KeyValueDefinition.
        :type value: str
        """

        self._value = value