import re
import requests

from io import BytesIO

from bs4 import BeautifulSoup

from slackbot_settings import TEAM_NAME, TEAM_COOKIE

URL_CUSTOMIZE = "https://{team_name}.slack.com/customize/emoji"
URL_ADD = "https://{team_name}.slack.com/api/emoji.add"
URL_LIST = "https://{team_name}.slack.com/api/emoji.adminList"

API_TOKEN_REGEX = r'"api_token":"([^"]*)"'
API_TOKEN_PATTERN = re.compile(API_TOKEN_REGEX)


def _session():
    session = requests.session()
    session.headers = {'Cookie': TEAM_COOKIE}
    session.url_customize = URL_CUSTOMIZE.format(team_name=TEAM_NAME)
    session.url_add = URL_ADD.format(team_name=TEAM_NAME)
    session.url_list = URL_LIST.format(team_name=TEAM_NAME)
    session.api_token = _fetch_api_token(session)
    return session


def _fetch_api_token(session):
    # Fetch the form first, to get an api_token.
    r = session.get(session.url_customize)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")

    all_script = soup.findAll("script")
    for script in all_script:
        for line in script.text.splitlines():
            if 'api_token' in line:
                # api_token: "xoxs-12345-abcdefg....",
                matched = API_TOKEN_PATTERN.search(line.strip()).group(0)
                token = matched.replace('"', '').replace('api_token:', '')
                return token

    raise Exception('api_token not found. response status={}'.format(
        r.status_code))


def generate(opt):
    url = 'https://emoji-gen.ninja/emoji'
    for i, (key, val) in enumerate(zip(opt.keys(), opt.values())):
        delimeter = '?' if i == 0 else '&'
        url += delimeter + key + '=' + val
    response = requests.get(url)
    return BytesIO(response.content)


def register(opt):
    session = _session()
    data = {'mode': 'data', 'name': opt['name'], 'token': session.api_token}
    files = {'image': generate(opt)}
    r = session.post(
        session.url_add, data=data, files=files, allow_redirects=False)
    r.raise_for_status()

    response_json = r.json()
    if not response_json['ok']:
        print("Error with uploading %s: %s" % (opt['name'], response_json))


def get_current_emoji_list(session):
    page = 1
    result = []
    while True:
        data = {
            'query': '',
            'page': page,
            'count': 1000,
            'token': session.api_token
        }
        r = session.post(session.url_list, data=data)
        r.raise_for_status()
        response_json = r.json()

        result.extend(map(lambda e: e["name"], response_json["emoji"]))
        if page >= response_json["paging"]["pages"]:
            break

        page = page + 1
    return result
