import os
import json
from jira import JIRA

JIRA_EMAIL = os.environ.get("JIRA_EMAIL")
JIRA_API_TOKEN = os.environ.get("JIRA_API_TOKEN")

JIRA_SERVER_URL = "https://projectdashboardexample.atlassian.net/"

jiraOptions = {'server': JIRA_SERVER_URL}
jira = JIRA(options=jiraOptions, basic_auth=(JIRA_EMAIL, JIRA_API_TOKEN))



def get_jira_data_for_project(project):
    issues = jira.search_issues(jql_str=f'project = {project}')
    issue_list = []
    for issue in issues:
         issue_list.append(convert_issue_to_dict(issue))
    if len(issue_list) != 0:
        write_jira_data_to_json(issue_list) 
    else:
        print("No JIRA issues found, not writing to JSON file")        


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


def write_jira_data_to_json(issue_list):
    with open("jira_issues_json", "w", encoding="utf-8") as file:
        json.dump(issue_list, file, indent=2, ensure_ascii=False)
