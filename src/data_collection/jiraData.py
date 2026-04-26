import os
from jira import JIRA
from json_handling import jsonFileHandling

JIRA_EMAIL = os.environ.get("JIRA_EMAIL")
JIRA_API_TOKEN = os.environ.get("JIRA_API_TOKEN")

JIRA_SERVER_URL = "https://projectdashboardexample.atlassian.net/"

JSON_FILE_NAME = "jira_data_json"

jiraOptions = {'server': JIRA_SERVER_URL}
jira = JIRA(options=jiraOptions, basic_auth=(JIRA_EMAIL, JIRA_API_TOKEN))



def get_jira_data_for_project(project):
    if not os.path.isfile(f"src/{JSON_FILE_NAME}"):
        issues = jira.search_issues(jql_str=f'project = {project}')
        issue_list = []
        for issue in issues:
            issue_list.append(convert_issue_to_dict(issue))
        if len(issue_list) != 0:
            jsonFileHandling.write_data_to_json(JSON_FILE_NAME, issue_list) 
        else:
            print("No JIRA issues found, not writing to JSON file")
    else:
        print("Jira file already exists. Skipping creation.")        


def convert_issue_to_dict(issue):
    issue_dict = {
        "id": issue.id,
        "key": issue.key,
        "summary": issue.fields.summary,
        "status": issue.fields.status.name,
        "assignee": issue.fields.assignee.displayName if issue.fields.assignee else None,
        "reporter": issue.fields.reporter.displayName if issue.fields.reporter else None,
        "priority": issue.fields.priority.name if issue.fields.priority else None,
        "issue_type": issue.fields.issuetype.name,
        "created": issue.fields.created,
    }
    return issue_dict 
