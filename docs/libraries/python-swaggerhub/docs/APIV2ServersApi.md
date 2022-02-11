# swagger_client.APIV2ServersApi

All URIs are relative to *https://api.fateslist.xyz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_random_server**](APIV2ServersApi.md#fetch_random_server) | **GET** /api/v2/guilds/{guild_id}/random | Fetch Random Server
[**fetch_server**](APIV2ServersApi.md#fetch_server) | **GET** /api/v2/guilds/{guild_id} | Fetch Server
[**get_server_invite**](APIV2ServersApi.md#get_server_invite) | **GET** /api/v2/guilds/{guild_id}/_sunbeam/invite | Get Server Invite
[**get_server_page**](APIV2ServersApi.md#get_server_page) | **GET** /api/v2/guilds/{guild_id}/_sunbeam | Get Server Page
[**get_server_widget**](APIV2ServersApi.md#get_server_widget) | **GET** /api/v2/guilds/{guild_id}/widget | Server Widget
[**get_server_ws_events**](APIV2ServersApi.md#get_server_ws_events) | **GET** /api/v2/guilds/{guild_id}/ws_events | Get Server Ws Events
[**regenerate_server_token**](APIV2ServersApi.md#regenerate_server_token) | **PATCH** /api/v2/guilds/{guild_id}/token | Regenerate Server Token
[**server_exists**](APIV2ServersApi.md#server_exists) | **HEAD** /api/v2/guilds/{guild_id} | Server Exists

# **fetch_random_server**
> GuildRandom fetch_random_server(guild_id, lang=lang)

Fetch Random Server

Fetch a random server. Server ID should be the recursive/root server 0.   Example: ```py import requests  def random_server():     res = requests.get(\"https://fateslist.xyz/api/guilds/0/random\")     json = res.json()     if not json.get(\"done\", True):         # Handle an error in the api         ...     return res, json ```

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIV2ServersApi()
guild_id = 56 # int | 
lang = 'default' # str |  (optional) (default to default)

try:
    # Fetch Random Server
    api_response = api_instance.fetch_random_server(guild_id, lang=lang)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2ServersApi->fetch_random_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **int**|  | 
 **lang** | **str**|  | [optional] [default to default]

### Return type

[**GuildRandom**](GuildRandom.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_server**
> Guild fetch_server(guild_id, compact=compact, no_cache=no_cache, sensitive=sensitive)

Fetch Server

Fetches server information given a server/guild ID. If not found, 404 will be returned.  Setting compact to true (default) -> description, long_description, long_description_type, keep_banner_decor and css will be null  No cache means cached responses will not be served (may be temp disabled in the case of a DDOS or temp disabled for specific servers as required)  Setting sensitive to true will expose sensitive info like invite channel, user whitelist/blacklist etc

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIV2ServersApi()
guild_id = 56 # int | 
compact = true # bool |  (optional) (default to true)
no_cache = false # bool |  (optional) (default to false)
sensitive = false # bool |  (optional) (default to false)

try:
    # Fetch Server
    api_response = api_instance.fetch_server(guild_id, compact=compact, no_cache=no_cache, sensitive=sensitive)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2ServersApi->fetch_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **int**|  | 
 **compact** | **bool**|  | [optional] [default to true]
 **no_cache** | **bool**|  | [optional] [default to false]
 **sensitive** | **bool**|  | [optional] [default to false]

### Return type

[**Guild**](Guild.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_invite**
> object get_server_invite(guild_id)

Get Server Invite

Internally used by sunbeam for inviting users.  **Usage of this API without explicit permission from said servers is not allowed**  Additionally, this API *will* trigger a WS Invite Event.  To protect against scraping, this endpoint requires a proper Frostpaw header to be set.  This API will also be heavily monitored. If we find you attempting to abuse this API endpoint or doing anything out of the ordinary with it, you may be IP or user banned. Calling it once or twice is OK but automating it is not. Use the Get Bot API instead for automation.  **This API is only documented because it's in our FastAPI backend and to be complete**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIV2ServersApi()
guild_id = 56 # int | 

try:
    # Get Server Invite
    api_response = api_instance.get_server_invite(guild_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2ServersApi->get_server_invite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_page**
> object get_server_page(guild_id, lang=lang)

Get Server Page

Internally used by sunbeam for server page getting.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIV2ServersApi()
guild_id = 56 # int | 
lang = 'en' # str |  (optional) (default to en)

try:
    # Get Server Page
    api_response = api_instance.get_server_page(guild_id, lang=lang)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2ServersApi->get_server_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **int**|  | 
 **lang** | **str**|  | [optional] [default to en]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_widget**
> object get_server_widget(guild_id, format, bgcolor=bgcolor, textcolor=textcolor)

Server Widget

Returns a widget. Superceded by Get Widget API

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIV2ServersApi()
guild_id = 56 # int | 
format = swagger_client.WidgetFormat() # WidgetFormat | 
bgcolor = swagger_client.Bgcolor() # Bgcolor |  (optional)
textcolor = swagger_client.Textcolor() # Textcolor |  (optional)

try:
    # Server Widget
    api_response = api_instance.get_server_widget(guild_id, format, bgcolor=bgcolor, textcolor=textcolor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2ServersApi->get_server_widget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **int**|  | 
 **format** | [**WidgetFormat**](.md)|  | 
 **bgcolor** | [**Bgcolor**](.md)|  | [optional] 
 **textcolor** | [**Textcolor**](.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_ws_events**
> object get_server_ws_events(guild_id)

Get Server Ws Events

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Server
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.APIV2ServersApi(swagger_client.ApiClient(configuration))
guild_id = 56 # int | 

try:
    # Get Server Ws Events
    api_response = api_instance.get_server_ws_events(guild_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2ServersApi->get_server_ws_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **int**|  | 

### Return type

**object**

### Authorization

[Server](../README.md#Server)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **regenerate_server_token**
> APIResponse regenerate_server_token(guild_id)

Regenerate Server Token

Regenerates a server token. Use this if it is compromised and you don't have time to use slash commands   Example:  ```py import requests  def regen_token(guild_id, token):     res = requests.patch(f\"https://fateslist.xyz/api/v2/guilds/{guild_id}/token\", headers={\"Authorization\": f\"Server {token}\"})     json = res.json()     if not json[\"done\"]:         # Handle failures         ...     return res, json ```

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Server
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.APIV2ServersApi(swagger_client.ApiClient(configuration))
guild_id = 56 # int | 

try:
    # Regenerate Server Token
    api_response = api_instance.regenerate_server_token(guild_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2ServersApi->regenerate_server_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **int**|  | 

### Return type

[**APIResponse**](APIResponse.md)

### Authorization

[Server](../README.md#Server)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **server_exists**
> object server_exists(guild_id)

Server Exists

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIV2ServersApi()
guild_id = 56 # int | 

try:
    # Server Exists
    api_response = api_instance.server_exists(guild_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2ServersApi->server_exists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

