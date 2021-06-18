# laserfiche_api.AttributesApi

All URIs are relative to *https://api.laserfiche.com/repository*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_trustee_attribute_key_value_pairs**](AttributesApi.md#get_trustee_attribute_key_value_pairs) | **GET** /v1-alpha/Repositories/{repoId}/Attributes | Get the attribute key value pairs associated with the authenticated user.
[**get_trustee_attribute_value_by_key**](AttributesApi.md#get_trustee_attribute_value_by_key) | **GET** /v1-alpha/Repositories/{repoId}/Attributes/{attributeKey} | Get an attribute object by key associated with the authenticated user.

# **get_trustee_attribute_key_value_pairs**
> ODataValueOfListOfAttribute get_trustee_attribute_key_value_pairs(repo_id, everyone=everyone, select=select, orderby=orderby, count=count)

Get the attribute key value pairs associated with the authenticated user.

- Returns the attribute key value pairs associated with the authenticated user. Alternatively, return only the attribute key value pairs that are associated with the \"Everyone\" group. - Attribute keys can be used with subsequent calls to get specific attribute values. - Allowed OData query options: Select, count, orderby. Optional query parameters : everyone (bool, default false). When true, this route does not return the attributes that are tied to the currently authenticated user, but rather the attributes assigned to the \"Everyone\" group. Note when this true, this response does not include both the \"Everyone\" groups attribute and the currently authenticated user, but only the \"Everyone\" groups.

### Example
```python
from __future__ import print_function
import time
import laserfiche_api
from laserfiche_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = laserfiche_api.AttributesApi(laserfiche_api.ApiClient(configuration))
repo_id = 'repo_id_example' # str | The requested repository id.
everyone = true # bool | Boolean value that indicates whether to return attributes key value pairs associated with everyone or the currently authenticated user. (optional)
select = 'select_example' # str | Limits the properties returned in the result. (optional)
orderby = 'orderby_example' # str | Specifies the order in which items are returned. The maximum number of expressions is 5. (optional)
count = true # bool | Indicates whether the total count of items within a collection are returned in the result. (optional)

try:
    # Get the attribute key value pairs associated with the authenticated user.
    api_response = api_instance.get_trustee_attribute_key_value_pairs(repo_id, everyone=everyone, select=select, orderby=orderby, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesApi->get_trustee_attribute_key_value_pairs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_id** | **str**| The requested repository id. | 
 **everyone** | **bool**| Boolean value that indicates whether to return attributes key value pairs associated with everyone or the currently authenticated user. | [optional] 
 **select** | **str**| Limits the properties returned in the result. | [optional] 
 **orderby** | **str**| Specifies the order in which items are returned. The maximum number of expressions is 5. | [optional] 
 **count** | **bool**| Indicates whether the total count of items within a collection are returned in the result. | [optional] 

### Return type

[**ODataValueOfListOfAttribute**](ODataValueOfListOfAttribute.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trustee_attribute_value_by_key**
> Attribute get_trustee_attribute_value_by_key(repo_id, attribute_key, everyone=everyone)

Get an attribute object by key associated with the authenticated user.

- Returns the attribute associated with the key. Alternatively, return the attribute associated with the key within \"Everyone\" group. - Optional query parameters : everyone (bool, default false). When true, the server only searches for the attribute value with the given key upon the authenticated users attributes. If false, only the authenticated users attributes will be queried.

### Example
```python
from __future__ import print_function
import time
import laserfiche_api
from laserfiche_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = laserfiche_api.AttributesApi(laserfiche_api.ApiClient(configuration))
repo_id = 'repo_id_example' # str | The requested repository id.
attribute_key = 'attribute_key_example' # str | The requested attribute key.
everyone = true # bool | Boolean value that indicates whether to return attributes associated with everyone or the currently authenticated user. (optional)

try:
    # Get an attribute object by key associated with the authenticated user.
    api_response = api_instance.get_trustee_attribute_value_by_key(repo_id, attribute_key, everyone=everyone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesApi->get_trustee_attribute_value_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_id** | **str**| The requested repository id. | 
 **attribute_key** | **str**| The requested attribute key. | 
 **everyone** | **bool**| Boolean value that indicates whether to return attributes associated with everyone or the currently authenticated user. | [optional] 

### Return type

[**Attribute**](Attribute.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

