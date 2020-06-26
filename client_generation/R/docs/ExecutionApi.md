# ExecutionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api26_execution_id_output_get**](ExecutionApi.md#api26_execution_id_output_get) | **GET** /api/26/execution/{id}/output | List input files for an execution


# **api26_execution_id_output_get**
> api26_execution_id_output_get(id, offset=var.offset, maxlines=var.maxlines)

List input files for an execution

### Example
```R
library(openlattice-rundeck)

var.id <- 'id_example' # character | 
var.offset <- 'offset_example' # character | 
var.maxlines <- TODO # AnyType | 

#List input files for an execution
api.instance <- ExecutionApi$new()
api.instance$api26_execution_id_output_get(var.id, offset=var.offset, maxlines=var.maxlines)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **character**|  | 
 **offset** | **character**|  | [optional] 
 **maxlines** | [**AnyType**](.md)|  | [optional] 

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
| **200** | List of execution input files |  -  |

