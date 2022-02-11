# swagger_client.APIV2CustomResourcesApi

All URIs are relative to *https://api.fateslist.xyz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_resources**](APIV2CustomResourcesApi.md#add_resources) | **POST** /api/v2/resources/{target_id} | Add Resources
[**delete_resources**](APIV2CustomResourcesApi.md#delete_resources) | **DELETE** /api/v2/resources/{target_id} | Delete Resources
[**get_resources**](APIV2CustomResourcesApi.md#get_resources) | **GET** /api/v2/resources/{target_id} | Get Resources

# **add_resources**
> object add_resources(body, target_type, target_id)

Add Resources

Adds a resource to your bot/guild. If it already exists, this will delete and readd the resource so it can be used to edit already existing resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bot
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: Server
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.APIV2CustomResourcesApi(swagger_client.ApiClient(configuration))
body = swagger_client.BotResources() # BotResources | 
target_type = swagger_client.ReviewType() # ReviewType | 
target_id = 56 # int | 

try:
    # Add Resources
    api_response = api_instance.add_resources(body, target_type, target_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2CustomResourcesApi->add_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BotResources**](BotResources.md)|  | 
 **target_type** | [**ReviewType**](.md)|  | 
 **target_id** | **int**|  | 

### Return type

**object**

### Authorization

[Bot](../README.md#Bot), [Server](../README.md#Server)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_resources**
> APIResponse delete_resources(body, target_type, target_id)

Delete Resources

If ids/names is provided, all resources with said ids/names will be deleted (this can be used together).  If nuke is provided, then all resources will deleted. Ids/names and nuke cannot be used at the same time

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bot
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: Server
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.APIV2CustomResourcesApi(swagger_client.ApiClient(configuration))
body = swagger_client.BotResourceDelete() # BotResourceDelete | 
target_type = swagger_client.ReviewType() # ReviewType | 
target_id = 56 # int | 

try:
    # Delete Resources
    api_response = api_instance.delete_resources(body, target_type, target_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2CustomResourcesApi->delete_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BotResourceDelete**](BotResourceDelete.md)|  | 
 **target_type** | [**ReviewType**](.md)|  | 
 **target_id** | **int**|  | 

### Return type

[**APIResponse**](APIResponse.md)

### Authorization

[Bot](../README.md#Bot), [Server](../README.md#Server)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resources**
> list[object] get_resources(target_id, target_type, filter=filter, lang=lang)

Get Resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIV2CustomResourcesApi()
target_id = 56 # int | 
target_type = swagger_client.ReviewType() # ReviewType | 
filter = 'filter_example' # str |  (optional)
lang = 'default' # str |  (optional) (default to default)

try:
    # Get Resources
    api_response = api_instance.get_resources(target_id, target_type, filter=filter, lang=lang)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2CustomResourcesApi->get_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_id** | **int**|  | 
 **target_type** | [**ReviewType**](.md)|  | 
 **filter** | **str**|  | [optional] 
 **lang** | **str**|  | [optional] [default to default]

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

