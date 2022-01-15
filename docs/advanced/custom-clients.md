# Custom Clients

Custom clients are supported however you are responsible for keeping them up-to-date. Some features require whitelisting in order to use (DM a Fates List staff member for this):

## Frostpaw Auth

!!! note
    This feature requires whitelisting in order to use

In order to authorize to the API through OAuth (without using a inputted user token, you need to use Frostpaw Authentication)

### Getting the login link

The first step in Frostpaw Auth is getting the login link:

To do this:

- Store the current location if needed (use localStorage if needed)

- Send a POST request to `https://fateslist.xyz/api/v2/oauth`.
    - Make sure to send the `Frostpaw` header (set this to the client version in the [About](https://fateslist.xyz/frostpaw/about) section)
    - Set the `Frostpaw-Server` header to the *origin servers hostname*, for example https://fateslist.xyz/bot/admin/add would set `Frostpaw-Server` as https://fateslist.xyz. You can use `window.location.origin` for this if this is for a browser
    - The final redirect *requires explicit whitelisting, possible source code access and a possible POC to be shown*

- JSON body should contain the scopes key (which should just be a array containing just `identify`). **redirect is deprecated**

- The final url to redirect to will be in the `url` key of the response

- We will guide you on the `redirect_uri` side. There is a very specific route you will need to give (official sunbeam client uses `/frostpaw/login` and as such your client will also need to expose a `/frostpaw/login` route as well)

- [Relevant API Docs](https://api.fateslist.xyz/api/docs/redoc#operation/get_login_link)

### Get login information

This step is domain-dependent, you might need another server to set the required cookies and/or parse JWTs. We do not recommend using `/jwtparse/_sunbeam` or our `Set-Cookie` headers without asking us beforehand as these may or may not work in the future and may need extra whitelisting in the future

The general idea is the below:

- Get the code and state from query string (`new URLSearchParams(window.location.search)` if you are on browser)

- Send a POST request to `https://api.fateslist.xyz/api/v2/users`
    - Make sure to send the `Frostpaw` header (set this to the client version in the [About](https://fateslist.xyz/frostpaw/about) section)
    - Set the `Frostpaw-Server` header to the *origin servers hostname*, for example https://fateslist.xyz/bot/admin/add would set `Frostpaw-Server` as https://fateslist.xyz. You can use `window.location.origin` for this if this is for a browser
    - Be sure to set `code` to the code you got from query string and `scopes` which should be a array containing just `identify`
    - Handle errors from our API properly (ask staff if you need a test account banned etc.). This is where `done` is set to `false`
    - If all goes well, you will get a json with `done` set to `true`. In this case, you will get a `token` and a `user` amongst other things (this changes constantly, see [here](https://api.fateslist.xyz/api/docs/redoc#operation/login_user) for up to date information) ([BaseUser](../structures/basic-structures.md#baseuser)). Store these somehow and redirect back to where they last were (you did store this in step 1 right?)

- [Relevant API Docs](https://api.fateslist.xyz/api/docs/redoc#operation/login_user)

### Bot/Server Pages

For Bot Pages, we recommend calling [Get Bot Page](https://api.fateslist.xyz/api/docs/redoc#operation/get_bot_page). Even if you do not use most/all the information in the response, it will still trigger analytics at least and won't trigger some of our anti abuse code we have on our API (which could get you banned).

Similarly for Server Pages, call [Get Server Page](https://api.fateslist.xyz/api/docs/redoc#operation/get_server_page). This is actually the only way to get server information actually as of time of writing, our other APIs require authorization.

## Bot/Server Invites

For Bots, use [Get Bot Invite](https://api.fateslist.xyz/api/docs/redoc#operation/get_bot_invite). This takes a ton of stuff into account and returns a proper invite URL. It also handles analytics and won't trigger some of our anti abuse code we have on our API (which could get you banned).

Similarly for Servers, use [Get Server Invite](https://api.fateslist.xyz/api/docs/redoc#operation/get_server_invite)

## Documentation

Not all of our APIs are fully documented especially for sunbeam and custom client stuff. This is to allow quick breaking changes to our API. When in doubt, try testing our API using cURL or [reqbin](https://reqbin.com)

## Headers

Make sure to send the `Frostpaw` header on *all requests* (set this to the client version in the [About](https://fateslist.xyz/frostpaw/about) section). Our anti-abuse code takes this header into account and your responses may be easier to parse as well with possibly fewer restrictions in some areas.