# StorageApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storage_key_create**](StorageApi.md#storage_key_create) | **POST** /api/26/storage/keys/{path} | Set storage key contents
[**storage_key_delete**](StorageApi.md#storage_key_delete) | **DELETE** /api/26/storage/keys/{path} | Deletes the file if it exists and returns 204 response.
[**storage_key_get_material**](StorageApi.md#storage_key_get_material) | **GET** /api/26/storage/keys/{keyPath} | Get key material at the specified PATH
[**storage_key_get_metadata**](StorageApi.md#storage_key_get_metadata) | **GET** /api/26/storage/keys/{path} | List resources at the specified PATH
[**storage_key_update**](StorageApi.md#storage_key_update) | **PUT** /api/26/storage/keys/{path} | Set storage key contents


# **storage_key_create**
> storage_key_create(path, body, content_type=var.content_type)

Set storage key contents

### Example
```R
library(openlattice_rundeck)

var.path <- TODO # AnyType | Key path
var.body <- NULL # object | 
var.content_type <- TODO # AnyType | 

#Set storage key contents
api.instance <- StorageApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
api.instance$storage_key_create(var.path, var.body, content_type=var.content_type)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | [**AnyType**](.md)| Key path | 
 **body** | **object**|  | 
 **content_type** | [**AnyType**](.md)|  | [optional] 

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
| **200** | Success ! |  -  |

# **storage_key_delete**
> storage_key_delete(path)

Deletes the file if it exists and returns 204 response.

### Example
```R
library(openlattice_rundeck)

var.path <- TODO # AnyType | Key path

#Deletes the file if it exists and returns 204 response.
api.instance <- StorageApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
api.instance$storage_key_delete(var.path)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | [**AnyType**](.md)| Key path | 

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
| **200** | Success ! |  -  |

# **storage_key_get_material**
> object storage_key_get_material(key_path, accept)

Get key material at the specified PATH

### Example
```R
library(openlattice_rundeck)

var.key_path <- TODO # AnyType | Key path
var.accept <- 'accept_example' # character | 

#Get key material at the specified PATH
api.instance <- StorageApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$storage_key_get_material(var.key_path, var.accept)
dput(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_path** | [**AnyType**](.md)| Key path | 
 **accept** | Enum [*/*] |  | 

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
| **200** | Content |  -  |

# **storage_key_get_metadata**
> StorageKeyListResponse storage_key_get_metadata(path, accept)

List resources at the specified PATH

### Example
```R
library(openlattice_rundeck)

var.path <- TODO # AnyType | Key path
var.accept <- 'accept_example' # character | 

#List resources at the specified PATH
api.instance <- StorageApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$storage_key_get_metadata(var.path, var.accept)
dput(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | [**AnyType**](.md)| Key path | 
 **accept** | Enum [application/json] |  | 

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
| **200** | Content |  -  |

# **storage_key_update**
> storage_key_update(path, body, content_type=var.content_type)

Set storage key contents

### Example
```R
library(openlattice_rundeck)

var.path <- TODO # AnyType | Key path
var.body <- NULL # object | 
var.content_type <- TODO # AnyType | 

#Set storage key contents
api.instance <- StorageApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
api.instance$storage_key_update(var.path, var.body, content_type=var.content_type)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | [**AnyType**](.md)| Key path | 
 **body** | **object**|  | 
 **content_type** | [**AnyType**](.md)|  | [optional] 

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
| **200** | Content updated |  -  |

