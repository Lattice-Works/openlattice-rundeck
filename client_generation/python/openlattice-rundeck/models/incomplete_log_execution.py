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

from openlattice-rundeck.configuration import Configuration


class IncompleteLogExecution(object):
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
        'project': 'str',
        'href': 'str',
        'permalink': 'str',
        'storage': 'object',
        'errors': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'project': 'project',
        'href': 'href',
        'permalink': 'permalink',
        'storage': 'storage',
        'errors': 'errors'
    }

    def __init__(self, id=None, project=None, href=None, permalink=None, storage=None, errors=None, local_vars_configuration=None):  # noqa: E501
        """IncompleteLogExecution - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._project = None
        self._href = None
        self._permalink = None
        self._storage = None
        self._errors = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if project is not None:
            self.project = project
        if href is not None:
            self.href = href
        if permalink is not None:
            self.permalink = permalink
        if storage is not None:
            self.storage = storage
        if errors is not None:
            self.errors = errors

    @property
    def id(self):
        """Gets the id of this IncompleteLogExecution.  # noqa: E501


        :return: The id of this IncompleteLogExecution.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IncompleteLogExecution.


        :param id: The id of this IncompleteLogExecution.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def project(self):
        """Gets the project of this IncompleteLogExecution.  # noqa: E501


        :return: The project of this IncompleteLogExecution.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this IncompleteLogExecution.


        :param project: The project of this IncompleteLogExecution.  # noqa: E501
        :type project: str
        """

        self._project = project

    @property
    def href(self):
        """Gets the href of this IncompleteLogExecution.  # noqa: E501


        :return: The href of this IncompleteLogExecution.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this IncompleteLogExecution.


        :param href: The href of this IncompleteLogExecution.  # noqa: E501
        :type href: str
        """

        self._href = href

    @property
    def permalink(self):
        """Gets the permalink of this IncompleteLogExecution.  # noqa: E501


        :return: The permalink of this IncompleteLogExecution.  # noqa: E501
        :rtype: str
        """
        return self._permalink

    @permalink.setter
    def permalink(self, permalink):
        """Sets the permalink of this IncompleteLogExecution.


        :param permalink: The permalink of this IncompleteLogExecution.  # noqa: E501
        :type permalink: str
        """

        self._permalink = permalink

    @property
    def storage(self):
        """Gets the storage of this IncompleteLogExecution.  # noqa: E501


        :return: The storage of this IncompleteLogExecution.  # noqa: E501
        :rtype: object
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this IncompleteLogExecution.


        :param storage: The storage of this IncompleteLogExecution.  # noqa: E501
        :type storage: object
        """

        self._storage = storage

    @property
    def errors(self):
        """Gets the errors of this IncompleteLogExecution.  # noqa: E501


        :return: The errors of this IncompleteLogExecution.  # noqa: E501
        :rtype: list[str]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this IncompleteLogExecution.


        :param errors: The errors of this IncompleteLogExecution.  # noqa: E501
        :type errors: list[str]
        """

        self._errors = errors

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
        if not isinstance(other, IncompleteLogExecution):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IncompleteLogExecution):
            return True

        return self.to_dict() != other.to_dict()
