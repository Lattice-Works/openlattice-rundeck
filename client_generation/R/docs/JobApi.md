# JobApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**project_archive_import**](JobApi.md#project_archive_import) | **PUT** /api/26/project/{project}/import | Import project archive.
[**project_jobs_export**](JobApi.md#project_jobs_export) | **GET** /api/26/project/{project}/jobs/export | Export the job definitions in XML or YAML formats.
[**project_jobs_import**](JobApi.md#project_jobs_import) | **POST** /api/26/project/{project}/jobs/import | Import job definitions in XML or YAML formats.


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

