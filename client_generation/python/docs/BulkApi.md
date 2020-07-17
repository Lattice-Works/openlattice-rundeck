# olrundeck.BulkApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**job_bulk_delete**](BulkApi.md#job_bulk_delete) | **POST** /api/26/jobs/delete | Delete multiple job definitions at once


# **job_bulk_delete**
> JobBulkOperationResponse job_bulk_delete(inline_object1)

Delete multiple job definitions at once

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
    api_instance = olrundeck.BulkApi(api_client)
    inline_object1 = olrundeck.InlineObject1() # InlineObject1 | 

    try:
        # Delete multiple job definitions at once
        api_response = api_instance.job_bulk_delete(inline_object1)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BulkApi->job_bulk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object1** | [**InlineObject1**](InlineObject1.md)|  | 

### Return type

[**JobBulkOperationResponse**](JobBulkOperationResponse.md)

### Authorization

[rundeck_auth](../README.md#rundeck_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job deleted response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

