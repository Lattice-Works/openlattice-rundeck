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
from olrundeck.models.execution_list import ExecutionList  # noqa: E501
from olrundeck.rest import ApiException

class TestExecutionList(unittest.TestCase):
    """ExecutionList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ExecutionList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = olrundeck.models.execution_list.ExecutionList()  # noqa: E501
        if include_optional :
            return ExecutionList(
                paging = olrundeck.models.paging.Paging(
                    count = 56, 
                    total = 56, 
                    offset = 56, 
                    max = 56, ), 
                executions = [
                    olrundeck.models.execution.Execution(
                        id = 1.337, 
                        href = '0', 
                        permalink = '0', 
                        status = 'running', 
                        custom_status = '0', 
                        project = '0', 
                        user = '0', 
                        server_uuid = '0', 
                        date_started = olrundeck.models.date_started.date-started(
                            unixtime = 1.337, 
                            date = '0', ), 
                        job = olrundeck.models.job_metadata.JobMetadata(
                            id = '0', 
                            name = '0', 
                            group = '0', 
                            project = '0', 
                            description = '0', 
                            href = '0', 
                            permalink = '0', 
                            scheduled = True, 
                            schedule_enabled = True, 
                            average_duration = 1.337, 
                            options = olrundeck.models.options.options(), ), 
                        description = '0', 
                        argstring = '0', 
                        successful_nodes = [
                            '0'
                            ], )
                    ]
            )
        else :
            return ExecutionList(
        )

    def testExecutionList(self):
        """Test ExecutionList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
