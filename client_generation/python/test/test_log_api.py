# coding: utf-8

"""
    Rundeck

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openlattice_rundeck
from openlattice_rundeck.api.log_api import LogApi  # noqa: E501
from openlattice_rundeck.rest import ApiException


class TestLogApi(unittest.TestCase):
    """LogApi unit test stubs"""

    def setUp(self):
        self.api = openlattice_rundeck.api.log_api.LogApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_system_incomplete_log_storage_executions_get(self):
        """Test case for system_incomplete_log_storage_executions_get

        List all executions with incomplete log storage  # noqa: E501
        """
        pass

    def test_system_incomplete_log_storage_executions_resume(self):
        """Test case for system_incomplete_log_storage_executions_resume

        Resume processing incomplete Log Storage uploads  # noqa: E501
        """
        pass

    def test_system_log_storage_info_get(self):
        """Test case for system_log_storage_info_get

        Get Log Storage information and stats  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()