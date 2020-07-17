# MetricApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metric_list**](MetricApi.md#metric_list) | **GET** /api/26/metrics | List links to enabled Metrics endpoints


# **metric_list**
> InlineResponse2001 metric_list()

List links to enabled Metrics endpoints

### Example
```R
library(olrundeck)


#List links to enabled Metrics endpoints
api.instance <- MetricApi$new()
# Configure API key authorization: rundeck_auth
api.instance$apiClient$apiKeys['X-Rundeck-Auth-Token'] <- 'TODO_YOUR_API_KEY';
result <- api.instance$metric_list()
dput(result)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2001**](inline_response_200_1.md)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Metrics endpoint links |  -  |

