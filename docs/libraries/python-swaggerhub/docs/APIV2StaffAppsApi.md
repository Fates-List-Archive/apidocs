# swagger_client.APIV2StaffAppsApi

All URIs are relative to *https://api.fateslist.xyz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**short_url**](APIV2StaffAppsApi.md#short_url) | **GET** /api/v2/staff-apps/qibli/{id} | Short Url

# **short_url**
> object short_url(id)

Short Url

Gets the qibli data for a id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIV2StaffAppsApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Short Url
    api_response = api_instance.short_url(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIV2StaffAppsApi->short_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

