import os
import re
from atlassian import Confluence
from json_handling import jsonFileHandling


CONFLUENCE_EMAIL = os.environ.get("JIRA_EMAIL")
CONFLUENCE_API_TOKEN = os.environ.get("JIRA_API_TOKEN")

CONFLUENCE_URL = 'https://projectdashboardexample.atlassian.net/wiki'

JSON_FILE_NAME = "confluence_data_json"

confluence = Confluence(
    url=CONFLUENCE_URL,
    username=CONFLUENCE_EMAIL,
    password=CONFLUENCE_API_TOKEN
)



def get_confluence_data(spaceKey):
    if not os.path.isfile(f"src/{JSON_FILE_NAME}"):
        print("Getting CONFLUENCE data...")
        pages = confluence.get_all_pages_from_space(spaceKey, expand='body.storage')
        pages_list = []
        for page in pages:
            pages_list.append(convert_page_to_dict(spaceKey, page))
        jsonFileHandling.write_data_to_json(JSON_FILE_NAME, pages_list)
    else:
        print("Confluence data already exists. Skipping creation.")         


def convert_page_to_dict(spaceKey, page):
    page_dict = {
        "id": page["id"],
        "title": page["title"],
        "body": strip_html(page["body"]['storage']['value']),
        "url": f"{CONFLUENCE_URL}/spaces/{spaceKey}/pages/{page['id']}"
    }
    return page_dict


def strip_html(text):
    text = re.sub('<[^<]+?>', '', text)
    return text
