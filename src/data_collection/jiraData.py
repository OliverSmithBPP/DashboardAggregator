import os
from jira import JIRA, JIRAError
from json_handling import jsonFileHandling

# Set up some global variables at the start. Using environment variables for credentials and tokens to avoid hardcoding the values.
JIRA_EMAIL = os.environ.get("JIRA_EMAIL")
JIRA_API_TOKEN = os.environ.get("JIRA_API_TOKEN")

JIRA_SERVER_URL = "https://projectdashboardexample.atlassian.net/"

JSON_FILE_NAME = "src/jira_data_json"

jiraOptions = {'server': JIRA_SERVER_URL}
jira = JIRA(options=jiraOptions, basic_auth=(JIRA_EMAIL, JIRA_API_TOKEN))


# Gets the JIRA Issues for a specific project and writes them to a JSON file.
def get_jira_data_for_project(project):
    try:
        # If the JSON file exists we avoid fetching the data.
        if not os.path.isfile(JSON_FILE_NAME):
            print("Getting JIRA data...")
            issues = jira.search_issues(jql_str=f'project = {project}')
            issue_list = []
            # For each Jira issue we extract the relevant data and convert it to a dictionary.
            for issue in issues:
                issue_list.append(convert_issue_to_dict(issue))
            # Check if issue list is empty first before trying to create the JSON file.    
            if len(issue_list) != 0:
                jsonFileHandling.write_data_to_json(JSON_FILE_NAME, issue_list) 
            else:
                print("No JIRA issues found, not writing to JSON file")
        else:
            print("Jira file already exists. Skipping creation.")
    # JIRAErrors are Jira API specific errors that are thrown if something goes wrong with the API.
    except (OSError, JIRAError) as e:
        print(f"Exception occurred while trying to get JIRA data: {e}")    


# The Jira API returns an Issue object, we convert this to a dictionary and remove the redundant data before creating the JSON file.
def convert_issue_to_dict(issue):
    issue_dict = {
        "id": issue.id,
        "key": issue.key,
        "url": issue.permalink() if hasattr(issue, "permalink") else None,
        "summary": issue.fields.summary,
        "status": issue.fields.status.name,
        "assignee": issue.fields.assignee.displayName if issue.fields.assignee else None,
        "reporter": issue.fields.reporter.displayName if issue.fields.reporter else None,
        "priority": issue.fields.priority.name if issue.fields.priority else None,
        "issue_type": issue.fields.issuetype.name,
        "created": issue.fields.created,
    }
    return issue_dict 
