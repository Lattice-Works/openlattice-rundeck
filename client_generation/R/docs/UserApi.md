# UserApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api26_user_roles_get**](UserApi.md#api26_user_roles_get) | **GET** /api/26/user/roles | List the roles of the authenticated user


# **api26_user_roles_get**
> api26_user_roles_get()

List the roles of the authenticated user

### Example
```R
library(openlattice-rundeck)


#List the roles of the authenticated user
api.instance <- UserApi$new()
api.instance$api26_user_roles_get()
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

