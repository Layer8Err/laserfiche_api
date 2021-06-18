# laserfiche_api.EntriesApi

All URIs are relative to *https://api.laserfiche.com/repository*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_entry_links**](EntriesApi.md#assign_entry_links) | **PUT** /v1-alpha/Repositories/{repoId}/Entries/{entryId}/links | 
[**assign_field_values**](EntriesApi.md#assign_field_values) | **PUT** /v1-alpha/Repositories/{repoId}/Entries/{entryId}/fields | 
[**assign_tags**](EntriesApi.md#assign_tags) | **PUT** /v1-alpha/Repositories/{repoId}/Entries/{entryId}/tags | 
[**copy_entry_async**](EntriesApi.md#copy_entry_async) | **POST** /v1-alpha/Repositories/{repoId}/Entries/{entryId}/Laserfiche.Repository.Folder/CopyAsync | 
[**create_or_copy_entry**](EntriesApi.md#create_or_copy_entry) | **POST** /v1-alpha/Repositories/{repoId}/Entries/{entryId}/Laserfiche.Repository.Folder/children | 
[**delete_assigned_template**](EntriesApi.md#delete_assigned_template) | **DELETE** /v1-alpha/Repositories/{repoId}/Entries/{entryId}/template | 
[**delete_entry_info**](EntriesApi.md#delete_entry_info) | **DELETE** /v1-alpha/Repositories/{repoId}/Entries/{entryId} | 
[**export_document**](EntriesApi.md#export_document) | **GET** /v1-alpha/Repositories/{repoId}/Entries/{entryId}/Laserfiche.Repository.Document/edoc | 
[**export_document_with_audit_reason**](EntriesApi.md#export_document_with_audit_reason) | **POST** /v1-alpha/Repositories/{repoId}/Entries/{entryId}/Laserfiche.Repository.Document/GetEdocWithAuditReason | 
[**get_document_content_type**](EntriesApi.md#get_document_content_type) | **HEAD** /v1-alpha/Repositories/{repoId}/Entries/{entryId}/Laserfiche.Repository.Document/edoc | 
[**get_dynamic_field_values**](EntriesApi.md#get_dynamic_field_values) | **POST** /v1-alpha/Repositories/{repoId}/Entries/{entryId}/fields/GetDynamicFieldLogicValue | 
[**get_entry**](EntriesApi.md#get_entry) | **GET** /v1-alpha/Repositories/{repoId}/Entries/{entryId} | 
[**get_entry_listing**](EntriesApi.md#get_entry_listing) | **GET** /v1-alpha/Repositories/{repoId}/Entries/{entryId}/Laserfiche.Repository.Folder/children | 
[**get_field_values**](EntriesApi.md#get_field_values) | **GET** /v1-alpha/Repositories/{repoId}/Entries/{entryId}/fields | 
[**get_link_values_from_entry**](EntriesApi.md#get_link_values_from_entry) | **GET** /v1-alpha/Repositories/{repoId}/Entries/{entryId}/links | 
[**get_tags_assigned_to_entry**](EntriesApi.md#get_tags_assigned_to_entry) | **GET** /v1-alpha/Repositories/{repoId}/Entries/{entryId}/tags | 
[**import_document**](EntriesApi.md#import_document) | **POST** /v1-alpha/Repositories/{repoId}/Entries/{parentEntryId}/{fileName} | 
[**move_or_rename_document**](EntriesApi.md#move_or_rename_document) | **PATCH** /v1-alpha/Repositories/{repoId}/Entries/{entryId} | 
[**write_template_value_to_entry**](EntriesApi.md#write_template_value_to_entry) | **PUT** /v1-alpha/Repositories/{repoId}/Entries/{entryId}/template | 

# **assign_entry_links**
> ODataValueOfIListOfWEntryLinkInfo assign_entry_links(repo_id, entry_id, body=body)



- Assign links to an entry. - Provide an entry ID and a list of links to assign to that entry. - This is an overwrite action. The request must include all links to assign to the entry, including existing links that should remain assigned to the entry.

### Example
```python
from __future__ import print_function
import time
import laserfiche_api
from laserfiche_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = laserfiche_api.EntriesApi(laserfiche_api.ApiClient(configuration))
repo_id = 'repo_id_example' # str | The request repository ID.
entry_id = 56 # int | The requested entry ID.
body = [laserfiche_api.PutLinksRequest()] # list[PutLinksRequest] |  (optional)

try:
    api_response = api_instance.assign_entry_links(repo_id, entry_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->assign_entry_links: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_id** | **str**| The request repository ID. | 
 **entry_id** | **int**| The requested entry ID. | 
 **body** | [**list[PutLinksRequest]**](PutLinksRequest.md)|  | [optional] 

### Return type

[**ODataValueOfIListOfWEntryLinkInfo**](ODataValueOfIListOfWEntryLinkInfo.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_field_values**
> ODataValueOfIListOfFieldValue assign_field_values(repo_id, entry_id, body=body)



- Update field values assigned to an entry. - Provide the new field values to assign to the entry, and remove/reset all previously assigned field values.  - This is an overwrite action. The request body must include all desired field values, including any existing field values that should remain assigned to the entry. Field values that are not included in the request will be deleted from the entry. If the field value that is not included is part of a template, it will still be assigned (as required by the template), but its value will be reset.

### Example
```python
from __future__ import print_function
import time
import laserfiche_api
from laserfiche_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = laserfiche_api.EntriesApi(laserfiche_api.ApiClient(configuration))
repo_id = 'repo_id_example' # str | The requested repository ID.
entry_id = 56 # int | The entry ID of the entry that will have its fields updated.
body = NULL # dict(str, FieldToUpdate) |  (optional)

try:
    api_response = api_instance.assign_field_values(repo_id, entry_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->assign_field_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_id** | **str**| The requested repository ID. | 
 **entry_id** | **int**| The entry ID of the entry that will have its fields updated. | 
 **body** | [**dict(str, FieldToUpdate)**](dict.md)|  | [optional] 

### Return type

[**ODataValueOfIListOfFieldValue**](ODataValueOfIListOfFieldValue.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_tags**
> ODataValueOfIListOfWTagInfo assign_tags(repo_id, entry_id, body=body)



- Assign tags to an entry. - Provide an entry ID and a list of tags to assign to that entry. - This is an overwrite action. The request must include all tags to assign to the entry, including existing tags that should remain assigned to the entry.

### Example
```python
from __future__ import print_function
import time
import laserfiche_api
from laserfiche_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = laserfiche_api.EntriesApi(laserfiche_api.ApiClient(configuration))
repo_id = 'repo_id_example' # str | The requested repository ID.
entry_id = 56 # int | The requested entry ID.
body = laserfiche_api.PutTagRequest() # PutTagRequest | The tags to add. (optional)

try:
    api_response = api_instance.assign_tags(repo_id, entry_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->assign_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_id** | **str**| The requested repository ID. | 
 **entry_id** | **int**| The requested entry ID. | 
 **body** | [**PutTagRequest**](PutTagRequest.md)| The tags to add. | [optional] 

### Return type

[**ODataValueOfIListOfWTagInfo**](ODataValueOfIListOfWTagInfo.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_entry_async**
> AcceptedOperation copy_entry_async(repo_id, entry_id, body=body, auto_rename=auto_rename)



- Copy a new child entry in the designated folder async, and potentially return an operationToken. - Provide the parent folder id, and copy an entry as a child of the designated folder. - Optional parameter: autoRename (default false). If an entry already exists with the given name, the entry will be automatically renamed.  - The status of the operation can be checked via the Tasks/{operationToken} route.

### Example
```python
from __future__ import print_function
import time
import laserfiche_api
from laserfiche_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = laserfiche_api.EntriesApi(laserfiche_api.ApiClient(configuration))
repo_id = 'repo_id_example' # str | The requested repository id.
entry_id = 56 # int | The folder id that the entry will be created in.
body = laserfiche_api.CopyAsyncRequest() # CopyAsyncRequest | Copy entry request. (optional)
auto_rename = true # bool | An optional query parameter used to indicate if the new entry should be automatically             renamed if an entry already exists with the given name in the folder. The default value is false. (optional)

try:
    api_response = api_instance.copy_entry_async(repo_id, entry_id, body=body, auto_rename=auto_rename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->copy_entry_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_id** | **str**| The requested repository id. | 
 **entry_id** | **int**| The folder id that the entry will be created in. | 
 **body** | [**CopyAsyncRequest**](CopyAsyncRequest.md)| Copy entry request. | [optional] 
 **auto_rename** | **bool**| An optional query parameter used to indicate if the new entry should be automatically             renamed if an entry already exists with the given name in the folder. The default value is false. | [optional] 

### Return type

[**AcceptedOperation**](AcceptedOperation.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_or_copy_entry**
> Entry create_or_copy_entry(repo_id, entry_id, body=body, auto_rename=auto_rename)



- Create/copy a new child entry in the designated folder. - Provide the parent folder id, and based on the request body, copy or create a folder/shortcut as a child entry of the designated folder. - Optional parameter: autoRename (default false). If an entry already exists with the given name, the entry will be automatically renamed.

### Example
```python
from __future__ import print_function
import time
import laserfiche_api
from laserfiche_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = laserfiche_api.EntriesApi(laserfiche_api.ApiClient(configuration))
repo_id = 'repo_id_example' # str | The requested repository id.
entry_id = 56 # int | The folder id that the entry will be created in.
body = laserfiche_api.PostEntryChildrenRequest() # PostEntryChildrenRequest | The entry to create. (optional)
auto_rename = true # bool | An optional query parameter used to indicate if the new entry should be automatically             renamed if an entry already exists with the given name in the folder. The default value is false. (optional)

try:
    api_response = api_instance.create_or_copy_entry(repo_id, entry_id, body=body, auto_rename=auto_rename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->create_or_copy_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_id** | **str**| The requested repository id. | 
 **entry_id** | **int**| The folder id that the entry will be created in. | 
 **body** | [**PostEntryChildrenRequest**](PostEntryChildrenRequest.md)| The entry to create. | [optional] 
 **auto_rename** | **bool**| An optional query parameter used to indicate if the new entry should be automatically             renamed if an entry already exists with the given name in the folder. The default value is false. | [optional] 

### Return type

[**Entry**](Entry.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_assigned_template**
> Entry delete_assigned_template(repo_id, entry_id)



- Remove the currently assigned template from the specified entry. - Provide an entry id to clear template value on. - If the entry does not have a template assigned, no change will be made.

### Example
```python
from __future__ import print_function
import time
import laserfiche_api
from laserfiche_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = laserfiche_api.EntriesApi(laserfiche_api.ApiClient(configuration))
repo_id = 'repo_id_example' # str | The requested repository id.
entry_id = 56 # int | The id of the entry that will have its template removed.

try:
    api_response = api_instance.delete_assigned_template(repo_id, entry_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->delete_assigned_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_id** | **str**| The requested repository id. | 
 **entry_id** | **int**| The id of the entry that will have its template removed. | 

### Return type

[**Entry**](Entry.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_entry_info**
> AcceptedOperation delete_entry_info(repo_id, entry_id, body=body)



- Begins a task to delete an entry, and returns an operationToken. - Provide an entry ID, and queue a delete task to remove it from the repository (includes nested objects if the entry is a Folder type). The entry will not be deleted immediately. - Optionally include an audit reason ID and comment in the JSON body. This route returns an operationToken, and will run as an asynchronous operation. Check the progress via the Tasks/{operationToken} route.

### Example
```python
from __future__ import print_function
import time
import laserfiche_api
from laserfiche_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = laserfiche_api.EntriesApi(laserfiche_api.ApiClient(configuration))
repo_id = 'repo_id_example' # str | The requested repository ID.
entry_id = 56 # int | The requested entry ID.
body = laserfiche_api.DeleteEntryWithAuditReason() # DeleteEntryWithAuditReason |  (optional)

try:
    api_response = api_instance.delete_entry_info(repo_id, entry_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->delete_entry_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_id** | **str**| The requested repository ID. | 
 **entry_id** | **int**| The requested entry ID. | 
 **body** | [**DeleteEntryWithAuditReason**](DeleteEntryWithAuditReason.md)|  | [optional] 

### Return type

[**AcceptedOperation**](AcceptedOperation.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_document**
> str export_document(repo_id, entry_id, range=range)



- Get an entry's edoc resource in a stream format. - Provide an entry id, and get the edoc resource as part of the response content. - Optional header: Range. Use the Range header (single range with byte unit) to retrieve partial content of the edoc, rather than the entire edoc.

### Example
```python
from __future__ import print_function
import time
import laserfiche_api
from laserfiche_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = laserfiche_api.EntriesApi(laserfiche_api.ApiClient(configuration))
repo_id = 'repo_id_example' # str | The requested repository id.
entry_id = 56 # int | The requested document id.
range = 'range_example' # str | An optional header used to retrieve partial content of the edoc. Only supports single             range with byte unit. (optional)

try:
    api_response = api_instance.export_document(repo_id, entry_id, range=range)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->export_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_id** | **str**| The requested repository id. | 
 **entry_id** | **int**| The requested document id. | 
 **range** | **str**| An optional header used to retrieve partial content of the edoc. Only supports single             range with byte unit. | [optional] 

### Return type

**str**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_document_with_audit_reason**
> str export_document_with_audit_reason(repo_id, entry_id, body=body, range=range)



- Get an entry's edoc resource in a stream format while including an audit reason. - Provide an entry id and audit reason/comment in the request body, and get the edoc resource as part of the response content. - Optional header: Range. Use the Range header (single range with byte unit) to retrieve partial content of the edoc, rather than the entire edoc. This route is identical to the GET edoc route, but allows clients to include an audit reason when downloading the edoc.

### Example
```python
from __future__ import print_function
import time
import laserfiche_api
from laserfiche_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = laserfiche_api.EntriesApi(laserfiche_api.ApiClient(configuration))
repo_id = 'repo_id_example' # str | The requested repository id.
entry_id = 56 # int | The requested document id.
body = laserfiche_api.GetEdocWithAuditReasonRequest() # GetEdocWithAuditReasonRequest |  (optional)
range = 'range_example' # str | An optional header used to retrieve partial content of the edoc. Only supports single             range with byte unit. (optional)

try:
    api_response = api_instance.export_document_with_audit_reason(repo_id, entry_id, body=body, range=range)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->export_document_with_audit_reason: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_id** | **str**| The requested repository id. | 
 **entry_id** | **int**| The requested document id. | 
 **body** | [**GetEdocWithAuditReasonRequest**](GetEdocWithAuditReasonRequest.md)|  | [optional] 
 **range** | **str**| An optional header used to retrieve partial content of the edoc. Only supports single             range with byte unit. | [optional] 

### Return type

**str**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_content_type**
> get_document_content_type(repo_id, entry_id)



- Get information about the edoc content of an entry, without downloading the edoc in its entirety. - Provide an entry id, and get back the Content-Type and Content-Length in the response headers. - This route does not provide a way to download the actual edoc. Instead, it just gives metadata information about the edoc associated with the entry.

### Example
```python
from __future__ import print_function
import time
import laserfiche_api
from laserfiche_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = laserfiche_api.EntriesApi(laserfiche_api.ApiClient(configuration))
repo_id = 'repo_id_example' # str | The requested repository id.
entry_id = 56 # int | The requested document id.

try:
    api_instance.get_document_content_type(repo_id, entry_id)
except ApiException as e:
    print("Exception when calling EntriesApi->get_document_content_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_id** | **str**| The requested repository id. | 
 **entry_id** | **int**| The requested document id. | 

### Return type

void (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dynamic_field_values**
> dict(str, list[str]) get_dynamic_field_values(repo_id, entry_id, body=body)



- Get dynamic field logic values with the current values of the fields in the template. - Provide an entry id and field values in the JSON body to get dynamic field logic values.  Independent and non-dynamic fields in the request body will be ignored, and only related dynamic field logic values for the assigned template will be returned.

### Example
```python
from __future__ import print_function
import time
import laserfiche_api
from laserfiche_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = laserfiche_api.EntriesApi(laserfiche_api.ApiClient(configuration))
repo_id = 'repo_id_example' # str | The requested repository id.
entry_id = 56 # int | The requested entry id.
body = laserfiche_api.GetDynamicFieldLogicValueRequest() # GetDynamicFieldLogicValueRequest |  (optional)

try:
    api_response = api_instance.get_dynamic_field_values(repo_id, entry_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->get_dynamic_field_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_id** | **str**| The requested repository id. | 
 **entry_id** | **int**| The requested entry id. | 
 **body** | [**GetDynamicFieldLogicValueRequest**](GetDynamicFieldLogicValueRequest.md)|  | [optional] 

### Return type

**dict(str, list[str])**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entry**
> Entry get_entry(repo_id, entry_id, select=select)



- Returns a single entry object. - Provide an entry ID, and get the entry associated with that ID. Useful when detailed information about the entry is required, such as metadata, path information, etc. - Allowed OData query options: Select. If the entry is a subtype (Folder, Document, or Shortcut), the entry will automatically be converted to include those model-specific properties.

### Example
```python
from __future__ import print_function
import time
import laserfiche_api
from laserfiche_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = laserfiche_api.EntriesApi(laserfiche_api.ApiClient(configuration))
repo_id = 'repo_id_example' # str | The requested repository ID.
entry_id = 56 # int | The requested entry ID.
select = 'select_example' # str | Limits the properties returned in the result. (optional)

try:
    api_response = api_instance.get_entry(repo_id, entry_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->get_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_id** | **str**| The requested repository ID. | 
 **entry_id** | **int**| The requested entry ID. | 
 **select** | **str**| Limits the properties returned in the result. | [optional] 

### Return type

[**Entry**](Entry.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entry_listing**
> ODataValueOfIListOfEntry get_entry_listing(repo_id, entry_id, group_by_entry_type=group_by_entry_type, prefer=prefer, select=select, orderby=orderby, top=top, skip=skip, count=count)



- Returns the children entries of a folder in the repository. - Provide an entry ID (must be a folder), and get a paged listing of entries in that folder. Used as a way of navigating through the repository. - Default page size: 100. Allowed OData query options: Select | Count | OrderBy | Skip | Top | SkipToken | Prefer. OData $OrderBy syntax should follow: \"PropertyName direction,PropertyName2 direction\". Sort order can be either value \"asc\" or \"desc\". Optional query parameters: groupByOrderType (bool). This query parameter decides if results are returned in groups based on their entry type. Entries returned in the listing are not automatically converted to their subtype (Folder, Shortcut, Document), so clients who want model-specific information should request it via the GET entry by ID route.

### Example
```python
from __future__ import print_function
import time
import laserfiche_api
from laserfiche_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = laserfiche_api.EntriesApi(laserfiche_api.ApiClient(configuration))
repo_id = 'repo_id_example' # str | The requested repository ID.
entry_id = 56 # int | The folder ID.
group_by_entry_type = true # bool | An optional query parameter used to indicate if the result should be grouped by entry type or not. (optional)
prefer = 'prefer_example' # str | An optional OData header. Can be used to set the maximum page size using odata.maxpagesize. (optional)
select = 'select_example' # str | Limits the properties returned in the result. (optional)
orderby = 'orderby_example' # str | Specifies the order in which items are returned. The maximum number of expressions is 5. (optional)
top = 56 # int | Limits the number of items returned from a collection. (optional)
skip = 56 # int | Excludes the specified number of items of the queried collection from the result. (optional)
count = true # bool | Indicates whether the total count of items within a collection are returned in the result. (optional)

try:
    api_response = api_instance.get_entry_listing(repo_id, entry_id, group_by_entry_type=group_by_entry_type, prefer=prefer, select=select, orderby=orderby, top=top, skip=skip, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->get_entry_listing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_id** | **str**| The requested repository ID. | 
 **entry_id** | **int**| The folder ID. | 
 **group_by_entry_type** | **bool**| An optional query parameter used to indicate if the result should be grouped by entry type or not. | [optional] 
 **prefer** | **str**| An optional OData header. Can be used to set the maximum page size using odata.maxpagesize. | [optional] 
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

# **get_field_values**
> ODataValueOfIListOfFieldValue get_field_values(repo_id, entry_id, prefer=prefer, format_value=format_value, culture=culture, select=select, orderby=orderby, top=top, skip=skip, count=count)



- Returns the fields assigned to an entry. - Provide an entry ID, and get a paged listing of all fields assigned to that entry. - Default page size: 100. Allowed OData query options: Select | Count | OrderBy | Skip | Top | SkipToken | Prefer.

### Example
```python
from __future__ import print_function
import time
import laserfiche_api
from laserfiche_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = laserfiche_api.EntriesApi(laserfiche_api.ApiClient(configuration))
repo_id = 'repo_id_example' # str | The requested repository ID.
entry_id = 56 # int | The requested entry ID.
prefer = 'prefer_example' # str | An optional OData header. Can be used to set the maximum page size using odata.maxpagesize. (optional)
format_value = false # bool | An optional query parameter used to indicate if the field values should be formatted.             The default value is false. (optional) (default to false)
culture = '' # str | An optional query parameter used to indicate the locale that should be used for formatting.             The value should be a standard language tag. The formatValue query parameter must be set to true, otherwise             culture will not be used for formatting. (optional)
select = 'select_example' # str | Limits the properties returned in the result. (optional)
orderby = 'orderby_example' # str | Specifies the order in which items are returned. The maximum number of expressions is 5. (optional)
top = 56 # int | Limits the number of items returned from a collection. (optional)
skip = 56 # int | Excludes the specified number of items of the queried collection from the result. (optional)
count = true # bool | Indicates whether the total count of items within a collection are returned in the result. (optional)

try:
    api_response = api_instance.get_field_values(repo_id, entry_id, prefer=prefer, format_value=format_value, culture=culture, select=select, orderby=orderby, top=top, skip=skip, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->get_field_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_id** | **str**| The requested repository ID. | 
 **entry_id** | **int**| The requested entry ID. | 
 **prefer** | **str**| An optional OData header. Can be used to set the maximum page size using odata.maxpagesize. | [optional] 
 **format_value** | **bool**| An optional query parameter used to indicate if the field values should be formatted.             The default value is false. | [optional] [default to false]
 **culture** | **str**| An optional query parameter used to indicate the locale that should be used for formatting.             The value should be a standard language tag. The formatValue query parameter must be set to true, otherwise             culture will not be used for formatting. | [optional] 
 **select** | **str**| Limits the properties returned in the result. | [optional] 
 **orderby** | **str**| Specifies the order in which items are returned. The maximum number of expressions is 5. | [optional] 
 **top** | **int**| Limits the number of items returned from a collection. | [optional] 
 **skip** | **int**| Excludes the specified number of items of the queried collection from the result. | [optional] 
 **count** | **bool**| Indicates whether the total count of items within a collection are returned in the result. | [optional] 

### Return type

[**ODataValueOfIListOfFieldValue**](ODataValueOfIListOfFieldValue.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_link_values_from_entry**
> ODataValueOfIListOfWEntryLinkInfo get_link_values_from_entry(repo_id, entry_id, prefer=prefer, select=select, orderby=orderby, top=top, skip=skip, count=count)



- Get the links assigned to an entry. - Provide an entry id, and get a paged listing of links assigned to that entry. - Default page size: 100. Allowed OData query options: Select | Count | OrderBy | Skip | Top | SkipToken | Prefer.

### Example
```python
from __future__ import print_function
import time
import laserfiche_api
from laserfiche_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = laserfiche_api.EntriesApi(laserfiche_api.ApiClient(configuration))
repo_id = 'repo_id_example' # str | The requested repository id.
entry_id = 56 # int | The requested entry id.
prefer = 'prefer_example' # str | An optional odata header. Can be used to set the maximum page size using odata.maxpagesize. (optional)
select = 'select_example' # str | Limits the properties returned in the result. (optional)
orderby = 'orderby_example' # str | Specifies the order in which items are returned. The maximum number of expressions is 5. (optional)
top = 56 # int | Limits the number of items returned from a collection. (optional)
skip = 56 # int | Excludes the specified number of items of the queried collection from the result. (optional)
count = true # bool | Indicates whether the total count of items within a collection are returned in the result. (optional)

try:
    api_response = api_instance.get_link_values_from_entry(repo_id, entry_id, prefer=prefer, select=select, orderby=orderby, top=top, skip=skip, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->get_link_values_from_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_id** | **str**| The requested repository id. | 
 **entry_id** | **int**| The requested entry id. | 
 **prefer** | **str**| An optional odata header. Can be used to set the maximum page size using odata.maxpagesize. | [optional] 
 **select** | **str**| Limits the properties returned in the result. | [optional] 
 **orderby** | **str**| Specifies the order in which items are returned. The maximum number of expressions is 5. | [optional] 
 **top** | **int**| Limits the number of items returned from a collection. | [optional] 
 **skip** | **int**| Excludes the specified number of items of the queried collection from the result. | [optional] 
 **count** | **bool**| Indicates whether the total count of items within a collection are returned in the result. | [optional] 

### Return type

[**ODataValueOfIListOfWEntryLinkInfo**](ODataValueOfIListOfWEntryLinkInfo.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tags_assigned_to_entry**
> ODataValueOfIListOfWTagInfo get_tags_assigned_to_entry(repo_id, entry_id, prefer=prefer, select=select, orderby=orderby, top=top, skip=skip, count=count)



- Get the tags assigned to an entry. - Provide an entry ID, and get a paged listing of tags assigned to that entry. - Default page size: 100. Allowed OData query options: Select | Count | OrderBy | Skip | Top | SkipToken | Prefer.

### Example
```python
from __future__ import print_function
import time
import laserfiche_api
from laserfiche_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = laserfiche_api.EntriesApi(laserfiche_api.ApiClient(configuration))
repo_id = 'repo_id_example' # str | The requested repository ID.
entry_id = 56 # int | The requested entry ID.
prefer = 'prefer_example' # str | An optional OData header. Can be used to set the maximum page size using odata.maxpagesize. (optional)
select = 'select_example' # str | Limits the properties returned in the result. (optional)
orderby = 'orderby_example' # str | Specifies the order in which items are returned. The maximum number of expressions is 5. (optional)
top = 56 # int | Limits the number of items returned from a collection. (optional)
skip = 56 # int | Excludes the specified number of items of the queried collection from the result. (optional)
count = true # bool | Indicates whether the total count of items within a collection are returned in the result. (optional)

try:
    api_response = api_instance.get_tags_assigned_to_entry(repo_id, entry_id, prefer=prefer, select=select, orderby=orderby, top=top, skip=skip, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->get_tags_assigned_to_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_id** | **str**| The requested repository ID. | 
 **entry_id** | **int**| The requested entry ID. | 
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

# **import_document**
> CreateEntryResult import_document(repo_id, parent_entry_id, file_name, electronic_document=electronic_document, request=request, auto_rename=auto_rename)



- Creates a new document in the specified folder. - Optionally sets metadata and electronic document component. - Optional parameter: autoRename (default false). If an entry already exists with the given name, the entry will be automatically renamed. With this route, partial success is possible. The response returns multiple operation (entryCreate operation, setEdoc operation, setLinks operation, etc..) objects, which contain information about any errors that may have occurred during the creation. As long as the entryCreate operation succeeds, the entry will be created, even if all other operations fail.

### Example
```python
from __future__ import print_function
import time
import laserfiche_api
from laserfiche_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = laserfiche_api.EntriesApi(laserfiche_api.ApiClient(configuration))
repo_id = 'repo_id_example' # str | The requested repository ID.
parent_entry_id = 56 # int | The entry ID of the folder that the document will be created in.
file_name = 'file_name_example' # str | The created document's file name.
electronic_document = 'electronic_document_example' # str |  (optional)
request = laserfiche_api.PostEntryWithEdocMetadataRequest() # PostEntryWithEdocMetadataRequest |  (optional)
auto_rename = true # bool | An optional query parameter used to indicate if the new document should be automatically             renamed if an entry already exists with the given name in the folder. The default value is false. (optional)

try:
    api_response = api_instance.import_document(repo_id, parent_entry_id, file_name, electronic_document=electronic_document, request=request, auto_rename=auto_rename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->import_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_id** | **str**| The requested repository ID. | 
 **parent_entry_id** | **int**| The entry ID of the folder that the document will be created in. | 
 **file_name** | **str**| The created document&#x27;s file name. | 
 **electronic_document** | **str**|  | [optional] 
 **request** | [**PostEntryWithEdocMetadataRequest**](.md)|  | [optional] 
 **auto_rename** | **bool**| An optional query parameter used to indicate if the new document should be automatically             renamed if an entry already exists with the given name in the folder. The default value is false. | [optional] 

### Return type

[**CreateEntryResult**](CreateEntryResult.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_or_rename_document**
> Entry move_or_rename_document(repo_id, entry_id, body=body, auto_rename=auto_rename)



- Moves and/or renames an entry. - Move and/or rename an entry by passing in the new parent folder ID or name in the JSON body. - Optional parameter: autoRename (default false). If an entry already exists with the given name, the entry will be automatically renamed.

### Example
```python
from __future__ import print_function
import time
import laserfiche_api
from laserfiche_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = laserfiche_api.EntriesApi(laserfiche_api.ApiClient(configuration))
repo_id = 'repo_id_example' # str | The requested repository ID.
entry_id = 56 # int | The requested entry ID.
body = laserfiche_api.PatchEntryRequest() # PatchEntryRequest | The request containing the folder ID that the entry will be moved to and the new name
            the entry will be renamed to. (optional)
auto_rename = true # bool | An optional query parameter used to indicate if the entry should be automatically             renamed if another entry already exists with the same name in the folder. The default value is false. (optional)

try:
    api_response = api_instance.move_or_rename_document(repo_id, entry_id, body=body, auto_rename=auto_rename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->move_or_rename_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_id** | **str**| The requested repository ID. | 
 **entry_id** | **int**| The requested entry ID. | 
 **body** | [**PatchEntryRequest**](PatchEntryRequest.md)| The request containing the folder ID that the entry will be moved to and the new name
            the entry will be renamed to. | [optional] 
 **auto_rename** | **bool**| An optional query parameter used to indicate if the entry should be automatically             renamed if another entry already exists with the same name in the folder. The default value is false. | [optional] 

### Return type

[**Entry**](Entry.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **write_template_value_to_entry**
> Entry write_template_value_to_entry(repo_id, entry_id, body=body)



- Assign a template to an entry. - Provide an entry id, template name, and a list of template fields to assign to that entry. - Only template values will be modified. Any existing independent fields on the entry will not be modified, nor will they be added if included in the request. The only modification to fields will only occur on templated fields. If the previously assigned template includes common template fields as the newly assigned template, the common field values will not be modified.

### Example
```python
from __future__ import print_function
import time
import laserfiche_api
from laserfiche_api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = laserfiche_api.EntriesApi(laserfiche_api.ApiClient(configuration))
repo_id = 'repo_id_example' # str | The requested repository id.
entry_id = 56 # int | The id of entry that will have its template updated.
body = laserfiche_api.PutTemplateRequest() # PutTemplateRequest | The template and template fields that will be assigned to the entry. (optional)

try:
    api_response = api_instance.write_template_value_to_entry(repo_id, entry_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->write_template_value_to_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_id** | **str**| The requested repository id. | 
 **entry_id** | **int**| The id of entry that will have its template updated. | 
 **body** | [**PutTemplateRequest**](PutTemplateRequest.md)| The template and template fields that will be assigned to the entry. | [optional] 

### Return type

[**Entry**](Entry.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

