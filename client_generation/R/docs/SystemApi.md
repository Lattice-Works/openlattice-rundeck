# SystemApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_acl_policy_delete**](SystemApi.md#system_acl_policy_delete) | **DELETE** /api/26/system/acl/{policyName} | Delete policy


# **system_acl_policy_delete**
> system_acl_policy_delete(policy_name)

Delete policy

### Example
```R
library(openlattice-rundeck)

var.policy_name <- 'policy_name_example' # character | Policy file name

#Delete policy
api.instance <- SystemApi$new()
api.instance$system_acl_policy_delete(var.policy_name)
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

