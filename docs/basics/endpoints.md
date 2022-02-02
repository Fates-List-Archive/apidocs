# Endpoints

You can see the documentation for the actual API endpoints provided by Fates List via Swagger, Redoc or the raw OpenAPI schema (for those who just want the raw OpenAPI schema to plug into an API tester):

Redoc (recommended): [https://api.fateslist.xyz/docs/redoc](https://api.fateslist.xyz/docs/redoc)

Swagger: [https://api.fateslist.xyz/docs/swagger](https://api.fateslist.xyz/docs/swagger)

OpenAPI JSON: [https://api.fateslist.xyz/docs/openapi](https://api.fateslist.xyz/docs/openapi)

???+ warning
    
    It is recommended to use (python) requests, (NodeJS) node-fetch or [reqbin](https://reqbin.com) though reqbin should be used as a **last resort** as it does not support DELETE requests with a request body.


These endpoints are subject to change over time. For information on the rest of the API and how to use the API, continue reading the API Documentation here. The above URLs cover all the endpoints while this documentation \(the main one\) just covers the additional things you need to know in order to read the above properly.

???+ note

    Both https://api.fateslist.xyz and https://api.fateslist.xyz/api are acceptable base URLs for the API. As such both https://api.fateslist.xyz/docs/swagger and https://api.fateslist.xyz/api/docs/swagger are valid