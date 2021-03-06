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
from olrundeck.models.storage_key_list_response import StorageKeyListResponse  # noqa: E501
from olrundeck.rest import ApiException

class TestStorageKeyListResponse(unittest.TestCase):
    """StorageKeyListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StorageKeyListResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = olrundeck.models.storage_key_list_response.StorageKeyListResponse()  # noqa: E501
        if include_optional :
            return StorageKeyListResponse(
                resources = [
                    olrundeck.models.storage_key_metadata.StorageKeyMetadata(
                        meta = olrundeck.models.meta.meta(
                            rundeck_key_type = 'private', 
                            rundeck_content_mask = '0', 
                            rundeck_content_size = '0', 
                            rundeck_content_type = '0', ), 
                        url = '0', 
                        name = '0', 
                        type = '0', 
                        path = '0', )
                    ], 
                meta = None, 
                url = '0', 
                type = '0', 
                path = '0'
            )
        else :
            return StorageKeyListResponse(
        )

    def testStorageKeyListResponse(self):
        """Test StorageKeyListResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
