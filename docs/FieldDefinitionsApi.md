# laserfiche_api.FieldDefinitionsApi

All URIs are relative to *https://api.laserfiche.com/repository*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_field_definition_by_id**](FieldDefinitionsApi.md#get_field_definition_by_id) | **GET** /v1-alpha/Repositories/{repoId}/FieldDefinitions/{fieldDefinitionId} | 
[**get_field_definitions**](FieldDefinitionsApi.md#get_field_definitions) | **GET** /v1-alpha/Repositories/{repoId}/FieldDefinitions | 

# **get_field_definition_by_id**
> WFieldInfo get_field_definition_by_id(repo_id, field_definition_id, select=select)



- Returns a single field definition associated with the specified ID.  - Useful when a route provides a minimal amount of details and more information about the specific field definition is needed. - Allowed OData query options: Select

### Example
```python
from __future__ import print_function
import time
import laserfiche_api
from laserfiche_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = laserfiche_api.FieldDefinitionsApi(laserfiche_api.ApiClient(configuration))
repo_id = 'repo_id_example' # str | The requested repository ID.
field_definition_id = 56 # int | The requested field definition ID.
select = 'select_example' # str | Limits the properties returned in the result. (optional)

try:
    api_response = api_instance.get_field_definition_by_id(repo_id, field_definition_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldDefinitionsApi->get_field_definition_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_id** | **str**| The requested repository ID. | 
 **field_definition_id** | **int**| The requested field definition ID. | 
 **select** | **str**| Limits the properties returned in the result. | [optional] 

### Return type

[**WFieldInfo**](WFieldInfo.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_field_definitions**
> ODataValueOfIListOfWFieldInfo get_field_definitions(repo_id, prefer=prefer, select=select, orderby=orderby, top=top, skip=skip, count=count)



- Returns a paged listing of field definitions available in the specified repository. - Useful when trying to find a list of all field definitions available, rather than only those assigned to a specific entry/template. - Default page size: 100. Allowed OData query options: Select | Count | OrderBy | Skip | Top | SkipToken | Prefer.

### Example
```python
from __future__ import print_function
import time
import laserfiche_api
from laserfiche_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = laserfiche_api.FieldDefinitionsApi(laserfiche_api.ApiClient(configuration))
repo_id = 'repo_id_example' # str | The requested repository ID.
prefer = 'prefer_example' # str | An optional OData header. Can be used to set the maximum page size using odata.maxpagesize. (optional)
select = 'select_example' # str | Limits the properties returned in the result. (optional)
orderby = 'orderby_example' # str | Specifies the order in which items are returned. The maximum number of expressions is 5. (optional)
top = 56 # int | Limits the number of items returned from a collection. (optional)
skip = 56 # int | Excludes the specified number of items of the queried collection from the result. (optional)
count = true # bool | Indicates whether the total count of items within a collection are returned in the result. (optional)

try:
    api_response = api_instance.get_field_definitions(repo_id, prefer=prefer, select=select, orderby=orderby, top=top, skip=skip, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldDefinitionsApi->get_field_definitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_id** | **str**| The requested repository ID. | 
 **prefer** | **str**| An optional OData header. Can be used to set the maximum page size using odata.maxpagesize. | [optional] 
 **select** | **str**| Limits the properties returned in the result. | [optional] 
 **orderby** | **str**| Specifies the order in which items are returned. The maximum number of expressions is 5. | [optional] 
 **top** | **int**| Limits the number of items returned from a collection. | [optional] 
 **skip** | **int**| Excludes the specified number of items of the queried collection from the result. | [optional] 
 **count** | **bool**| Indicates whether the total count of items within a collection are returned in the result. | [optional] 

### Return type

[**ODataValueOfIListOfWFieldInfo**](ODataValueOfIListOfWFieldInfo.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

