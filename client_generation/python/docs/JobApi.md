# openlattice_rundeck.JobApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**job_bulk_delete**](JobApi.md#job_bulk_delete) | **POST** /api/26/jobs/delete | Delete multiple job definitions at once
[**job_delete**](JobApi.md#job_delete) | **DELETE** /api/26/job/{id} | Delete a single job definition.
[**job_execution_bulk_disable**](JobApi.md#job_execution_bulk_disable) | **POST** /api/26/jobs/execution/disable | Bulk disable job executions
[**job_execution_bulk_enable**](JobApi.md#job_execution_bulk_enable) | **POST** /api/26/jobs/execution/enable | Bulk enable job executions
[**job_execution_delete**](JobApi.md#job_execution_delete) | **DELETE** /api/26/job/{id}/executions | Delete all job executions
[**job_execution_disable**](JobApi.md#job_execution_disable) | **POST** /api/26/job/{id}/execution/disable | Disable all executions for a job (scheduled or manual). (ACL requires toggle_execution action for a job.)
[**job_execution_enable**](JobApi.md#job_execution_enable) | **POST** /api/26/job/{id}/execution/enable | Enable executions for a job. (ACL requires toggle_execution action for a job.)
[**job_execution_list**](JobApi.md#job_execution_list) | **GET** /api/26/job/{id}/executions | List job executions
[**job_execution_run**](JobApi.md#job_execution_run) | **POST** /api/26/job/{id}/executions | Run the specified job
[**job_get**](JobApi.md#job_get) | **GET** /api/26/job/{id} | Export a single job definition in XML or YAML formats.
[**job_info_get**](JobApi.md#job_info_get) | **GET** /api/26/job/{id}/info | Get metadata about a specific job.
[**job_input_file_info_get**](JobApi.md#job_input_file_info_get) | **GET** /api/26/jobs/file/{id} | Get job input file info
[**job_input_file_upload**](JobApi.md#job_input_file_upload) | **POST** /api/26/job/{id}/input/file | Upload file as job option
[**job_input_files_upload**](JobApi.md#job_input_files_upload) | **GET** /api/26/job/{id}/input/files | List uploaded input files for job
[**job_list**](JobApi.md#job_list) | **GET** /api/26/project/{project}/jobs | List the jobs that exist for a project
[**job_retry_execution**](JobApi.md#job_retry_execution) | **POST** /api/26/job/{jobID}/retry/{executionID} | Retry a failed job execution on failed nodes only or on the same as the execution. This is the same functionality as the &#x60;Retry Failed Nodes ...&#x60; button on the execution page.
[**job_schedule_bulk_disable**](JobApi.md#job_schedule_bulk_disable) | **POST** /api/26/jobs/schedule/disable | Bulk disable job schedule
[**job_schedule_bulk_enable**](JobApi.md#job_schedule_bulk_enable) | **POST** /api/26/jobs/schedule/enable | Bulk enable job schedule
[**job_schedule_disable**](JobApi.md#job_schedule_disable) | **POST** /api/26/job/{id}/schedule/disable | Disable the schedule for a job. (ACL requires toggle_schedule action for a job.)
[**job_schedule_enable**](JobApi.md#job_schedule_enable) | **POST** /api/26/job/{id}/schedule/enable | Enable the schedule for a job. (ACL requires toggle_schedule action for a job.)
[**job_workflow_get**](JobApi.md#job_workflow_get) | **GET** /api/34/job/{id}/workflow | Get job workflow tree.
[**project_archive_import**](JobApi.md#project_archive_import) | **PUT** /api/26/project/{project}/import | Import project archive.
[**project_jobs_export**](JobApi.md#project_jobs_export) | **GET** /api/26/project/{project}/jobs/export | Export the job definitions in XML or YAML formats.
[**project_jobs_import**](JobApi.md#project_jobs_import) | **POST** /api/26/project/{project}/jobs/import | Import job definitions in XML or YAML formats.
[**system_scheduled_jobs_for_server**](JobApi.md#system_scheduled_jobs_for_server) | **GET** /api/26/scheduler/server/{uuid}/jobs | List the scheduled Jobs with their schedule owned by the cluster server with the specified UUID
[**system_scheduled_jobs_list**](JobApi.md#system_scheduled_jobs_list) | **GET** /api/26/scheduler/jobs | List the scheduled Jobs with their schedule owned by the cluster server
[**system_scheduler_takeover**](JobApi.md#system_scheduler_takeover) | **PUT** /api/26/scheduler/takeover | Tell a Rundeck server in cluster mode to claim all scheduled jobs from another cluster server


# **job_bulk_delete**
> job_bulk_delete(inline_object1)

Delete multiple job definitions at once

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
    inline_object1 = openlattice_rundeck.InlineObject1() # InlineObject1 | 

    try:
        # Delete multiple job definitions at once
        api_instance.job_bulk_delete(inline_object1)
    except ApiException as e:
        print("Exception when calling JobApi->job_bulk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object1** | [**InlineObject1**](InlineObject1.md)|  | 

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
**200** | Job deleted response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_delete**
> job_delete(id)

Delete a single job definition.

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
    id = 'id_example' # str | ID of job to delete.

    try:
        # Delete a single job definition.
        api_instance.job_delete(id)
    except ApiException as e:
        print("Exception when calling JobApi->job_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of job to delete. | 

### Return type

void (empty response body)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success ! |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_execution_bulk_disable**
> job_execution_bulk_disable(inline_object3)

Bulk disable job executions

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
    inline_object3 = openlattice_rundeck.InlineObject3() # InlineObject3 | 

    try:
        # Bulk disable job executions
        api_instance.job_execution_bulk_disable(inline_object3)
    except ApiException as e:
        print("Exception when calling JobApi->job_execution_bulk_disable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object3** | [**InlineObject3**](InlineObject3.md)|  | 

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
**200** | Job toggle execution response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_execution_bulk_enable**
> job_execution_bulk_enable(inline_object2)

Bulk enable job executions

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
    inline_object2 = openlattice_rundeck.InlineObject2() # InlineObject2 | 

    try:
        # Bulk enable job executions
        api_instance.job_execution_bulk_enable(inline_object2)
    except ApiException as e:
        print("Exception when calling JobApi->job_execution_bulk_enable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object2** | [**InlineObject2**](InlineObject2.md)|  | 

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
**200** | Job deleted response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_execution_delete**
> job_execution_delete(id)

Delete all job executions

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
    id = 56 # int | Job ID

    try:
        # Delete all job executions
        api_instance.job_execution_delete(id)
    except ApiException as e:
        print("Exception when calling JobApi->job_execution_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Job ID | 

### Return type

void (empty response body)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success ! |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_execution_disable**
> job_execution_disable(id)

Disable all executions for a job (scheduled or manual). (ACL requires toggle_execution action for a job.)

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
    id = None # object | 

    try:
        # Disable all executions for a job (scheduled or manual). (ACL requires toggle_execution action for a job.)
        api_instance.job_execution_disable(id)
    except ApiException as e:
        print("Exception when calling JobApi->job_execution_disable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job executions disabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_execution_enable**
> job_execution_enable(id)

Enable executions for a job. (ACL requires toggle_execution action for a job.)

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
    id = None # object | 

    try:
        # Enable executions for a job. (ACL requires toggle_execution action for a job.)
        api_instance.job_execution_enable(id)
    except ApiException as e:
        print("Exception when calling JobApi->job_execution_enable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job executions enabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_execution_list**
> job_execution_list(id)

List job executions

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
    id = 'id_example' # str | Job ID

    try:
        # List job executions
        api_instance.job_execution_list(id)
    except ApiException as e:
        print("Exception when calling JobApi->job_execution_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Job ID | 

### Return type

void (empty response body)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of executions for job |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_execution_run**
> job_execution_run(id, body=body)

Run the specified job

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
    id = 'id_example' # str | Job ID
body = None # object |  (optional)

    try:
        # Run the specified job
        api_instance.job_execution_run(id, body=body)
    except ApiException as e:
        print("Exception when calling JobApi->job_execution_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Job ID | 
 **body** | **object**|  | [optional] 

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
**200** | Expected response for a valid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_get**
> job_get(id, format=format)

Export a single job definition in XML or YAML formats.

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
    id = 'id_example' # str | ID of the job to export.
format = None # object |  (optional)

    try:
        # Export a single job definition in XML or YAML formats.
        api_instance.job_get(id, format=format)
    except ApiException as e:
        print("Exception when calling JobApi->job_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the job to export. | 
 **format** | [**object**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response to a valid request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_info_get**
> job_info_get(id)

Get metadata about a specific job.

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
    id = 'id_example' # str | 

    try:
        # Get metadata about a specific job.
        api_instance.job_info_get(id)
    except ApiException as e:
        print("Exception when calling JobApi->job_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response to a valid request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_input_file_info_get**
> job_input_file_info_get(id)

Get job input file info

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
    id = 'id_example' # str | 

    try:
        # Get job input file info
        api_instance.job_input_file_info_get(id)
    except ApiException as e:
        print("Exception when calling JobApi->job_input_file_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job input file info |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_input_file_upload**
> job_input_file_upload(id, option_name, file_name, body)

Upload file as job option

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
    id = 'id_example' # str | 
option_name = 'option_name_example' # str | 
file_name = 'file_name_example' # str | 
body = None # object | 

    try:
        # Upload file as job option
        api_instance.job_input_file_upload(id, option_name, file_name, body)
    except ApiException as e:
        print("Exception when calling JobApi->job_input_file_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **option_name** | **str**|  | 
 **file_name** | **str**|  | 
 **body** | **object**|  | 

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
**200** | Yay |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_input_files_upload**
> job_input_files_upload(id)

List uploaded input files for job

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
    id = 'id_example' # str | 

    try:
        # List uploaded input files for job
        api_instance.job_input_files_upload(id)
    except ApiException as e:
        print("Exception when calling JobApi->job_input_files_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of input files |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_list**
> job_list(project, id_list=id_list, group_path=group_path, job_filter=job_filter, job_exact_filter=job_exact_filter, group_path_exact=group_path_exact, scheduled_filter=scheduled_filter, server_node_uuid_filter=server_node_uuid_filter)

List the jobs that exist for a project

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
    project = 'project_example' # str | Project name
id_list = 'id_list_example' # str | Comma separated list of Job IDs to include (optional)
group_path = 'group_path_example' # str | Group or partial group path to include all jobs within that group path. Set to the special value \"-\" to match the top level jobs only. (optional)
job_filter = 'job_filter_example' # str | A filter for the job name. Matches any job name that contains this value. (optional)
job_exact_filter = 'job_exact_filter_example' # str | An exact job name to match. (optional)
group_path_exact = 'group_path_exact_example' # str | An exact group path to match. Set to the special value \"-\" to match the top level jobs only. (optional)
scheduled_filter = True # bool | Specify whether to return only scheduled or only not scheduled jobs. (optional)
server_node_uuid_filter = 'server_node_uuid_filter_example' # str | In cluster mode, use to select scheduled jobs assigned to the server with the given UUID. (optional)

    try:
        # List the jobs that exist for a project
        api_instance.job_list(project, id_list=id_list, group_path=group_path, job_filter=job_filter, job_exact_filter=job_exact_filter, group_path_exact=group_path_exact, scheduled_filter=scheduled_filter, server_node_uuid_filter=server_node_uuid_filter)
    except ApiException as e:
        print("Exception when calling JobApi->job_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | 
 **id_list** | **str**| Comma separated list of Job IDs to include | [optional] 
 **group_path** | **str**| Group or partial group path to include all jobs within that group path. Set to the special value \&quot;-\&quot; to match the top level jobs only. | [optional] 
 **job_filter** | **str**| A filter for the job name. Matches any job name that contains this value. | [optional] 
 **job_exact_filter** | **str**| An exact job name to match. | [optional] 
 **group_path_exact** | **str**| An exact group path to match. Set to the special value \&quot;-\&quot; to match the top level jobs only. | [optional] 
 **scheduled_filter** | **bool**| Specify whether to return only scheduled or only not scheduled jobs. | [optional] 
 **server_node_uuid_filter** | **str**| In cluster mode, use to select scheduled jobs assigned to the server with the given UUID. | [optional] 

### Return type

void (empty response body)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response to a valid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_retry_execution**
> job_retry_execution(job_id, execution_id, body=body)

Retry a failed job execution on failed nodes only or on the same as the execution. This is the same functionality as the `Retry Failed Nodes ...` button on the execution page.

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
    job_id = 'job_id_example' # str | 
execution_id = 56 # int | 
body = None # object |  (optional)

    try:
        # Retry a failed job execution on failed nodes only or on the same as the execution. This is the same functionality as the `Retry Failed Nodes ...` button on the execution page.
        api_instance.job_retry_execution(job_id, execution_id, body=body)
    except ApiException as e:
        print("Exception when calling JobApi->job_retry_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 
 **execution_id** | **int**|  | 
 **body** | **object**|  | [optional] 

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
**200** | Exected response to a valid request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_schedule_bulk_disable**
> job_schedule_bulk_disable(inline_object5)

Bulk disable job schedule

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
    inline_object5 = openlattice_rundeck.InlineObject5() # InlineObject5 | 

    try:
        # Bulk disable job schedule
        api_instance.job_schedule_bulk_disable(inline_object5)
    except ApiException as e:
        print("Exception when calling JobApi->job_schedule_bulk_disable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object5** | [**InlineObject5**](InlineObject5.md)|  | 

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
**200** | Job toggle schedule response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_schedule_bulk_enable**
> job_schedule_bulk_enable(inline_object4)

Bulk enable job schedule

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
    inline_object4 = openlattice_rundeck.InlineObject4() # InlineObject4 | 

    try:
        # Bulk enable job schedule
        api_instance.job_schedule_bulk_enable(inline_object4)
    except ApiException as e:
        print("Exception when calling JobApi->job_schedule_bulk_enable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object4** | [**InlineObject4**](InlineObject4.md)|  | 

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
**200** | Job toggle schedule response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_schedule_disable**
> job_schedule_disable(id)

Disable the schedule for a job. (ACL requires toggle_schedule action for a job.)

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
    id = None # object | 

    try:
        # Disable the schedule for a job. (ACL requires toggle_schedule action for a job.)
        api_instance.job_schedule_disable(id)
    except ApiException as e:
        print("Exception when calling JobApi->job_schedule_disable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job schedules disabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_schedule_enable**
> job_schedule_enable(id)

Enable the schedule for a job. (ACL requires toggle_schedule action for a job.)

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
    id = None # object | 

    try:
        # Enable the schedule for a job. (ACL requires toggle_schedule action for a job.)
        api_instance.job_schedule_enable(id)
    except ApiException as e:
        print("Exception when calling JobApi->job_schedule_enable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job schedule enabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_workflow_get**
> job_workflow_get(id)

Get job workflow tree.

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
    id = 'id_example' # str | 

    try:
        # Get job workflow tree.
        api_instance.job_workflow_get(id)
    except ApiException as e:
        print("Exception when calling JobApi->job_workflow_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response to a valid request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
> project_jobs_export(project, format=format, idlist=idlist, group_path=group_path, job_filter=job_filter)

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
        api_instance.project_jobs_export(project, format=format, idlist=idlist, group_path=group_path, job_filter=job_filter)
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

void (empty response body)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response to a valid request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_jobs_import**
> project_jobs_import(project, body, content_type=content_type, accept=accept, file_format=file_format, dupe_option=dupe_option, uuid_option=uuid_option)

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
        api_instance.project_jobs_import(project, body, content_type=content_type, accept=accept, file_format=file_format, dupe_option=dupe_option, uuid_option=uuid_option)
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

void (empty response body)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response to a valid request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_scheduled_jobs_for_server**
> system_scheduled_jobs_for_server(uuid)

List the scheduled Jobs with their schedule owned by the cluster server with the specified UUID

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
    uuid = 'uuid_example' # str | The ID of the user to retrieve profile information for

    try:
        # List the scheduled Jobs with their schedule owned by the cluster server with the specified UUID
        api_instance.system_scheduled_jobs_for_server(uuid)
    except ApiException as e:
        print("Exception when calling JobApi->system_scheduled_jobs_for_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The ID of the user to retrieve profile information for | 

### Return type

void (empty response body)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response to a valid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_scheduled_jobs_list**
> system_scheduled_jobs_list()

List the scheduled Jobs with their schedule owned by the cluster server

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
    
    try:
        # List the scheduled Jobs with their schedule owned by the cluster server
        api_instance.system_scheduled_jobs_list()
    except ApiException as e:
        print("Exception when calling JobApi->system_scheduled_jobs_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response to a valid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_scheduler_takeover**
> system_scheduler_takeover(inline_object10)

Tell a Rundeck server in cluster mode to claim all scheduled jobs from another cluster server

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
    inline_object10 = openlattice_rundeck.InlineObject10() # InlineObject10 | 

    try:
        # Tell a Rundeck server in cluster mode to claim all scheduled jobs from another cluster server
        api_instance.system_scheduler_takeover(inline_object10)
    except ApiException as e:
        print("Exception when calling JobApi->system_scheduler_takeover: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object10** | [**InlineObject10**](InlineObject10.md)|  | 

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

