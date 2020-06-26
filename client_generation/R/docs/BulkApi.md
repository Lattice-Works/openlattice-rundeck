# BulkApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**job_bulk_delete**](BulkApi.md#job_bulk_delete) | **POST** /api/26/jobs/delete | Delete multiple job definitions at once


# **job_bulk_delete**
> JobBulkOperationResponse job_bulk_delete(inline_object1)

Delete multiple job definitions at once

### Example
```R
library(openlattice_rundeck)

var.inline_object1 <- inline_object_1$new(list("ids_example")) # InlineObject1 | 

#Delete multiple job definitions at once
api.instance <- BulkApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$job_bulk_delete(var.inline_object1)
dput(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object1** | [**InlineObject1**](InlineObject1.md)|  | 

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
| **200** | Job deleted response |  -  |

