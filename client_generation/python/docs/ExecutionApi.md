# olrundeck.ExecutionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execution_bulk_delete**](ExecutionApi.md#execution_bulk_delete) | **POST** /api/26/executions/delete | Bulk delete executions
[**execution_delete**](ExecutionApi.md#execution_delete) | **DELETE** /api/26/execution/{id} | Delete an exeuction by ID
[**execution_input_files_list**](ExecutionApi.md#execution_input_files_list) | **GET** /api/26/execution/{id}/input/files | List input files for an execution
[**execution_list_running**](ExecutionApi.md#execution_list_running) | **GET** /api/26/project/{project}/executions/running | List job executions
[**execution_output_get**](ExecutionApi.md#execution_output_get) | **GET** /api/26/execution/{id}/output | List input files for an execution
[**execution_query**](ExecutionApi.md#execution_query) | **GET** /api/26/project/{project}/executions | Query for Executions based on Job or Execution details
[**execution_state_get**](ExecutionApi.md#execution_state_get) | **GET** /api/26/execution/{id}/state | Get detail about the node and step state of an execution by ID. The execution can be currently running or completed.
[**execution_status_get**](ExecutionApi.md#execution_status_get) | **GET** /api/26/execution/{id} | Get the status of an execution by ID
[**job_execution_bulk_disable**](ExecutionApi.md#job_execution_bulk_disable) | **POST** /api/26/jobs/execution/disable | Bulk disable job executions
[**job_execution_bulk_enable**](ExecutionApi.md#job_execution_bulk_enable) | **POST** /api/26/jobs/execution/enable | Bulk enable job executions
[**job_execution_delete**](ExecutionApi.md#job_execution_delete) | **DELETE** /api/26/job/{id}/executions | Delete all job executions
[**job_execution_disable**](ExecutionApi.md#job_execution_disable) | **POST** /api/26/job/{id}/execution/disable | Disable all executions for a job (scheduled or manual). (ACL requires toggle_execution action for a job.)
[**job_execution_enable**](ExecutionApi.md#job_execution_enable) | **POST** /api/26/job/{id}/execution/enable | Enable executions for a job. (ACL requires toggle_execution action for a job.)
[**job_execution_list**](ExecutionApi.md#job_execution_list) | **GET** /api/26/job/{id}/executions | List job executions
[**job_execution_run**](ExecutionApi.md#job_execution_run) | **POST** /api/26/job/{id}/executions | Run the specified job
[**job_retry_execution**](ExecutionApi.md#job_retry_execution) | **POST** /api/26/job/{jobID}/retry/{executionID} | Retry a failed job execution on failed nodes only or on the same as the execution. This is the same functionality as the &#x60;Retry Failed Nodes ...&#x60; button on the execution page.
[**system_executions_disable**](ExecutionApi.md#system_executions_disable) | **POST** /api/26/system/executions/disable | Disables executions, preventing adhoc and manual and scheduled jobs from running.
[**system_executions_enable**](ExecutionApi.md#system_executions_enable) | **POST** /api/26/system/executions/enable | Enables executions, allowing adhoc and manual and scheduled jobs to be run
[**system_incomplete_log_storage_executions_get**](ExecutionApi.md#system_incomplete_log_storage_executions_get) | **GET** /api/26/system/logstorage/incomplete | List all executions with incomplete log storage
[**system_incomplete_log_storage_executions_resume**](ExecutionApi.md#system_incomplete_log_storage_executions_resume) | **POST** /api/26/system/logstorage/incomplete/resume | Resume processing incomplete Log Storage uploads


# **execution_bulk_delete**
> JobExecutionDelete execution_bulk_delete(inline_object)

Bulk delete executions

### Example

* Api Key Authentication (rundeck_auth):
```python
from __future__ import print_function
import time
import olrundeck
from olrundeck.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = olrundeck.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: rundeck_auth
configuration = olrundeck.Configuration(
    host = "http://localhost",
    api_key = {
        'rundeck_auth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['rundeck_auth'] = 'Bearer'

# Enter a context with an instance of the API client
with olrundeck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = olrundeck.ExecutionApi(api_client)
    inline_object = olrundeck.InlineObject() # InlineObject | 

    try:
        # Bulk delete executions
        api_response = api_instance.execution_bulk_delete(inline_object)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExecutionApi->execution_bulk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object** | [**InlineObject**](InlineObject.md)|  | 

### Return type

[**JobExecutionDelete**](JobExecutionDelete.md)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Execution deleted response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execution_delete**
> execution_delete(id)

Delete an exeuction by ID

### Example

* Api Key Authentication (rundeck_auth):
```python
from __future__ import print_function
import time
import olrundeck
from olrundeck.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = olrundeck.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: rundeck_auth
configuration = olrundeck.Configuration(
    host = "http://localhost",
    api_key = {
        'rundeck_auth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['rundeck_auth'] = 'Bearer'

# Enter a context with an instance of the API client
with olrundeck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = olrundeck.ExecutionApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete an exeuction by ID
        api_instance.execution_delete(id)
    except ApiException as e:
        print("Exception when calling ExecutionApi->execution_delete: %s\n" % e)
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
**200** | Success ! |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execution_input_files_list**
> object execution_input_files_list(id)

List input files for an execution

### Example

* Api Key Authentication (rundeck_auth):
```python
from __future__ import print_function
import time
import olrundeck
from olrundeck.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = olrundeck.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: rundeck_auth
configuration = olrundeck.Configuration(
    host = "http://localhost",
    api_key = {
        'rundeck_auth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['rundeck_auth'] = 'Bearer'

# Enter a context with an instance of the API client
with olrundeck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = olrundeck.ExecutionApi(api_client)
    id = 'id_example' # str | 

    try:
        # List input files for an execution
        api_response = api_instance.execution_input_files_list(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExecutionApi->execution_input_files_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**object**

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of execution input files |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execution_list_running**
> ExecutionList execution_list_running(project)

List job executions

### Example

* Api Key Authentication (rundeck_auth):
```python
from __future__ import print_function
import time
import olrundeck
from olrundeck.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = olrundeck.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: rundeck_auth
configuration = olrundeck.Configuration(
    host = "http://localhost",
    api_key = {
        'rundeck_auth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['rundeck_auth'] = 'Bearer'

# Enter a context with an instance of the API client
with olrundeck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = olrundeck.ExecutionApi(api_client)
    project = 'project_example' # str | Project name or * for all projects

    try:
        # List job executions
        api_response = api_instance.execution_list_running(project)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExecutionApi->execution_list_running: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name or * for all projects | 

### Return type

[**ExecutionList**](ExecutionList.md)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of executions for job |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execution_output_get**
> ExecutionOutput execution_output_get(id, offset=offset, maxlines=maxlines)

List input files for an execution

### Example

* Api Key Authentication (rundeck_auth):
```python
from __future__ import print_function
import time
import olrundeck
from olrundeck.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = olrundeck.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: rundeck_auth
configuration = olrundeck.Configuration(
    host = "http://localhost",
    api_key = {
        'rundeck_auth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['rundeck_auth'] = 'Bearer'

# Enter a context with an instance of the API client
with olrundeck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = olrundeck.ExecutionApi(api_client)
    id = 'id_example' # str | 
offset = 'offset_example' # str |  (optional)
maxlines = None # object |  (optional)

    try:
        # List input files for an execution
        api_response = api_instance.execution_output_get(id, offset=offset, maxlines=maxlines)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExecutionApi->execution_output_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **offset** | **str**|  | [optional] 
 **maxlines** | [**object**](.md)|  | [optional] 

### Return type

[**ExecutionOutput**](ExecutionOutput.md)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of execution input files |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execution_query**
> execution_query(project, status_filter=status_filter, abortedby_filter=abortedby_filter, user_filter=user_filter, recent_filter=recent_filter, older_filter=older_filter, begin=begin, adhoc=adhoc)

Query for Executions based on Job or Execution details

### Example

* Api Key Authentication (rundeck_auth):
```python
from __future__ import print_function
import time
import olrundeck
from olrundeck.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = olrundeck.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: rundeck_auth
configuration = olrundeck.Configuration(
    host = "http://localhost",
    api_key = {
        'rundeck_auth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['rundeck_auth'] = 'Bearer'

# Enter a context with an instance of the API client
with olrundeck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = olrundeck.ExecutionApi(api_client)
    project = 'project_example' # str | 
status_filter = 'status_filter_example' # str |  (optional)
abortedby_filter = 'abortedby_filter_example' # str | Username who aborted an execution (optional)
user_filter = 'user_filter_example' # str | Username who started the execution (optional)
recent_filter = 'recent_filter_example' # str | Use a simple text format to filter executions that completed within a period of time. The format is “XY” where X is an integer, and “Y” is one of: * h: hour * d: day  (optional)
older_filter = 'older_filter_example' # str | (same format as recentFilter) return executions that completed before the specified relative period of time (optional)
begin = 'begin_example' # str | Specify exact date for earliest execution completion time (optional)
adhoc = True # bool |  (optional)

    try:
        # Query for Executions based on Job or Execution details
        api_instance.execution_query(project, status_filter=status_filter, abortedby_filter=abortedby_filter, user_filter=user_filter, recent_filter=recent_filter, older_filter=older_filter, begin=begin, adhoc=adhoc)
    except ApiException as e:
        print("Exception when calling ExecutionApi->execution_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**|  | 
 **status_filter** | **str**|  | [optional] 
 **abortedby_filter** | **str**| Username who aborted an execution | [optional] 
 **user_filter** | **str**| Username who started the execution | [optional] 
 **recent_filter** | **str**| Use a simple text format to filter executions that completed within a period of time. The format is “XY” where X is an integer, and “Y” is one of: * h: hour * d: day  | [optional] 
 **older_filter** | **str**| (same format as recentFilter) return executions that completed before the specified relative period of time | [optional] 
 **begin** | **str**| Specify exact date for earliest execution completion time | [optional] 
 **adhoc** | **bool**|  | [optional] 

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
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execution_state_get**
> execution_state_get(id)

Get detail about the node and step state of an execution by ID. The execution can be currently running or completed.

### Example

* Api Key Authentication (rundeck_auth):
```python
from __future__ import print_function
import time
import olrundeck
from olrundeck.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = olrundeck.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: rundeck_auth
configuration = olrundeck.Configuration(
    host = "http://localhost",
    api_key = {
        'rundeck_auth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['rundeck_auth'] = 'Bearer'

# Enter a context with an instance of the API client
with olrundeck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = olrundeck.ExecutionApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get detail about the node and step state of an execution by ID. The execution can be currently running or completed.
        api_instance.execution_state_get(id)
    except ApiException as e:
        print("Exception when calling ExecutionApi->execution_state_get: %s\n" % e)
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
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execution_status_get**
> Execution execution_status_get(id)

Get the status of an execution by ID

### Example

* Api Key Authentication (rundeck_auth):
```python
from __future__ import print_function
import time
import olrundeck
from olrundeck.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = olrundeck.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: rundeck_auth
configuration = olrundeck.Configuration(
    host = "http://localhost",
    api_key = {
        'rundeck_auth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['rundeck_auth'] = 'Bearer'

# Enter a context with an instance of the API client
with olrundeck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = olrundeck.ExecutionApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get the status of an execution by ID
        api_response = api_instance.execution_status_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExecutionApi->execution_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Execution**](Execution.md)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Execution status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_execution_bulk_disable**
> JobBulkOperationResponse job_execution_bulk_disable(inline_object3)

Bulk disable job executions

### Example

* Api Key Authentication (rundeck_auth):
```python
from __future__ import print_function
import time
import olrundeck
from olrundeck.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = olrundeck.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: rundeck_auth
configuration = olrundeck.Configuration(
    host = "http://localhost",
    api_key = {
        'rundeck_auth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['rundeck_auth'] = 'Bearer'

# Enter a context with an instance of the API client
with olrundeck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = olrundeck.ExecutionApi(api_client)
    inline_object3 = olrundeck.InlineObject3() # InlineObject3 | 

    try:
        # Bulk disable job executions
        api_response = api_instance.job_execution_bulk_disable(inline_object3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExecutionApi->job_execution_bulk_disable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object3** | [**InlineObject3**](InlineObject3.md)|  | 

### Return type

[**JobBulkOperationResponse**](JobBulkOperationResponse.md)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job toggle execution response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_execution_bulk_enable**
> JobBulkOperationResponse job_execution_bulk_enable(inline_object2)

Bulk enable job executions

### Example

* Api Key Authentication (rundeck_auth):
```python
from __future__ import print_function
import time
import olrundeck
from olrundeck.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = olrundeck.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: rundeck_auth
configuration = olrundeck.Configuration(
    host = "http://localhost",
    api_key = {
        'rundeck_auth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['rundeck_auth'] = 'Bearer'

# Enter a context with an instance of the API client
with olrundeck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = olrundeck.ExecutionApi(api_client)
    inline_object2 = olrundeck.InlineObject2() # InlineObject2 | 

    try:
        # Bulk enable job executions
        api_response = api_instance.job_execution_bulk_enable(inline_object2)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExecutionApi->job_execution_bulk_enable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object2** | [**InlineObject2**](InlineObject2.md)|  | 

### Return type

[**JobBulkOperationResponse**](JobBulkOperationResponse.md)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

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
import olrundeck
from olrundeck.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = olrundeck.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: rundeck_auth
configuration = olrundeck.Configuration(
    host = "http://localhost",
    api_key = {
        'rundeck_auth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['rundeck_auth'] = 'Bearer'

# Enter a context with an instance of the API client
with olrundeck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = olrundeck.ExecutionApi(api_client)
    id = 56 # int | Job ID

    try:
        # Delete all job executions
        api_instance.job_execution_delete(id)
    except ApiException as e:
        print("Exception when calling ExecutionApi->job_execution_delete: %s\n" % e)
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
> object job_execution_disable(id)

Disable all executions for a job (scheduled or manual). (ACL requires toggle_execution action for a job.)

### Example

* Api Key Authentication (rundeck_auth):
```python
from __future__ import print_function
import time
import olrundeck
from olrundeck.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = olrundeck.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: rundeck_auth
configuration = olrundeck.Configuration(
    host = "http://localhost",
    api_key = {
        'rundeck_auth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['rundeck_auth'] = 'Bearer'

# Enter a context with an instance of the API client
with olrundeck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = olrundeck.ExecutionApi(api_client)
    id = None # object | 

    try:
        # Disable all executions for a job (scheduled or manual). (ACL requires toggle_execution action for a job.)
        api_response = api_instance.job_execution_disable(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExecutionApi->job_execution_disable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

**object**

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job executions disabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_execution_enable**
> object job_execution_enable(id)

Enable executions for a job. (ACL requires toggle_execution action for a job.)

### Example

* Api Key Authentication (rundeck_auth):
```python
from __future__ import print_function
import time
import olrundeck
from olrundeck.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = olrundeck.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: rundeck_auth
configuration = olrundeck.Configuration(
    host = "http://localhost",
    api_key = {
        'rundeck_auth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['rundeck_auth'] = 'Bearer'

# Enter a context with an instance of the API client
with olrundeck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = olrundeck.ExecutionApi(api_client)
    id = None # object | 

    try:
        # Enable executions for a job. (ACL requires toggle_execution action for a job.)
        api_response = api_instance.job_execution_enable(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExecutionApi->job_execution_enable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

**object**

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job executions enabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_execution_list**
> ExecutionList job_execution_list(id, status=status, max=max, offset=offset)

List job executions

### Example

* Api Key Authentication (rundeck_auth):
```python
from __future__ import print_function
import time
import olrundeck
from olrundeck.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = olrundeck.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: rundeck_auth
configuration = olrundeck.Configuration(
    host = "http://localhost",
    api_key = {
        'rundeck_auth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['rundeck_auth'] = 'Bearer'

# Enter a context with an instance of the API client
with olrundeck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = olrundeck.ExecutionApi(api_client)
    id = 'id_example' # str | Job ID
status = 'status_example' # str | the status of executions you want to be returned. Must be one of \"succeeded\", \"failed\", \"aborted\", or \"running\". If this parameter is blank or unset, include all executions. (optional)
max = 56 # int | indicate the maximum number of results to return. If unspecified, all results will be returned. (optional)
offset = 56 # int | indicate the 0-indexed offset for the first result to return. (optional)

    try:
        # List job executions
        api_response = api_instance.job_execution_list(id, status=status, max=max, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExecutionApi->job_execution_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Job ID | 
 **status** | **str**| the status of executions you want to be returned. Must be one of \&quot;succeeded\&quot;, \&quot;failed\&quot;, \&quot;aborted\&quot;, or \&quot;running\&quot;. If this parameter is blank or unset, include all executions. | [optional] 
 **max** | **int**| indicate the maximum number of results to return. If unspecified, all results will be returned. | [optional] 
 **offset** | **int**| indicate the 0-indexed offset for the first result to return. | [optional] 

### Return type

[**ExecutionList**](ExecutionList.md)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of executions for job |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_execution_run**
> Execution job_execution_run(id, body=body)

Run the specified job

### Example

* Api Key Authentication (rundeck_auth):
```python
from __future__ import print_function
import time
import olrundeck
from olrundeck.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = olrundeck.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: rundeck_auth
configuration = olrundeck.Configuration(
    host = "http://localhost",
    api_key = {
        'rundeck_auth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['rundeck_auth'] = 'Bearer'

# Enter a context with an instance of the API client
with olrundeck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = olrundeck.ExecutionApi(api_client)
    id = 'id_example' # str | Job ID
body = None # object |  (optional)

    try:
        # Run the specified job
        api_response = api_instance.job_execution_run(id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExecutionApi->job_execution_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Job ID | 
 **body** | **object**|  | [optional] 

### Return type

[**Execution**](Execution.md)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response for a valid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_retry_execution**
> ExecutionList job_retry_execution(job_id, execution_id, body=body)

Retry a failed job execution on failed nodes only or on the same as the execution. This is the same functionality as the `Retry Failed Nodes ...` button on the execution page.

### Example

* Api Key Authentication (rundeck_auth):
```python
from __future__ import print_function
import time
import olrundeck
from olrundeck.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = olrundeck.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: rundeck_auth
configuration = olrundeck.Configuration(
    host = "http://localhost",
    api_key = {
        'rundeck_auth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['rundeck_auth'] = 'Bearer'

# Enter a context with an instance of the API client
with olrundeck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = olrundeck.ExecutionApi(api_client)
    job_id = 'job_id_example' # str | 
execution_id = 56 # int | 
body = None # object |  (optional)

    try:
        # Retry a failed job execution on failed nodes only or on the same as the execution. This is the same functionality as the `Retry Failed Nodes ...` button on the execution page.
        api_response = api_instance.job_retry_execution(job_id, execution_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExecutionApi->job_retry_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 
 **execution_id** | **int**|  | 
 **body** | **object**|  | [optional] 

### Return type

[**ExecutionList**](ExecutionList.md)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Exected response to a valid request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_executions_disable**
> object system_executions_disable()

Disables executions, preventing adhoc and manual and scheduled jobs from running.

### Example

* Api Key Authentication (rundeck_auth):
```python
from __future__ import print_function
import time
import olrundeck
from olrundeck.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = olrundeck.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: rundeck_auth
configuration = olrundeck.Configuration(
    host = "http://localhost",
    api_key = {
        'rundeck_auth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['rundeck_auth'] = 'Bearer'

# Enter a context with an instance of the API client
with olrundeck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = olrundeck.ExecutionApi(api_client)
    
    try:
        # Disables executions, preventing adhoc and manual and scheduled jobs from running.
        api_response = api_instance.system_executions_disable()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExecutionApi->system_executions_disable: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response to a valid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_executions_enable**
> object system_executions_enable()

Enables executions, allowing adhoc and manual and scheduled jobs to be run

### Example

* Api Key Authentication (rundeck_auth):
```python
from __future__ import print_function
import time
import olrundeck
from olrundeck.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = olrundeck.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: rundeck_auth
configuration = olrundeck.Configuration(
    host = "http://localhost",
    api_key = {
        'rundeck_auth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['rundeck_auth'] = 'Bearer'

# Enter a context with an instance of the API client
with olrundeck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = olrundeck.ExecutionApi(api_client)
    
    try:
        # Enables executions, allowing adhoc and manual and scheduled jobs to be run
        api_response = api_instance.system_executions_enable()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExecutionApi->system_executions_enable: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response to a valid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_incomplete_log_storage_executions_get**
> IncompleteLogExecutions system_incomplete_log_storage_executions_get()

List all executions with incomplete log storage

### Example

* Api Key Authentication (rundeck_auth):
```python
from __future__ import print_function
import time
import olrundeck
from olrundeck.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = olrundeck.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: rundeck_auth
configuration = olrundeck.Configuration(
    host = "http://localhost",
    api_key = {
        'rundeck_auth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['rundeck_auth'] = 'Bearer'

# Enter a context with an instance of the API client
with olrundeck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = olrundeck.ExecutionApi(api_client)
    
    try:
        # List all executions with incomplete log storage
        api_response = api_instance.system_incomplete_log_storage_executions_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExecutionApi->system_incomplete_log_storage_executions_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IncompleteLogExecutions**](IncompleteLogExecutions.md)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response to a valid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_incomplete_log_storage_executions_resume**
> object system_incomplete_log_storage_executions_resume()

Resume processing incomplete Log Storage uploads

### Example

* Api Key Authentication (rundeck_auth):
```python
from __future__ import print_function
import time
import olrundeck
from olrundeck.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = olrundeck.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: rundeck_auth
configuration = olrundeck.Configuration(
    host = "http://localhost",
    api_key = {
        'rundeck_auth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['rundeck_auth'] = 'Bearer'

# Enter a context with an instance of the API client
with olrundeck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = olrundeck.ExecutionApi(api_client)
    
    try:
        # Resume processing incomplete Log Storage uploads
        api_response = api_instance.system_incomplete_log_storage_executions_resume()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExecutionApi->system_incomplete_log_storage_executions_resume: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response to a valid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

