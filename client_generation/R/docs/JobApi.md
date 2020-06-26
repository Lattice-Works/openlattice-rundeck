# JobApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**job_bulk_delete**](JobApi.md#job_bulk_delete) | **POST** /api/26/jobs/delete | Delete multiple job definitions at once
[**job_delete**](JobApi.md#job_delete) | **DELETE** /api/26/job/{id} | Delete a single job definition.
[**job_execution_bulk_disable**](JobApi.md#job_execution_bulk_disable) | **POST** /api/26/jobs/execution/disable | Bulk disable job executions
[**job_execution_bulk_enable**](JobApi.md#job_execution_bulk_enable) | **POST** /api/26/jobs/execution/enable | Bulk enable job executions
[**job_execution_delete**](JobApi.md#job_execution_delete) | **DELETE** /api/26/job/{id}/executions | Delete all job executions
[**job_execution_disable**](JobApi.md#job_execution_disable) | **POST** /api/26/job/{id}/execution/disable | Disable all executions for a job (scheduled or manual). (ACL requires toggle_execution action for a job.)
[**job_execution_enable**](JobApi.md#job_execution_enable) | **POST** /api/26/job/{id}/execution/enable | Enable executions for a job. (ACL requires toggle_execution action for a job.)
[**job_execution_list**](JobApi.md#job_execution_list) | **GET** /api/26/job/{id}/executions | List job executions
[**job_execution_run**](JobApi.md#job_execution_run) | **POST** /api/26/job/{id}/executions | Run the specified job
[**job_get**](JobApi.md#job_get) | **GET** /api/26/job/{id} | Export a single job definition in XML or YAML formats.
[**job_info_get**](JobApi.md#job_info_get) | **GET** /api/26/job/{id}/info | Get metadata about a specific job.
[**job_input_file_info_get**](JobApi.md#job_input_file_info_get) | **GET** /api/26/jobs/file/{id} | Get job input file info
[**job_input_file_upload**](JobApi.md#job_input_file_upload) | **POST** /api/26/job/{id}/input/file | Upload file as job option
[**job_input_files_upload**](JobApi.md#job_input_files_upload) | **GET** /api/26/job/{id}/input/files | List uploaded input files for job
[**job_list**](JobApi.md#job_list) | **GET** /api/26/project/{project}/jobs | List the jobs that exist for a project
[**job_retry_execution**](JobApi.md#job_retry_execution) | **POST** /api/26/job/{jobID}/retry/{executionID} | Retry a failed job execution on failed nodes only or on the same as the execution. This is the same functionality as the &#x60;Retry Failed Nodes ...&#x60; button on the execution page.
[**job_schedule_bulk_disable**](JobApi.md#job_schedule_bulk_disable) | **POST** /api/26/jobs/schedule/disable | Bulk disable job schedule
[**job_schedule_bulk_enable**](JobApi.md#job_schedule_bulk_enable) | **POST** /api/26/jobs/schedule/enable | Bulk enable job schedule
[**job_schedule_disable**](JobApi.md#job_schedule_disable) | **POST** /api/26/job/{id}/schedule/disable | Disable the schedule for a job. (ACL requires toggle_schedule action for a job.)
[**job_schedule_enable**](JobApi.md#job_schedule_enable) | **POST** /api/26/job/{id}/schedule/enable | Enable the schedule for a job. (ACL requires toggle_schedule action for a job.)
[**job_workflow_get**](JobApi.md#job_workflow_get) | **GET** /api/34/job/{id}/workflow | Get job workflow tree.
[**project_archive_import**](JobApi.md#project_archive_import) | **PUT** /api/26/project/{project}/import | Import project archive.
[**project_jobs_export**](JobApi.md#project_jobs_export) | **GET** /api/26/project/{project}/jobs/export | Export the job definitions in XML or YAML formats.
[**project_jobs_import**](JobApi.md#project_jobs_import) | **POST** /api/26/project/{project}/jobs/import | Import job definitions in XML or YAML formats.
[**system_scheduled_jobs_for_server**](JobApi.md#system_scheduled_jobs_for_server) | **GET** /api/26/scheduler/server/{uuid}/jobs | List the scheduled Jobs with their schedule owned by the cluster server with the specified UUID
[**system_scheduled_jobs_list**](JobApi.md#system_scheduled_jobs_list) | **GET** /api/26/scheduler/jobs | List the scheduled Jobs with their schedule owned by the cluster server
[**system_scheduler_takeover**](JobApi.md#system_scheduler_takeover) | **PUT** /api/26/scheduler/takeover | Tell a Rundeck server in cluster mode to claim all scheduled jobs from another cluster server


# **job_bulk_delete**
> JobBulkOperationResponse job_bulk_delete(inline_object1)

Delete multiple job definitions at once

### Example
```R
library(openlattice_rundeck)

var.inline_object1 <- inline_object_1$new(list("ids_example")) # InlineObject1 | 

#Delete multiple job definitions at once
api.instance <- JobApi$new()
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

# **job_delete**
> job_delete(id)

Delete a single job definition.

### Example
```R
library(openlattice_rundeck)

var.id <- 'id_example' # character | ID of job to delete.

#Delete a single job definition.
api.instance <- JobApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
api.instance$job_delete(var.id)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **character**| ID of job to delete. | 

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

# **job_execution_bulk_disable**
> JobBulkOperationResponse job_execution_bulk_disable(inline_object3)

Bulk disable job executions

### Example
```R
library(openlattice_rundeck)

var.inline_object3 <- inline_object_3$new(list("ids_example")) # InlineObject3 | 

#Bulk disable job executions
api.instance <- JobApi$new()
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
api.instance <- JobApi$new()
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
api.instance <- JobApi$new()
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
api.instance <- JobApi$new()
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
api.instance <- JobApi$new()
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
api.instance <- JobApi$new()
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
api.instance <- JobApi$new()
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

# **job_get**
> object job_get(id, format=var.format)

Export a single job definition in XML or YAML formats.

### Example
```R
library(openlattice_rundeck)

var.id <- 'id_example' # character | ID of the job to export.
var.format <- TODO # AnyType | 

#Export a single job definition in XML or YAML formats.
api.instance <- JobApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$job_get(var.id, format=var.format)
dput(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **character**| ID of the job to export. | 
 **format** | [**AnyType**](.md)|  | [optional] 

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
| **200** | Expected response to a valid request. |  -  |

# **job_info_get**
> JobMetadata job_info_get(id)

Get metadata about a specific job.

### Example
```R
library(openlattice_rundeck)

var.id <- 'id_example' # character | 

#Get metadata about a specific job.
api.instance <- JobApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$job_info_get(var.id)
dput(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **character**|  | 

### Return type

[**JobMetadata**](JobMetadata.md)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Expected response to a valid request. |  -  |

# **job_input_file_info_get**
> JobInputFileInfo job_input_file_info_get(id)

Get job input file info

### Example
```R
library(openlattice_rundeck)

var.id <- 'id_example' # character | 

#Get job input file info
api.instance <- JobApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$job_input_file_info_get(var.id)
dput(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **character**|  | 

### Return type

[**JobInputFileInfo**](JobInputFileInfo.md)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Job input file info |  -  |

# **job_input_file_upload**
> job_input_file_upload(id, option_name, file_name, body)

Upload file as job option

### Example
```R
library(openlattice_rundeck)

var.id <- 'id_example' # character | 
var.option_name <- 'option_name_example' # character | 
var.file_name <- 'file_name_example' # character | 
var.body <- NULL # object | 

#Upload file as job option
api.instance <- JobApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
api.instance$job_input_file_upload(var.id, var.option_name, var.file_name, var.body)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **character**|  | 
 **option_name** | **character**|  | 
 **file_name** | **character**|  | 
 **body** | **object**|  | 

### Return type

void (empty response body)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Yay |  -  |

# **job_input_files_upload**
> JobInputFileListResponse job_input_files_upload(id)

List uploaded input files for job

### Example
```R
library(openlattice_rundeck)

var.id <- 'id_example' # character | 

#List uploaded input files for job
api.instance <- JobApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$job_input_files_upload(var.id)
dput(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **character**|  | 

### Return type

[**JobInputFileListResponse**](JobInputFileListResponse.md)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of input files |  -  |

# **job_list**
> array[Job] job_list(project, id_list=var.id_list, group_path=var.group_path, job_filter=var.job_filter, job_exact_filter=var.job_exact_filter, group_path_exact=var.group_path_exact, scheduled_filter=var.scheduled_filter, server_node_uuid_filter=var.server_node_uuid_filter)

List the jobs that exist for a project

### Example
```R
library(openlattice_rundeck)

var.project <- 'project_example' # character | Project name
var.id_list <- 'id_list_example' # character | Comma separated list of Job IDs to include
var.group_path <- 'group_path_example' # character | Group or partial group path to include all jobs within that group path. Set to the special value \"-\" to match the top level jobs only.
var.job_filter <- 'job_filter_example' # character | A filter for the job name. Matches any job name that contains this value.
var.job_exact_filter <- 'job_exact_filter_example' # character | An exact job name to match.
var.group_path_exact <- 'group_path_exact_example' # character | An exact group path to match. Set to the special value \"-\" to match the top level jobs only.
var.scheduled_filter <- 'scheduled_filter_example' # character | Specify whether to return only scheduled or only not scheduled jobs.
var.server_node_uuid_filter <- 'server_node_uuid_filter_example' # character | In cluster mode, use to select scheduled jobs assigned to the server with the given UUID.

#List the jobs that exist for a project
api.instance <- JobApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$job_list(var.project, id_list=var.id_list, group_path=var.group_path, job_filter=var.job_filter, job_exact_filter=var.job_exact_filter, group_path_exact=var.group_path_exact, scheduled_filter=var.scheduled_filter, server_node_uuid_filter=var.server_node_uuid_filter)
dput(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **character**| Project name | 
 **id_list** | **character**| Comma separated list of Job IDs to include | [optional] 
 **group_path** | **character**| Group or partial group path to include all jobs within that group path. Set to the special value \&quot;-\&quot; to match the top level jobs only. | [optional] 
 **job_filter** | **character**| A filter for the job name. Matches any job name that contains this value. | [optional] 
 **job_exact_filter** | **character**| An exact job name to match. | [optional] 
 **group_path_exact** | **character**| An exact group path to match. Set to the special value \&quot;-\&quot; to match the top level jobs only. | [optional] 
 **scheduled_filter** | **character**| Specify whether to return only scheduled or only not scheduled jobs. | [optional] 
 **server_node_uuid_filter** | **character**| In cluster mode, use to select scheduled jobs assigned to the server with the given UUID. | [optional] 

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
api.instance <- JobApi$new()
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

# **job_schedule_bulk_disable**
> JobBulkOperationResponse job_schedule_bulk_disable(inline_object5)

Bulk disable job schedule

### Example
```R
library(openlattice_rundeck)

var.inline_object5 <- inline_object_5$new(list("ids_example")) # InlineObject5 | 

#Bulk disable job schedule
api.instance <- JobApi$new()
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
api.instance <- JobApi$new()
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
api.instance <- JobApi$new()
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
api.instance <- JobApi$new()
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

# **job_workflow_get**
> object job_workflow_get(id)

Get job workflow tree.

### Example
```R
library(openlattice_rundeck)

var.id <- 'id_example' # character | 

#Get job workflow tree.
api.instance <- JobApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$job_workflow_get(var.id)
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
| **200** | Expected response to a valid request. |  -  |

# **project_archive_import**
> project_archive_import(project, body, job_uuid_option=var.job_uuid_option, import_executions=var.import_executions, import_config=var.import_config, import_acl=var.import_acl)

Import project archive.

### Example
```R
library(openlattice_rundeck)

var.project <- 'project_example' # character | Name of the project to import jobs into.
var.body <- NULL # object | 
var.job_uuid_option <- TODO # AnyType | 
var.import_executions <- 'import_executions_example' # character | 
var.import_config <- 'import_config_example' # character | 
var.import_acl <- 'import_acl_example' # character | 

#Import project archive.
api.instance <- JobApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
api.instance$project_archive_import(var.project, var.body, job_uuid_option=var.job_uuid_option, import_executions=var.import_executions, import_config=var.import_config, import_acl=var.import_acl)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **character**| Name of the project to import jobs into. | 
 **body** | **object**|  | 
 **job_uuid_option** | [**AnyType**](.md)|  | [optional] 
 **import_executions** | **character**|  | [optional] 
 **import_config** | **character**|  | [optional] 
 **import_acl** | **character**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Expected response to a valid request |  -  |

# **project_jobs_export**
> character project_jobs_export(project, format=var.format, idlist=var.idlist, group_path=var.group_path, job_filter=var.job_filter)

Export the job definitions in XML or YAML formats.

### Example
```R
library(openlattice_rundeck)

var.project <- 'project_example' # character | The project to export jobs for.
var.format <- TODO # AnyType | XML or YAML format for exported jobs.
var.idlist <- 'idlist_example' # character | A comma-separated list of Job IDs to export.
var.group_path <- 'group_path_example' # character | Group or partial group path to include all jobs within that group path.
var.job_filter <- 'job_filter_example' # character | Filter for the job Name.

#Export the job definitions in XML or YAML formats.
api.instance <- JobApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$project_jobs_export(var.project, format=var.format, idlist=var.idlist, group_path=var.group_path, job_filter=var.job_filter)
dput(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **character**| The project to export jobs for. | 
 **format** | [**AnyType**](.md)| XML or YAML format for exported jobs. | [optional] 
 **idlist** | **character**| A comma-separated list of Job IDs to export. | [optional] 
 **group_path** | **character**| Group or partial group path to include all jobs within that group path. | [optional] 
 **job_filter** | **character**| Filter for the job Name. | [optional] 

### Return type

**character**

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Expected response to a valid request. |  -  |

# **project_jobs_import**
> object project_jobs_import(project, body, content_type=var.content_type, accept=var.accept, file_format=var.file_format, dupe_option=var.dupe_option, uuid_option=var.uuid_option)

Import job definitions in XML or YAML formats.

### Example
```R
library(openlattice_rundeck)

var.project <- 'project_example' # character | Name of the project to import jobs into.
var.body <- NULL # object | 
var.content_type <- TODO # AnyType | 
var.accept <- TODO # AnyType | 
var.file_format <- TODO # AnyType | 
var.dupe_option <- TODO # AnyType | 
var.uuid_option <- TODO # AnyType | 

#Import job definitions in XML or YAML formats.
api.instance <- JobApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$project_jobs_import(var.project, var.body, content_type=var.content_type, accept=var.accept, file_format=var.file_format, dupe_option=var.dupe_option, uuid_option=var.uuid_option)
dput(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **character**| Name of the project to import jobs into. | 
 **body** | **object**|  | 
 **content_type** | [**AnyType**](.md)|  | [optional] 
 **accept** | [**AnyType**](.md)|  | [optional] 
 **file_format** | [**AnyType**](.md)|  | [optional] 
 **dupe_option** | [**AnyType**](.md)|  | [optional] 
 **uuid_option** | [**AnyType**](.md)|  | [optional] 

### Return type

**object**

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Expected response to a valid request. |  -  |

# **system_scheduled_jobs_for_server**
> array[Job] system_scheduled_jobs_for_server(uuid)

List the scheduled Jobs with their schedule owned by the cluster server with the specified UUID

### Example
```R
library(openlattice_rundeck)

var.uuid <- 'uuid_example' # character | The ID of the user to retrieve profile information for

#List the scheduled Jobs with their schedule owned by the cluster server with the specified UUID
api.instance <- JobApi$new()
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
library(openlattice_rundeck)


#List the scheduled Jobs with their schedule owned by the cluster server
api.instance <- JobApi$new()
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
library(openlattice_rundeck)

var.inline_object10 <- inline_object_10$new(_api_26_scheduler_takeover_server$new("uuid_example", "all_example"), "project_example", _api_26_scheduler_takeover_job$new("id_example")) # InlineObject10 | 

#Tell a Rundeck server in cluster mode to claim all scheduled jobs from another cluster server
api.instance <- JobApi$new()
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

