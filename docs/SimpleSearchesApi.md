# laserfiche_api.SimpleSearchesApi

All URIs are relative to *https://api.laserfiche.com/repository*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_simple_search_operation**](SimpleSearchesApi.md#create_simple_search_operation) | **POST** /v1-alpha/Repositories/{repoId}/SimpleSearches | 

# **create_simple_search_operation**
> ODataValueOfIListOfEntry create_simple_search_operation(repo_id, body=body)



- Runs a \"simple\" search operation on the repository. - Returns a truncated search result listing. - Search result listing may be truncated, depending on number of results. Additionally, searches may time out if they take too long. Use the other search route to run full searches.

### Example
```python
from __future__ import print_function
import time
import laserfiche_api
from laserfiche_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = laserfiche_api.SimpleSearchesApi(laserfiche_api.ApiClient(configuration))
repo_id = 'repo_id_example' # str | The requested repository ID.
body = laserfiche_api.SimpleSearchRequest() # SimpleSearchRequest | The Laserfiche search command to run. (optional)

try:
    api_response = api_instance.create_simple_search_operation(repo_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimpleSearchesApi->create_simple_search_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_id** | **str**| The requested repository ID. | 
 **body** | [**SimpleSearchRequest**](SimpleSearchRequest.md)| The Laserfiche search command to run. | [optional] 

### Return type

[**ODataValueOfIListOfEntry**](ODataValueOfIListOfEntry.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

