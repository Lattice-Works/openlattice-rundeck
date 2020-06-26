# ScheduleApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**job_schedule_bulk_disable**](ScheduleApi.md#job_schedule_bulk_disable) | **POST** /api/26/jobs/schedule/disable | Bulk disable job schedule
[**job_schedule_bulk_enable**](ScheduleApi.md#job_schedule_bulk_enable) | **POST** /api/26/jobs/schedule/enable | Bulk enable job schedule
[**job_schedule_disable**](ScheduleApi.md#job_schedule_disable) | **POST** /api/26/job/{id}/schedule/disable | Disable the schedule for a job. (ACL requires toggle_schedule action for a job.)
[**job_schedule_enable**](ScheduleApi.md#job_schedule_enable) | **POST** /api/26/job/{id}/schedule/enable | Enable the schedule for a job. (ACL requires toggle_schedule action for a job.)


# **job_schedule_bulk_disable**
> JobBulkOperationResponse job_schedule_bulk_disable(inline_object5)

Bulk disable job schedule

### Example
```R
library(openlattice_rundeck)

var.inline_object5 <- inline_object_5$new(list("ids_example")) # InlineObject5 | 

#Bulk disable job schedule
api.instance <- ScheduleApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$job_schedule_bulk_disable(var.inline_object5)
dput(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object5** | [**InlineObject5**](InlineObject5.md)|  | 

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
| **200** | Job toggle schedule response |  -  |

# **job_schedule_bulk_enable**
> JobBulkOperationResponse job_schedule_bulk_enable(inline_object4)

Bulk enable job schedule

### Example
```R
library(openlattice_rundeck)

var.inline_object4 <- inline_object_4$new(list("ids_example")) # InlineObject4 | 

#Bulk enable job schedule
api.instance <- ScheduleApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$job_schedule_bulk_enable(var.inline_object4)
dput(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object4** | [**InlineObject4**](InlineObject4.md)|  | 

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
| **200** | Job toggle schedule response |  -  |

# **job_schedule_disable**
> object job_schedule_disable(id)

Disable the schedule for a job. (ACL requires toggle_schedule action for a job.)

### Example
```R
library(openlattice_rundeck)

var.id <- TODO # AnyType | 

#Disable the schedule for a job. (ACL requires toggle_schedule action for a job.)
api.instance <- ScheduleApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$job_schedule_disable(var.id)
dput(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**AnyType**](.md)|  | 

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
| **200** | Job schedules disabled |  -  |

# **job_schedule_enable**
> object job_schedule_enable(id)

Enable the schedule for a job. (ACL requires toggle_schedule action for a job.)

### Example
```R
library(openlattice_rundeck)

var.id <- TODO # AnyType | 

#Enable the schedule for a job. (ACL requires toggle_schedule action for a job.)
api.instance <- ScheduleApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$job_schedule_enable(var.id)
dput(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**AnyType**](.md)|  | 

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
| **200** | Job schedule enabled |  -  |

