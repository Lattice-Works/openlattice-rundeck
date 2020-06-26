# ProjectApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**project_archive_export_sync**](ProjectApi.md#project_archive_export_sync) | **GET** /api/26/project/{project}/export | Export archive of project synchronously
[**project_archive_import**](ProjectApi.md#project_archive_import) | **PUT** /api/26/project/{project}/import | Import project archive.
[**project_config_key_delete**](ProjectApi.md#project_config_key_delete) | **DELETE** /api/26/project/{project}/config/{key} | Delete project config key
[**project_config_update**](ProjectApi.md#project_config_update) | **PUT** /api/26/project/{project}/config | Update project config
[**project_create**](ProjectApi.md#project_create) | **POST** /api/26/projects | Create a new project
[**project_delete**](ProjectApi.md#project_delete) | **DELETE** /api/26/project/{project} | Delete project
[**project_jobs_export**](ProjectApi.md#project_jobs_export) | **GET** /api/26/project/{project}/jobs/export | Export the job definitions in XML or YAML formats.
[**project_jobs_import**](ProjectApi.md#project_jobs_import) | **POST** /api/26/project/{project}/jobs/import | Import job definitions in XML or YAML formats.
[**project_motd_delete**](ProjectApi.md#project_motd_delete) | **DELETE** /api/26/project/{project}/motd.md | Delete project motd.md
[**project_readme_delete**](ProjectApi.md#project_readme_delete) | **DELETE** /api/26/project/{project}/readme.md | Delete project README.md


# **project_archive_export_sync**
> project_archive_export_sync(project, execution_ids=var.execution_ids, export_all=var.export_all, export_jobs=var.export_jobs, export_executions=var.export_executions, export_configs=var.export_configs, export_readmes=var.export_readmes, export_acls=var.export_acls)

Export archive of project synchronously

### Example
```R
library(openlattice-rundeck)

var.project <- 'project_example' # character | Name of the project to import jobs into.
var.execution_ids <- 'execution_ids_example' # character | A list (comma-separated) of execution IDs. If this is specified then the archive will contain only executions that are specified, and will not contain Jobs, ACLs, or project configuration/readme files.
var.export_all <- TODO # AnyType | Export all project resources
var.export_jobs <- 'export_jobs_example' # character | Export all project resources
var.export_executions <- 'export_executions_example' # character | Export all project resources
var.export_configs <- 'export_configs_example' # character | Export all project resources
var.export_readmes <- 'export_readmes_example' # character | Export all project resources
var.export_acls <- 'export_acls_example' # character | Export all project resources

#Export archive of project synchronously
api.instance <- ProjectApi$new()
api.instance$project_archive_export_sync(var.project, execution_ids=var.execution_ids, export_all=var.export_all, export_jobs=var.export_jobs, export_executions=var.export_executions, export_configs=var.export_configs, export_readmes=var.export_readmes, export_acls=var.export_acls)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **character**| Name of the project to import jobs into. | 
 **execution_ids** | **character**| A list (comma-separated) of execution IDs. If this is specified then the archive will contain only executions that are specified, and will not contain Jobs, ACLs, or project configuration/readme files. | [optional] 
 **export_all** | [**AnyType**](.md)| Export all project resources | [optional] 
 **export_jobs** | **character**| Export all project resources | [optional] 
 **export_executions** | **character**| Export all project resources | [optional] 
 **export_configs** | **character**| Export all project resources | [optional] 
 **export_readmes** | **character**| Export all project resources | [optional] 
 **export_acls** | **character**| Export all project resources | [optional] 

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
| **200** | Zip archive |  -  |

# **project_archive_import**
> project_archive_import(project, body, job_uuid_option=var.job_uuid_option, import_executions=var.import_executions, import_config=var.import_config, import_acl=var.import_acl)

Import project archive.

### Example
```R
library(openlattice-rundeck)

var.project <- 'project_example' # character | Name of the project to import jobs into.
var.body <- NULL # object | 
var.job_uuid_option <- TODO # AnyType | 
var.import_executions <- 'import_executions_example' # character | 
var.import_config <- 'import_config_example' # character | 
var.import_acl <- 'import_acl_example' # character | 

#Import project archive.
api.instance <- ProjectApi$new()
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Expected response to a valid request |  -  |

# **project_config_key_delete**
> project_config_key_delete(project, key)

Delete project config key

### Example
```R
library(openlattice-rundeck)

var.project <- 'project_example' # character | 
var.key <- 'key_example' # character | 

#Delete project config key
api.instance <- ProjectApi$new()
api.instance$project_config_key_delete(var.project, var.key)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **character**|  | 
 **key** | **character**|  | 

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
| **200** | Success ! |  -  |

# **project_config_update**
> project_config_update(project, body)

Update project config

### Example
```R
library(openlattice-rundeck)

var.project <- 'project_example' # character | 
var.body <- NULL # object | 

#Update project config
api.instance <- ProjectApi$new()
api.instance$project_config_update(var.project, var.body)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **character**|  | 
 **body** | **object**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Project config updated |  -  |

# **project_create**
> project_create(project_create_request)

Create a new project

### Example
```R
library(openlattice-rundeck)

var.project_create_request <- TODO # AnyType | 

#Create a new project
api.instance <- ProjectApi$new()
api.instance$project_create(var.project_create_request)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_create_request** | [**AnyType**](.md)|  | 

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
| **200** | Success ! |  -  |

# **project_delete**
> project_delete(project)

Delete project

### Example
```R
library(openlattice-rundeck)

var.project <- 'project_example' # character | 

#Delete project
api.instance <- ProjectApi$new()
api.instance$project_delete(var.project)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **character**|  | 

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
| **200** | Success ! |  -  |

# **project_jobs_export**
> project_jobs_export(project, format=var.format, idlist=var.idlist, group_path=var.group_path, job_filter=var.job_filter)

Export the job definitions in XML or YAML formats.

### Example
```R
library(openlattice-rundeck)

var.project <- 'project_example' # character | The project to export jobs for.
var.format <- TODO # AnyType | XML or YAML format for exported jobs.
var.idlist <- 'idlist_example' # character | A comma-separated list of Job IDs to export.
var.group_path <- 'group_path_example' # character | Group or partial group path to include all jobs within that group path.
var.job_filter <- 'job_filter_example' # character | Filter for the job Name.

#Export the job definitions in XML or YAML formats.
api.instance <- ProjectApi$new()
api.instance$project_jobs_export(var.project, format=var.format, idlist=var.idlist, group_path=var.group_path, job_filter=var.job_filter)
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

# **project_jobs_import**
> project_jobs_import(project, body, content_type=var.content_type, accept=var.accept, file_format=var.file_format, dupe_option=var.dupe_option, uuid_option=var.uuid_option)

Import job definitions in XML or YAML formats.

### Example
```R
library(openlattice-rundeck)

var.project <- 'project_example' # character | Name of the project to import jobs into.
var.body <- NULL # object | 
var.content_type <- TODO # AnyType | 
var.accept <- TODO # AnyType | 
var.file_format <- TODO # AnyType | 
var.dupe_option <- TODO # AnyType | 
var.uuid_option <- TODO # AnyType | 

#Import job definitions in XML or YAML formats.
api.instance <- ProjectApi$new()
api.instance$project_jobs_import(var.project, var.body, content_type=var.content_type, accept=var.accept, file_format=var.file_format, dupe_option=var.dupe_option, uuid_option=var.uuid_option)
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

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Expected response to a valid request. |  -  |

# **project_motd_delete**
> project_motd_delete(project)

Delete project motd.md

### Example
```R
library(openlattice-rundeck)

var.project <- 'project_example' # character | Name of the project to import jobs into.

#Delete project motd.md
api.instance <- ProjectApi$new()
api.instance$project_motd_delete(var.project)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **character**| Name of the project to import jobs into. | 

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
| **200** | Success ! |  -  |

# **project_readme_delete**
> project_readme_delete(project)

Delete project README.md

### Example
```R
library(openlattice-rundeck)

var.project <- 'project_example' # character | Name of the project to import jobs into.

#Delete project README.md
api.instance <- ProjectApi$new()
api.instance$project_readme_delete(var.project)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **character**| Name of the project to import jobs into. | 

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
| **200** | Success ! |  -  |

