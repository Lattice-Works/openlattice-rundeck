# openlattice-rundeck.ProjectApi

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
> project_archive_export_sync(project, execution_ids=execution_ids, export_all=export_all, export_jobs=export_jobs, export_executions=export_executions, export_configs=export_configs, export_readmes=export_readmes, export_acls=export_acls)

Export archive of project synchronously

### Example

```python
from __future__ import print_function
import time
import openlattice-rundeck
from openlattice-rundeck.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openlattice-rundeck.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openlattice-rundeck.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openlattice-rundeck.ProjectApi(api_client)
    project = 'project_example' # str | Name of the project to import jobs into.
execution_ids = True # bool | A list (comma-separated) of execution IDs. If this is specified then the archive will contain only executions that are specified, and will not contain Jobs, ACLs, or project configuration/readme files. (optional)
export_all = None # object | Export all project resources (optional)
export_jobs = True # bool | Export all project resources (optional)
export_executions = True # bool | Export all project resources (optional)
export_configs = True # bool | Export all project resources (optional)
export_readmes = True # bool | Export all project resources (optional)
export_acls = True # bool | Export all project resources (optional)

    try:
        # Export archive of project synchronously
        api_instance.project_archive_export_sync(project, execution_ids=execution_ids, export_all=export_all, export_jobs=export_jobs, export_executions=export_executions, export_configs=export_configs, export_readmes=export_readmes, export_acls=export_acls)
    except ApiException as e:
        print("Exception when calling ProjectApi->project_archive_export_sync: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Name of the project to import jobs into. | 
 **execution_ids** | **bool**| A list (comma-separated) of execution IDs. If this is specified then the archive will contain only executions that are specified, and will not contain Jobs, ACLs, or project configuration/readme files. | [optional] 
 **export_all** | [**object**](.md)| Export all project resources | [optional] 
 **export_jobs** | **bool**| Export all project resources | [optional] 
 **export_executions** | **bool**| Export all project resources | [optional] 
 **export_configs** | **bool**| Export all project resources | [optional] 
 **export_readmes** | **bool**| Export all project resources | [optional] 
 **export_acls** | **bool**| Export all project resources | [optional] 

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
**200** | Zip archive |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_archive_import**
> project_archive_import(project, body, job_uuid_option=job_uuid_option, import_executions=import_executions, import_config=import_config, import_acl=import_acl)

Import project archive.

### Example

```python
from __future__ import print_function
import time
import openlattice-rundeck
from openlattice-rundeck.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openlattice-rundeck.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openlattice-rundeck.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openlattice-rundeck.ProjectApi(api_client)
    project = 'project_example' # str | Name of the project to import jobs into.
