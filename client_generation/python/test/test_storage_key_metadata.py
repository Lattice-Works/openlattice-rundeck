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
from olrundeck.models.storage_key_metadata import StorageKeyMetadata  # noqa: E501
from olrundeck.rest import ApiException

class TestStorageKeyMetadata(unittest.TestCase):
    """StorageKeyMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StorageKeyMetadata
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = olrundeck.models.storage_key_metadata.StorageKeyMetadata()  # noqa: E501
        if include_optional :
            return StorageKeyMetadata(
                meta = None, 
                url = '0', 
                name = '0', 
                type = '0', 
                path = '0'
            )
        else :
            return StorageKeyMetadata(
        )

    def testStorageKeyMetadata(self):
        """Test StorageKeyMetadata"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
