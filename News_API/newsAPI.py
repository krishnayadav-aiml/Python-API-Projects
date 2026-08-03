import requests
import json
CATEGORY = input("enter Category: ")
API_KEY = "YOUR API KEY"
url= f"https://newsdata.io/api/1/latest?apikey={API_KEY}"

params = {
    "country": "in",
    "language": "en",
    "category": CATEGORY
}

response = requests.get(url, params=params)
data = response.json()

if response.status_code == 200:
    for article in data["results"][:10]:
        print(f"Title: {article['title']}\n")
        print(f"Description: {article['description']}\n")
        print(f"Source: {article['source_name']}\n")
        print(f"Country: {article['country'][0]}\n")
        print(f"Publish Date: {article["pubDate"]}\n\n")
elif response.status_code == 401:
    print("invalid APi Key")
elif response.status_code == 404:
    print("City Not Found")
else:
    print("Something Went Wrong")

    
