import requests

class Calendly:
    def __init__(self, token: str):
        self.base_url = "https://api.calendly.com"
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        
    def test(self):
        if self.headers.get("Authorization") is None:
            return "Non è stata configurata l'API Key, impossibile ottenere eventi."
        return "API Key configurata correttamente."

    def get_user(self):
        url = f"{self.base_url}/users/me"
        response = requests.get(url, headers=self.headers)
        if response.status_code == requests.codes.ok:
            return response.json()
        else:
            print(f"Failed to fetch user information: {response.text}")
            return None
    
    def get_events(self, sort = {"name": "asc"}):
        formatted_data = []
        active_events = True
        url = f"{self.base_url}/event_types"
        user = self.get_user()["resource"]["uri"]
        if(user is None):
            return "Non sono riuscito a trovare l'utente, riprova più tardi."
        response = requests.get(url, headers=self.headers, 
                                params={"active": active_events, "sort": sort, "user": user})
        if response.status_code == requests.codes.ok:
            for event in response.json()["collection"]:
                formatted_event = {
                "name": event["name"],
                "description_plain": event["description_plain"],
                "duration": event["duration"],
                "location": event["locations"][0]["location"],
                "scheduling_url": event["scheduling_url"]
                }
                formatted_data.append(formatted_event)
            return formatted_data
        else:
            print(f"Failed to fetch events: {response.text}")
            return None