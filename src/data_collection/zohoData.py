import os
import requests
from json_handling import jsonFileHandling

# Set up some global variables at the start. Using environment variables for credentials and tokens to avoid storing the values publicly.
ZOHO_CLIENT_ID = os.environ.get("ZOHO_CLIENT_ID")
ZOHO_CLIENT_SECRET = os.environ.get("ZOHO_CLIENT_SECRET")
ZOHO_REFRESH_TOKEN = os.environ.get("ZOHO_REFRESH_TOKEN")
ZOHO_ORG_ID = os.environ.get("ZOHO_ORG_ID")

JSON_FILE_NAME = "src/zoho_data_json"


# Zoho uses the OAuth 2.0, we need to get the access token before calling the service.
def get_access_token():
    try:
        response = requests.post("https://accounts.zoho.eu/oauth/v2/token", data={
            "grant_type": "refresh_token",
            "client_id": ZOHO_CLIENT_ID,
            "client_secret": ZOHO_CLIENT_SECRET,
            "refresh_token": ZOHO_REFRESH_TOKEN,
        })
        return response.json()["access_token"]
    except Exception as e:
        print(f"Exception occurred while trying to get Zoho access token: {e}")


# Fetches the tickets from Zoho Desk and writes them to a JSON file.
def get_tickets():
    try:
        # If the file exists we skip fetching the data.
        if not os.path.isfile(JSON_FILE_NAME):
            print("Getting ZOHO data...")
            access_token = get_access_token()
            response = requests.get("https://desk.zoho.eu/api/v1/tickets", headers={
                "Authorization": f"Zoho-oauthtoken {access_token}",
                "orgId": ZOHO_ORG_ID,
            })
            # Writing the data to a JSON file.
            jsonFileHandling.write_data_to_json(JSON_FILE_NAME, response.json()["data"])
        else:
            print("Zoho data already exists. Skipping creation.")
    except Exception as e:
        print(f"Exception occurred while trying to retrieve ticket data from Zoho: {e}")



