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
from openlattice_rundeck.models.inline_object8 import InlineObject8  # noqa: E501
from openlattice_rundeck.rest import ApiException

class TestInlineObject8(unittest.TestCase):
    """InlineObject8 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineObject8
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openlattice_rundeck.models.inline_object8.InlineObject8()  # noqa: E501
        if include_optional :
            return InlineObject8(
                contents = '0'
            )
        else :
            return InlineObject8(
        )

    def testInlineObject8(self):
        """Test InlineObject8"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
