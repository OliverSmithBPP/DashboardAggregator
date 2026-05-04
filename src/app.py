import os
from flask import Flask, render_template
from data_collection import jiraData, confluenceData, zohoData
from json_handling import jsonFileHandling

app = Flask(__name__)

json_files = ["jira_data_json", "confluence_data_json", "zoho_data_json"]


@app.route('/')
def index():

    # Check if each file is older than the timeout and delete it. This creates a cache system where we're storing and not retrieving the data everytime the page is loaded.
    for file in json_files:
        file_path = os.path.join(app.root_path, file)
        if jsonFileHandling.check_file_age(file_path):
            jsonFileHandling.remove_file(file_path)
    
    # Getting the data from each of our sources and creating the JSON files. The functions only run if the file is absent.
    jiraData.get_jira_data_for_project("SCRUM")
    confluenceData.get_confluence_data("SD")
    zohoData.get_tickets()

    # Loading the JSON files into respective variables to be used in the HTML.
    jira_data = jsonFileHandling.load_json('src/jira_data_json')
    confluence_data = jsonFileHandling.load_json('src/confluence_data_json')
    zoho_data = jsonFileHandling.load_json('src/zoho_data_json')
 
    return render_template('index.html', jira_data=jira_data, confluence_data=confluence_data, zoho_data=zoho_data)


if __name__ == "__main__":
    app.run(debug=True)
