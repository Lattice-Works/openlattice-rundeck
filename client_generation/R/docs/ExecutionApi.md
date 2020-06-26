# ExecutionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execution_bulk_delete**](ExecutionApi.md#execution_bulk_delete) | **POST** /api/26/executions/delete | Bulk delete executions
[**execution_delete**](ExecutionApi.md#execution_delete) | **DELETE** /api/26/execution/{id} | Delete an exeuction by ID
[**execution_input_files_list**](ExecutionApi.md#execution_input_files_list) | **GET** /api/26/execution/{id}/input/files | List input files for an execution
[**execution_list_running**](ExecutionApi.md#execution_list_running) | **GET** /api/26/project/{project}/executions/running | List job executions
[**execution_output_get**](ExecutionApi.md#execution_output_get) | **GET** /api/26/execution/{id}/output | List input files for an execution
[**execution_query**](ExecutionApi.md#execution_query) | **GET** /api/26/project/{project}/executions | Query for Executions based on Job or Execution details
[**execution_state_get**](ExecutionApi.md#execution_state_get) | **GET** /api/26/execution/{id}/state | Get detail about the node and step state of an execution by ID. The execution can be currently running or completed.
[**execution_status_get**](ExecutionApi.md#execution_status_get) | **GET** /api/26/execution/{id} | Get the status of an execution by ID
[**job_execution_bulk_disable**](ExecutionApi.md#job_execution_bulk_disable) | **POST** /api/26/jobs/execution/disable | Bulk disable job executions
[**job_execution_bulk_enable**](ExecutionApi.md#job_execution_bulk_enable) | **POST** /api/26/jobs/execution/enable | Bulk enable job executions
[**job_execution_delete**](ExecutionApi.md#job_execution_delete) | **DELETE** /api/26/job/{id}/executions | Delete all job executions
[**job_execution_disable**](ExecutionApi.md#job_execution_disable) | **POST** /api/26/job/{id}/execution/disable | Disable all executions for a job (scheduled or manual). (ACL requires toggle_execution action for a job.)
[**job_execution_enable**](ExecutionApi.md#job_execution_enable) | **POST** /api/26/job/{id}/execution/enable | Enable executions for a job. (ACL requires toggle_execution action for a job.)
[**job_execution_list**](ExecutionApi.md#job_execution_list) | **GET** /api/26/job/{id}/executions | List job executions
[**job_execution_run**](ExecutionApi.md#job_execution_run) | **POST** /api/26/job/{id}/executions | Run the specified job
[**job_retry_execution**](ExecutionApi.md#job_retry_execution) | **POST** /api/26/job/{jobID}/retry/{executionID} | Retry a failed job execution on failed nodes only or on the same as the execution. This is the same functionality as the &#x60;Retry Failed Nodes ...&#x60; button on the execution page.
[**system_executions_disable**](ExecutionApi.md#system_executions_disable) | **POST** /api/26/system/executions/disable | Disables executions, preventing adhoc and manual and scheduled jobs from running.
[**system_executions_enable**](ExecutionApi.md#system_executions_enable) | **POST** /api/26/system/executions/enable | Enables executions, allowing adhoc and manual and scheduled jobs to be run
[**system_incomplete_log_storage_executions_get**](ExecutionApi.md#system_incomplete_log_storage_executions_get) | **GET** /api/26/system/logstorage/incomplete | List all executions with incomplete log storage
[**system_incomplete_log_storage_executions_resume**](ExecutionApi.md#system_incomplete_log_storage_executions_resume) | **POST** /api/26/system/logstorage/incomplete/resume | Resume processing incomplete Log Storage uploads


# **execution_bulk_delete**
> JobExecutionDelete execution_bulk_delete(inline_object)

Bulk delete executions

### Example
```R
library(openlattice_rundeck)

var.inline_object <- inline_object$new(list("ids_example")) # InlineObject | 

#Bulk delete executions
api.instance <- ExecutionApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$execution_bulk_delete(var.inline_object)
dput(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object** | [**InlineObject**](InlineObject.md)|  | 

### Return type

[**JobExecutionDelete**](JobExecutionDelete.md)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Execution deleted response |  -  |

# **execution_delete**
> execution_delete(id)

Delete an exeuction by ID

### Example
```R
library(openlattice_rundeck)

var.id <- 'id_example' # character | 

#Delete an exeuction by ID
api.instance <- ExecutionApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
api.instance$execution_delete(var.id)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **character**|  | 

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

# **execution_input_files_list**
> object execution_input_files_list(id)

List input files for an execution

### Example
```R
library(openlattice_rundeck)

var.id <- 'id_example' # character | 

#List input files for an execution
api.instance <- ExecutionApi$new()
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

# **execution_list_running**
> ExecutionList execution_list_running(project)

List job executions

### Example
```R
library(openlattice_rundeck)

var.project <- 'project_example' # character | Project name or * for all projects

#List job executions
api.instance <- ExecutionApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$execution_list_running(var.project)
dput(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **character**| Project name or * for all projects | 

### Return type

[**ExecutionList**](ExecutionList.md)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of executions for job |  -  |

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
api.instance <- ExecutionApi$new()
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

# **execution_query**
> execution_query(project, status_filter=var.status_filter, abortedby_filter=var.abortedby_filter, user_filter=var.user_filter, recent_filter=var.recent_filter, older_filter=var.older_filter, begin=var.begin, adhoc=var.adhoc)

Query for Executions based on Job or Execution details

### Example
```R
library(openlattice_rundeck)

var.project <- 'project_example' # character | 
var.status_filter <- 'status_filter_example' # character | 
var.abortedby_filter <- 'abortedby_filter_example' # character | Username who aborted an execution
var.user_filter <- 'user_filter_example' # character | Username who started the execution
var.recent_filter <- 'recent_filter_example' # character | Use a simple text format to filter executions that completed within a period of time. The format is “XY” where X is an integer, and “Y” is one of: * h: hour * d: day 
var.older_filter <- 'older_filter_example' # character | (same format as recentFilter) return executions that completed before the specified relative period of time
var.begin <- 'begin_example' # character | Specify exact date for earliest execution completion time
var.adhoc <- 'adhoc_example' # character | 

#Query for Executions based on Job or Execution details
api.instance <- ExecutionApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
api.instance$execution_query(var.project, status_filter=var.status_filter, abortedby_filter=var.abortedby_filter, user_filter=var.user_filter, recent_filter=var.recent_filter, older_filter=var.older_filter, begin=var.begin, adhoc=var.adhoc)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **character**|  | 
 **status_filter** | Enum [running, succeeded, failed, aborted, timedout, failed-with-retry, scheduled, other] |  | [optional] 
 **abortedby_filter** | **character**| Username who aborted an execution | [optional] 
 **user_filter** | **character**| Username who started the execution | [optional] 
 **recent_filter** | **character**| Use a simple text format to filter executions that completed within a period of time. The format is “XY” where X is an integer, and “Y” is one of: * h: hour * d: day  | [optional] 
 **older_filter** | **character**| (same format as recentFilter) return executions that completed before the specified relative period of time | [optional] 
 **begin** | **character**| Specify exact date for earliest execution completion time | [optional] 
 **adhoc** | **character**|  | [optional] 

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
| **200** | Success |  -  |

# **execution_state_get**
> execution_state_get(id)

Get detail about the node and step state of an execution by ID. The execution can be currently running or completed.

### Example
```R
library(openlattice_rundeck)

var.id <- 'id_example' # character | 

#Get detail about the node and step state of an execution by ID. The execution can be currently running or completed.
api.instance <- ExecutionApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
api.instance$execution_state_get(var.id)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **character**|  | 

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
| **200** | Ok |  -  |

# **execution_status_get**
> Execution execution_status_get(id)

Get the status of an execution by ID

### Example
```R
library(openlattice_rundeck)

var.id <- 'id_example' # character | 

#Get the status of an execution by ID
api.instance <- ExecutionApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$execution_status_get(var.id)
dput(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **character**|  | 

### Return type

[**Execution**](Execution.md)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Execution status |  -  |

# **job_execution_bulk_disable**
> JobBulkOperationResponse job_execution_bulk_disable(inline_object3)

Bulk disable job executions

### Example
```R
library(openlattice_rundeck)

var.inline_object3 <- inline_object_3$new(list("ids_example")) # InlineObject3 | 

#Bulk disable job executions
api.instance <- ExecutionApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$job_execution_bulk_disable(var.inline_object3)
dput(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object3** | [**InlineObject3**](InlineObject3.md)|  | 

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
| **200** | Job toggle execution response |  -  |

# **job_execution_bulk_enable**
> JobBulkOperationResponse job_execution_bulk_enable(inline_object2)

Bulk enable job executions

### Example
```R
library(openlattice_rundeck)

var.inline_object2 <- inline_object_2$new(list("ids_example")) # InlineObject2 | 

#Bulk enable job executions
api.instance <- ExecutionApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$job_execution_bulk_enable(var.inline_object2)
dput(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object2** | [**InlineObject2**](InlineObject2.md)|  | 

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

# **job_execution_delete**
> job_execution_delete(id)

Delete all job executions

### Example
```R
library(openlattice_rundeck)

var.id <- 56 # integer | Job ID

#Delete all job executions
api.instance <- ExecutionApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
api.instance$job_execution_delete(var.id)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **integer**| Job ID | 

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

# **job_execution_disable**
> object job_execution_disable(id)

Disable all executions for a job (scheduled or manual). (ACL requires toggle_execution action for a job.)

### Example
```R
library(openlattice_rundeck)

var.id <- TODO # AnyType | 

#Disable all executions for a job (scheduled or manual). (ACL requires toggle_execution action for a job.)
api.instance <- ExecutionApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$job_execution_disable(var.id)
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
| **200** | Job executions disabled |  -  |

# **job_execution_enable**
> object job_execution_enable(id)

Enable executions for a job. (ACL requires toggle_execution action for a job.)

### Example
```R
library(openlattice_rundeck)

var.id <- TODO # AnyType | 

#Enable executions for a job. (ACL requires toggle_execution action for a job.)
api.instance <- ExecutionApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$job_execution_enable(var.id)
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
| **200** | Job executions enabled |  -  |

# **job_execution_list**
> ExecutionList job_execution_list(id)

List job executions

### Example
```R
library(openlattice_rundeck)

var.id <- 'id_example' # character | Job ID

#List job executions
api.instance <- ExecutionApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$job_execution_list(var.id)
dput(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **character**| Job ID | 

### Return type

[**ExecutionList**](ExecutionList.md)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of executions for job |  -  |

# **job_execution_run**
> Execution job_execution_run(id, body=var.body)

Run the specified job

### Example
```R
library(openlattice_rundeck)

var.id <- 'id_example' # character | Job ID
var.body <- NULL # object | 

#Run the specified job
api.instance <- ExecutionApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$job_execution_run(var.id, body=var.body)
dput(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **character**| Job ID | 
 **body** | **object**|  | [optional] 

### Return type

[**Execution**](Execution.md)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Expected response for a valid request |  -  |

# **job_retry_execution**
> ExecutionList job_retry_execution(job_id, execution_id, body=var.body)

Retry a failed job execution on failed nodes only or on the same as the execution. This is the same functionality as the `Retry Failed Nodes ...` button on the execution page.

### Example
```R
library(openlattice_rundeck)

var.job_id <- 'job_id_example' # character | 
var.execution_id <- 56 # integer | 
var.body <- NULL # object | 

#Retry a failed job execution on failed nodes only or on the same as the execution. This is the same functionality as the `Retry Failed Nodes ...` button on the execution page.
api.instance <- ExecutionApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$job_retry_execution(var.job_id, var.execution_id, body=var.body)
dput(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **character**|  | 
 **execution_id** | **integer**|  | 
 **body** | **object**|  | [optional] 

### Return type

[**ExecutionList**](ExecutionList.md)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Exected response to a valid request. |  -  |

# **system_executions_disable**
> object system_executions_disable()

Disables executions, preventing adhoc and manual and scheduled jobs from running.

### Example
```R
library(openlattice_rundeck)


#Disables executions, preventing adhoc and manual and scheduled jobs from running.
api.instance <- ExecutionApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$system_executions_disable()
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

# **system_executions_enable**
> object system_executions_enable()

Enables executions, allowing adhoc and manual and scheduled jobs to be run

### Example
```R
library(openlattice_rundeck)


#Enables executions, allowing adhoc and manual and scheduled jobs to be run
api.instance <- ExecutionApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$system_executions_enable()
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

# **system_incomplete_log_storage_executions_get**
> IncompleteLogExecutions system_incomplete_log_storage_executions_get()

List all executions with incomplete log storage

### Example
```R
library(openlattice_rundeck)


#List all executions with incomplete log storage
api.instance <- ExecutionApi$new()
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
library(openlattice_rundeck)


#Resume processing incomplete Log Storage uploads
api.instance <- ExecutionApi$new()
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

