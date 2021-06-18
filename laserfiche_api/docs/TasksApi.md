# laserfiche-api.TasksApi

All URIs are relative to *https://api.laserfiche.com/repository*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_operation**](TasksApi.md#cancel_operation) | **DELETE** /v1-alpha/Repositories/{repoId}/Tasks/{operationToken} | 
[**get_operation_status_and_progress**](TasksApi.md#get_operation_status_and_progress) | **GET** /v1-alpha/Repositories/{repoId}/Tasks/{operationToken} | 

# **cancel_operation**
> cancel_operation(repo_id, operation_token)



- Cancels an operation. - Provide an operationToken to cancel the operation, if possible. Should be used if an operation was created in error, or is no longer necessary. - Rollbacks must be done manually. For example, if a copy operation is started and is halfway complete when canceled, the client application is responsible for cleaning up the files that were successfully copied before the operation was canceled.

### Example
```python
from __future__ import print_function
import time
import laserfiche-api
from laserfiche-api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = laserfiche-api.TasksApi(laserfiche-api.ApiClient(configuration))
repo_id = 'repo_id_example' # str | The requested repository ID.
operation_token = 'operation_token_example' # str | The operation token 

try:
    api_instance.cancel_operation(repo_id, operation_token)
except ApiException as e:
    print("Exception when calling TasksApi->cancel_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_id** | **str**| The requested repository ID. | 
 **operation_token** | **str**| The operation token  | 

### Return type

void (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_operation_status_and_progress**
> OperationProgress get_operation_status_and_progress(repo_id, operation_token)



- Returns the status of an operation. - Provide an operationToken (returned in other asynchronous routes) to get the operation status, progress, and any errors that may have occurred. When the operation is completed, the Location header can be inspected as a link to the modified resources (if relevant). - OperationStatus can be one of the following values: NotStarted, InProgress, Completed, or Failed.

### Example
```python
from __future__ import print_function
import time
import laserfiche-api
from laserfiche-api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = laserfiche-api.TasksApi(laserfiche-api.ApiClient(configuration))
repo_id = 'repo_id_example' # str | The requested repository ID.
operation_token = 'operation_token_example' # str | The operation token.

try:
    api_response = api_instance.get_operation_status_and_progress(repo_id, operation_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_operation_status_and_progress: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_id** | **str**| The requested repository ID. | 
 **operation_token** | **str**| The operation token. | 

### Return type

[**OperationProgress**](OperationProgress.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

