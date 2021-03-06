# olrundeck.MetricApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metric_list**](MetricApi.md#metric_list) | **GET** /api/26/metrics | List links to enabled Metrics endpoints


# **metric_list**
> InlineResponse2001 metric_list()

List links to enabled Metrics endpoints

### Example

* Api Key Authentication (rundeck_auth):
```python
from __future__ import print_function
import time
import olrundeck
from olrundeck.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = olrundeck.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: rundeck_auth
configuration = olrundeck.Configuration(
    host = "http://localhost",
    api_key = {
        'rundeck_auth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['rundeck_auth'] = 'Bearer'

# Enter a context with an instance of the API client
with olrundeck.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = olrundeck.MetricApi(api_client)
    
    try:
        # List links to enabled Metrics endpoints
        api_response = api_instance.metric_list()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricApi->metric_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Metrics endpoint links |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

