# JobApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**job_workflow_get**](JobApi.md#job_workflow_get) | **GET** /api/34/job/{id}/workflow | Get job workflow tree.


# **job_workflow_get**
> job_workflow_get(id)

Get job workflow tree.

### Example
```R
library(openlattice-rundeck)

var.id <- 'id_example' # character | 

#Get job workflow tree.
api.instance <- JobApi$new()
api.instance$job_workflow_get(var.id)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **character**|  | 

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
| **200** | Expected response to a valid request. |  -  |

