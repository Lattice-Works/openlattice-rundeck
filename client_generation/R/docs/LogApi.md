# LogApi

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
```R
library(olrundeck)


#List all executions with incomplete log storage
api.instance <- LogApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$system_incomplete_log_storage_executions_get()
dput(result)
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
| **200** | Expected response to a valid request |  -  |

# **system_incomplete_log_storage_executions_resume**
> object system_incomplete_log_storage_executions_resume()

Resume processing incomplete Log Storage uploads

### Example
```R
library(olrundeck)


#Resume processing incomplete Log Storage uploads
api.instance <- LogApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$system_incomplete_log_storage_executions_resume()
dput(result)
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
| **200** | Expected response to a valid request |  -  |

# **system_log_storage_info_get**
> LogStorage system_log_storage_info_get()

Get Log Storage information and stats

### Example
```R
library(olrundeck)


#Get Log Storage information and stats
api.instance <- LogApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$system_log_storage_info_get()
dput(result)
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
| **200** | Expected reponse to a valid request |  -  |

