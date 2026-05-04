import os
import re
from atlassian import Confluence
from json_handling import jsonFileHandling

# Set up some global variables at the start. Using environment variables for credentials and tokens to avoid hardcoding the values.
CONFLUENCE_EMAIL = os.environ.get("JIRA_EMAIL")
CONFLUENCE_API_TOKEN = os.environ.get("JIRA_API_TOKEN")

CONFLUENCE_URL = 'https://projectdashboardexample.atlassian.net/wiki'

JSON_FILE_NAME = "src/confluence_data_json"

confluence = Confluence(
    url=CONFLUENCE_URL,
    username=CONFLUENCE_EMAIL,
    password=CONFLUENCE_API_TOKEN
)


# Gets the Confluence pages from a specific space. Creates JSON file using all the pages.
def get_confluence_data(spaceKey):
    try:
        # If the JSON file exists then we skip getting the data.
        if not os.path.isfile(JSON_FILE_NAME):
            print("Getting CONFLUENCE data...")
            pages = confluence.get_all_pages_from_space(spaceKey, expand='body.storage')
            pages_list = []
            # For each page we get, we need to extract the data that is relevant.
            for page in pages:
                pages_list.append(convert_page_to_dict(spaceKey, page))
            # When we get all the data we write it to a JSON file.
            jsonFileHandling.write_data_to_json(JSON_FILE_NAME, pages_list)
        else:
            print("Confluence data already exists. Skipping creation.")         
    except Exception as e:
        print(f"Exception occurred while trying to get Confluence data: {e}")


# We have lots of data we dont need, so we need to extract the useful data/fields.
def convert_page_to_dict(spaceKey, page):
    page_dict = {
        "id": page["id"],
        "title": page["title"],
        "body": strip_html(page["body"]['storage']['value']),
        "url": f"{CONFLUENCE_URL}/spaces/{spaceKey}/pages/{page['id']}"
    }
    return page_dict


# Getting pages returns raw HTML content for each page in a confluence space. We need to strip the HTML syntax to get the body text we want.
def strip_html(text):
    text = re.sub('<[^<]+?>', '', text)
    return text
