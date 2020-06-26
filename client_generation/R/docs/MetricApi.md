# MetricApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metric_list**](MetricApi.md#metric_list) | **GET** /api/26/metrics | List links to enabled Metrics endpoints


# **metric_list**
> metric_list()

List links to enabled Metrics endpoints

### Example
```R
library(openlattice-rundeck)


#List links to enabled Metrics endpoints
api.instance <- MetricApi$new()
api.instance$metric_list()
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
| **200** | List of Metrics endpoint links |  -  |

