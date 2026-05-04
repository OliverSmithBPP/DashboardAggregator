import unittest
from data_collection import confluenceData

class TestConfluenceData(unittest.TestCase):

    # Makes sure we can strip raw HTML and get the required text.
    def test_strip_html(self):
        result = confluenceData.strip_html("<p>strip html test</p>")
        
        assert result == "strip html test"


    # Makes sure that the Confluence pages return the expected data.
    def test_convert_page_to_dict(self):
        fake_spaceKey = "test"
        fake_page = {"id": "12345", "title": "fake title", "body": {"storage": {"value": "fake body"}}}
        result = confluenceData.convert_page_to_dict(fake_spaceKey, fake_page)

        assert result["id"] == "12345"
        assert result["title"] == "fake title"
        assert result["body"] == "fake body"
        assert result["url"] == "https://projectdashboardexample.atlassian.net/wiki/spaces/test/pages/12345"
