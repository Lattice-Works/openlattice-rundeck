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
from olrundeck.models.inline_object5 import InlineObject5  # noqa: E501
from olrundeck.rest import ApiException

class TestInlineObject5(unittest.TestCase):
    """InlineObject5 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineObject5
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = olrundeck.models.inline_object5.InlineObject5()  # noqa: E501
        if include_optional :
            return InlineObject5(
                ids = [
                    '0'
                    ]
            )
        else :
            return InlineObject5(
        )

    def testInlineObject5(self):
        """Test InlineObject5"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
