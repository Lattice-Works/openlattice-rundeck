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

import olrundeck
from olrundeck.models.api26_scheduler_takeover_server import Api26SchedulerTakeoverServer  # noqa: E501
from olrundeck.rest import ApiException

class TestApi26SchedulerTakeoverServer(unittest.TestCase):
    """Api26SchedulerTakeoverServer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Api26SchedulerTakeoverServer
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = olrundeck.models.api26_scheduler_takeover_server.Api26SchedulerTakeoverServer()  # noqa: E501
        if include_optional :
            return Api26SchedulerTakeoverServer(
                uuid = '0', 
                all = True
            )
        else :
            return Api26SchedulerTakeoverServer(
                uuid = '0',
                all = True,
        )

    def testApi26SchedulerTakeoverServer(self):
        """Test Api26SchedulerTakeoverServer"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
