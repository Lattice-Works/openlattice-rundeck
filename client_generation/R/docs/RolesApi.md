# RolesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_role_list**](RolesApi.md#user_role_list) | **GET** /api/26/user/roles | List the roles of the authenticated user


# **user_role_list**
> user_role_list()

List the roles of the authenticated user

### Example
```R
library(openlattice-rundeck)


#List the roles of the authenticated user
api.instance <- RolesApi$new()
api.instance$user_role_list()
```

### Parameters
This endpoint does not need any parameter.

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
| **200** | Expected response to a valid request |  -  |

