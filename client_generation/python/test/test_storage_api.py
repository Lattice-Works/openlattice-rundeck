# coding: utf-8

"""
    Rundeck

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openlattice-rundeck
from openlattice-rundeck.api.storage_api import StorageApi  # noqa: E501
from openlattice-rundeck.rest import ApiException


class TestStorageApi(unittest.TestCase):
    """StorageApi unit test stubs"""

    def setUp(self):
        self.api = openlattice-rundeck.api.storage_api.StorageApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api26_storage_keys_path_delete(self):
        """Test case for api26_storage_keys_path_delete

        Deletes the file if it exists and returns 204 response.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
