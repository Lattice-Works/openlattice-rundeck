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
from openlattice-rundeck.models.project import Project  # noqa: E501
from openlattice-rundeck.rest import ApiException

class TestProject(unittest.TestCase):
    """Project unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Project
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openlattice-rundeck.models.project.Project()  # noqa: E501
        if include_optional :
            return Project(
                description = '0', 
                name = '0', 
                url = '0', 
                config = None
            )
        else :
            return Project(
        )

    def testProject(self):
        """Test Project"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
