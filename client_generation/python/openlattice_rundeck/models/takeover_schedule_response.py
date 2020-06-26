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

from openlattice_rundeck.configuration import Configuration


class TakeoverScheduleResponse(object):
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
        'takeover_schedule': 'object',
        '_self': 'object',
        'message': 'str',
        'apiversion': 'float',
        'success': 'bool'
    }

    attribute_map = {
        'takeover_schedule': 'takeoverSchedule',
        '_self': 'self',
        'message': 'message',
        'apiversion': 'apiversion',
        'success': 'success'
    }

    def __init__(self, takeover_schedule=None, _self=None, message=None, apiversion=None, success=None, local_vars_configuration=None):  # noqa: E501
        """TakeoverScheduleResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._takeover_schedule = None
        self.__self = None
        self._message = None
        self._apiversion = None
        self._success = None
        self.discriminator = None

        if takeover_schedule is not None:
            self.takeover_schedule = takeover_schedule
        if _self is not None:
            self._self = _self
        if message is not None:
            self.message = message
        if apiversion is not None:
            self.apiversion = apiversion
        if success is not None:
            self.success = success

    @property
    def takeover_schedule(self):
        """Gets the takeover_schedule of this TakeoverScheduleResponse.  # noqa: E501


        :return: The takeover_schedule of this TakeoverScheduleResponse.  # noqa: E501
        :rtype: object
        """
        return self._takeover_schedule

    @takeover_schedule.setter
    def takeover_schedule(self, takeover_schedule):
        """Sets the takeover_schedule of this TakeoverScheduleResponse.


        :param takeover_schedule: The takeover_schedule of this TakeoverScheduleResponse.  # noqa: E501
        :type takeover_schedule: object
        """

        self._takeover_schedule = takeover_schedule

    @property
    def _self(self):
        """Gets the _self of this TakeoverScheduleResponse.  # noqa: E501


        :return: The _self of this TakeoverScheduleResponse.  # noqa: E501
        :rtype: object
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this TakeoverScheduleResponse.


        :param _self: The _self of this TakeoverScheduleResponse.  # noqa: E501
        :type _self: object
        """

        self.__self = _self

    @property
    def message(self):
        """Gets the message of this TakeoverScheduleResponse.  # noqa: E501


        :return: The message of this TakeoverScheduleResponse.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this TakeoverScheduleResponse.


        :param message: The message of this TakeoverScheduleResponse.  # noqa: E501
        :type message: str
        """

        self._message = message

    @property
    def apiversion(self):
        """Gets the apiversion of this TakeoverScheduleResponse.  # noqa: E501


        :return: The apiversion of this TakeoverScheduleResponse.  # noqa: E501
        :rtype: float
        """
        return self._apiversion

    @apiversion.setter
    def apiversion(self, apiversion):
        """Sets the apiversion of this TakeoverScheduleResponse.


        :param apiversion: The apiversion of this TakeoverScheduleResponse.  # noqa: E501
        :type apiversion: float
        """

        self._apiversion = apiversion

    @property
    def success(self):
        """Gets the success of this TakeoverScheduleResponse.  # noqa: E501


        :return: The success of this TakeoverScheduleResponse.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this TakeoverScheduleResponse.


        :param success: The success of this TakeoverScheduleResponse.  # noqa: E501
        :type success: bool
        """

        self._success = success

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
        if not isinstance(other, TakeoverScheduleResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TakeoverScheduleResponse):
            return True

        return self.to_dict() != other.to_dict()