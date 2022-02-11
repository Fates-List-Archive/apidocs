# swagger_client.APIV2BotsApi

All URIs are relative to *https://api.fateslist.xyz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bot_exists**](APIV2BotsApi.md#bot_exists) | **HEAD** /api/v2/bots/{bot_id} | Bot Exists
[**fetch_bot**](APIV2BotsApi.md#fetch_bot) | **GET** /api/v2/bots/{bot_id} | Fetch Bot
[**fetch_random_bot**](APIV2BotsApi.md#fetch_random_bot) | **GET** /api/v2/bots/{bot_id}/random | Fetch Random Bot
[**get_bot_invite**](APIV2BotsApi.md#get_bot_invite) | **GET** /api/v2/bots/{bot_id}/_sunbeam/invite | Get Bot Invite
[**get_bot_page**](APIV2BotsApi.md#get_bot_page) | **GET** /api/v2/bots/{bot_id}/_sunbeam | Get Bot Page
[**get_bot_settings**](APIV2BotsApi.md#get_bot_settings) | **GET** /api/v2/bots/{bot_id}/_sunbeam/settings | Get Bot Settings
[**get_bot_widget**](APIV2BotsApi.md#get_bot_widget) | **GET** /api/v2/bots/{bot_id}/widget | Bot Widget
[**get_bot_ws_events**](APIV2BotsApi.md#get_bot_ws_events) | **GET** /api/v2/bots/{bot_id}/ws_events | Get Bot Ws Events
[**get_votes_per_month**](APIV2BotsApi.md#get_votes_per_month) | **GET** /api/v2/bots/{bot_id}/vpm | Get Votes Per Month
[**regenerate_bot_token**](APIV2BotsApi.md#regenerate_bot_token) | **PATCH** /api/v2/bots/{bot_id}/token | Regenerate Bot Token
[**set_bot_stats**](APIV2BotsApi.md#set_bot_stats) | **POST** /api/v2/bots/{bot_id}/stats | Set Bot Stats

# **bot_exists**
> object bot_exists(bot_id)

Bot Exists

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIV2BotsApi()
bot_id = 56 # int | 

try:
    # Bot Exists
    api_response = api_instance.bot_exists(bot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2BotsApi->bot_exists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_bot**
> Bot fetch_bot(bot_id, compact=compact, no_cache=no_cache)

Fetch Bot

Fetches bot information given a bot ID. If not found, 404 will be returned.   This endpoint handles both bot IDs and client IDs  - **compact** (default `true`) -> long_description_type, long_description, css and keep_banner_decor will be not be given  - **no_cache** (default: `false`) -> cached responses will not be served (may be temp disabled in the case of a DDOS or temp disabled for specific  bots as required). **Uncached requests may take up to 100-200 times longer or possibly more**  **Important note: the first owner may or may not be the main owner.  Use the `main` key instead of object order**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIV2BotsApi()
bot_id = 56 # int | 
compact = true # bool |  (optional) (default to true)
no_cache = false # bool |  (optional) (default to false)

try:
    # Fetch Bot
    api_response = api_instance.fetch_bot(bot_id, compact=compact, no_cache=no_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2BotsApi->fetch_bot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **int**|  | 
 **compact** | **bool**|  | [optional] [default to true]
 **no_cache** | **bool**|  | [optional] [default to false]

### Return type

[**Bot**](Bot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_random_bot**
> BotRandom fetch_random_bot(bot_id, lang=lang)

Fetch Random Bot

Fetch a random bot. Bot ID should be the root bot 0   Example: ```py import requests  def random_bot():     res = requests.get(\"https://fateslist.xyz/api/bots/0/random\")     json = res.json()     if not json.get(\"done\", True):         # Handle an error in the api         ...     return res, json ```

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIV2BotsApi()
bot_id = 56 # int | 
lang = 'default' # str |  (optional) (default to default)

try:
    # Fetch Random Bot
    api_response = api_instance.fetch_random_bot(bot_id, lang=lang)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2BotsApi->fetch_random_bot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **int**|  | 
 **lang** | **str**|  | [optional] [default to default]

### Return type

[**BotRandom**](BotRandom.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bot_invite**
> object get_bot_invite(bot_id, user_id=user_id)

Get Bot Invite

Internally used by sunbeam for inviting users.  While the data you get from this API is sanitized because it is actually rendered for users, it is *not* recommended to rely or use this API outside of internal use cases. Data is unstructured and will constantly change. **This API is not backwards compatible whatsoever**  Additionally, this API *will* trigger a WS Invite Event.  To protect against scraping, this endpoint requires a proper Frostpaw header to be set.  This API will also be heavily monitored. If we find you attempting to abuse this API endpoint or doing anything out of the ordinary with it, you may be IP or user banned. Calling it once or twice is OK but automating it is not. Use the Get Bot API instead for automation.  **This API is only documented because it's in our FastAPI backend and to be complete**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIV2BotsApi()
bot_id = 56 # int | 
user_id = 0 # int |  (optional) (default to 0)

try:
    # Get Bot Invite
    api_response = api_instance.get_bot_invite(bot_id, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2BotsApi->get_bot_invite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **int**|  | 
 **user_id** | **int**|  | [optional] [default to 0]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bot_page**
> object get_bot_page(bot_id, lang=lang)

Get Bot Page

Internally used by sunbeam to render bot pages.  While the data you get from this API is sanitized because it is actually rendered for users, it is *not* recommended to rely or use this API outside of internal use cases. Data is unstructured and will constantly change. **This API is not backwards compatible whatsoever**  Additionally, this API *will* trigger a WS View Event.  To protect against scraping and browsers, this endpoint requires a  proper Frostpaw header to be set.  This API will also be heavily monitored. If we find you attempting to abuse this API endpoint or doing anything out of the ordinary with it, you may be IP or user banned. Calling it once or twice is OK but automating it is not. Use the Get Bot API instead for automation.  **This API is only documented because it's in our FastAPI backend and to be complete**  Response models will *never* be documented as it changes very frequently

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIV2BotsApi()
bot_id = 56 # int | 
lang = 'en' # str |  (optional) (default to en)

try:
    # Get Bot Page
    api_response = api_instance.get_bot_page(bot_id, lang=lang)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2BotsApi->get_bot_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **int**|  | 
 **lang** | **str**|  | [optional] [default to en]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bot_settings**
> object get_bot_settings(bot_id, user_id)

Get Bot Settings

Internally used by sunbeam for bot settings.  While the data you get from this API is sanitized because it is actually rendered for users, it is *not* recommended to rely or use this API outside of internal use cases. Data is unstructured and will constantly change. **This API is not backwards compatible whatsoever**  To protect against scraping, this endpoint requires a proper Frostpaw header to be set.  This API will also be heavily monitored. If we find you attempting to abuse this API endpoint or doing anything out of the ordinary with it, you may be IP or user banned. Calling it once or twice is OK but automating it is not. Use the Get Bot API instead for automation.  **This API is only documented because it's in our FastAPI backend and to be complete**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: User
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.APIV2BotsApi(swagger_client.ApiClient(configuration))
bot_id = 56 # int | 
user_id = 56 # int | 

try:
    # Get Bot Settings
    api_response = api_instance.get_bot_settings(bot_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2BotsApi->get_bot_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **int**|  | 
 **user_id** | **int**|  | 

### Return type

**object**

### Authorization

[User](../README.md#User)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bot_widget**
> object get_bot_widget(bot_id, format, bgcolor=bgcolor, textcolor=textcolor)

Bot Widget

Returns a bots widget. This has been superceded by Get Widget and merely redirects to it now

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIV2BotsApi()
bot_id = 56 # int | 
format = swagger_client.WidgetFormat() # WidgetFormat | 
bgcolor = swagger_client.Bgcolor1() # Bgcolor1 |  (optional)
textcolor = swagger_client.Textcolor1() # Textcolor1 |  (optional)

try:
    # Bot Widget
    api_response = api_instance.get_bot_widget(bot_id, format, bgcolor=bgcolor, textcolor=textcolor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2BotsApi->get_bot_widget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **int**|  | 
 **format** | [**WidgetFormat**](.md)|  | 
 **bgcolor** | [**Bgcolor1**](.md)|  | [optional] 
 **textcolor** | [**Textcolor1**](.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bot_ws_events**
> object get_bot_ws_events(bot_id)

Get Bot Ws Events

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
api_instance = swagger_client.APIV2BotsApi(swagger_client.ApiClient(configuration))
bot_id = 56 # int | 

try:
    # Get Bot Ws Events
    api_response = api_instance.get_bot_ws_events(bot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2BotsApi->get_bot_ws_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **int**|  | 

### Return type

**object**

### Authorization

[Bot](../README.md#Bot)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_votes_per_month**
> object get_votes_per_month(bot_id)

Get Votes Per Month

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIV2BotsApi()
bot_id = 56 # int | 

try:
    # Get Votes Per Month
    api_response = api_instance.get_votes_per_month(bot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2BotsApi->get_votes_per_month: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **regenerate_bot_token**
> APIResponse regenerate_bot_token(bot_id)

Regenerate Bot Token

Regenerates a bot token. Use this if it is compromised   Example:  ```py import requests  def regen_token(bot_id, token):     res = requests.patch(f\"https://fateslist.xyz/api/v2/bots/{bot_id}/token\", headers={\"Authorization\": f\"Bot {token}\"})     json = res.json()     if not json[\"done\"]:         # Handle failures         ...     return res, json ```

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
api_instance = swagger_client.APIV2BotsApi(swagger_client.ApiClient(configuration))
bot_id = 56 # int | 

try:
    # Regenerate Bot Token
    api_response = api_instance.regenerate_bot_token(bot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2BotsApi->regenerate_bot_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **int**|  | 

### Return type

[**APIResponse**](APIResponse.md)

### Authorization

[Bot](../README.md#Bot)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_bot_stats**
> APIResponse set_bot_stats(body, bot_id)

Set Bot Stats

This endpoint allows you to set the guild + shard counts for your bot   Example: ```py # This will use aiohttp and not requests as this is likely to used by discord.py bots import aiohttp   # On dpy, guild_count is usually the below guild_count = len(client.guilds)  # If you are using sharding shard_count = len(client.shards) shards = client.shards.keys()  # Optional: User count (this is not accurate for larger bots) user_count = len(client.users)   async def set_stats(bot_id, token, guild_count, shard_count = None, shards = None, user_count = None):     json = {\"guild_count\": guild_count, \"shard_count\": shard_count, \"shards\": shards, \"user_count\": user_count}      async with aiohttp.ClientSession() as sess:         async with sess.post(f\"https://fateslist.xyz/api/bots/{bot_id}/stats\", headers={\"Authorization\": f\"Bot {token}\"}, json=json) as res:             json = await res.json()             if not json[\"done\"]:                 # Handle or log this error                 ... ```

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
api_instance = swagger_client.APIV2BotsApi(swagger_client.ApiClient(configuration))
body = swagger_client.BotStats() # BotStats | 
bot_id = 56 # int | 

try:
    # Set Bot Stats
    api_response = api_instance.set_bot_stats(body, bot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2BotsApi->set_bot_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BotStats**](BotStats.md)|  | 
 **bot_id** | **int**|  | 

### Return type

[**APIResponse**](APIResponse.md)

### Authorization

[Bot](../README.md#Bot)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

