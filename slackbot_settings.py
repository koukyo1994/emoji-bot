import sys
import json

sys.path.append("..")
sys.path.append("./")

with open("credentials.json", "r") as f:
    _json = json.load(f)

# team name
TEAM_NAME = _json["teamName"]

# tokens
API_TOKEN = _json["apiToken"]

# cookie
TEAM_COOKIE = _json["teamCookie"]

# default reply
DEFAULT_REPLY = _json["defaultReply"]

# plugins
PLUGINS = _json["plugins"]
