# StorageApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storage_key_delete**](StorageApi.md#storage_key_delete) | **DELETE** /api/26/storage/keys/{path} | Deletes the file if it exists and returns 204 response.


# **storage_key_delete**
> storage_key_delete(path)

Deletes the file if it exists and returns 204 response.

### Example
```R
library(openlattice-rundeck)

var.path <- TODO # AnyType | Key path

#Deletes the file if it exists and returns 204 response.
api.instance <- StorageApi$new()
api.instance$storage_key_delete(var.path)
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

