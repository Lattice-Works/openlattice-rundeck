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


class JobBulkOperationResponse(object):
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
        'request_count': 'float',
        'allsuccessful': 'bool',
        'succeeded': 'list[BulkJobSucceededInfo]',
        'failed': 'list[BulkJobFailedInfo]'
    }

    attribute_map = {
        'request_count': 'requestCount',
        'allsuccessful': 'allsuccessful',
        'succeeded': 'succeeded',
        'failed': 'failed'
    }

    def __init__(self, request_count=None, allsuccessful=None, succeeded=None, failed=None, local_vars_configuration=None):  # noqa: E501
        """JobBulkOperationResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._request_count = None
        self._allsuccessful = None
        self._succeeded = None
        self._failed = None
        self.discriminator = None

        self.request_count = request_count
        self.allsuccessful = allsuccessful
        if succeeded is not None:
            self.succeeded = succeeded
        if failed is not None:
            self.failed = failed

    @property
    def request_count(self):
        """Gets the request_count of this JobBulkOperationResponse.  # noqa: E501

        The number of job IDs that were in the delete request.  # noqa: E501

        :return: The request_count of this JobBulkOperationResponse.  # noqa: E501
        :rtype: float
        """
        return self._request_count

    @request_count.setter
    def request_count(self, request_count):
        """Sets the request_count of this JobBulkOperationResponse.

        The number of job IDs that were in the delete request.  # noqa: E501

        :param request_count: The request_count of this JobBulkOperationResponse.  # noqa: E501
        :type request_count: float
        """
        if self.local_vars_configuration.client_side_validation and request_count is None:  # noqa: E501
            raise ValueError("Invalid value for `request_count`, must not be `None`")  # noqa: E501

        self._request_count = request_count

    @property
    def allsuccessful(self):
        """Gets the allsuccessful of this JobBulkOperationResponse.  # noqa: E501


        :return: The allsuccessful of this JobBulkOperationResponse.  # noqa: E501
        :rtype: bool
        """
        return self._allsuccessful

    @allsuccessful.setter
    def allsuccessful(self, allsuccessful):
        """Sets the allsuccessful of this JobBulkOperationResponse.


        :param allsuccessful: The allsuccessful of this JobBulkOperationResponse.  # noqa: E501
        :type allsuccessful: bool
        """
        if self.local_vars_configuration.client_side_validation and allsuccessful is None:  # noqa: E501
            raise ValueError("Invalid value for `allsuccessful`, must not be `None`")  # noqa: E501

        self._allsuccessful = allsuccessful

    @property
    def succeeded(self):
        """Gets the succeeded of this JobBulkOperationResponse.  # noqa: E501


        :return: The succeeded of this JobBulkOperationResponse.  # noqa: E501
        :rtype: list[BulkJobSucceededInfo]
        """
        return self._succeeded

    @succeeded.setter
    def succeeded(self, succeeded):
        """Sets the succeeded of this JobBulkOperationResponse.


        :param succeeded: The succeeded of this JobBulkOperationResponse.  # noqa: E501
        :type succeeded: list[BulkJobSucceededInfo]
        """

        self._succeeded = succeeded

    @property
    def failed(self):
        """Gets the failed of this JobBulkOperationResponse.  # noqa: E501


        :return: The failed of this JobBulkOperationResponse.  # noqa: E501
        :rtype: list[BulkJobFailedInfo]
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """Sets the failed of this JobBulkOperationResponse.


        :param failed: The failed of this JobBulkOperationResponse.  # noqa: E501
        :type failed: list[BulkJobFailedInfo]
        """

        self._failed = failed

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
        if not isinstance(other, JobBulkOperationResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JobBulkOperationResponse):
            return True

        return self.to_dict() != other.to_dict()
