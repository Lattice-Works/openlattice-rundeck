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


class JobMetadata(object):
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
        'name': 'str',
        'group': 'str',
        'project': 'str',
        'description': 'str',
        'href': 'str',
        'permalink': 'str',
        'scheduled': 'bool',
        'schedule_enabled': 'bool',
        'average_duration': 'float',
        'options': 'object'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'group': 'group',
        'project': 'project',
        'description': 'description',
        'href': 'href',
        'permalink': 'permalink',
        'scheduled': 'scheduled',
        'schedule_enabled': 'scheduleEnabled',
        'average_duration': 'averageDuration',
        'options': 'options'
    }

    def __init__(self, id=None, name=None, group=None, project=None, description=None, href=None, permalink=None, scheduled=None, schedule_enabled=None, average_duration=None, options=None, local_vars_configuration=None):  # noqa: E501
        """JobMetadata - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._group = None
        self._project = None
        self._description = None
        self._href = None
        self._permalink = None
        self._scheduled = None
        self._schedule_enabled = None
        self._average_duration = None
        self._options = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if group is not None:
            self.group = group
        if project is not None:
            self.project = project
        if description is not None:
            self.description = description
        if href is not None:
            self.href = href
        if permalink is not None:
            self.permalink = permalink
        if scheduled is not None:
            self.scheduled = scheduled
        if schedule_enabled is not None:
            self.schedule_enabled = schedule_enabled
        if average_duration is not None:
            self.average_duration = average_duration
        if options is not None:
            self.options = options

    @property
    def id(self):
        """Gets the id of this JobMetadata.  # noqa: E501


        :return: The id of this JobMetadata.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JobMetadata.


        :param id: The id of this JobMetadata.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this JobMetadata.  # noqa: E501


        :return: The name of this JobMetadata.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JobMetadata.


        :param name: The name of this JobMetadata.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def group(self):
        """Gets the group of this JobMetadata.  # noqa: E501


        :return: The group of this JobMetadata.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this JobMetadata.


        :param group: The group of this JobMetadata.  # noqa: E501
        :type group: str
        """

        self._group = group

    @property
    def project(self):
        """Gets the project of this JobMetadata.  # noqa: E501


        :return: The project of this JobMetadata.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this JobMetadata.


        :param project: The project of this JobMetadata.  # noqa: E501
        :type project: str
        """

        self._project = project

    @property
    def description(self):
        """Gets the description of this JobMetadata.  # noqa: E501


        :return: The description of this JobMetadata.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this JobMetadata.


        :param description: The description of this JobMetadata.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def href(self):
        """Gets the href of this JobMetadata.  # noqa: E501


        :return: The href of this JobMetadata.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this JobMetadata.


        :param href: The href of this JobMetadata.  # noqa: E501
        :type href: str
        """

        self._href = href

    @property
    def permalink(self):
        """Gets the permalink of this JobMetadata.  # noqa: E501


        :return: The permalink of this JobMetadata.  # noqa: E501
        :rtype: str
        """
        return self._permalink

    @permalink.setter
    def permalink(self, permalink):
        """Sets the permalink of this JobMetadata.


        :param permalink: The permalink of this JobMetadata.  # noqa: E501
        :type permalink: str
        """

        self._permalink = permalink

    @property
    def scheduled(self):
        """Gets the scheduled of this JobMetadata.  # noqa: E501


        :return: The scheduled of this JobMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._scheduled

    @scheduled.setter
    def scheduled(self, scheduled):
        """Sets the scheduled of this JobMetadata.


        :param scheduled: The scheduled of this JobMetadata.  # noqa: E501
        :type scheduled: bool
        """

        self._scheduled = scheduled

    @property
    def schedule_enabled(self):
        """Gets the schedule_enabled of this JobMetadata.  # noqa: E501


        :return: The schedule_enabled of this JobMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._schedule_enabled

    @schedule_enabled.setter
    def schedule_enabled(self, schedule_enabled):
        """Sets the schedule_enabled of this JobMetadata.


        :param schedule_enabled: The schedule_enabled of this JobMetadata.  # noqa: E501
        :type schedule_enabled: bool
        """

        self._schedule_enabled = schedule_enabled

    @property
    def average_duration(self):
        """Gets the average_duration of this JobMetadata.  # noqa: E501


        :return: The average_duration of this JobMetadata.  # noqa: E501
        :rtype: float
        """
        return self._average_duration

    @average_duration.setter
    def average_duration(self, average_duration):
        """Sets the average_duration of this JobMetadata.


        :param average_duration: The average_duration of this JobMetadata.  # noqa: E501
        :type average_duration: float
        """

        self._average_duration = average_duration

    @property
    def options(self):
        """Gets the options of this JobMetadata.  # noqa: E501


        :return: The options of this JobMetadata.  # noqa: E501
        :rtype: object
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this JobMetadata.


        :param options: The options of this JobMetadata.  # noqa: E501
        :type options: object
        """

        self._options = options

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
        if not isinstance(other, JobMetadata):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JobMetadata):
            return True

        return self.to_dict() != other.to_dict()