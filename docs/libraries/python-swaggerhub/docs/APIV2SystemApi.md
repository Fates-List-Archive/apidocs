# swagger_client.APIV2SystemApi

All URIs are relative to *https://api.fateslist.xyz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_bot_info**](APIV2SystemApi.md#add_bot_info) | **GET** /api/v2/_sunbeam/add-bot | Add Bot Info
[**check_staff_member**](APIV2SystemApi.md#check_staff_member) | **GET** /api/v2/is_staff | Check Staff Member
[**csp_report**](APIV2SystemApi.md#csp_report) | **POST** /api/v2/_csp | Csp Report
[**get_all_vote_reminders**](APIV2SystemApi.md#get_all_vote_reminders) | **GET** /api/v2/vote-reminders | Get All Vote Reminders
[**get_botlist_stats**](APIV2SystemApi.md#get_botlist_stats) | **GET** /api/v2/blstats | Get Botlist Stats
[**get_bots_filtered**](APIV2SystemApi.md#get_bots_filtered) | **GET** /api/v2/bots/filter | Get Bots Filtered
[**get_index**](APIV2SystemApi.md#get_index) | **GET** /api/v2/index | Get Index
[**get_partners**](APIV2SystemApi.md#get_partners) | **GET** /api/v2/partners | Get Partners
[**get_staff_roles**](APIV2SystemApi.md#get_staff_roles) | **GET** /api/v2/staff_roles | Get Staff Roles
[**get_top_spots**](APIV2SystemApi.md#get_top_spots) | **GET** /api/v2/top-spots | Get Top Spots
[**get_vanity**](APIV2SystemApi.md#get_vanity) | **GET** /api/v2/code/{vanity} | Get Vanity
[**search_by_tag**](APIV2SystemApi.md#search_by_tag) | **GET** /api/v2/search/tags | Search By Tag
[**search_list**](APIV2SystemApi.md#search_list) | **GET** /api/v2/search | Search List
[**sellix_webhook**](APIV2SystemApi.md#sellix_webhook) | **POST** /api/v2/sellix-webhook | Sellix Webhook
[**stats_page**](APIV2SystemApi.md#stats_page) | **GET** /api/v2/blstats-full | Stats Page
[**troubleshoot_api**](APIV2SystemApi.md#troubleshoot_api) | **GET** /api/v2/_sunbeam/troubleshoot | Troubleshoot Api

# **add_bot_info**
> AddBotInfo add_bot_info(user_id)

Add Bot Info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIV2SystemApi()
user_id = 56 # int | 

try:
    # Add Bot Info
    api_response = api_instance.add_bot_info(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2SystemApi->add_bot_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

[**AddBotInfo**](AddBotInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_staff_member**
> IsStaff check_staff_member(user_id, min_perm=min_perm)

Check Staff Member

Admin route to check if a user is staff or not

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIV2SystemApi()
user_id = 56 # int | 
min_perm = 2 # int |  (optional) (default to 2)

try:
    # Check Staff Member
    api_response = api_instance.check_staff_member(user_id, min_perm=min_perm)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2SystemApi->check_staff_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **min_perm** | **int**|  | [optional] [default to 2]

### Return type

[**IsStaff**](IsStaff.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **csp_report**
> APIResponse csp_report()

Csp Report

This is where CSP reports should be sent to.  CSP reports should not happen in practice.  **These requests are logged to loguru**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIV2SystemApi()

try:
    # Csp Report
    api_response = api_instance.csp_report()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2SystemApi->csp_report: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**APIResponse**](APIResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_vote_reminders**
> object get_all_vote_reminders()

Get All Vote Reminders

Get vote reminders

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIV2SystemApi()

try:
    # Get All Vote Reminders
    api_response = api_instance.get_all_vote_reminders()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2SystemApi->get_all_vote_reminders: %s\n" % e)
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

# **get_botlist_stats**
> BotListStats get_botlist_stats()

Get Botlist Stats

Returns uptime and stats about the list.  **uptime** - The current uptime for the given worker. All workers reboot periodically to avoid memory leaks so this will mostly be low  **pid** - The pid of the worker you are connected to  **up** - Whether the databases are up on this worker  **server_uptime** - How long the Fates List Server has been up for totally  **bot_count_total** - The bot count of the list  **bot_count** - The approved and certified bots on the list  **workers** - The worker pids. This is sorted and retrived from dragon IPC if not directly available on the worker

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIV2SystemApi()

try:
    # Get Botlist Stats
    api_response = api_instance.get_botlist_stats()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2SystemApi->get_botlist_stats: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BotListStats**](BotListStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bots_filtered**
> BotQueueGet get_bots_filtered(state, verifier=verifier, limit=limit, offset=offset)

Get Bots Filtered

API to get all bots filtered by its state  Limit must be less than or equal to 100  **This API now guarantees that the bot list is only what you request**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIV2SystemApi()
state = [swagger_client.BotState()] # list[BotState] | Bot states like ?state=0&state=6
verifier = 56 # int |  (optional)
limit = 100 # int |  (optional) (default to 100)
offset = 0 # int |  (optional) (default to 0)

try:
    # Get Bots Filtered
    api_response = api_instance.get_bots_filtered(state, verifier=verifier, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2SystemApi->get_bots_filtered: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | [**list[BotState]**](BotState.md)| Bot states like ?state&#x3D;0&amp;state&#x3D;6 | 
 **verifier** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**BotQueueGet**](BotQueueGet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_index**
> BotIndex get_index(type=type)

Get Index

Returns the bot/server index JSON  This is internally used by sunbeam to render the index page

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIV2SystemApi()
type = swagger_client.Type() # Type |  (optional)

try:
    # Get Index
    api_response = api_instance.get_index(type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2SystemApi->get_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**Type**](.md)|  | [optional] 

### Return type

[**BotIndex**](BotIndex.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_partners**
> Partners get_partners()

Get Partners

Gets the partner list.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIV2SystemApi()

try:
    # Get Partners
    api_response = api_instance.get_partners()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2SystemApi->get_partners: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Partners**](Partners.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_staff_roles**
> StaffRoles get_staff_roles()

Get Staff Roles

Return all staff roles and their role ids if you ever wanted them...

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIV2SystemApi()

try:
    # Get Staff Roles
    api_response = api_instance.get_staff_roles()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2SystemApi->get_staff_roles: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StaffRoles**](StaffRoles.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_top_spots**
> object get_top_spots()

Get Top Spots

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIV2SystemApi()

try:
    # Get Top Spots
    api_response = api_instance.get_top_spots()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2SystemApi->get_top_spots: %s\n" % e)
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

# **get_vanity**
> BotVanity get_vanity(vanity)

Get Vanity

Gets information about a vanity given a vanity code  This is used by sunbeam in handling vanities

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIV2SystemApi()
vanity = 'vanity_example' # str | 

try:
    # Get Vanity
    api_response = api_instance.get_vanity(vanity)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2SystemApi->get_vanity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vanity** | **str**|  | 

### Return type

[**BotVanity**](BotVanity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_by_tag**
> TagSearch search_by_tag(tag, target_type)

Search By Tag

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIV2SystemApi()
tag = 'tag_example' # str | 
target_type = swagger_client.SearchType() # SearchType | 

try:
    # Search By Tag
    api_response = api_instance.search_by_tag(tag, target_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2SystemApi->search_by_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**|  | 
 **target_type** | [**SearchType**](.md)|  | 

### Return type

[**TagSearch**](TagSearch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_list**
> Search search_list(q)

Search List

Searches the list for any bot/server/profile available Q is the query to search for. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIV2SystemApi()
q = 'q_example' # str | 

try:
    # Search List
    api_response = api_instance.search_list(q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2SystemApi->search_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**|  | 

### Return type

[**Search**](Search.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sellix_webhook**
> object sellix_webhook()

Sellix Webhook

**Warning**: Only documented for internal use  Can be used by staff in case you didn't get the actual order

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIV2SystemApi()

try:
    # Sellix Webhook
    api_response = api_instance.sellix_webhook()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2SystemApi->sellix_webhook: %s\n" % e)
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

# **stats_page**
> BotStatsFull stats_page(full=full)

Stats Page

Returns the full set of botlist stats

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIV2SystemApi()
full = false # bool |  (optional) (default to false)

try:
    # Stats Page
    api_response = api_instance.stats_page(full=full)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2SystemApi->stats_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **full** | **bool**|  | [optional] [default to false]

### Return type

[**BotStatsFull**](BotStatsFull.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **troubleshoot_api**
> Troubleshoot troubleshoot_api(user_id=user_id)

Troubleshoot Api

Internal API used by sunbeam for troubleshooting issues  Used in https://fateslist.xyz/frostpaw/troubleshoot  This requires a Frostpaw header to be properly set

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIV2SystemApi()
user_id = 56 # int |  (optional)

try:
    # Troubleshoot Api
    api_response = api_instance.troubleshoot_api(user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2SystemApi->troubleshoot_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | [optional] 

### Return type

[**Troubleshoot**](Troubleshoot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

