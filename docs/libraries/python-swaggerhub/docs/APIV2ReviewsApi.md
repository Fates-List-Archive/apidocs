# swagger_client.APIV2ReviewsApi

All URIs are relative to *https://api.fateslist.xyz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_review**](APIV2ReviewsApi.md#delete_review) | **DELETE** /api/v2/users/{user_id}/reviews/{id} | Delete Review
[**edit_review**](APIV2ReviewsApi.md#edit_review) | **PATCH** /api/v2/users/{user_id}/reviews/{id} | Edit Review
[**get_all_reviews**](APIV2ReviewsApi.md#get_all_reviews) | **GET** /api/v2/reviews/{target_id}/all | Get All Reviews
[**new_review**](APIV2ReviewsApi.md#new_review) | **POST** /api/v2/users/{user_id}/reviews | New Review
[**vote_review_api**](APIV2ReviewsApi.md#vote_review_api) | **PATCH** /api/v2/users/{user_id}/reviews/{rid}/votes | Vote Review Api

# **delete_review**
> APIResponse delete_review(user_id, id)

Delete Review

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
api_instance = swagger_client.APIV2ReviewsApi(swagger_client.ApiClient(configuration))
user_id = 56 # int | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Delete Review
    api_response = api_instance.delete_review(user_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2ReviewsApi->delete_review: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **id** | [**str**](.md)|  | 

### Return type

[**APIResponse**](APIResponse.md)

### Authorization

[User](../README.md#User)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_review**
> APIResponse edit_review(body, user_id, id)

Edit Review

Deletes a review. Note that the (body) id, target_id, target_type and the reply flags are not honored for this endpoint

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
api_instance = swagger_client.APIV2ReviewsApi(swagger_client.ApiClient(configuration))
body = swagger_client.BotReviewPartial() # BotReviewPartial | 
user_id = 56 # int | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Edit Review
    api_response = api_instance.edit_review(body, user_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2ReviewsApi->edit_review: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BotReviewPartial**](BotReviewPartial.md)|  | 
 **user_id** | **int**|  | 
 **id** | [**str**](.md)|  | 

### Return type

[**APIResponse**](APIResponse.md)

### Authorization

[User](../README.md#User)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_reviews**
> BotReviews get_all_reviews(target_id, target_type, page=page, recache=recache)

Get All Reviews

Gets all reviews for a target bot or server/guild

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIV2ReviewsApi()
target_id = 56 # int | 
target_type = swagger_client.ReviewType() # ReviewType | 
page = 1 # int |  (optional) (default to 1)
recache = false # bool |  (optional) (default to false)

try:
    # Get All Reviews
    api_response = api_instance.get_all_reviews(target_id, target_type, page=page, recache=recache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2ReviewsApi->get_all_reviews: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_id** | **int**|  | 
 **target_type** | [**ReviewType**](.md)|  | 
 **page** | **int**|  | [optional] [default to 1]
 **recache** | **bool**|  | [optional] [default to false]

### Return type

[**BotReviews**](BotReviews.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **new_review**
> APIResponse new_review(body, user_id)

New Review

target_id is who the review is targetted to, target_type is whether its a guild or bot, 0 means bot, 1 means server

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
api_instance = swagger_client.APIV2ReviewsApi(swagger_client.ApiClient(configuration))
body = swagger_client.BotReviewPartialExt() # BotReviewPartialExt | 
user_id = 56 # int | 

try:
    # New Review
    api_response = api_instance.new_review(body, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2ReviewsApi->new_review: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BotReviewPartialExt**](BotReviewPartialExt.md)|  | 
 **user_id** | **int**|  | 

### Return type

[**APIResponse**](APIResponse.md)

### Authorization

[User](../README.md#User)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vote_review_api**
> APIResponse vote_review_api(body, user_id, rid)

Vote Review Api

Creates a vote for a review

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
api_instance = swagger_client.APIV2ReviewsApi(swagger_client.ApiClient(configuration))
body = swagger_client.BotReviewVote() # BotReviewVote | 
user_id = 56 # int | 
rid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Vote Review Api
    api_response = api_instance.vote_review_api(body, user_id, rid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2ReviewsApi->vote_review_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BotReviewVote**](BotReviewVote.md)|  | 
 **user_id** | **int**|  | 
 **rid** | [**str**](.md)|  | 

### Return type

[**APIResponse**](APIResponse.md)

### Authorization

[User](../README.md#User)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

