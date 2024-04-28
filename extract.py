import requests
import json
import os

#https://developer.twitter.com/en/portal/products/free


bearer_token = os.environ.get("BEARER_TOKEN")
search_url = "https://api.twitter.com/2/tweets/search/recent"

# Ajout des hashtags dans la requête de recherche
query_params = {
    'query': '#jo2024 OR #Paris2024 OR #Génération2024 OR #Jeux2024 OR #Olympiques2024 -is:retweet',
    'tweet.fields': 'author_id,created_at'
}

def bearer_oauth(r):
    """
    Méthode requise pour l'authentification avec un Bearer Token.
    """
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(f"Status code: {response.status_code}")
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def main():
    json_response = connect_to_endpoint(search_url, query_params)
    print(json.dumps(json_response, indent=4, sort_keys=True))

if __name__ == "__main__":
    main()