body = None # object | 
job_uuid_option = None # object |  (optional)
import_executions = True # bool |  (optional)
import_config = True # bool |  (optional)
import_acl = True # bool |  (optional)

    try:
        # Import project archive.
        api_instance.project_archive_import(project, body, job_uuid_option=job_uuid_option, import_executions=import_executions, import_config=import_config, import_acl=import_acl)
    except ApiException as e:
        print("Exception when calling ProjectApi->project_archive_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Name of the project to import jobs into. | 
 **body** | **object**|  | 
 **job_uuid_option** | [**object**](.md)|  | [optional] 
 **import_executions** | **bool**|  | [optional] 
 **import_config** | **bool**|  | [optional] 
 **import_acl** | **bool**|  | [optional] 

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
**200** | Expected response to a valid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_config_key_delete**
> project_config_key_delete(project, key)

Delete project config key

### Example

```python
from __future__ import print_function
import time
import openlattice-rundeck
from openlattice-rundeck.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openlattice-rundeck.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openlattice-rundeck.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openlattice-rundeck.ProjectApi(api_client)
    project = 'project_example' # str | 
key = 'key_example' # str | 

    try:
        # Delete project config key
        api_instance.project_config_key_delete(project, key)
    except ApiException as e:
        print("Exception when calling ProjectApi->project_config_key_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**|  | 
 **key** | **str**|  | 

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
**200** | Success ! |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_config_update**
> project_config_update(project, body)

Update project config

### Example

```python
from __future__ import print_function
import time
import openlattice-rundeck
from openlattice-rundeck.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openlattice-rundeck.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openlattice-rundeck.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openlattice-rundeck.ProjectApi(api_client)
    project = 'project_example' # str | 
body = None # object | 

    try:
        # Update project config
        api_instance.project_config_update(project, body)
    except ApiException as e:
        print("Exception when calling ProjectApi->project_config_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**|  | 
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
**200** | Project config updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_create**
> project_create(project_create_request)

Create a new project

### Example

```python
from __future__ import print_function
import time
import openlattice-rundeck
from openlattice-rundeck.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openlattice-rundeck.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openlattice-rundeck.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openlattice-rundeck.ProjectApi(api_client)
    project_create_request = None # object | 

    try:
        # Create a new project
        api_instance.project_create(project_create_request)
    except ApiException as e:
        print("Exception when calling ProjectApi->project_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_create_request** | [**object**](.md)|  | 

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
**200** | Success ! |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_delete**
> project_delete(project)

Delete project

### Example

```python
from __future__ import print_function
import time
import openlattice-rundeck
from openlattice-rundeck.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openlattice-rundeck.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openlattice-rundeck.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openlattice-rundeck.ProjectApi(api_client)
    project = 'project_example' # str | 

    try:
        # Delete project
        api_instance.project_delete(project)
    except ApiException as e:
        print("Exception when calling ProjectApi->project_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**|  | 

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
**200** | Success ! |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_jobs_export**
> project_jobs_export(project, format=format, idlist=idlist, group_path=group_path, job_filter=job_filter)

Export the job definitions in XML or YAML formats.

### Example

```python
from __future__ import print_function
import time
import openlattice-rundeck
from openlattice-rundeck.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openlattice-rundeck.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openlattice-rundeck.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openlattice-rundeck.ProjectApi(api_client)
    project = 'project_example' # str | The project to export jobs for.
format = None # object | XML or YAML format for exported jobs. (optional)
idlist = 'idlist_example' # str | A comma-separated list of Job IDs to export. (optional)
group_path = 'group_path_example' # str | Group or partial group path to include all jobs within that group path. (optional)
job_filter = 'job_filter_example' # str | Filter for the job Name. (optional)

    try:
        # Export the job definitions in XML or YAML formats.
        api_instance.project_jobs_export(project, format=format, idlist=idlist, group_path=group_path, job_filter=job_filter)
    except ApiException as e:
        print("Exception when calling ProjectApi->project_jobs_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The project to export jobs for. | 
 **format** | [**object**](.md)| XML or YAML format for exported jobs. | [optional] 
 **idlist** | **str**| A comma-separated list of Job IDs to export. | [optional] 
 **group_path** | **str**| Group or partial group path to include all jobs within that group path. | [optional] 
 **job_filter** | **str**| Filter for the job Name. | [optional] 

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
**200** | Expected response to a valid request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_jobs_import**
> project_jobs_import(project, body, content_type=content_type, accept=accept, file_format=file_format, dupe_option=dupe_option, uuid_option=uuid_option)

Import job definitions in XML or YAML formats.

### Example

```python
from __future__ import print_function
import time
import openlattice-rundeck
from openlattice-rundeck.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openlattice-rundeck.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openlattice-rundeck.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openlattice-rundeck.ProjectApi(api_client)
    project = 'project_example' # str | Name of the project to import jobs into.
body = None # object | 
content_type = None # object |  (optional)
accept = None # object |  (optional)
file_format = None # object |  (optional)
dupe_option = None # object |  (optional)
uuid_option = None # object |  (optional)

    try:
        # Import job definitions in XML or YAML formats.
        api_instance.project_jobs_import(project, body, content_type=content_type, accept=accept, file_format=file_format, dupe_option=dupe_option, uuid_option=uuid_option)
    except ApiException as e:
        print("Exception when calling ProjectApi->project_jobs_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Name of the project to import jobs into. | 
 **body** | **object**|  | 
 **content_type** | [**object**](.md)|  | [optional] 
 **accept** | [**object**](.md)|  | [optional] 
 **file_format** | [**object**](.md)|  | [optional] 
 **dupe_option** | [**object**](.md)|  | [optional] 
 **uuid_option** | [**object**](.md)|  | [optional] 

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
**200** | Expected response to a valid request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_motd_delete**
> project_motd_delete(project)

Delete project motd.md

### Example

```python
from __future__ import print_function
import time
import openlattice-rundeck
from openlattice-rundeck.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openlattice-rundeck.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openlattice-rundeck.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openlattice-rundeck.ProjectApi(api_client)
    project = 'project_example' # str | Name of the project to import jobs into.

    try:
        # Delete project motd.md
        api_instance.project_motd_delete(project)
    except ApiException as e:
        print("Exception when calling ProjectApi->project_motd_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Name of the project to import jobs into. | 

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
**200** | Success ! |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_readme_delete**
> project_readme_delete(project)

Delete project README.md

### Example

```python
from __future__ import print_function
import time
import openlattice-rundeck
from openlattice-rundeck.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openlattice-rundeck.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openlattice-rundeck.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openlattice-rundeck.ProjectApi(api_client)
    project = 'project_example' # str | Name of the project to import jobs into.

    try:
        # Delete project README.md
        api_instance.project_readme_delete(project)
    except ApiException as e:
        print("Exception when calling ProjectApi->project_readme_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Name of the project to import jobs into. | 

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
**200** | Success ! |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

