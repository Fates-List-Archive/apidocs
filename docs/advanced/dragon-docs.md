## GET /api/dragon/ping
### ping_server

**Description:**Ping the server

**Request Body:**
```json
{"done":false,"reason":null,"context":null}
```

## GET /api/dragon/__stats
### get_stats

**Description:**Get stats of websocket server

**Request Body:**
```json
null
```

## POST /api/dragon/github
### github_webhook

**Description:**Post to github webhook. Needs authorization

**Request Body:**
```json
{"done":false,"reason":null,"context":null}
```

## OPTIONS /api/dragon/bots/:id/votes
### vote_bot

**Description:**Creates a vote for a bot. Needs authorization. This is the CORS code

**Request Body:**
```json
{"done":false,"reason":null,"context":null}
```

## OPTIONS /api/dragon/bots/:id/votes
### vote_bot

**Description:**Creates a vote for a bot. Needs authorization. This is the actual route

**Request Body:**
```json
{"done":false,"reason":null,"context":null}
```

## WS /api/dragon/ws
### websocket

**Description:**The websocket gateway for Fates List

**Request Body:**
```json
null
```


