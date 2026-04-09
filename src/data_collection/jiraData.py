import os
from jira import JIRA

JIRA_EMAIL = os.environ.get("JIRA_EMAIL")
JIRA_API_TOKEN = os.environ.get("JIRA_API_TOKEN")

JIRA_SERVER_URL = "https://projectdashboardexample.atlassian.net/"

jiraOptions = {'server': JIRA_SERVER_URL}
jira = JIRA(options=jiraOptions, basic_auth=(JIRA_EMAIL, JIRA_API_TOKEN))



def collect_jira_data(project):
    for issue in jira.search_issues(jql_str=f'project = {project}'):
        print(f'Key = {issue.key}, Summary = {issue.fields.summary}, Name = {issue.fields.reporter.displayName}')



if __name__ == "__main__":
    collect_jira_data("SCRUM")


