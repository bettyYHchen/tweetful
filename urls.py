API_URL = "https://api.twitter.com"
REQUEST_TOKEN_URL = API_URL + "/oauth/request_token"
AUTHORIZE_URL = API_URL + "/oauth/authorize?oauth_token={request_token}"
ACCESS_TOKEN_URL = API_URL + "/oauth/access_token"
TIMELINE_URL = API_URL + "/1.1/statuses/home_timeline.json"
USERS_URL = API_URL + "/1.1/users/show.json?screen_name=infsmall"
RTM_URL = API_URL + "/1.1/statuses/retweets_of_me.json"