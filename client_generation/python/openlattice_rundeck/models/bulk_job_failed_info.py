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


class BulkJobFailedInfo(object):
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
        'id': 'str',
        'error_code': 'str',
        'message': 'str'
    }

    attribute_map = {
        'id': 'id',
        'error_code': 'errorCode',
        'message': 'message'
    }

    def __init__(self, id=None, error_code=None, message=None, local_vars_configuration=None):  # noqa: E501
        """BulkJobFailedInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._error_code = None
        self._message = None
        self.discriminator = None

        self.id = id
        self.error_code = error_code
        self.message = message

    @property
    def id(self):
        """Gets the id of this BulkJobFailedInfo.  # noqa: E501


        :return: The id of this BulkJobFailedInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BulkJobFailedInfo.


        :param id: The id of this BulkJobFailedInfo.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def error_code(self):
        """Gets the error_code of this BulkJobFailedInfo.  # noqa: E501


        :return: The error_code of this BulkJobFailedInfo.  # noqa: E501
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this BulkJobFailedInfo.


        :param error_code: The error_code of this BulkJobFailedInfo.  # noqa: E501
        :type error_code: str
        """
        if self.local_vars_configuration.client_side_validation and error_code is None:  # noqa: E501
            raise ValueError("Invalid value for `error_code`, must not be `None`")  # noqa: E501

        self._error_code = error_code

    @property
    def message(self):
        """Gets the message of this BulkJobFailedInfo.  # noqa: E501


        :return: The message of this BulkJobFailedInfo.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this BulkJobFailedInfo.


        :param message: The message of this BulkJobFailedInfo.  # noqa: E501
        :type message: str
        """
        if self.local_vars_configuration.client_side_validation and message is None:  # noqa: E501
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

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
        if not isinstance(other, BulkJobFailedInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BulkJobFailedInfo):
            return True

        return self.to_dict() != other.to_dict()
