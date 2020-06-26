# UserApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_list**](UserApi.md#user_list) | **GET** /api/26/user/list | List user profiles
[**user_profile_get**](UserApi.md#user_profile_get) | **GET** /api/26/user/info | Get same user profile data
[**user_profile_get_by_id**](UserApi.md#user_profile_get_by_id) | **GET** /api/26/user/info/{userID} | Get another user&#39;s profile data
[**user_profile_update**](UserApi.md#user_profile_update) | **POST** /api/26/user/info | Modify same user profile data
[**user_profile_update_by_id**](UserApi.md#user_profile_update_by_id) | **POST** /api/26/user/info/{userID} | Modify another user&#39;s profile data
[**user_role_list**](UserApi.md#user_role_list) | **GET** /api/26/user/roles | List the roles of the authenticated user


# **user_list**
> array[User] user_list()

List user profiles

### Example
```R
library(openlattice_rundeck)


#List user profiles
api.instance <- UserApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$user_list()
dput(result)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**array[User]**](User.md)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Expected response to a valid request |  -  |

# **user_profile_get**
> User user_profile_get()

Get same user profile data

### Example
```R
library(openlattice_rundeck)


#Get same user profile data
api.instance <- UserApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$user_profile_get()
dput(result)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Expected response to a valid request |  -  |

# **user_profile_get_by_id**
> User user_profile_get_by_id(user_id)

Get another user's profile data

### Example
```R
library(openlattice_rundeck)

var.user_id <- 'user_id_example' # character | The ID of the user to retrieve profile information for

#Get another user's profile data
api.instance <- UserApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$user_profile_get_by_id(var.user_id)
dput(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **character**| The ID of the user to retrieve profile information for | 

### Return type

[**User**](User.md)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Expected response to a valid request |  -  |

# **user_profile_update**
> User user_profile_update(body)

Modify same user profile data

### Example
```R
library(openlattice_rundeck)

var.body <- NULL # object | 

#Modify same user profile data
api.instance <- UserApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$user_profile_update(var.body)
dput(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

### Return type

[**User**](User.md)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Expected response to a valid request |  -  |

# **user_profile_update_by_id**
> User user_profile_update_by_id(user_id, body)

Modify another user's profile data

### Example
```R
library(openlattice_rundeck)

var.user_id <- 'user_id_example' # character | The ID of the user to retrieve profile information for
var.body <- NULL # object | 

#Modify another user's profile data
api.instance <- UserApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$user_profile_update_by_id(var.user_id, var.body)
dput(result)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **character**| The ID of the user to retrieve profile information for | 
 **body** | **object**|  | 

### Return type

[**User**](User.md)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Expected response to a valid request |  -  |

# **user_role_list**
> object user_role_list()

List the roles of the authenticated user

### Example
```R
library(openlattice_rundeck)


#List the roles of the authenticated user
api.instance <- UserApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$user_role_list()
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

