# swagger_client.APIV2CommandsApi

All URIs are relative to *https://api.fateslist.xyz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_commands**](APIV2CommandsApi.md#add_commands) | **POST** /api/v2/bots/{bot_id}/commands | Add Commands
[**delete_commands**](APIV2CommandsApi.md#delete_commands) | **DELETE** /api/v2/bots/{bot_id}/commands | Delete Commands
[**get_commands**](APIV2CommandsApi.md#get_commands) | **GET** /api/v2/bots/{bot_id}/commands | Get Commands

# **add_commands**
> object add_commands(body, bot_id)

Add Commands

Adds a command to your bot. If it already exists, this will delete and readd the command so it can be used to edit already existing commands

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
api_instance = swagger_client.APIV2CommandsApi(swagger_client.ApiClient(configuration))
body = swagger_client.BotCommands() # BotCommands | 
bot_id = 56 # int | 

try:
    # Add Commands
    api_response = api_instance.add_commands(body, bot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2CommandsApi->add_commands: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BotCommands**](BotCommands.md)|  | 
 **bot_id** | **int**|  | 

### Return type

**object**

### Authorization

[Bot](../README.md#Bot)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_commands**
> APIResponse delete_commands(body, bot_id)

Delete Commands

If ids/names is provided, all commands with said ids/names will be deleted (this can be used together).  If nuke is provided, then all commands will deleted. Ids/names and nuke cannot be used at the same time

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
api_instance = swagger_client.APIV2CommandsApi(swagger_client.ApiClient(configuration))
body = swagger_client.BotCommandDelete() # BotCommandDelete | 
bot_id = 56 # int | 

try:
    # Delete Commands
    api_response = api_instance.delete_commands(body, bot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2CommandsApi->delete_commands: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BotCommandDelete**](BotCommandDelete.md)|  | 
 **bot_id** | **int**|  | 

### Return type

[**APIResponse**](APIResponse.md)

### Authorization

[Bot](../README.md#Bot)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_commands**
> BotCommandsGet get_commands(bot_id, filter=filter, lang=lang)

Get Commands

Gets the command list of a bot  **The `get_bot_commands` function used by this API is internally called by the Get Bot Page API and as such this API endpoint itself is not used by Sunbeam for those curious**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIV2CommandsApi()
bot_id = 56 # int | 
filter = 'filter_example' # str |  (optional)
lang = 'default' # str |  (optional) (default to default)

try:
    # Get Commands
    api_response = api_instance.get_commands(bot_id, filter=filter, lang=lang)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2CommandsApi->get_commands: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **int**|  | 
 **filter** | **str**|  | [optional] 
 **lang** | **str**|  | [optional] [default to default]

### Return type

[**BotCommandsGet**](BotCommandsGet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

