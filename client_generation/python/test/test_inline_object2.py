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
from openlattice_rundeck.models.inline_object2 import InlineObject2  # noqa: E501
from openlattice_rundeck.rest import ApiException

class TestInlineObject2(unittest.TestCase):
    """InlineObject2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineObject2
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openlattice_rundeck.models.inline_object2.InlineObject2()  # noqa: E501
        if include_optional :
            return InlineObject2(
                ids = [
                    '0'
                    ]
            )
        else :
            return InlineObject2(
        )

    def testInlineObject2(self):
        """Test InlineObject2"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()