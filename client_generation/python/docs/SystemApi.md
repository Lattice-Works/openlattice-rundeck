# openlattice_rundeck.SystemApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_acl_policy_create**](SystemApi.md#system_acl_policy_create) | **POST** /api/26/system/acl/{policyName} | Create a policy
[**system_acl_policy_delete**](SystemApi.md#system_acl_policy_delete) | **DELETE** /api/26/system/acl/{policyName} | Delete policy
[**system_acl_policy_get**](SystemApi.md#system_acl_policy_get) | **GET** /api/26/system/acl/{policyName} | Retrieve the YAML texas of the ACL Policy file
[**system_acl_policy_list**](SystemApi.md#system_acl_policy_list) | **GET** /api/26/system/acl/ | List ACL Policies
[**system_acl_policy_update**](SystemApi.md#system_acl_policy_update) | **PUT** /api/26/system/acl/{policyName} | Update policy
[**system_executions_disable**](SystemApi.md#system_executions_disable) | **POST** /api/26/system/executions/disable | Disables executions, preventing adhoc and manual and scheduled jobs from running.
[**system_executions_enable**](SystemApi.md#system_executions_enable) | **POST** /api/26/system/executions/enable | Enables executions, allowing adhoc and manual and scheduled jobs to be run
[**system_incomplete_log_storage_executions_get**](SystemApi.md#system_incomplete_log_storage_executions_get) | **GET** /api/26/system/logstorage/incomplete | List all executions with incomplete log storage
[**system_incomplete_log_storage_executions_resume**](SystemApi.md#system_incomplete_log_storage_executions_resume) | **POST** /api/26/system/logstorage/incomplete/resume | Resume processing incomplete Log Storage uploads
[**system_info_get**](SystemApi.md#system_info_get) | **GET** /api/26/system/info | Get Rundeck server information and stats
[**system_log_storage_info_get**](SystemApi.md#system_log_storage_info_get) | **GET** /api/26/system/logstorage | Get Log Storage information and stats


# **system_acl_policy_create**
> system_acl_policy_create(policy_name, inline_object12)

Create a policy

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
    api_instance = openlattice_rundeck.SystemApi(api_client)
    policy_name = 'policy_name_example' # str | Policy file name
inline_object12 = openlattice_rundeck.InlineObject12() # InlineObject12 | 

    try:
        # Create a policy
        api_instance.system_acl_policy_create(policy_name, inline_object12)
    except ApiException as e:
        print("Exception when calling SystemApi->system_acl_policy_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_name** | **str**| Policy file name | 
 **inline_object12** | [**InlineObject12**](InlineObject12.md)|  | 

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
**200** | Success ! |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_acl_policy_delete**
> system_acl_policy_delete(policy_name)

Delete policy

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
    api_instance = openlattice_rundeck.SystemApi(api_client)
    policy_name = 'policy_name_example' # str | Policy file name

    try:
        # Delete policy
        api_instance.system_acl_policy_delete(policy_name)
    except ApiException as e:
        print("Exception when calling SystemApi->system_acl_policy_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_name** | **str**| Policy file name | 

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

# **system_acl_policy_get**
> system_acl_policy_get(policy_name)

Retrieve the YAML texas of the ACL Policy file

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
    api_instance = openlattice_rundeck.SystemApi(api_client)
    policy_name = 'policy_name_example' # str | Policy file name

    try:
        # Retrieve the YAML texas of the ACL Policy file
        api_instance.system_acl_policy_get(policy_name)
    except ApiException as e:
        print("Exception when calling SystemApi->system_acl_policy_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_name** | **str**| Policy file name | 

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

# **system_acl_policy_list**
> system_acl_policy_list()

List ACL Policies

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
    api_instance = openlattice_rundeck.SystemApi(api_client)
    
    try:
        # List ACL Policies
        api_instance.system_acl_policy_list()
    except ApiException as e:
        print("Exception when calling SystemApi->system_acl_policy_list: %s\n" % e)
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

# **system_acl_policy_update**
> system_acl_policy_update(policy_name, inline_object11)

Update policy

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
    api_instance = openlattice_rundeck.SystemApi(api_client)
    policy_name = 'policy_name_example' # str | Policy file name
inline_object11 = openlattice_rundeck.InlineObject11() # InlineObject11 | 

    try:
        # Update policy
        api_instance.system_acl_policy_update(policy_name, inline_object11)
    except ApiException as e:
        print("Exception when calling SystemApi->system_acl_policy_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_name** | **str**| Policy file name | 
 **inline_object11** | [**InlineObject11**](InlineObject11.md)|  | 

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

# **system_executions_disable**
> system_executions_disable()

Disables executions, preventing adhoc and manual and scheduled jobs from running.

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
    api_instance = openlattice_rundeck.SystemApi(api_client)
    
    try:
        # Disables executions, preventing adhoc and manual and scheduled jobs from running.
        api_instance.system_executions_disable()
    except ApiException as e:
        print("Exception when calling SystemApi->system_executions_disable: %s\n" % e)
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

# **system_executions_enable**
> system_executions_enable()

Enables executions, allowing adhoc and manual and scheduled jobs to be run

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
    api_instance = openlattice_rundeck.SystemApi(api_client)
    
    try:
        # Enables executions, allowing adhoc and manual and scheduled jobs to be run
        api_instance.system_executions_enable()
    except ApiException as e:
        print("Exception when calling SystemApi->system_executions_enable: %s\n" % e)
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

# **system_incomplete_log_storage_executions_get**
> system_incomplete_log_storage_executions_get()

List all executions with incomplete log storage

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
    api_instance = openlattice_rundeck.SystemApi(api_client)
    
    try:
        # List all executions with incomplete log storage
        api_instance.system_incomplete_log_storage_executions_get()
    except ApiException as e:
        print("Exception when calling SystemApi->system_incomplete_log_storage_executions_get: %s\n" % e)
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

# **system_incomplete_log_storage_executions_resume**
> system_incomplete_log_storage_executions_resume()

Resume processing incomplete Log Storage uploads

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
    api_instance = openlattice_rundeck.SystemApi(api_client)
    
    try:
        # Resume processing incomplete Log Storage uploads
        api_instance.system_incomplete_log_storage_executions_resume()
    except ApiException as e:
        print("Exception when calling SystemApi->system_incomplete_log_storage_executions_resume: %s\n" % e)
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

# **system_info_get**
> system_info_get()

Get Rundeck server information and stats

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
    api_instance = openlattice_rundeck.SystemApi(api_client)
    
    try:
        # Get Rundeck server information and stats
        api_instance.system_info_get()
    except ApiException as e:
        print("Exception when calling SystemApi->system_info_get: %s\n" % e)
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
**200** | System info response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_log_storage_info_get**
> system_log_storage_info_get()

Get Log Storage information and stats

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
    api_instance = openlattice_rundeck.SystemApi(api_client)
    
    try:
        # Get Log Storage information and stats
        api_instance.system_log_storage_info_get()
    except ApiException as e:
        print("Exception when calling SystemApi->system_log_storage_info_get: %s\n" % e)
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
**200** | Expected reponse to a valid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

