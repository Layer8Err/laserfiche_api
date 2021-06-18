# laserfiche_api.TemplateDefinitionsApi

All URIs are relative to *https://api.laserfiche.com/repository*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_template_definition_by_id**](TemplateDefinitionsApi.md#get_template_definition_by_id) | **GET** /v1-alpha/Repositories/{repoId}/TemplateDefinitions/{templateId} | 
[**get_template_definitions**](TemplateDefinitionsApi.md#get_template_definitions) | **GET** /v1-alpha/Repositories/{repoId}/TemplateDefinitions | 
[**get_template_field_definitions**](TemplateDefinitionsApi.md#get_template_field_definitions) | **GET** /v1-alpha/Repositories/{repoId}/TemplateDefinitions/{templateId}/fields | 

# **get_template_definition_by_id**
> WTemplateInfo get_template_definition_by_id(repo_id, template_id)



- Returns a single template definition (including field definitions, if relevant). - Provide a template definition ID, and get the single template definition associated with that ID. Useful when a route provides a minimal amount of details, and more information about the specific template is needed. - Allowed OData query options: Select

### Example
```python
from __future__ import print_function
import time
import laserfiche_api
from laserfiche_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = laserfiche_api.TemplateDefinitionsApi(laserfiche_api.ApiClient(configuration))
repo_id = 'repo_id_example' # str | The requested repository ID.
template_id = 56 # int | The requested template definition ID.

try:
    api_response = api_instance.get_template_definition_by_id(repo_id, template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateDefinitionsApi->get_template_definition_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_id** | **str**| The requested repository ID. | 
 **template_id** | **int**| The requested template definition ID. | 

### Return type

[**WTemplateInfo**](WTemplateInfo.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_definitions**
> ODataValueOfIListOfWTemplateInfo get_template_definitions(repo_id, prefer=prefer, select=select, orderby=orderby, top=top, skip=skip, count=count)



- Returns all template definitions (including field definitions) in the repository. - Provide a repository ID, and get a paged listing of template definitions available in the repository. Useful when trying to find a list of all template definitions available, rather than a specific one. - Default page size: 100. Allowed OData query options: Select | Count | OrderBy | Skip | Top | SkipToken | Prefer.

### Example
```python
from __future__ import print_function
import time
import laserfiche_api
from laserfiche_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = laserfiche_api.TemplateDefinitionsApi(laserfiche_api.ApiClient(configuration))
repo_id = 'repo_id_example' # str | The requested repository ID.
prefer = 'prefer_example' # str | An optional OData header. Can be used to set the maximum page size using odata.maxpagesize. (optional)
select = 'select_example' # str | Limits the properties returned in the result. (optional)
orderby = 'orderby_example' # str | Specifies the order in which items are returned. The maximum number of expressions is 5. (optional)
top = 56 # int | Limits the number of items returned from a collection. (optional)
skip = 56 # int | Excludes the specified number of items of the queried collection from the result. (optional)
count = true # bool | Indicates whether the total count of items within a collection are returned in the result. (optional)

try:
    api_response = api_instance.get_template_definitions(repo_id, prefer=prefer, select=select, orderby=orderby, top=top, skip=skip, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateDefinitionsApi->get_template_definitions: %s\n" % e)
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

[**ODataValueOfIListOfWTemplateInfo**](ODataValueOfIListOfWTemplateInfo.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_field_definitions**
> ODataValueOfIListOfTemplateFieldInfo get_template_field_definitions(repo_id, template_id, prefer=prefer, select=select, orderby=orderby, top=top, skip=skip, count=count)



- Returns the field definitions assigned to a template definition. - Provide a template definition ID, and get a paged listing of the field definitions assigned to that template.  - Default page size: 100. Allowed OData query options: Select | Count | OrderBy | Skip | Top | SkipToken | Prefer.

### Example
```python
from __future__ import print_function
import time
import laserfiche_api
from laserfiche_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = laserfiche_api.TemplateDefinitionsApi(laserfiche_api.ApiClient(configuration))
repo_id = 'repo_id_example' # str | The requested repository ID.
template_id = 56 # int | The requested template definition ID.
prefer = 'prefer_example' # str | An optional OData header. Can be used to set the maximum page size using odata.maxpagesize. (optional)
select = 'select_example' # str | Limits the properties returned in the result. (optional)
orderby = 'orderby_example' # str | Specifies the order in which items are returned. The maximum number of expressions is 5. (optional)
top = 56 # int | Limits the number of items returned from a collection. (optional)
skip = 56 # int | Excludes the specified number of items of the queried collection from the result. (optional)
count = true # bool | Indicates whether the total count of items within a collection are returned in the result. (optional)

try:
    api_response = api_instance.get_template_field_definitions(repo_id, template_id, prefer=prefer, select=select, orderby=orderby, top=top, skip=skip, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateDefinitionsApi->get_template_field_definitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_id** | **str**| The requested repository ID. | 
 **template_id** | **int**| The requested template definition ID. | 
 **prefer** | **str**| An optional OData header. Can be used to set the maximum page size using odata.maxpagesize. | [optional] 
 **select** | **str**| Limits the properties returned in the result. | [optional] 
 **orderby** | **str**| Specifies the order in which items are returned. The maximum number of expressions is 5. | [optional] 
 **top** | **int**| Limits the number of items returned from a collection. | [optional] 
 **skip** | **int**| Excludes the specified number of items of the queried collection from the result. | [optional] 
 **count** | **bool**| Indicates whether the total count of items within a collection are returned in the result. | [optional] 

### Return type

[**ODataValueOfIListOfTemplateFieldInfo**](ODataValueOfIListOfTemplateFieldInfo.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

