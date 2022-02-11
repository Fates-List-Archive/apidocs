# swagger_client.APIV2PoliciesApi

All URIs are relative to *https://api.fateslist.xyz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_policies**](APIV2PoliciesApi.md#all_policies) | **GET** /api/v2/policies/all | All Policies
[**privacy_policy**](APIV2PoliciesApi.md#privacy_policy) | **GET** /api/v2/policies/privacy | Privacy Policy
[**rules**](APIV2PoliciesApi.md#rules) | **GET** /api/v2/policies/rules | Rules

# **all_policies**
> object all_policies()

All Policies

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIV2PoliciesApi()

try:
    # All Policies
    api_response = api_instance.all_policies()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2PoliciesApi->all_policies: %s\n" % e)
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

# **privacy_policy**
> object privacy_policy()

Privacy Policy

Returns the privacy policy for fates list as a JSON

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIV2PoliciesApi()

try:
    # Privacy Policy
    api_response = api_instance.privacy_policy()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2PoliciesApi->privacy_policy: %s\n" % e)
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

# **rules**
> object rules()

Rules

Returns the rules for fates list as a JSON

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIV2PoliciesApi()

try:
    # Rules
    api_response = api_instance.rules()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2PoliciesApi->rules: %s\n" % e)
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

