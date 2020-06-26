# FileApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execution_input_files_list**](FileApi.md#execution_input_files_list) | **GET** /api/26/execution/{id}/input/files | List input files for an execution
[**execution_output_get**](FileApi.md#execution_output_get) | **GET** /api/26/execution/{id}/output | List input files for an execution


# **execution_input_files_list**
> object execution_input_files_list(id)

List input files for an execution

### Example
```R
library(openlattice_rundeck)

var.id <- 'id_example' # character | 

#List input files for an execution
api.instance <- FileApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$execution_input_files_list(var.id)
dput(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **character**|  | 

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
| **200** | List of execution input files |  -  |

# **execution_output_get**
> ExecutionOutput execution_output_get(id, offset=var.offset, maxlines=var.maxlines)

List input files for an execution

### Example
```R
library(openlattice_rundeck)

var.id <- 'id_example' # character | 
var.offset <- 'offset_example' # character | 
var.maxlines <- TODO # AnyType | 

#List input files for an execution
api.instance <- FileApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$execution_output_get(var.id, offset=var.offset, maxlines=var.maxlines)
dput(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **character**|  | 
 **offset** | **character**|  | [optional] 
 **maxlines** | [**AnyType**](.md)|  | [optional] 

### Return type

[**ExecutionOutput**](ExecutionOutput.md)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of execution input files |  -  |

