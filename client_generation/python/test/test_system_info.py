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

import openlattice_rundeck
from openlattice_rundeck.models.system_info import SystemInfo  # noqa: E501
from openlattice_rundeck.rest import ApiException

class TestSystemInfo(unittest.TestCase):
    """SystemInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SystemInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openlattice_rundeck.models.system_info.SystemInfo()  # noqa: E501
        if include_optional :
            return SystemInfo(
                system = None
            )
        else :
            return SystemInfo(
        )

    def testSystemInfo(self):
        """Test SystemInfo"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
