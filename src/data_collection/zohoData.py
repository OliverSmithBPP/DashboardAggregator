import os
import requests
from json_handling import jsonFileHandling


ZOHO_CLIENT_ID = os.environ.get("ZOHO_CLIENT_ID")
ZOHO_CLIENT_SECRET = os.environ.get("ZOHO_CLIENT_SECRET")
ZOHO_REFRESH_TOKEN = os.environ.get("ZOHO_REFRESH_TOKEN")
ZOHO_ORG_ID = os.environ.get("ZOHO_ORG_ID")

JSON_FILE_NAME = "zoho_data_json"



def get_access_token():
    response = requests.post("https://accounts.zoho.eu/oauth/v2/token", data={
        "grant_type": "refresh_token",
        "client_id": ZOHO_CLIENT_ID,
        "client_secret": ZOHO_CLIENT_SECRET,
        "refresh_token": ZOHO_REFRESH_TOKEN,
    })
    return response.json()["access_token"]


def get_tickets():
    access_token = get_access_token()
    response = requests.get("https://desk.zoho.eu/api/v1/tickets", headers={
        "Authorization": f"Zoho-oauthtoken {access_token}",
        "orgId": ZOHO_ORG_ID,
    })
    jsonFileHandling.write_data_to_json(JSON_FILE_NAME, response.json())




