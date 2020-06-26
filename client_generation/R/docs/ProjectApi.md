# ProjectApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api26_project_project_motd_md_delete**](ProjectApi.md#api26_project_project_motd_md_delete) | **DELETE** /api/26/project/{project}/motd.md | Delete project motd.md


# **api26_project_project_motd_md_delete**
> api26_project_project_motd_md_delete(project)

Delete project motd.md

### Example
```R
library(openlattice-rundeck)

var.project <- 'project_example' # character | Name of the project to import jobs into.

#Delete project motd.md
api.instance <- ProjectApi$new()
api.instance$api26_project_project_motd_md_delete(var.project)
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

