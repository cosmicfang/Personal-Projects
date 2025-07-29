import os
import requests
from dotenv import load_dotenv
from balldontlie import BalldontlieAPI


load_dotenv()
API_KEY = os.getenv('API_KEY')

# # Fetch NBA teams using the public API endpoint
# def get_nba_teams(api_key=API_KEY):
#     api = BalldontlieAPI(api_key)
#     teams = api.nba.teams.list()
#     return teams
    

# if __name__ == '__main__':
#     print(get_nba_teams())


import requests

def get_nba_teams():
    url = "https://api.balldontlie.io/v1/teams"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["data"]
    else:
        raise Exception(f"Failed to fetch teams: {response.status_code}")

if __name__ == "__main__":
    teams = get_nba_teams()
    for team in teams:
        print(f"{team['full_name']} ({team['abbreviation']})")


