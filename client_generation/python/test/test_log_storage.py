# coding: utf-8

"""
    Rundeck

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openlattice-rundeck
from openlattice-rundeck.models.log_storage import LogStorage  # noqa: E501
from openlattice-rundeck.rest import ApiException

class TestLogStorage(unittest.TestCase):
    """LogStorage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LogStorage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openlattice-rundeck.models.log_storage.LogStorage()  # noqa: E501
        if include_optional :
            return LogStorage(
                enabled = True, 
                plugin_name = '0', 
                succeeded_count = 1.337, 
                failed_count = 1.337, 
                queued_count = 1.337, 
                total_count = 1.337, 
                incomplete_count = 1.337, 
                missing_count = 1.337
            )
        else :
            return LogStorage(
        )

    def testLogStorage(self):
        """Test LogStorage"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
