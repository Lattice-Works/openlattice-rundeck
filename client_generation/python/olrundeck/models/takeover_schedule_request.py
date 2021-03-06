# coding: utf-8

"""
    Rundeck

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from olrundeck.configuration import Configuration


class TakeoverScheduleRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'server': 'object',
        'project': 'str',
        'job': 'object'
    }

    attribute_map = {
        'server': 'server',
        'project': 'project',
        'job': 'job'
    }

    def __init__(self, server=None, project=None, job=None, local_vars_configuration=None):  # noqa: E501
        """TakeoverScheduleRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._server = None
        self._project = None
        self._job = None
        self.discriminator = None

        if server is not None:
            self.server = server
        if project is not None:
            self.project = project
        if job is not None:
            self.job = job

    @property
    def server(self):
        """Gets the server of this TakeoverScheduleRequest.  # noqa: E501


        :return: The server of this TakeoverScheduleRequest.  # noqa: E501
        :rtype: object
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this TakeoverScheduleRequest.


        :param server: The server of this TakeoverScheduleRequest.  # noqa: E501
        :type server: object
        """

        self._server = server

    @property
    def project(self):
        """Gets the project of this TakeoverScheduleRequest.  # noqa: E501


        :return: The project of this TakeoverScheduleRequest.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this TakeoverScheduleRequest.


        :param project: The project of this TakeoverScheduleRequest.  # noqa: E501
        :type project: str
        """

        self._project = project

    @property
    def job(self):
        """Gets the job of this TakeoverScheduleRequest.  # noqa: E501


        :return: The job of this TakeoverScheduleRequest.  # noqa: E501
        :rtype: object
        """
        return self._job

    @job.setter
    def job(self, job):
        """Sets the job of this TakeoverScheduleRequest.


        :param job: The job of this TakeoverScheduleRequest.  # noqa: E501
        :type job: object
        """

        self._job = job

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TakeoverScheduleRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TakeoverScheduleRequest):
            return True

        return self.to_dict() != other.to_dict()
