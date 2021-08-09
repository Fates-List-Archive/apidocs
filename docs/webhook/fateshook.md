# FatesHook (Fates Client)

!!! note
    There are many types of webhooks in Fates List. Please choose the one you use carefully. Also note that all Fates List webhooks (excl. Discord Integration) will have a Authorization header with your API Token so you can validate the request.

FatesHook is a webhook type to get additional events like edit bot, review events and more. These events cannot be sent using something like vote webhook and need their own format which is what FatesHook is for. All Fates Client Webhooks like the Vote Webhook will be sent as a JSON with the Authorization header being your API token.

!!! warning
    All Fates Client libraries which support v2 will support this. Some v1 libraries may also work but this is not guaranteed as the format for webhooks has changed a bit during the transition to v2

### Basic Format

All Fates Hook Webhooks follow the [Event](../structures/event.md) format.
