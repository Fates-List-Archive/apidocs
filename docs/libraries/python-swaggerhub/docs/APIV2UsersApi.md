# swagger_client.APIV2UsersApi

All URIs are relative to *https://api.fateslist.xyz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_bot**](APIV2UsersApi.md#add_bot) | **PUT** /api/v2/users/{user_id}/bots/{bot_id} | Add Bot
[**appeal_bot**](APIV2UsersApi.md#appeal_bot) | **POST** /api/v2/users/{user_id}/bots/{bot_id}/appeal | Appeal Bot
[**bot_backup**](APIV2UsersApi.md#bot_backup) | **GET** /api/v2/users/{user_id}/bots/{bot_id}/backup | Bot Backup
[**certify_bot_request**](APIV2UsersApi.md#certify_bot_request) | **POST** /api/v2/users/{user_id}/bots/{bot_id}/certification | Certify Bot Request
[**create_bot_pack**](APIV2UsersApi.md#create_bot_pack) | **POST** /api/v2/users/{user_id}/packs | Create Bot Pack
[**delete_bot**](APIV2UsersApi.md#delete_bot) | **DELETE** /api/v2/users/{user_id}/bots/{bot_id} | Delete Bot
[**delete_bot_pack**](APIV2UsersApi.md#delete_bot_pack) | **DELETE** /api/v2/users/{user_id}/packs/{pack_id} | Delete Bot Pack
[**edit_bot**](APIV2UsersApi.md#edit_bot) | **PATCH** /api/v2/users/{user_id}/bots/{bot_id} | Edit Bot
[**fetch_user**](APIV2UsersApi.md#fetch_user) | **GET** /api/v2/users/{user_id} | Fetch User
[**get_cache_user**](APIV2UsersApi.md#get_cache_user) | **GET** /api/v2/users/{user_id}/obj | Get Cache User
[**get_user_votes**](APIV2UsersApi.md#get_user_votes) | **GET** /api/v2/users/{user_id}/bots/{bot_id}/votes | Get User Votes
[**regenerate_user_token**](APIV2UsersApi.md#regenerate_user_token) | **PATCH** /api/v2/users/{user_id}/token | Regenerate User Token
[**transfer_bot_ownership**](APIV2UsersApi.md#transfer_bot_ownership) | **PATCH** /api/v2/users/{user_id}/bots/{bot_id}/ownership | Transfer Bot Ownership
[**update_bot_pack**](APIV2UsersApi.md#update_bot_pack) | **PATCH** /api/v2/users/{user_id}/packs/{pack_id} | Update Bot Pack
[**update_user_preferences**](APIV2UsersApi.md#update_user_preferences) | **PATCH** /api/v2/users/{user_id}/preferences | Update User Preferences
[**update_vote_reminders**](APIV2UsersApi.md#update_vote_reminders) | **PATCH** /api/v2/users/{user_id}/vote-reminders | Update Vote Reminders

# **add_bot**
> APIResponse add_bot(body, user_id, bot_id)

Add Bot

Adds a bot to fates list

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
api_instance = swagger_client.APIV2UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.BotMeta() # BotMeta | 
user_id = 56 # int | 
bot_id = 56 # int | 

try:
    # Add Bot
    api_response = api_instance.add_bot(body, user_id, bot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2UsersApi->add_bot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BotMeta**](BotMeta.md)|  | 
 **user_id** | **int**|  | 
 **bot_id** | **int**|  | 

### Return type

[**APIResponse**](APIResponse.md)

### Authorization

[User](../README.md#User)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **appeal_bot**
> APIResponse appeal_bot(body, user_id, bot_id)

Appeal Bot

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
api_instance = swagger_client.APIV2UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.BotAppeal() # BotAppeal | 
user_id = 56 # int | 
bot_id = 56 # int | 

try:
    # Appeal Bot
    api_response = api_instance.appeal_bot(body, user_id, bot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2UsersApi->appeal_bot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BotAppeal**](BotAppeal.md)|  | 
 **user_id** | **int**|  | 
 **bot_id** | **int**|  | 

### Return type

[**APIResponse**](APIResponse.md)

### Authorization

[User](../README.md#User)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bot_backup**
> object bot_backup(user_id, bot_id)

Bot Backup

Backs up a bot returning the backup. Backups are not stored

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
api_instance = swagger_client.APIV2UsersApi(swagger_client.ApiClient(configuration))
user_id = 56 # int | 
bot_id = 56 # int | 

try:
    # Bot Backup
    api_response = api_instance.bot_backup(user_id, bot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2UsersApi->bot_backup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **bot_id** | **int**|  | 

### Return type

**object**

### Authorization

[User](../README.md#User)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **certify_bot_request**
> APIResponse certify_bot_request(body, bot_id, user_id)

Certify Bot Request

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
api_instance = swagger_client.APIV2UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.BotAppeal() # BotAppeal | 
bot_id = 56 # int | 
user_id = 56 # int | 

try:
    # Certify Bot Request
    api_response = api_instance.certify_bot_request(body, bot_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2UsersApi->certify_bot_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BotAppeal**](BotAppeal.md)|  | 
 **bot_id** | **int**|  | 
 **user_id** | **int**|  | 

### Return type

[**APIResponse**](APIResponse.md)

### Authorization

[User](../README.md#User)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_bot_pack**
> IDResponse create_bot_pack(body, user_id)

Create Bot Pack

Creates a new bot pack on the list

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
api_instance = swagger_client.APIV2UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.BotPackPartial() # BotPackPartial | 
user_id = 56 # int | 

try:
    # Create Bot Pack
    api_response = api_instance.create_bot_pack(body, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2UsersApi->create_bot_pack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BotPackPartial**](BotPackPartial.md)|  | 
 **user_id** | **int**|  | 

### Return type

[**IDResponse**](IDResponse.md)

### Authorization

[User](../README.md#User)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bot**
> APIResponse delete_bot(user_id, bot_id)

Delete Bot

Deletes a bot.

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
api_instance = swagger_client.APIV2UsersApi(swagger_client.ApiClient(configuration))
user_id = 56 # int | 
bot_id = 56 # int | 

try:
    # Delete Bot
    api_response = api_instance.delete_bot(user_id, bot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2UsersApi->delete_bot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **bot_id** | **int**|  | 

### Return type

[**APIResponse**](APIResponse.md)

### Authorization

[User](../README.md#User)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bot_pack**
> APIResponse delete_bot_pack(user_id, pack_id)

Delete Bot Pack

Deletes an existing bot pack on the list

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
api_instance = swagger_client.APIV2UsersApi(swagger_client.ApiClient(configuration))
user_id = 56 # int | 
pack_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Delete Bot Pack
    api_response = api_instance.delete_bot_pack(user_id, pack_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2UsersApi->delete_bot_pack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **pack_id** | [**str**](.md)|  | 

### Return type

[**APIResponse**](APIResponse.md)

### Authorization

[User](../README.md#User)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_bot**
> APIResponse edit_bot(body, user_id, bot_id)

Edit Bot

Edits a bot, the owner here must be the owner editing the bot.

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
api_instance = swagger_client.APIV2UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.BotMeta() # BotMeta | 
user_id = 56 # int | 
bot_id = 56 # int | 

try:
    # Edit Bot
    api_response = api_instance.edit_bot(body, user_id, bot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2UsersApi->edit_bot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BotMeta**](BotMeta.md)|  | 
 **user_id** | **int**|  | 
 **bot_id** | **int**|  | 

### Return type

[**APIResponse**](APIResponse.md)

### Authorization

[User](../README.md#User)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_user**
> Profile fetch_user(user_id, bot_logs=bot_logs, system_bots=system_bots)

Fetch User

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIV2UsersApi()
user_id = 56 # int | 
bot_logs = false # bool |  (optional) (default to false)
system_bots = false # bool |  (optional) (default to false)

try:
    # Fetch User
    api_response = api_instance.fetch_user(user_id, bot_logs=bot_logs, system_bots=system_bots)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2UsersApi->fetch_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **bot_logs** | **bool**|  | [optional] [default to false]
 **system_bots** | **bool**|  | [optional] [default to false]

### Return type

[**Profile**](Profile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cache_user**
> BaseUser get_cache_user(user_id)

Get Cache User

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIV2UsersApi()
user_id = 56 # int | 

try:
    # Get Cache User
    api_response = api_instance.get_cache_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2UsersApi->get_cache_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

[**BaseUser**](BaseUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_votes**
> BotVoteCheck get_user_votes(bot_id, user_id)

Get User Votes

Endpoint to check amount of votes a user has.   **votes** - The amount of votes the bot has.  **voted** - Whether or not the user has *ever* voted for the bot.  **vote_epoch** - The redis TTL of the users vote lock. This is not time_to_vote which is the elapsed time the user has waited since their last vote.  **vts** - A list of timestamps that the user has voted for the bot on that has been recorded.  **time_to_vote** - The time the user has waited since they last voted.  **vote_right_now** - Whether a user can vote right now. Currently equivalent to `vote_epoch < 0`.

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
# Configure API key authorization: User
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.APIV2UsersApi(swagger_client.ApiClient(configuration))
bot_id = 56 # int | 
user_id = 56 # int | 

try:
    # Get User Votes
    api_response = api_instance.get_user_votes(bot_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2UsersApi->get_user_votes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **int**|  | 
 **user_id** | **int**|  | 

### Return type

[**BotVoteCheck**](BotVoteCheck.md)

### Authorization

[Bot](../README.md#Bot), [User](../README.md#User)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **regenerate_user_token**
> object regenerate_user_token(user_id)

Regenerate User Token

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
api_instance = swagger_client.APIV2UsersApi(swagger_client.ApiClient(configuration))
user_id = 56 # int | 

try:
    # Regenerate User Token
    api_response = api_instance.regenerate_user_token(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2UsersApi->regenerate_user_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

**object**

### Authorization

[User](../README.md#User)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_bot_ownership**
> APIResponse transfer_bot_ownership(body, user_id, bot_id)

Transfer Bot Ownership

Transfers ownership of a bot. If you are staff, this requires a high enough permission level and for the bot in question to be staff unlocked first

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
api_instance = swagger_client.APIV2UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.OwnershipTransfer() # OwnershipTransfer | 
user_id = 56 # int | 
bot_id = 56 # int | 

try:
    # Transfer Bot Ownership
    api_response = api_instance.transfer_bot_ownership(body, user_id, bot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2UsersApi->transfer_bot_ownership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OwnershipTransfer**](OwnershipTransfer.md)|  | 
 **user_id** | **int**|  | 
 **bot_id** | **int**|  | 

### Return type

[**APIResponse**](APIResponse.md)

### Authorization

[User](../README.md#User)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bot_pack**
> APIResponse update_bot_pack(body, user_id, pack_id)

Update Bot Pack

Updates an existing bot pack on the list

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
api_instance = swagger_client.APIV2UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.BotPackPartial() # BotPackPartial | 
user_id = 56 # int | 
pack_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Update Bot Pack
    api_response = api_instance.update_bot_pack(body, user_id, pack_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2UsersApi->update_bot_pack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BotPackPartial**](BotPackPartial.md)|  | 
 **user_id** | **int**|  | 
 **pack_id** | [**str**](.md)|  | 

### Return type

[**APIResponse**](APIResponse.md)

### Authorization

[User](../README.md#User)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_preferences**
> APIResponse update_user_preferences(body, user_id)

Update User Preferences

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
api_instance = swagger_client.APIV2UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateUserPreferences() # UpdateUserPreferences | 
user_id = 56 # int | 

try:
    # Update User Preferences
    api_response = api_instance.update_user_preferences(body, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2UsersApi->update_user_preferences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateUserPreferences**](UpdateUserPreferences.md)|  | 
 **user_id** | **int**|  | 

### Return type

[**APIResponse**](APIResponse.md)

### Authorization

[User](../README.md#User)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vote_reminders**
> APIResponse update_vote_reminders(body, user_id)

Update Vote Reminders

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
api_instance = swagger_client.APIV2UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateVoteReminders() # UpdateVoteReminders | 
user_id = 56 # int | 

try:
    # Update Vote Reminders
    api_response = api_instance.update_vote_reminders(body, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2UsersApi->update_vote_reminders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateVoteReminders**](UpdateVoteReminders.md)|  | 
 **user_id** | **int**|  | 

### Return type

[**APIResponse**](APIResponse.md)

### Authorization

[User](../README.md#User)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

