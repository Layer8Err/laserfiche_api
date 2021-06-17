# laserfiche-api.AuditReasonsApi

All URIs are relative to *https://api.laserfiche.com/repository*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_audit_reasons**](AuditReasonsApi.md#get_audit_reasons) | **GET** /v1-alpha/Repositories/{repoId}/AuditReasons | Get the audit reasons associated with the authenticated user.

# **get_audit_reasons**
> AuditReasons get_audit_reasons(repo_id)

Get the audit reasons associated with the authenticated user.

- Returns the audit reasons associated with the authenticated user. Inherited audit reasons are included. - Only includes audit reasons associated with available API functionalities, like delete entry and export document. - If the authenticated user does not have the appropriate Laserfiche feature right, the audit reasons associated with that feature right will not be included.

### Example
```python
from __future__ import print_function
import time
import laserfiche-api
from laserfiche-api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = laserfiche-api.AuditReasonsApi(laserfiche-api.ApiClient(configuration))
repo_id = 'repo_id_example' # str | The requested repository ID.

try:
    # Get the audit reasons associated with the authenticated user.
    api_response = api_instance.get_audit_reasons(repo_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditReasonsApi->get_audit_reasons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_id** | **str**| The requested repository ID. | 

### Return type

[**AuditReasons**](AuditReasons.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

