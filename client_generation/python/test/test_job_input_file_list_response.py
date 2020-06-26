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
from openlattice_rundeck.models.job_input_file_list_response import JobInputFileListResponse  # noqa: E501
from openlattice_rundeck.rest import ApiException

class TestJobInputFileListResponse(unittest.TestCase):
    """JobInputFileListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test JobInputFileListResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openlattice_rundeck.models.job_input_file_list_response.JobInputFileListResponse()  # noqa: E501
        if include_optional :
            return JobInputFileListResponse(
                paging = openlattice_rundeck.models.paging.Paging(
                    count = 56, 
                    total = 56, 
                    offset = 56, 
                    max = 56, ), 
                files = [
                    openlattice_rundeck.models.job_input_file_info.JobInputFileInfo(
                        id = '0', 
                        user = '0', 
                        file_state = 'temp', 
                        sha = '0', 
                        job_id = '0', 
                        date_created = '0', 
                        server_node_uuid = '0', 
                        file_name = '0', 
                        size = 56, 
                        expiration_date = '0', 
                        exec_id = '0', )
                    ]
            )
        else :
            return JobInputFileListResponse(
                paging = openlattice_rundeck.models.paging.Paging(
                    count = 56, 
                    total = 56, 
                    offset = 56, 
                    max = 56, ),
                files = [
                    openlattice_rundeck.models.job_input_file_info.JobInputFileInfo(
                        id = '0', 
                        user = '0', 
                        file_state = 'temp', 
                        sha = '0', 
                        job_id = '0', 
                        date_created = '0', 
                        server_node_uuid = '0', 
                        file_name = '0', 
                        size = 56, 
                        expiration_date = '0', 
                        exec_id = '0', )
                    ],
        )

    def testJobInputFileListResponse(self):
        """Test JobInputFileListResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
