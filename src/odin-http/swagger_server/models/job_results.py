# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.job_definition import JobDefinition  # noqa: F401,E501
from swagger_server import util


class JobResults(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, jobs: List[JobDefinition]=None):  # noqa: E501
        """JobResults - a model defined in Swagger

        :param jobs: The jobs of this JobResults.  # noqa: E501
        :type jobs: List[JobDefinition]
        """
        self.swagger_types = {
            'jobs': List[JobDefinition]
        }

        self.attribute_map = {
            'jobs': 'jobs'
        }
        self._jobs = jobs

    @classmethod
    def from_dict(cls, dikt) -> 'JobResults':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The JobResults of this JobResults.  # noqa: E501
        :rtype: JobResults
        """
        return util.deserialize_model(dikt, cls)

    @property
    def jobs(self) -> List[JobDefinition]:
        """Gets the jobs of this JobResults.


        :return: The jobs of this JobResults.
        :rtype: List[JobDefinition]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs: List[JobDefinition]):
        """Sets the jobs of this JobResults.


        :param jobs: The jobs of this JobResults.
        :type jobs: List[JobDefinition]
        """

        self._jobs = jobs