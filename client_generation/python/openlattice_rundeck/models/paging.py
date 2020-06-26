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


class Paging(object):
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
        'count': 'int',
        'total': 'int',
        'offset': 'int',
        'max': 'int'
    }

    attribute_map = {
        'count': 'count',
        'total': 'total',
        'offset': 'offset',
        'max': 'max'
    }

    def __init__(self, count=None, total=None, offset=None, max=None, local_vars_configuration=None):  # noqa: E501
        """Paging - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._count = None
        self._total = None
        self._offset = None
        self._max = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if total is not None:
            self.total = total
        if offset is not None:
            self.offset = offset
        if max is not None:
            self.max = max

    @property
    def count(self):
        """Gets the count of this Paging.  # noqa: E501


        :return: The count of this Paging.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this Paging.


        :param count: The count of this Paging.  # noqa: E501
        :type count: int
        """

        self._count = count

    @property
    def total(self):
        """Gets the total of this Paging.  # noqa: E501


        :return: The total of this Paging.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this Paging.


        :param total: The total of this Paging.  # noqa: E501
        :type total: int
        """

        self._total = total

    @property
    def offset(self):
        """Gets the offset of this Paging.  # noqa: E501


        :return: The offset of this Paging.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this Paging.


        :param offset: The offset of this Paging.  # noqa: E501
        :type offset: int
        """

        self._offset = offset

    @property
    def max(self):
        """Gets the max of this Paging.  # noqa: E501


        :return: The max of this Paging.  # noqa: E501
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this Paging.


        :param max: The max of this Paging.  # noqa: E501
        :type max: int
        """

        self._max = max

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
        if not isinstance(other, Paging):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Paging):
            return True

        return self.to_dict() != other.to_dict()
