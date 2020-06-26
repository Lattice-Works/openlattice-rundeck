# SystemApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api26_system_acl_policy_name_delete**](SystemApi.md#api26_system_acl_policy_name_delete) | **DELETE** /api/26/system/acl/{policyName} | Delete policy


# **api26_system_acl_policy_name_delete**
> api26_system_acl_policy_name_delete(policy_name)

Delete policy

### Example
```R
library(openlattice-rundeck)

var.policy_name <- 'policy_name_example' # character | Policy file name

#Delete policy
api.instance <- SystemApi$new()
api.instance$api26_system_acl_policy_name_delete(var.policy_name)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_name** | **character**| Policy file name | 

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

