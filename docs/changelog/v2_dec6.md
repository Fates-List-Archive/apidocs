# API v2 December 6th update

### Changes

* API Restructure/Reorganize finished: This is not yet done, but will soon be done. All API endpoints will now be categorized in the docs
* Create Votes API has been moved to Dragon (/api/dragin/users/vote?user\_id=USERID&bot\_id=BOTID&test=TESTVOTEORNOT). Right now, test votes
can be sent by anyone, so you should check for test votes beforehand...
* **All events are now websocket only**
* **Some API's have had breaking changes, please recheck the docs for all endpoints you are using for now. Full list will be sent here soon**

### Fixes

* The API is now much faster
* Stability improvements
* Crashes in multiple API endpoints have been resolved
