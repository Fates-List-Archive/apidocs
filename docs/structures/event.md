# Events

All Events are made of two parts. The metadata (m) and the context (ctx). Keys outside this is not considered part of the event and is extra, usuallt for convenience of the developer.

Metadata

| Key | Description | Type |
| :--- | :--- | :--- |
| e | Event Name (see [here](https://github.com/Fates-List/FatesList/blob/cf339725f2f3082eae39dc03b67be8807a782efb/modules/models/enums.py#L59)) | Integer |
| eid | Event ID (random on websocket auth) | UUID |
| t | Event Type (multi) | Integer/List |
| id | Target Bot/User ID | Snowflake |
| ts | Event Timestamp | Float |
| wt | Webhook Type (Webhook Only) (see [here](enums.autogen.md)) | Integer |

**Key** 

multi: List can be returned if multiple choices are present

### Base Event Context

All event contexts in Fates List share the basic format in the below table. If it does not, then you have 99% found a bug and you should report it on our support server. Additional key valie pairs may be present and these will be noted below.

| Key | Value | Type |
| :--- | :--- | :--- |
| user | This is the User ID responsible for the event | Snowflake |

### Special Event Contexts

If an event does not appear here, then it uses the simple base context format.

#### Reviews

The context of a new review or a edit review event is a [Partial Review](partial-review.md) object
