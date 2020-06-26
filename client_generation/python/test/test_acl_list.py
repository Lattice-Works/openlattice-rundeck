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
from openlattice-rundeck.models.acl_list import AclList  # noqa: E501
from openlattice-rundeck.rest import ApiException

class TestAclList(unittest.TestCase):
    """AclList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AclList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openlattice-rundeck.models.acl_list.AclList()  # noqa: E501
        if include_optional :
            return AclList(
                path = '0', 
                type = '0', 
                href = '0', 
                resources = [
                    openlattice-rundeck.models.acl_reference.AclReference(
                        path = '0', 
                        type = '0', 
                        name = '0', 
                        href = '0', )
                    ]
            )
        else :
            return AclList(
        )

    def testAclList(self):
        """Test AclList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
