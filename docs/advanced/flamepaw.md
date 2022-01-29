# Flamepaw
Flamepaw is internally used by the bot to provide a RESTful API for tasks requiring high concurrency.

## Ping Server

#### GET /api/dragon/ping
**Description:** Ping the server

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

## Get Stats

#### GET /api/dragon/__stats
**Description:** Get stats of websocket server

**Request Body:**
```json
null
```

**Response Body:**
```json
null
```

## Github Webhook

#### POST /api/dragon/github
**Description:** Post to github webhook. Needs authorization

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
	},
	"pull_request": {
		"id": 0,
		"number": 0,
		"state": "",
		"locked": false,
		"title": "",
		"body": "",
		"html_url": "",
		"url": "",
		"user": {
			"login": "",
			"id": 0,
			"avatar_url": "",
			"url": "",
			"html_url": "",
			"organizations_url": ""
		},
		"base": {
			"repo": {
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
			"id": 0,
			"number": 0,
			"state": "",
			"title": "",
			"body": "",
			"html_url": "",
			"url": "",
			"ref": "",
			"label": "",
			"user": {
				"login": "",
				"id": 0,
				"avatar_url": "",
				"url": "",
				"html_url": "",
				"organizations_url": ""
			},
			"commits_url": ""
		},
		"head": {
			"repo": {
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
			"id": 0,
			"number": 0,
			"state": "",
			"title": "",
			"body": "",
			"html_url": "",
			"url": "",
			"ref": "",
			"label": "",
			"user": {
				"login": "",
				"id": 0,
				"avatar_url": "",
				"url": "",
				"html_url": "",
				"organizations_url": ""
			},
			"commits_url": ""
		}
	},
	"issue": {
		"id": 0,
		"number": 0,
		"state": "",
		"title": "",
		"body": "",
		"html_url": "",
		"url": "",
		"user": {
			"login": "",
			"id": 0,
			"avatar_url": "",
			"url": "",
			"html_url": "",
			"organizations_url": ""
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

## Vote Bot

#### OPTIONS /api/dragon/bots/:id/votes
**Description:** Creates a vote for a bot. Needs authorization. This is the CORS code

**Request Body:**
```json
null
```

**Response Body:**
```json
null
```

## Vote Bot

#### PATCH /api/dragon/bots/:id/votes
**Description:** Creates a vote for a bot. Needs authorization. This is the actual route

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

## Websocket

#### WS /api/dragon/ws
**Description:** The websocket gateway for Fates List

**Request Body:**
```json
null
```

**Response Body:**
```json
null
```


