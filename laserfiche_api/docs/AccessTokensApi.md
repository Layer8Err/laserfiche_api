# laserfiche-api.AccessTokensApi

All URIs are relative to *https://api.laserfiche.com/repository*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_access_token**](AccessTokensApi.md#create_access_token) | **POST** /v1-alpha/Repositories/{repoId}/AccessTokens/Create | 
[**invalidate_access_token**](AccessTokensApi.md#invalidate_access_token) | **POST** /v1-alpha/Repositories/{repoId}/AccessTokens/Invalidate | 
[**refresh_access_token**](AccessTokensApi.md#refresh_access_token) | **POST** /v1-alpha/Repositories/{repoId}/AccessTokens/Refresh | 

# **create_access_token**
> SessionKeyInfo create_access_token(repo_id, body=body, create_cookie=create_cookie, customer_id=customer_id)



- Creates an access token for use with the Laserfiche API. - Provides credentials and uses the access token returned with subsequent API calls as a means of authorization. - Adding createCookie=true as a query parameter results a response that includes a Set-Cookie header containing an authToken value. The default value for createCookie is false.

### Example
```python
from __future__ import print_function
import time
import laserfiche-api
from laserfiche-api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = laserfiche-api.AccessTokensApi(laserfiche-api.ApiClient(configuration))
repo_id = 'repo_id_example' # str | The requested repository ID.
body = laserfiche-api.CreateConnectionRequest() # CreateConnectionRequest | The username and password used to create the session connection. (optional)
create_cookie = true # bool | An optional query parameter used to indicate whether a Set-Cookie header containing             the authToken is returned in the response. (optional)
customer_id = 'customer_id_example' # str | The Laserfiche Cloud account ID to use when using username and password to create a session connection. (optional)

try:
    api_response = api_instance.create_access_token(repo_id, body=body, create_cookie=create_cookie, customer_id=customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessTokensApi->create_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_id** | **str**| The requested repository ID. | 
 **body** | [**CreateConnectionRequest**](CreateConnectionRequest.md)| The username and password used to create the session connection. | [optional] 
 **create_cookie** | **bool**| An optional query parameter used to indicate whether a Set-Cookie header containing             the authToken is returned in the response. | [optional] 
 **customer_id** | **str**| The Laserfiche Cloud account ID to use when using username and password to create a session connection. | [optional] 

### Return type

[**SessionKeyInfo**](SessionKeyInfo.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invalidate_access_token**
> ODataValueOfBoolean invalidate_access_token(repo_id)



- Invalidates the access token. - Acts as a \"logout\" operation, and invalidates the session associated with the provided access token. This method should be used when the client wants to clean up the current session.

### Example
```python
from __future__ import print_function
import time
import laserfiche-api
from laserfiche-api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = laserfiche-api.AccessTokensApi(laserfiche-api.ApiClient(configuration))
repo_id = 'repo_id_example' # str | The requested repository ID.

try:
    api_response = api_instance.invalidate_access_token(repo_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessTokensApi->invalidate_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_id** | **str**| The requested repository ID. | 

### Return type

[**ODataValueOfBoolean**](ODataValueOfBoolean.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_access_token**
> ODataValueOfDateTime refresh_access_token(repo_id, keep_alive=keep_alive)



- Refreshes the session associated with the access token. - When a client application wants to keep an idle session alive, this route should be used to refresh the expiration timer associated with the access token. - Optionally, a Keep-Alive header can be included with the request to specify how long the session should be kept alive when idle. The maximum timeout value is 1 hour.

### Example
```python
from __future__ import print_function
import time
import laserfiche-api
from laserfiche-api.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = laserfiche-api.AccessTokensApi(laserfiche-api.ApiClient(configuration))
repo_id = 'repo_id_example' # str | The requested repository ID.
keep_alive = 'keep_alive_example' # str | An optional Keep-Alive header with timeout value can be used to specify how long the             session should be kept alive when idle. The maximum timeout value is 1 hour. (optional)

try:
    api_response = api_instance.refresh_access_token(repo_id, keep_alive=keep_alive)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessTokensApi->refresh_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_id** | **str**| The requested repository ID. | 
 **keep_alive** | **str**| An optional Keep-Alive header with timeout value can be used to specify how long the             session should be kept alive when idle. The maximum timeout value is 1 hour. | [optional] 

### Return type

[**ODataValueOfDateTime**](ODataValueOfDateTime.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

