# swagger_client.APIV2WidgetsApi

All URIs are relative to *https://api.fateslist.xyz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_widget**](APIV2WidgetsApi.md#get_widget) | **GET** /api/v2/widgets/{target_id} | Get Widget

# **get_widget**
> object get_widget(target_id, target_type, format, bgcolor=bgcolor, textcolor=textcolor, no_cache=no_cache, cd=cd, desc_length=desc_length)

Get Widget

    Returns a widget      **For colors (bgcolor, textcolor), use H for html hex instead of #. Example: H123456**      - cd - A custom description you wish to set for the widget      - desc_length - Set this to anything less than 0 to try and use full length (may 500), otherwise this sets the length of description to use.      **Using 0 for desc_length will disable description**      no_cache - If this is set to true, cache will not be used but will still be updated. If using cd, set this option to true and cache the image yourself     Note that no_cache is slow and may lead to ratelimits and/or your got being banned if used excessively     

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIV2WidgetsApi()
target_id = 56 # int | 
target_type = swagger_client.ReviewType() # ReviewType | 
format = swagger_client.WidgetFormat() # WidgetFormat | 
bgcolor = 'black' # str |  (optional) (default to black)
textcolor = 'white' # str |  (optional) (default to white)
no_cache = false # bool |  (optional) (default to false)
cd = 'cd_example' # str |  (optional)
desc_length = 25 # int |  (optional) (default to 25)

try:
    # Get Widget
    api_response = api_instance.get_widget(target_id, target_type, format, bgcolor=bgcolor, textcolor=textcolor, no_cache=no_cache, cd=cd, desc_length=desc_length)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2WidgetsApi->get_widget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_id** | **int**|  | 
 **target_type** | [**ReviewType**](.md)|  | 
 **format** | [**WidgetFormat**](.md)|  | 
 **bgcolor** | **str**|  | [optional] [default to black]
 **textcolor** | **str**|  | [optional] [default to white]
 **no_cache** | **bool**|  | [optional] [default to false]
 **cd** | **str**|  | [optional] 
 **desc_length** | **int**|  | [optional] [default to 25]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

