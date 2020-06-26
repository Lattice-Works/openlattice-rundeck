# ProjectApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execution_list_running**](ProjectApi.md#execution_list_running) | **GET** /api/26/project/{project}/executions/running | List job executions
[**job_list**](ProjectApi.md#job_list) | **GET** /api/26/project/{project}/jobs | List the jobs that exist for a project
[**project_archive_export_sync**](ProjectApi.md#project_archive_export_sync) | **GET** /api/26/project/{project}/export | Export archive of project synchronously
[**project_archive_import**](ProjectApi.md#project_archive_import) | **PUT** /api/26/project/{project}/import | Import project archive.
[**project_config_get**](ProjectApi.md#project_config_get) | **GET** /api/26/project/{project}/config | Get project config
[**project_config_key_delete**](ProjectApi.md#project_config_key_delete) | **DELETE** /api/26/project/{project}/config/{key} | Delete project config key
[**project_config_key_get**](ProjectApi.md#project_config_key_get) | **GET** /api/26/project/{project}/config/{key} | Get project config key
[**project_config_key_set**](ProjectApi.md#project_config_key_set) | **PUT** /api/26/project/{project}/config/{key} | Get project config key
[**project_config_update**](ProjectApi.md#project_config_update) | **PUT** /api/26/project/{project}/config | Update project config
[**project_create**](ProjectApi.md#project_create) | **POST** /api/26/projects | Create a new project
[**project_delete**](ProjectApi.md#project_delete) | **DELETE** /api/26/project/{project} | Delete project
[**project_get**](ProjectApi.md#project_get) | **GET** /api/26/project/{project} | Get information about a project
[**project_jobs_export**](ProjectApi.md#project_jobs_export) | **GET** /api/26/project/{project}/jobs/export | Export the job definitions in XML or YAML formats.
[**project_jobs_import**](ProjectApi.md#project_jobs_import) | **POST** /api/26/project/{project}/jobs/import | Import job definitions in XML or YAML formats.
[**project_list**](ProjectApi.md#project_list) | **GET** /api/26/projects | List projects
[**project_motd_delete**](ProjectApi.md#project_motd_delete) | **DELETE** /api/26/project/{project}/motd.md | Delete project motd.md
[**project_motd_get**](ProjectApi.md#project_motd_get) | **GET** /api/26/project/{project}/motd.md | Get the readme.md contents
[**project_motd_put**](ProjectApi.md#project_motd_put) | **PUT** /api/26/project/{project}/motd.md | Create or modify project MOTD.md
[**project_readme_delete**](ProjectApi.md#project_readme_delete) | **DELETE** /api/26/project/{project}/readme.md | Delete project README.md
[**project_readme_get**](ProjectApi.md#project_readme_get) | **GET** /api/26/project/{project}/readme.md | Get the readme.md contents
[**project_readme_put**](ProjectApi.md#project_readme_put) | **PUT** /api/26/project/{project}/readme.md | Create or modify project README.md


# **execution_list_running**
> ExecutionList execution_list_running(project)

List job executions

### Example
```R
library(openlattice_rundeck)

var.project <- 'project_example' # character | Project name or * for all projects

#List job executions
api.instance <- ProjectApi$new()
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
api.instance <- ProjectApi$new()
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

# **project_archive_export_sync**
> object project_archive_export_sync(project, execution_ids=var.execution_ids, export_all=var.export_all, export_jobs=var.export_jobs, export_executions=var.export_executions, export_configs=var.export_configs, export_readmes=var.export_readmes, export_acls=var.export_acls)

Export archive of project synchronously

### Example
```R
library(openlattice_rundeck)

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
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$project_archive_export_sync(var.project, execution_ids=var.execution_ids, export_all=var.export_all, export_jobs=var.export_jobs, export_executions=var.export_executions, export_configs=var.export_configs, export_readmes=var.export_readmes, export_acls=var.export_acls)
dput(result)
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

**object**

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Zip archive |  -  |

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
api.instance <- ProjectApi$new()
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

# **project_config_get**
> object project_config_get(project)

Get project config

### Example
```R
library(openlattice_rundeck)

var.project <- 'project_example' # character | 

#Get project config
api.instance <- ProjectApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$project_config_get(var.project)
dput(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **character**|  | 

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
| **200** | Project info |  -  |

# **project_config_key_delete**
> project_config_key_delete(project, key)

Delete project config key

### Example
```R
library(openlattice_rundeck)

var.project <- 'project_example' # character | 
var.key <- 'key_example' # character | 

#Delete project config key
api.instance <- ProjectApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
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

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success ! |  -  |

# **project_config_key_get**
> object project_config_key_get(project, key)

Get project config key

### Example
```R
library(openlattice_rundeck)

var.project <- 'project_example' # character | 
var.key <- 'key_example' # character | 

#Get project config key
api.instance <- ProjectApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$project_config_key_get(var.project, var.key)
dput(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **character**|  | 
 **key** | **character**|  | 

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
| **200** | Project config key and value |  -  |

# **project_config_key_set**
> object project_config_key_set(project, key, inline_object7)

Get project config key

### Example
```R
library(openlattice_rundeck)

var.project <- 'project_example' # character | 
var.key <- 'key_example' # character | 
var.inline_object7 <- inline_object_7$new("value_example") # InlineObject7 | 

#Get project config key
api.instance <- ProjectApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$project_config_key_set(var.project, var.key, var.inline_object7)
dput(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **character**|  | 
 **key** | **character**|  | 
 **inline_object7** | [**InlineObject7**](InlineObject7.md)|  | 

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
| **200** | Project config key set |  -  |

# **project_config_update**
> project_config_update(project, body)

Update project config

### Example
```R
library(openlattice_rundeck)

var.project <- 'project_example' # character | 
var.body <- NULL # object | 

#Update project config
api.instance <- ProjectApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
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

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Project config updated |  -  |

# **project_create**
> project_create(inline_object6)

Create a new project

### Example
```R
library(openlattice_rundeck)

var.inline_object6 <- inline_object_6$new("name_example", 123) # InlineObject6 | 

#Create a new project
api.instance <- ProjectApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
api.instance$project_create(var.inline_object6)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object6** | [**InlineObject6**](InlineObject6.md)|  | 

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
| **200** | Success ! |  -  |

# **project_delete**
> project_delete(project)

Delete project

### Example
```R
library(openlattice_rundeck)

var.project <- 'project_example' # character | 

#Delete project
api.instance <- ProjectApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
api.instance$project_delete(var.project)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **character**|  | 

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

# **project_get**
> Project project_get(project)

Get information about a project

### Example
```R
library(openlattice_rundeck)

var.project <- 'project_example' # character | 

#Get information about a project
api.instance <- ProjectApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$project_get(var.project)
dput(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **character**|  | 

### Return type

[**Project**](Project.md)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Project info |  -  |

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
api.instance <- ProjectApi$new()
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
api.instance <- ProjectApi$new()
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

# **project_list**
> array[InlineResponse200] project_list()

List projects

### Example
```R
library(openlattice_rundeck)


#List projects
api.instance <- ProjectApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$project_list()
dput(result)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**array[InlineResponse200]**](inline_response_200.md)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of projects |  -  |

# **project_motd_delete**
> project_motd_delete(project)

Delete project motd.md

### Example
```R
library(openlattice_rundeck)

var.project <- 'project_example' # character | Name of the project to import jobs into.

#Delete project motd.md
api.instance <- ProjectApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
api.instance$project_motd_delete(var.project)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **character**| Name of the project to import jobs into. | 

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

# **project_motd_get**
> object project_motd_get(project)

Get the readme.md contents

### Example
```R
library(openlattice_rundeck)

var.project <- 'project_example' # character | Name of the project to import jobs into.

#Get the readme.md contents
api.instance <- ProjectApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$project_motd_get(var.project)
dput(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **character**| Name of the project to import jobs into. | 

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
| **200** | motd.md contents |  -  |

# **project_motd_put**
> project_motd_put(project, inline_object9)

Create or modify project MOTD.md

### Example
```R
library(openlattice_rundeck)

var.project <- 'project_example' # character | Name of the project to import jobs into.
var.inline_object9 <- inline_object_9$new("contents_example") # InlineObject9 | 

#Create or modify project MOTD.md
api.instance <- ProjectApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
api.instance$project_motd_put(var.project, var.inline_object9)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **character**| Name of the project to import jobs into. | 
 **inline_object9** | [**InlineObject9**](InlineObject9.md)|  | 

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
| **200** | Expected response to a valid request. |  -  |

# **project_readme_delete**
> project_readme_delete(project)

Delete project README.md

### Example
```R
library(openlattice_rundeck)

var.project <- 'project_example' # character | Name of the project to import jobs into.

#Delete project README.md
api.instance <- ProjectApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
api.instance$project_readme_delete(var.project)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **character**| Name of the project to import jobs into. | 

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

# **project_readme_get**
> object project_readme_get(project)

Get the readme.md contents

### Example
```R
library(openlattice_rundeck)

var.project <- 'project_example' # character | Name of the project to import jobs into.

#Get the readme.md contents
api.instance <- ProjectApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$project_readme_get(var.project)
dput(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **character**| Name of the project to import jobs into. | 

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
| **200** | readme.md contents |  -  |

# **project_readme_put**
> project_readme_put(project, inline_object8)

Create or modify project README.md

### Example
```R
library(openlattice_rundeck)

var.project <- 'project_example' # character | Name of the project to import jobs into.
var.inline_object8 <- inline_object_8$new("contents_example") # InlineObject8 | 

#Create or modify project README.md
api.instance <- ProjectApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
api.instance$project_readme_put(var.project, var.inline_object8)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **character**| Name of the project to import jobs into. | 
 **inline_object8** | [**InlineObject8**](InlineObject8.md)|  | 

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

