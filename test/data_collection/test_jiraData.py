import unittest
from types import SimpleNamespace
from data_collection import jiraData

class TestJiraData(unittest.TestCase): 

    # We need to mimic the Jira Issue object. The object has nested atrributes so we can't used a dict, instead we create a fake object with SimpleNamespace.
    def test_convert_issue_to_dict(self):
        # Create the fake issue using SimpleNamespace for the attributes.       
        fake_issue = SimpleNamespace()
        fake_issue.fields = SimpleNamespace()
        fake_issue.fields.status = SimpleNamespace()
        fake_issue.fields.issuetype = SimpleNamespace()

        # Assign values to the fields.
        fake_issue.id = "12345"
        fake_issue.key = "TEST"
        fake_issue.fields.summary = "Test Summary"
        fake_issue.fields.status.name = "To Do"
        fake_issue.fields.assignee = None
        fake_issue.fields.reporter = None
        fake_issue.fields.priority = None
        fake_issue.fields.issuetype.name = "Task"
        fake_issue.fields.created = "2026-01-01T20:00:00.000+0100"

        result = jiraData.convert_issue_to_dict(fake_issue)

        assert result["id"] == "12345"
        assert result["key"] == "TEST"
        assert result["summary"] == "Test Summary"
        assert result["status"] == "To Do"
        assert result["issue_type"] == "Task"
        assert result["created"] == "2026-01-01T20:00:00.000+0100"
