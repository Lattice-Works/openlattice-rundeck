# SystemApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_acl_policy_create**](SystemApi.md#system_acl_policy_create) | **POST** /api/26/system/acl/{policyName} | Create a policy
[**system_acl_policy_delete**](SystemApi.md#system_acl_policy_delete) | **DELETE** /api/26/system/acl/{policyName} | Delete policy
[**system_acl_policy_get**](SystemApi.md#system_acl_policy_get) | **GET** /api/26/system/acl/{policyName} | Retrieve the YAML texas of the ACL Policy file
[**system_acl_policy_list**](SystemApi.md#system_acl_policy_list) | **GET** /api/26/system/acl/ | List ACL Policies
[**system_acl_policy_update**](SystemApi.md#system_acl_policy_update) | **PUT** /api/26/system/acl/{policyName} | Update policy
[**system_executions_disable**](SystemApi.md#system_executions_disable) | **POST** /api/26/system/executions/disable | Disables executions, preventing adhoc and manual and scheduled jobs from running.
[**system_executions_enable**](SystemApi.md#system_executions_enable) | **POST** /api/26/system/executions/enable | Enables executions, allowing adhoc and manual and scheduled jobs to be run
[**system_incomplete_log_storage_executions_get**](SystemApi.md#system_incomplete_log_storage_executions_get) | **GET** /api/26/system/logstorage/incomplete | List all executions with incomplete log storage
[**system_incomplete_log_storage_executions_resume**](SystemApi.md#system_incomplete_log_storage_executions_resume) | **POST** /api/26/system/logstorage/incomplete/resume | Resume processing incomplete Log Storage uploads
[**system_info_get**](SystemApi.md#system_info_get) | **GET** /api/26/system/info | Get Rundeck server information and stats
[**system_log_storage_info_get**](SystemApi.md#system_log_storage_info_get) | **GET** /api/26/system/logstorage | Get Log Storage information and stats


# **system_acl_policy_create**
> system_acl_policy_create(policy_name, inline_object12)

Create a policy

### Example
```R
library(openlattice_rundeck)

var.policy_name <- 'policy_name_example' # character | Policy file name
var.inline_object12 <- inline_object_12$new("contents_example") # InlineObject12 | 

#Create a policy
api.instance <- SystemApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
api.instance$system_acl_policy_create(var.policy_name, var.inline_object12)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_name** | **character**| Policy file name | 
 **inline_object12** | [**InlineObject12**](InlineObject12.md)|  | 

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

# **system_acl_policy_delete**
> system_acl_policy_delete(policy_name)

Delete policy

### Example
```R
library(openlattice_rundeck)

var.policy_name <- 'policy_name_example' # character | Policy file name

#Delete policy
api.instance <- SystemApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
api.instance$system_acl_policy_delete(var.policy_name)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_name** | **character**| Policy file name | 

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

# **system_acl_policy_get**
> AclPolicyResponse system_acl_policy_get(policy_name)

Retrieve the YAML texas of the ACL Policy file

### Example
```R
library(openlattice_rundeck)

var.policy_name <- 'policy_name_example' # character | Policy file name

#Retrieve the YAML texas of the ACL Policy file
api.instance <- SystemApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$system_acl_policy_get(var.policy_name)
dput(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_name** | **character**| Policy file name | 

### Return type

[**AclPolicyResponse**](AclPolicyResponse.md)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Expected response to a valid request |  -  |

# **system_acl_policy_list**
> AclList system_acl_policy_list()

List ACL Policies

### Example
```R
library(openlattice_rundeck)


#List ACL Policies
api.instance <- SystemApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$system_acl_policy_list()
dput(result)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AclList**](AclList.md)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Expected response to a valid request |  -  |

# **system_acl_policy_update**
> AclPolicyResponse system_acl_policy_update(policy_name, inline_object11)

Update policy

### Example
```R
library(openlattice_rundeck)

var.policy_name <- 'policy_name_example' # character | Policy file name
var.inline_object11 <- inline_object_11$new("contents_example") # InlineObject11 | 

#Update policy
api.instance <- SystemApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$system_acl_policy_update(var.policy_name, var.inline_object11)
dput(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_name** | **character**| Policy file name | 
 **inline_object11** | [**InlineObject11**](InlineObject11.md)|  | 

### Return type

[**AclPolicyResponse**](AclPolicyResponse.md)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Expected response to a valid request |  -  |

# **system_executions_disable**
> object system_executions_disable()

Disables executions, preventing adhoc and manual and scheduled jobs from running.

### Example
```R
library(openlattice_rundeck)


#Disables executions, preventing adhoc and manual and scheduled jobs from running.
api.instance <- SystemApi$new()
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
api.instance <- SystemApi$new()
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
api.instance <- SystemApi$new()
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
api.instance <- SystemApi$new()
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

# **system_info_get**
> SystemInfo system_info_get()

Get Rundeck server information and stats

### Example
```R
library(openlattice_rundeck)


#Get Rundeck server information and stats
api.instance <- SystemApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$system_info_get()
dput(result)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemInfo**](SystemInfo.md)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | System info response |  -  |

# **system_log_storage_info_get**
> LogStorage system_log_storage_info_get()

Get Log Storage information and stats

### Example
```R
library(openlattice_rundeck)


#Get Log Storage information and stats
api.instance <- SystemApi$new()
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

