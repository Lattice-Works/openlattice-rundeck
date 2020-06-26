# openlattice-rundeck
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 0.1.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openlattice-rundeck
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openlattice-rundeck
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function

import time
import openlattice-rundeck
from openlattice-rundeck.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openlattice-rundeck.Configuration(
    host = "http://localhost"
)



# Enter a context with an instance of the API client
with openlattice-rundeck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openlattice-rundeck.JobApi(api_client)
    project = 'project_example' # str | Name of the project to import jobs into.
body = None # object | 
job_uuid_option = None # object |  (optional)
import_executions = True # bool |  (optional)
import_config = True # bool |  (optional)
import_acl = True # bool |  (optional)

    try:
        # Import project archive.
        api_instance.project_archive_import(project, body, job_uuid_option=job_uuid_option, import_executions=import_executions, import_config=import_config, import_acl=import_acl)
    except ApiException as e:
        print("Exception when calling JobApi->project_archive_import: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*JobApi* | [**project_archive_import**](docs/JobApi.md#project_archive_import) | **PUT** /api/26/project/{project}/import | Import project archive.
*JobApi* | [**project_jobs_export**](docs/JobApi.md#project_jobs_export) | **GET** /api/26/project/{project}/jobs/export | Export the job definitions in XML or YAML formats.
*JobApi* | [**project_jobs_import**](docs/JobApi.md#project_jobs_import) | **POST** /api/26/project/{project}/jobs/import | Import job definitions in XML or YAML formats.
*ProjectApi* | [**project_archive_export_sync**](docs/ProjectApi.md#project_archive_export_sync) | **GET** /api/26/project/{project}/export | Export archive of project synchronously
*ProjectApi* | [**project_archive_import**](docs/ProjectApi.md#project_archive_import) | **PUT** /api/26/project/{project}/import | Import project archive.
*ProjectApi* | [**project_config_key_delete**](docs/ProjectApi.md#project_config_key_delete) | **DELETE** /api/26/project/{project}/config/{key} | Delete project config key
*ProjectApi* | [**project_config_update**](docs/ProjectApi.md#project_config_update) | **PUT** /api/26/project/{project}/config | Update project config
*ProjectApi* | [**project_create**](docs/ProjectApi.md#project_create) | **POST** /api/26/projects | Create a new project
*ProjectApi* | [**project_delete**](docs/ProjectApi.md#project_delete) | **DELETE** /api/26/project/{project} | Delete project
*ProjectApi* | [**project_jobs_export**](docs/ProjectApi.md#project_jobs_export) | **GET** /api/26/project/{project}/jobs/export | Export the job definitions in XML or YAML formats.
*ProjectApi* | [**project_jobs_import**](docs/ProjectApi.md#project_jobs_import) | **POST** /api/26/project/{project}/jobs/import | Import job definitions in XML or YAML formats.
*ProjectApi* | [**project_motd_delete**](docs/ProjectApi.md#project_motd_delete) | **DELETE** /api/26/project/{project}/motd.md | Delete project motd.md
*ProjectApi* | [**project_readme_delete**](docs/ProjectApi.md#project_readme_delete) | **DELETE** /api/26/project/{project}/readme.md | Delete project README.md


## Documentation For Models

 - [AclList](docs/AclList.md)
 - [AclPolicyResponse](docs/AclPolicyResponse.md)
 - [AclReference](docs/AclReference.md)
 - [BulkJobFailedInfo](docs/BulkJobFailedInfo.md)
 - [BulkJobSucceededInfo](docs/BulkJobSucceededInfo.md)
 - [ExecuteJobRequest](docs/ExecuteJobRequest.md)
 - [Execution](docs/Execution.md)
 - [ExecutionList](docs/ExecutionList.md)
 - [ExecutionOutput](docs/ExecutionOutput.md)
 - [ExecutionOutputEntry](docs/ExecutionOutputEntry.md)
 - [IncompleteFileType](docs/IncompleteFileType.md)
 - [IncompleteLogExecution](docs/IncompleteLogExecution.md)
 - [IncompleteLogExecutions](docs/IncompleteLogExecutions.md)
 - [InvalidAclPolicyResponse](docs/InvalidAclPolicyResponse.md)
 - [InvalidAclPolicyResponsePolicies](docs/InvalidAclPolicyResponsePolicies.md)
 - [Job](docs/Job.md)
 - [JobBulkOperationResponse](docs/JobBulkOperationResponse.md)
 - [JobExecutionDelete](docs/JobExecutionDelete.md)
 - [JobExecutionDeleteFailures](docs/JobExecutionDeleteFailures.md)
 - [JobInputFileInfo](docs/JobInputFileInfo.md)
 - [JobInputFileListResponse](docs/JobInputFileListResponse.md)
 - [JobMetadata](docs/JobMetadata.md)
 - [JobReference](docs/JobReference.md)
 - [LogStorage](docs/LogStorage.md)
 - [ModifyUserRequest](docs/ModifyUserRequest.md)
 - [Paging](docs/Paging.md)
 - [Project](docs/Project.md)
 - [RetryExecutionRequest](docs/RetryExecutionRequest.md)
 - [StorageKeyListResponse](docs/StorageKeyListResponse.md)
 - [StorageKeyMetaType](docs/StorageKeyMetaType.md)
 - [StorageKeyMetadata](docs/StorageKeyMetadata.md)
 - [SystemInfo](docs/SystemInfo.md)
 - [TakeoverScheduleRequest](docs/TakeoverScheduleRequest.md)
 - [TakeoverScheduleResponse](docs/TakeoverScheduleResponse.md)
 - [User](docs/User.md)
 - [WorkflowStep](docs/WorkflowStep.md)


## Documentation For Authorization


## rundeck_auth

- **Type**: API key
- **API key parameter name**: X-Rundeck-Auth-Token
- **Location**: HTTP header


## Author



