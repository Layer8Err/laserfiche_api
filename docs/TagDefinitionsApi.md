# laserfiche_api.TagDefinitionsApi

All URIs are relative to *https://api.laserfiche.com/repository*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tag_definition_by_id**](TagDefinitionsApi.md#get_tag_definition_by_id) | **GET** /v1-alpha/Repositories/{repoId}/TagDefinitions/{tagId} | 
[**get_tag_definitions**](TagDefinitionsApi.md#get_tag_definitions) | **GET** /v1-alpha/Repositories/{repoId}/TagDefinitions | 

# **get_tag_definition_by_id**
> WTagInfo get_tag_definition_by_id(repo_id, tag_id)



- Returns a single tag definition. - Provide a tag definition ID, and get the single tag definition associated with that ID. Useful when another route provides a minimal amount of details, and more information about the specific tag is needed. - Allowed OData query options: Select

### Example
```python
from __future__ import print_function
import time
import laserfiche_api
from laserfiche_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = laserfiche_api.TagDefinitionsApi(laserfiche_api.ApiClient(configuration))
repo_id = 'repo_id_example' # str | The requested repository ID.
tag_id = 56 # int | The requested tag definition ID.

try:
    api_response = api_instance.get_tag_definition_by_id(repo_id, tag_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagDefinitionsApi->get_tag_definition_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_id** | **str**| The requested repository ID. | 
 **tag_id** | **int**| The requested tag definition ID. | 

### Return type

[**WTagInfo**](WTagInfo.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag_definitions**
> ODataValueOfIListOfWTagInfo get_tag_definitions(repo_id, prefer=prefer, select=select, orderby=orderby, top=top, skip=skip, count=count)



- Returns all tag definitions in the repository. - Provide a repository ID and get a paged listing of tag definitions available in the repository. Useful when trying to display all tag definitions available, not only tags assigned to a specific entry. - Default page size: 100. Allowed OData query options: Select | Count | OrderBy | Skip | Top | SkipToken | Prefer.

### Example
```python
from __future__ import print_function
import time
import laserfiche_api
from laserfiche_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = laserfiche_api.TagDefinitionsApi(laserfiche_api.ApiClient(configuration))
repo_id = 'repo_id_example' # str | The requested repository ID.
prefer = 'prefer_example' # str | An optional OData header. Can be used to set the maximum page size using odata.maxpagesize. (optional)
select = 'select_example' # str | Limits the properties returned in the result. (optional)
orderby = 'orderby_example' # str | Specifies the order in which items are returned. The maximum number of expressions is 5. (optional)
top = 56 # int | Limits the number of items returned from a collection. (optional)
skip = 56 # int | Excludes the specified number of items of the queried collection from the result. (optional)
count = true # bool | Indicates whether the total count of items within a collection are returned in the result. (optional)

try:
    api_response = api_instance.get_tag_definitions(repo_id, prefer=prefer, select=select, orderby=orderby, top=top, skip=skip, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagDefinitionsApi->get_tag_definitions: %s\n" % e)
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

[**ODataValueOfIListOfWTagInfo**](ODataValueOfIListOfWTagInfo.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

