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


class Api26SchedulerTakeoverServer(object):
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
        'uuid': 'str',
        'all': 'bool'
    }

    attribute_map = {
        'uuid': 'uuid',
        'all': 'all'
    }

    def __init__(self, uuid=None, all=None, local_vars_configuration=None):  # noqa: E501
        """Api26SchedulerTakeoverServer - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uuid = None
        self._all = None
        self.discriminator = None

        self.uuid = uuid
        self.all = all

    @property
    def uuid(self):
        """Gets the uuid of this Api26SchedulerTakeoverServer.  # noqa: E501


        :return: The uuid of this Api26SchedulerTakeoverServer.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this Api26SchedulerTakeoverServer.


        :param uuid: The uuid of this Api26SchedulerTakeoverServer.  # noqa: E501
        :type uuid: str
        """
        if self.local_vars_configuration.client_side_validation and uuid is None:  # noqa: E501
            raise ValueError("Invalid value for `uuid`, must not be `None`")  # noqa: E501

        self._uuid = uuid

    @property
    def all(self):
        """Gets the all of this Api26SchedulerTakeoverServer.  # noqa: E501


        :return: The all of this Api26SchedulerTakeoverServer.  # noqa: E501
        :rtype: bool
        """
        return self._all

    @all.setter
    def all(self, all):
        """Sets the all of this Api26SchedulerTakeoverServer.


        :param all: The all of this Api26SchedulerTakeoverServer.  # noqa: E501
        :type all: bool
        """
        if self.local_vars_configuration.client_side_validation and all is None:  # noqa: E501
            raise ValueError("Invalid value for `all`, must not be `None`")  # noqa: E501

        self._all = all

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
        if not isinstance(other, Api26SchedulerTakeoverServer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Api26SchedulerTakeoverServer):
            return True

        return self.to_dict() != other.to_dict()
