# coding: utf-8

"""
    Rundeck

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openlattice_rundeck
from openlattice_rundeck.api.cluster_api import ClusterApi  # noqa: E501
from openlattice_rundeck.rest import ApiException


class TestClusterApi(unittest.TestCase):
    """ClusterApi unit test stubs"""

    def setUp(self):
        self.api = openlattice_rundeck.api.cluster_api.ClusterApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_system_scheduled_jobs_for_server(self):
        """Test case for system_scheduled_jobs_for_server

        List the scheduled Jobs with their schedule owned by the cluster server with the specified UUID  # noqa: E501
        """
        pass

    def test_system_scheduled_jobs_list(self):
        """Test case for system_scheduled_jobs_list

        List the scheduled Jobs with their schedule owned by the cluster server  # noqa: E501
        """
        pass

    def test_system_scheduler_takeover(self):
        """Test case for system_scheduler_takeover

        Tell a Rundeck server in cluster mode to claim all scheduled jobs from another cluster server  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
