## GET /api/dragon/ping
#### ping_server

**Description:**Ping the server

**Request Body:**
```json
null
```

**Response Body:**
```json
{
  "done": false,
  "reason": null,
  "context": null
}
```

## GET /api/dragon/__stats
#### get_stats

**Description:**Get stats of websocket server

**Request Body:**
```json
null
```

**Response Body:**
```json
null
```

## POST /api/dragon/github
#### github_webhook

**Description:**Post to github webhook. Needs authorization

**Request Body:**
```json
{
  "ref": "",
  "action": "",
  "Commits": null,
  "repository": {
    "id": 0,
    "name": "",
    "full_name": "",
    "description": "",
    "url": "",
    "owner": {
      "login": "",
      "id": 0,
      "avatar_url": "",
      "url": "",
      "html_url": "",
      "organizations_url": ""
    },
    "html_url": "",
    "commits_url": ""
  },
  "pusher": {
    "name": "",
    "description": ""
  },
  "sender": {
    "login": "",
    "id": 0,
    "avatar_url": "",
    "url": "",
    "html_url": "",
    "organizations_url": ""
  },
  "head_commit": {
    "id": "",
    "message": "",
    "author": {
      "name": "",
      "email": "",
      "username": ""
    }
  }
}
```

**Response Body:**
```json
{
  "done": false,
  "reason": null,
  "context": null
}
```

## OPTIONS /api/dragon/bots/:id/votes
#### vote_bot

**Description:**Creates a vote for a bot. Needs authorization. This is the CORS code

**Request Body:**
```json
null
```

**Response Body:**
```json
null
```

## PATCH /api/dragon/bots/:id/votes
#### vote_bot

**Description:**Creates a vote for a bot. Needs authorization. This is the actual route

**Request Body:**
```json
{
  "user_id": "",
  "bot_id": "",
  "test": false
}
```

**Response Body:**
```json
{
  "done": false,
  "reason": null,
  "context": null
}
```

## WS /api/dragon/ws
#### websocket

**Description:**The websocket gateway for Fates List

**Request Body:**
```json
null
```

**Response Body:**
```json
null
```


