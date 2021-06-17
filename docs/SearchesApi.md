# laserfiche-api.SearchesApi

All URIs are relative to *https://api.laserfiche.com/repository*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_or_close_a_search**](SearchesApi.md#cancel_or_close_a_search) | **DELETE** /v1-alpha/Repositories/{repoId}/Searches/{searchToken} | Cancel or close an advanced search.
[**create_search_operation**](SearchesApi.md#create_search_operation) | **POST** /v1-alpha/Repositories/{repoId}/Searches | Run a search in the specified repository.
[**get_search_context_hits**](SearchesApi.md#get_search_context_hits) | **GET** /v1-alpha/Repositories/{repoId}/Searches/{searchToken}/Results/{rowNumber}/ContextHits | 
[**get_search_results**](SearchesApi.md#get_search_results) | **GET** /v1-alpha/Repositories/{repoId}/Searches/{searchToken}/Results | Get the search results listing of a search.
[**get_search_status**](SearchesApi.md#get_search_status) | **GET** /v1-alpha/Repositories/{repoId}/Searches/{searchToken} | Get the status of a search using a token.

# **cancel_or_close_a_search**
> ODataValueOfBoolean cancel_or_close_a_search(repo_id, search_token)

Cancel or close an advanced search.

- Cancels a currently running search. - Closes a completed search.

### Example
```python
from __future__ import print_function
import time
import laserfiche-api
from laserfiche-api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = laserfiche-api.SearchesApi(laserfiche-api.ApiClient(configuration))
repo_id = 'repo_id_example' # str | The requested repository ID.
search_token = 'search_token_example' # str | The requested searchToken.

try:
    # Cancel or close an advanced search.
    api_response = api_instance.cancel_or_close_a_search(repo_id, search_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchesApi->cancel_or_close_a_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_id** | **str**| The requested repository ID. | 
 **search_token** | **str**| The requested searchToken. | 

### Return type

[**ODataValueOfBoolean**](ODataValueOfBoolean.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_search_operation**
> AcceptedOperation create_search_operation(repo_id, body=body)

Run a search in the specified repository.

- Runs a search operation on the repository. - Optional body parameters: FuzzyType: (default none), which can be used to determine what is considered a match by number of letters or percentage. FuzzyFactor: integer value that determines the degree to which a search will be considered a match (integer value for NumberOfLetters, or int value representing a percentage). The status for search operations must be checked via the Search specific status checking route.         

### Example
```python
from __future__ import print_function
import time
import laserfiche-api
from laserfiche-api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = laserfiche-api.SearchesApi(laserfiche-api.ApiClient(configuration))
repo_id = 'repo_id_example' # str | The requested repository ID.
body = laserfiche-api.AdvancedSearchRequest() # AdvancedSearchRequest | The Laserfiche search command to run, optionally include fuzzy search settings. (optional)

try:
    # Run a search in the specified repository.
    api_response = api_instance.create_search_operation(repo_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchesApi->create_search_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_id** | **str**| The requested repository ID. | 
 **body** | [**AdvancedSearchRequest**](AdvancedSearchRequest.md)| The Laserfiche search command to run, optionally include fuzzy search settings. | [optional] 

### Return type

[**AcceptedOperation**](AcceptedOperation.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_search_context_hits**
> ODataValueOfIListOfContextHit get_search_context_hits(repo_id, search_token, row_number, prefer=prefer, select=select, orderby=orderby, top=top, skip=skip, count=count)



- Returns the context hits associated with a search result entry. - Given a searchToken, and rowNumber associated with a search entry in the listing, return the context hits for that entry. - Default page size: 150. Allowed OData query options: Select | Count | OrderBy | Skip | Top | SkipToken | Prefer.

### Example
```python
from __future__ import print_function
import time
import laserfiche-api
from laserfiche-api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = laserfiche-api.SearchesApi(laserfiche-api.ApiClient(configuration))
repo_id = 'repo_id_example' # str | The requested repository ID.
search_token = 'search_token_example' # str | The requested searchToken.
row_number = 56 # int | The search result listing row number to get context hits for.
prefer = 'prefer_example' # str | An optional OData header. Can be used to set the maximum page size using odata.maxpagesize. (optional)
select = 'select_example' # str | Limits the properties returned in the result. (optional)
orderby = 'orderby_example' # str | Specifies the order in which items are returned. The maximum number of expressions is 5. (optional)
top = 56 # int | Limits the number of items returned from a collection. (optional)
skip = 56 # int | Excludes the specified number of items of the queried collection from the result. (optional)
count = true # bool | Indicates whether the total count of items within a collection are returned in the result. (optional)

try:
    api_response = api_instance.get_search_context_hits(repo_id, search_token, row_number, prefer=prefer, select=select, orderby=orderby, top=top, skip=skip, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchesApi->get_search_context_hits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_id** | **str**| The requested repository ID. | 
 **search_token** | **str**| The requested searchToken. | 
 **row_number** | **int**| The search result listing row number to get context hits for. | 
 **prefer** | **str**| An optional OData header. Can be used to set the maximum page size using odata.maxpagesize. | [optional] 
 **select** | **str**| Limits the properties returned in the result. | [optional] 
 **orderby** | **str**| Specifies the order in which items are returned. The maximum number of expressions is 5. | [optional] 
 **top** | **int**| Limits the number of items returned from a collection. | [optional] 
 **skip** | **int**| Excludes the specified number of items of the queried collection from the result. | [optional] 
 **count** | **bool**| Indicates whether the total count of items within a collection are returned in the result. | [optional] 

### Return type

[**ODataValueOfIListOfContextHit**](ODataValueOfIListOfContextHit.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_search_results**
> ODataValueOfIListOfEntry get_search_results(repo_id, search_token, group_by_entry_type=group_by_entry_type, refresh=refresh, prefer=prefer, select=select, orderby=orderby, top=top, skip=skip, count=count)

Get the search results listing of a search.

- Returns a search result listing if the search is completed. - Optional query parameter: groupByOrderType (default false). This query parameter decides whether or not results are returned in groups based on their entry type. - Optional query parameter: refresh (default false). If the search listing should be refreshed to show updated values. - Default page size: 150. Allowed OData query options: Select | Count | OrderBy | Skip | Top | SkipToken | Prefer. OData $OrderBy syntax should follow: \"PropertyName direction,PropertyName2 direction\". sort order can be either \"asc\" or \"desc\".

### Example
```python
from __future__ import print_function
import time
import laserfiche-api
from laserfiche-api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = laserfiche-api.SearchesApi(laserfiche-api.ApiClient(configuration))
repo_id = 'repo_id_example' # str | The requested repository ID.
search_token = 'search_token_example' # str | The requested searchToken.
group_by_entry_type = true # bool | An optional query parameter used to indicate if the result should be grouped by entry type or not. (optional)
refresh = true # bool | If the search listing should be refreshed to show updated values. (optional)
prefer = 'prefer_example' # str | An optional odata header. Can be used to set the maximum page size using odata.maxpagesize. (optional)
select = 'select_example' # str | Limits the properties returned in the result. (optional)
orderby = 'orderby_example' # str | Specifies the order in which items are returned. The maximum number of expressions is 5. (optional)
top = 56 # int | Limits the number of items returned from a collection. (optional)
skip = 56 # int | Excludes the specified number of items of the queried collection from the result. (optional)
count = true # bool | Indicates whether the total count of items within a collection are returned in the result. (optional)

try:
    # Get the search results listing of a search.
    api_response = api_instance.get_search_results(repo_id, search_token, group_by_entry_type=group_by_entry_type, refresh=refresh, prefer=prefer, select=select, orderby=orderby, top=top, skip=skip, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchesApi->get_search_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_id** | **str**| The requested repository ID. | 
 **search_token** | **str**| The requested searchToken. | 
 **group_by_entry_type** | **bool**| An optional query parameter used to indicate if the result should be grouped by entry type or not. | [optional] 
 **refresh** | **bool**| If the search listing should be refreshed to show updated values. | [optional] 
 **prefer** | **str**| An optional odata header. Can be used to set the maximum page size using odata.maxpagesize. | [optional] 
 **select** | **str**| Limits the properties returned in the result. | [optional] 
 **orderby** | **str**| Specifies the order in which items are returned. The maximum number of expressions is 5. | [optional] 
 **top** | **int**| Limits the number of items returned from a collection. | [optional] 
 **skip** | **int**| Excludes the specified number of items of the queried collection from the result. | [optional] 
 **count** | **bool**| Indicates whether the total count of items within a collection are returned in the result. | [optional] 

### Return type

[**ODataValueOfIListOfEntry**](ODataValueOfIListOfEntry.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_search_status**
> OperationProgress get_search_status(repo_id, search_token)

Get the status of a search using a token.

- Returns search status. - Provide a token (returned in the create search asynchronous route), and get the search status, progress, and any errors that may have occurred. When the search is completed, the Location header can be inspected as a link to the search results. - OperationStatus can be one of the following : NotStarted, InProgress, Completed, Failed, or Canceled.

### Example
```python
from __future__ import print_function
import time
import laserfiche-api
from laserfiche-api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = laserfiche-api.SearchesApi(laserfiche-api.ApiClient(configuration))
repo_id = 'repo_id_example' # str | The requested repository ID.
search_token = 'search_token_example' # str | The requested searchToken.

try:
    # Get the status of a search using a token.
    api_response = api_instance.get_search_status(repo_id, search_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchesApi->get_search_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_id** | **str**| The requested repository ID. | 
 **search_token** | **str**| The requested searchToken. | 

### Return type

[**OperationProgress**](OperationProgress.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

