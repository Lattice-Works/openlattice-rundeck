# ClusterApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_scheduled_jobs_for_server**](ClusterApi.md#system_scheduled_jobs_for_server) | **GET** /api/26/scheduler/server/{uuid}/jobs | List the scheduled Jobs with their schedule owned by the cluster server with the specified UUID
[**system_scheduled_jobs_list**](ClusterApi.md#system_scheduled_jobs_list) | **GET** /api/26/scheduler/jobs | List the scheduled Jobs with their schedule owned by the cluster server
[**system_scheduler_takeover**](ClusterApi.md#system_scheduler_takeover) | **PUT** /api/26/scheduler/takeover | Tell a Rundeck server in cluster mode to claim all scheduled jobs from another cluster server


# **system_scheduled_jobs_for_server**
> array[Job] system_scheduled_jobs_for_server(uuid)

List the scheduled Jobs with their schedule owned by the cluster server with the specified UUID

### Example
```R
library(olrundeck)

var.uuid <- 'uuid_example' # character | The ID of the user to retrieve profile information for

#List the scheduled Jobs with their schedule owned by the cluster server with the specified UUID
api.instance <- ClusterApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$system_scheduled_jobs_for_server(var.uuid)
dput(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **character**| The ID of the user to retrieve profile information for | 

### Return type

[**array[Job]**](Job.md)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Expected response to a valid request |  -  |

# **system_scheduled_jobs_list**
> array[Job] system_scheduled_jobs_list()

List the scheduled Jobs with their schedule owned by the cluster server

### Example
```R
library(olrundeck)


#List the scheduled Jobs with their schedule owned by the cluster server
api.instance <- ClusterApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$system_scheduled_jobs_list()
dput(result)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**array[Job]**](Job.md)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Expected response to a valid request |  -  |

# **system_scheduler_takeover**
> TakeoverScheduleResponse system_scheduler_takeover(inline_object10)

Tell a Rundeck server in cluster mode to claim all scheduled jobs from another cluster server

### Example
```R
library(olrundeck)

var.inline_object10 <- inline_object_10$new(_api_26_scheduler_takeover_server$new("uuid_example", "all_example"), "project_example", _api_26_scheduler_takeover_job$new("id_example")) # InlineObject10 | 

#Tell a Rundeck server in cluster mode to claim all scheduled jobs from another cluster server
api.instance <- ClusterApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$system_scheduler_takeover(var.inline_object10)
dput(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object10** | [**InlineObject10**](InlineObject10.md)|  | 

### Return type

[**TakeoverScheduleResponse**](TakeoverScheduleResponse.md)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Expected response to a valid request |  -  |

