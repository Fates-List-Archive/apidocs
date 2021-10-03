# Getting Started

Fates List offers websockets to allow you to get real time stats about your bot. This has been rewritten in golang to allow for better performance and reliability as well as new features that could not be implemented performantly in python

### What are Websockets?

Please read [this nice MDN doc on WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) first before attempting this. Check if your library supports the new v2 websocket rewrite first or use one of the example reference libraries [here](https://github.com/Fates-List/FatesList/tree/main/data/snowfall/info).

### Receiving Responses

Large responses are seperated using ASCII Code 31 This is ``\x1f`` in python.

Some example code on how to recieve responses from websocket is below:

```py

for m in event.split("\x1f"):
    for e in m.split("\x1f"):
        if e == "":
            continue
        e_json = json.loads(e)
        if e_json.get("m"):
            e_type = e_json["m"].get("e")
            ...
        elif e_json.get("control"):
            ...
        await self.hooks["default"](e_json)
```

### Payloads

Payloads sent by the websocket server are either [events](../structures/event.md) or control payloads.

The format for sending data from the client to the websocket is still being worked on and is not yet implemented in any case.

Below is the format for a control payload:

| Key | Description | Type |
| :--- | :--- | :--- |
| code | The control payload name. This can be used to check for an identity etc. | String |
| detail | Human friendly information describing the control payload for debugging. May be used in future for non-debugging purposes | String |
| ts | The timestamp in seconds for the event | Integer/Float |
| requests_remaining | The amount of requests remaining before you are ratelimited. Is always -1 in initial identity *for now* | Integer |
| control | Always set to true in a control payload | Boolean |

All other payloads sent to you by websocket will be a event as of right now. This may change in the future.

### Identity

When you recieve a ``identity`` control payload, you should respond with the following format (or as given in the ``detail`` key)

| Key | Description | Type |
| :--- | :--- | :--- |
| id | Bot ID | Snowflake |
| token | API Token | String |
| send_all | Whether or not to send all prior events. This may cause disconnects/instability, more memory usage and ratelimits | Boolean |
| send_none | Whether or not to send events after sending prior events if ``send_all`` is set | Boolean |

After a successful identity, you will now have a established websocket connection