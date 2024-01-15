import requests

class DotaClient:
    
    def __init__(self):
        self.url = "https://api.opendota.com"

    def get_player(self, account_id):
        url = f'{self.url}/api/players/{account_id}'
        resp  = requests.get(url)
        if resp.status_code != 200:
            raise ValueError(f"Failed to fetch player info for account_id {account_id}. Status code: {resp.status_code}")
        
        return resp.json()


    def get_match(self, match_id):
        url = f'{self.url}/api/matches/{match_id}'
        resp  = requests.get(url)
        if resp.status_code != 200:
            raise ValueError(f"Failed to fetch player info for account_id {match_id}. Status code: {resp.status_code}")
        
        return resp.json()
