# olrundeck.LogApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_incomplete_log_storage_executions_get**](LogApi.md#system_incomplete_log_storage_executions_get) | **GET** /api/26/system/logstorage/incomplete | List all executions with incomplete log storage
[**system_incomplete_log_storage_executions_resume**](LogApi.md#system_incomplete_log_storage_executions_resume) | **POST** /api/26/system/logstorage/incomplete/resume | Resume processing incomplete Log Storage uploads
[**system_log_storage_info_get**](LogApi.md#system_log_storage_info_get) | **GET** /api/26/system/logstorage | Get Log Storage information and stats


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
    api_instance = olrundeck.LogApi(api_client)
    
    try:
        # List all executions with incomplete log storage
        api_response = api_instance.system_incomplete_log_storage_executions_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LogApi->system_incomplete_log_storage_executions_get: %s\n" % e)
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
    api_instance = olrundeck.LogApi(api_client)
    
    try:
        # Resume processing incomplete Log Storage uploads
        api_response = api_instance.system_incomplete_log_storage_executions_resume()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LogApi->system_incomplete_log_storage_executions_resume: %s\n" % e)
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

# **system_log_storage_info_get**
> LogStorage system_log_storage_info_get()

Get Log Storage information and stats

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
    api_instance = olrundeck.LogApi(api_client)
    
    try:
        # Get Log Storage information and stats
        api_response = api_instance.system_log_storage_info_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LogApi->system_log_storage_info_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LogStorage**](LogStorage.md)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected reponse to a valid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

