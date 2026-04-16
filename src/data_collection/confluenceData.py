import os
from atlassian import Confluence


CONFLUENCE_EMAIL = os.environ.get("JIRA_EMAIL")
CONFLUENCE_API_TOKEN = os.environ.get("JIRA_API_TOKEN")

CONFLUENCE_URL = 'https://projectdashboardexample.atlassian.net/wiki'

confluence = Confluence(
    url=CONFLUENCE_URL,
    username=CONFLUENCE_EMAIL,
    password=CONFLUENCE_API_TOKEN
)



def get_confluence_data(pageId):
    page = confluence.get_page_by_id(pageId, expand='body.storage')
    print(f"Page = {page['body']['storage']['value']}")
