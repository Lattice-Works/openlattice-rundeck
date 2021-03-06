# olrundeck.ClusterApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_scheduled_jobs_for_server**](ClusterApi.md#system_scheduled_jobs_for_server) | **GET** /api/26/scheduler/server/{uuid}/jobs | List the scheduled Jobs with their schedule owned by the cluster server with the specified UUID
[**system_scheduled_jobs_list**](ClusterApi.md#system_scheduled_jobs_list) | **GET** /api/26/scheduler/jobs | List the scheduled Jobs with their schedule owned by the cluster server
[**system_scheduler_takeover**](ClusterApi.md#system_scheduler_takeover) | **PUT** /api/26/scheduler/takeover | Tell a Rundeck server in cluster mode to claim all scheduled jobs from another cluster server


# **system_scheduled_jobs_for_server**
> list[Job] system_scheduled_jobs_for_server(uuid)

List the scheduled Jobs with their schedule owned by the cluster server with the specified UUID

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
    api_instance = olrundeck.ClusterApi(api_client)
    uuid = 'uuid_example' # str | The ID of the user to retrieve profile information for

    try:
        # List the scheduled Jobs with their schedule owned by the cluster server with the specified UUID
        api_response = api_instance.system_scheduled_jobs_for_server(uuid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClusterApi->system_scheduled_jobs_for_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The ID of the user to retrieve profile information for | 

### Return type

[**list[Job]**](Job.md)

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

# **system_scheduled_jobs_list**
> list[Job] system_scheduled_jobs_list()

List the scheduled Jobs with their schedule owned by the cluster server

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
    api_instance = olrundeck.ClusterApi(api_client)
    
    try:
        # List the scheduled Jobs with their schedule owned by the cluster server
        api_response = api_instance.system_scheduled_jobs_list()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClusterApi->system_scheduled_jobs_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Job]**](Job.md)

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

# **system_scheduler_takeover**
> TakeoverScheduleResponse system_scheduler_takeover(inline_object10)

Tell a Rundeck server in cluster mode to claim all scheduled jobs from another cluster server

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
    api_instance = olrundeck.ClusterApi(api_client)
    inline_object10 = olrundeck.InlineObject10() # InlineObject10 | 

    try:
        # Tell a Rundeck server in cluster mode to claim all scheduled jobs from another cluster server
        api_response = api_instance.system_scheduler_takeover(inline_object10)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClusterApi->system_scheduler_takeover: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object10** | [**InlineObject10**](InlineObject10.md)|  | 

### Return type

[**TakeoverScheduleResponse**](TakeoverScheduleResponse.md)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response to a valid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

