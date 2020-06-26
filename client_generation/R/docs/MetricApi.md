# MetricApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api26_metrics_get**](MetricApi.md#api26_metrics_get) | **GET** /api/26/metrics | List links to enabled Metrics endpoints


# **api26_metrics_get**
> api26_metrics_get()

List links to enabled Metrics endpoints

### Example
```R
library(openlattice-rundeck)


#List links to enabled Metrics endpoints
api.instance <- MetricApi$new()
api.instance$api26_metrics_get()
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

