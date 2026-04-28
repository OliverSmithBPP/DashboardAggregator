import json
import os
from flask import Flask, render_template
from data_collection import jiraData, confluenceData, zohoData
from json_handling import jsonFileHandling

app = Flask(__name__)


json_files = ["jira_data_json", "confluence_data_json", "zoho_data_json"]


def load_json(filename):
    file_path = os.path.join(app.root_path, filename)
    with open(file_path, 'r') as file:
        return json.load(file)


@app.route('/')
def index():

    for file in json_files:
        file_path = os.path.join(app.root_path, file)
        if jsonFileHandling.check_file_age(file_path):
            jsonFileHandling.remove_file(file_path)
    
    jiraData.get_jira_data_for_project("SCRUM")
    confluenceData.get_confluence_data("SD")
    zohoData.get_tickets()

    jira_data = load_json('jira_data_json')
    confluence_data = load_json('confluence_data_json')
    zoho_data = load_json('zoho_data_json')
 
    return render_template('index.html', jira_data=jira_data, confluence_data=confluence_data, zoho_data=zoho_data)


if __name__ == "__main__":
    app.run(debug=True)
