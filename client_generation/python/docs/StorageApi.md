# openlattice_rundeck.StorageApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storage_key_create**](StorageApi.md#storage_key_create) | **POST** /api/26/storage/keys/{path} | Set storage key contents
[**storage_key_delete**](StorageApi.md#storage_key_delete) | **DELETE** /api/26/storage/keys/{path} | Deletes the file if it exists and returns 204 response.
[**storage_key_get_material**](StorageApi.md#storage_key_get_material) | **GET** /api/26/storage/keys/{keyPath} | Get key material at the specified PATH
[**storage_key_get_metadata**](StorageApi.md#storage_key_get_metadata) | **GET** /api/26/storage/keys/{path} | List resources at the specified PATH
[**storage_key_update**](StorageApi.md#storage_key_update) | **PUT** /api/26/storage/keys/{path} | Set storage key contents


# **storage_key_create**
> storage_key_create(path, body, content_type=content_type)

Set storage key contents

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
    api_instance = openlattice_rundeck.StorageApi(api_client)
    path = None # object | Key path
body = None # object | 
content_type = None # object |  (optional)

    try:
        # Set storage key contents
        api_instance.storage_key_create(path, body, content_type=content_type)
    except ApiException as e:
        print("Exception when calling StorageApi->storage_key_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | [**object**](.md)| Key path | 
 **body** | **object**|  | 
 **content_type** | [**object**](.md)|  | [optional] 

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

# **storage_key_delete**
> storage_key_delete(path)

Deletes the file if it exists and returns 204 response.

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
    api_instance = openlattice_rundeck.StorageApi(api_client)
    path = None # object | Key path

    try:
        # Deletes the file if it exists and returns 204 response.
        api_instance.storage_key_delete(path)
    except ApiException as e:
        print("Exception when calling StorageApi->storage_key_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | [**object**](.md)| Key path | 

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

# **storage_key_get_material**
> object storage_key_get_material(key_path, accept)

Get key material at the specified PATH

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
    api_instance = openlattice_rundeck.StorageApi(api_client)
    key_path = None # object | Key path
accept = 'accept_example' # str | 

    try:
        # Get key material at the specified PATH
        api_response = api_instance.storage_key_get_material(key_path, accept)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->storage_key_get_material: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_path** | [**object**](.md)| Key path | 
 **accept** | **str**|  | 

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
**200** | Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_key_get_metadata**
> StorageKeyListResponse storage_key_get_metadata(path, accept)

List resources at the specified PATH

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
    api_instance = openlattice_rundeck.StorageApi(api_client)
    path = None # object | Key path
accept = 'accept_example' # str | 

    try:
        # List resources at the specified PATH
        api_response = api_instance.storage_key_get_metadata(path, accept)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->storage_key_get_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | [**object**](.md)| Key path | 
 **accept** | **str**|  | 

### Return type

[**StorageKeyListResponse**](StorageKeyListResponse.md)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_key_update**
> storage_key_update(path, body, content_type=content_type)

Set storage key contents

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
    api_instance = openlattice_rundeck.StorageApi(api_client)
    path = None # object | Key path
body = None # object | 
content_type = None # object |  (optional)

    try:
        # Set storage key contents
        api_instance.storage_key_update(path, body, content_type=content_type)
    except ApiException as e:
        print("Exception when calling StorageApi->storage_key_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | [**object**](.md)| Key path | 
 **body** | **object**|  | 
 **content_type** | [**object**](.md)|  | [optional] 

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
**200** | Content updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

