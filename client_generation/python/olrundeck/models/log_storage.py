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


class LogStorage(object):
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
        'enabled': 'bool',
        'plugin_name': 'str',
        'succeeded_count': 'float',
        'failed_count': 'float',
        'queued_count': 'float',
        'total_count': 'float',
        'incomplete_count': 'float',
        'missing_count': 'float'
    }

    attribute_map = {
        'enabled': 'enabled',
        'plugin_name': 'pluginName',
        'succeeded_count': 'succeededCount',
        'failed_count': 'failedCount',
        'queued_count': 'queuedCount',
        'total_count': 'totalCount',
        'incomplete_count': 'incompleteCount',
        'missing_count': 'missingCount'
    }

    def __init__(self, enabled=None, plugin_name=None, succeeded_count=None, failed_count=None, queued_count=None, total_count=None, incomplete_count=None, missing_count=None, local_vars_configuration=None):  # noqa: E501
        """LogStorage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._enabled = None
        self._plugin_name = None
        self._succeeded_count = None
        self._failed_count = None
        self._queued_count = None
        self._total_count = None
        self._incomplete_count = None
        self._missing_count = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if plugin_name is not None:
            self.plugin_name = plugin_name
        if succeeded_count is not None:
            self.succeeded_count = succeeded_count
        if failed_count is not None:
            self.failed_count = failed_count
        if queued_count is not None:
            self.queued_count = queued_count
        if total_count is not None:
            self.total_count = total_count
        if incomplete_count is not None:
            self.incomplete_count = incomplete_count
        if missing_count is not None:
            self.missing_count = missing_count

    @property
    def enabled(self):
        """Gets the enabled of this LogStorage.  # noqa: E501

        True if plugin is configured  # noqa: E501

        :return: The enabled of this LogStorage.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this LogStorage.

        True if plugin is configured  # noqa: E501

        :param enabled: The enabled of this LogStorage.  # noqa: E501
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def plugin_name(self):
        """Gets the plugin_name of this LogStorage.  # noqa: E501

        Name of the configured plugin  # noqa: E501

        :return: The plugin_name of this LogStorage.  # noqa: E501
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        """Sets the plugin_name of this LogStorage.

        Name of the configured plugin  # noqa: E501

        :param plugin_name: The plugin_name of this LogStorage.  # noqa: E501
        :type plugin_name: str
        """

        self._plugin_name = plugin_name

    @property
    def succeeded_count(self):
        """Gets the succeeded_count of this LogStorage.  # noqa: E501

        Number of successful storage requests  # noqa: E501

        :return: The succeeded_count of this LogStorage.  # noqa: E501
        :rtype: float
        """
        return self._succeeded_count

    @succeeded_count.setter
    def succeeded_count(self, succeeded_count):
        """Sets the succeeded_count of this LogStorage.

        Number of successful storage requests  # noqa: E501

        :param succeeded_count: The succeeded_count of this LogStorage.  # noqa: E501
        :type succeeded_count: float
        """

        self._succeeded_count = succeeded_count

    @property
    def failed_count(self):
        """Gets the failed_count of this LogStorage.  # noqa: E501

        Number of failed storage requests  # noqa: E501

        :return: The failed_count of this LogStorage.  # noqa: E501
        :rtype: float
        """
        return self._failed_count

    @failed_count.setter
    def failed_count(self, failed_count):
        """Sets the failed_count of this LogStorage.

        Number of failed storage requests  # noqa: E501

        :param failed_count: The failed_count of this LogStorage.  # noqa: E501
        :type failed_count: float
        """

        self._failed_count = failed_count

    @property
    def queued_count(self):
        """Gets the queued_count of this LogStorage.  # noqa: E501

        Number of queued storage requests  # noqa: E501

        :return: The queued_count of this LogStorage.  # noqa: E501
        :rtype: float
        """
        return self._queued_count

    @queued_count.setter
    def queued_count(self, queued_count):
        """Sets the queued_count of this LogStorage.

        Number of queued storage requests  # noqa: E501

        :param queued_count: The queued_count of this LogStorage.  # noqa: E501
        :type queued_count: float
        """

        self._queued_count = queued_count

    @property
    def total_count(self):
        """Gets the total_count of this LogStorage.  # noqa: E501

        Total number of storage requests (currently queued plus previously processed)  # noqa: E501

        :return: The total_count of this LogStorage.  # noqa: E501
        :rtype: float
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this LogStorage.

        Total number of storage requests (currently queued plus previously processed)  # noqa: E501

        :param total_count: The total_count of this LogStorage.  # noqa: E501
        :type total_count: float
        """

        self._total_count = total_count

    @property
    def incomplete_count(self):
        """Gets the incomplete_count of this LogStorage.  # noqa: E501

        Number of storage requests which have not completed successfully  # noqa: E501

        :return: The incomplete_count of this LogStorage.  # noqa: E501
        :rtype: float
        """
        return self._incomplete_count

    @incomplete_count.setter
    def incomplete_count(self, incomplete_count):
        """Sets the incomplete_count of this LogStorage.

        Number of storage requests which have not completed successfully  # noqa: E501

        :param incomplete_count: The incomplete_count of this LogStorage.  # noqa: E501
        :type incomplete_count: float
        """

        self._incomplete_count = incomplete_count

    @property
    def missing_count(self):
        """Gets the missing_count of this LogStorage.  # noqa: E501

        Number of executions for this cluster node which have no associated storage requests  # noqa: E501

        :return: The missing_count of this LogStorage.  # noqa: E501
        :rtype: float
        """
        return self._missing_count

    @missing_count.setter
    def missing_count(self, missing_count):
        """Sets the missing_count of this LogStorage.

        Number of executions for this cluster node which have no associated storage requests  # noqa: E501

        :param missing_count: The missing_count of this LogStorage.  # noqa: E501
        :type missing_count: float
        """

        self._missing_count = missing_count

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
        if not isinstance(other, LogStorage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LogStorage):
            return True

        return self.to_dict() != other.to_dict()
