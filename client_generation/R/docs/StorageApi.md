# StorageApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api26_storage_keys_path_delete**](StorageApi.md#api26_storage_keys_path_delete) | **DELETE** /api/26/storage/keys/{path} | Deletes the file if it exists and returns 204 response.


# **api26_storage_keys_path_delete**
> api26_storage_keys_path_delete(path)

Deletes the file if it exists and returns 204 response.

### Example
```R
library(openlattice-rundeck)

var.path <- TODO # AnyType | Key path

#Deletes the file if it exists and returns 204 response.
api.instance <- StorageApi$new()
api.instance$api26_storage_keys_path_delete(var.path)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | [**AnyType**](.md)| Key path | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success ! |  -  |

