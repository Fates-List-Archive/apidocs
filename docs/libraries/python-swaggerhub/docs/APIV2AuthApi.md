# swagger_client.APIV2AuthApi

All URIs are relative to *https://api.fateslist.xyz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_login_link**](APIV2AuthApi.md#get_login_link) | **POST** /api/v2/oauth | Get Login Link
[**login_user**](APIV2AuthApi.md#login_user) | **POST** /api/v2/users | Login User
[**logout_sunbeam**](APIV2AuthApi.md#logout_sunbeam) | **POST** /api/v2/logout/_sunbeam | Logout Sunbeam

# **get_login_link**
> OAuthInfo get_login_link()

Get Login Link

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIV2AuthApi()

try:
    # Get Login Link
    api_response = api_instance.get_login_link()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2AuthApi->get_login_link: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OAuthInfo**](OAuthInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_user**
> LoginResponse login_user(body)

Login User

Returns a cookie containing login information

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIV2AuthApi()
body = swagger_client.Login() # Login | 

try:
    # Login User
    api_response = api_instance.login_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2AuthApi->login_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Login**](Login.md)|  | 

### Return type

[**LoginResponse**](LoginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout_sunbeam**
> object logout_sunbeam()

Logout Sunbeam

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIV2AuthApi()

try:
    # Logout Sunbeam
    api_response = api_instance.logout_sunbeam()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2AuthApi->logout_sunbeam: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

