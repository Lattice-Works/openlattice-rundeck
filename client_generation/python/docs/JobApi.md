# openlattice_rundeck.JobApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**project_archive_import**](JobApi.md#project_archive_import) | **PUT** /api/26/project/{project}/import | Import project archive.
[**project_jobs_export**](JobApi.md#project_jobs_export) | **GET** /api/26/project/{project}/jobs/export | Export the job definitions in XML or YAML formats.
[**project_jobs_import**](JobApi.md#project_jobs_import) | **POST** /api/26/project/{project}/jobs/import | Import job definitions in XML or YAML formats.


# **project_archive_import**
> project_archive_import(project, body, job_uuid_option=job_uuid_option, import_executions=import_executions, import_config=import_config, import_acl=import_acl)

Import project archive.

### Example

* Api Key Authentication (rundeck_auth):
```python
from __future__ import print_function
import time
import openlattice_rundeck
from openlattice_rundeck.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openlattice_rundeck.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: rundeck_auth
configuration = openlattice_rundeck.Configuration(
    host = "http://localhost",
    api_key = {
        'rundeck_auth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['rundeck_auth'] = 'Bearer'

# Enter a context with an instance of the API client
with openlattice_rundeck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openlattice_rundeck.JobApi(api_client)
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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Name of the project to import jobs into. | 
 **body** | **object**|  | 
 **job_uuid_option** | [**object**](.md)|  | [optional] 
 **import_executions** | **bool**|  | [optional] 
 **import_config** | **bool**|  | [optional] 
 **import_acl** | **bool**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response to a valid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_jobs_export**
> str project_jobs_export(project, format=format, idlist=idlist, group_path=group_path, job_filter=job_filter)

Export the job definitions in XML or YAML formats.

### Example

* Api Key Authentication (rundeck_auth):
```python
from __future__ import print_function
import time
import openlattice_rundeck
from openlattice_rundeck.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openlattice_rundeck.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: rundeck_auth
configuration = openlattice_rundeck.Configuration(
    host = "http://localhost",
    api_key = {
        'rundeck_auth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['rundeck_auth'] = 'Bearer'

# Enter a context with an instance of the API client
with openlattice_rundeck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openlattice_rundeck.JobApi(api_client)
    project = 'project_example' # str | The project to export jobs for.
format = None # object | XML or YAML format for exported jobs. (optional)
idlist = 'idlist_example' # str | A comma-separated list of Job IDs to export. (optional)
group_path = 'group_path_example' # str | Group or partial group path to include all jobs within that group path. (optional)
job_filter = 'job_filter_example' # str | Filter for the job Name. (optional)

    try:
        # Export the job definitions in XML or YAML formats.
        api_response = api_instance.project_jobs_export(project, format=format, idlist=idlist, group_path=group_path, job_filter=job_filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobApi->project_jobs_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project to export jobs for. | 
 **format** | [**object**](.md)| XML or YAML format for exported jobs. | [optional] 
 **idlist** | **str**| A comma-separated list of Job IDs to export. | [optional] 
 **group_path** | **str**| Group or partial group path to include all jobs within that group path. | [optional] 
 **job_filter** | **str**| Filter for the job Name. | [optional] 

### Return type

**str**

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response to a valid request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_jobs_import**
> object project_jobs_import(project, body, content_type=content_type, accept=accept, file_format=file_format, dupe_option=dupe_option, uuid_option=uuid_option)

Import job definitions in XML or YAML formats.

### Example

* Api Key Authentication (rundeck_auth):
```python
from __future__ import print_function
import time
import openlattice_rundeck
from openlattice_rundeck.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openlattice_rundeck.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: rundeck_auth
configuration = openlattice_rundeck.Configuration(
    host = "http://localhost",
    api_key = {
        'rundeck_auth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['rundeck_auth'] = 'Bearer'

# Enter a context with an instance of the API client
with openlattice_rundeck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openlattice_rundeck.JobApi(api_client)
    project = 'project_example' # str | Name of the project to import jobs into.
body = None # object | 
content_type = None # object |  (optional)
accept = None # object |  (optional)
file_format = None # object |  (optional)
dupe_option = None # object |  (optional)
uuid_option = None # object |  (optional)

    try:
        # Import job definitions in XML or YAML formats.
        api_response = api_instance.project_jobs_import(project, body, content_type=content_type, accept=accept, file_format=file_format, dupe_option=dupe_option, uuid_option=uuid_option)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobApi->project_jobs_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Name of the project to import jobs into. | 
 **body** | **object**|  | 
 **content_type** | [**object**](.md)|  | [optional] 
 **accept** | [**object**](.md)|  | [optional] 
 **file_format** | [**object**](.md)|  | [optional] 
 **dupe_option** | [**object**](.md)|  | [optional] 
 **uuid_option** | [**object**](.md)|  | [optional] 

### Return type

**object**

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response to a valid request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

