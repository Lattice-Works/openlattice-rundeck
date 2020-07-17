# AclApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_acl_policy_create**](AclApi.md#system_acl_policy_create) | **POST** /api/26/system/acl/{policyName} | Create a policy
[**system_acl_policy_delete**](AclApi.md#system_acl_policy_delete) | **DELETE** /api/26/system/acl/{policyName} | Delete policy
[**system_acl_policy_get**](AclApi.md#system_acl_policy_get) | **GET** /api/26/system/acl/{policyName} | Retrieve the YAML texas of the ACL Policy file
[**system_acl_policy_list**](AclApi.md#system_acl_policy_list) | **GET** /api/26/system/acl/ | List ACL Policies
[**system_acl_policy_update**](AclApi.md#system_acl_policy_update) | **PUT** /api/26/system/acl/{policyName} | Update policy


# **system_acl_policy_create**
> system_acl_policy_create(policy_name, inline_object12)

Create a policy

### Example
```R
library(olrundeck)

var.policy_name <- 'policy_name_example' # character | Policy file name
var.inline_object12 <- inline_object_12$new("contents_example") # InlineObject12 | 

#Create a policy
api.instance <- AclApi$new()
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
library(olrundeck)

var.policy_name <- 'policy_name_example' # character | Policy file name

#Delete policy
api.instance <- AclApi$new()
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
library(olrundeck)

var.policy_name <- 'policy_name_example' # character | Policy file name

#Retrieve the YAML texas of the ACL Policy file
api.instance <- AclApi$new()
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
library(olrundeck)


#List ACL Policies
api.instance <- AclApi$new()
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
library(olrundeck)

var.policy_name <- 'policy_name_example' # character | Policy file name
var.inline_object11 <- inline_object_11$new("contents_example") # InlineObject11 | 

#Update policy
api.instance <- AclApi$new()
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

