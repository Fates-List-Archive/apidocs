# swagger_client.APIV2PromotionsApi

All URIs are relative to *https://api.fateslist.xyz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_promotion**](APIV2PromotionsApi.md#delete_promotion) | **DELETE** /api/v2/bots/{bot_id}/promotions/{id} | Delete Promotion
[**edit_promotion**](APIV2PromotionsApi.md#edit_promotion) | **PATCH** /api/v2/bots/{bot_id}/promotions/{id} | Edit Promotion
[**get_promotion**](APIV2PromotionsApi.md#get_promotion) | **GET** /api/v2/bots/{bot_id}/promotions | Get Promotion
[**new_promotion**](APIV2PromotionsApi.md#new_promotion) | **POST** /api/v2/bots/{bot_id}/promotions | New Promotion

# **delete_promotion**
> APIResponse delete_promotion(bot_id, id)

Delete Promotion

Deletes a bots promotion

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

# create an instance of the API class
api_instance = swagger_client.APIV2PromotionsApi(swagger_client.ApiClient(configuration))
bot_id = 56 # int | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Delete Promotion
    api_response = api_instance.delete_promotion(bot_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2PromotionsApi->delete_promotion: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **int**|  | 
 **id** | [**str**](.md)|  | 

### Return type

[**APIResponse**](APIResponse.md)

### Authorization

[Bot](../README.md#Bot)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_promotion**
> APIResponse edit_promotion(body, bot_id, id)

Edit Promotion

Edits an promotion for a bot given its promotion ID.

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

# create an instance of the API class
api_instance = swagger_client.APIV2PromotionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.BotPromotion() # BotPromotion | 
bot_id = 56 # int | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Edit Promotion
    api_response = api_instance.edit_promotion(body, bot_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2PromotionsApi->edit_promotion: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BotPromotion**](BotPromotion.md)|  | 
 **bot_id** | **int**|  | 
 **id** | [**str**](.md)|  | 

### Return type

[**APIResponse**](APIResponse.md)

### Authorization

[Bot](../README.md#Bot)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_promotion**
> BotPromotions get_promotion(bot_id)

Get Promotion

Returns all the promotions for a bot on Fates List

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIV2PromotionsApi()
bot_id = 56 # int | 

try:
    # Get Promotion
    api_response = api_instance.get_promotion(bot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2PromotionsApi->get_promotion: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **int**|  | 

### Return type

[**BotPromotions**](BotPromotions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **new_promotion**
> APIResponse new_promotion(body, bot_id)

New Promotion

Creates a promotion for a bot. Type can be 1 for announcement, 2 for promotion or 3 for generic

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

# create an instance of the API class
api_instance = swagger_client.APIV2PromotionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.BotPromotion() # BotPromotion | 
bot_id = 56 # int | 

try:
    # New Promotion
    api_response = api_instance.new_promotion(body, bot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2PromotionsApi->new_promotion: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BotPromotion**](BotPromotion.md)|  | 
 **bot_id** | **int**|  | 

### Return type

[**APIResponse**](APIResponse.md)

### Authorization

[Bot](../README.md#Bot)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

