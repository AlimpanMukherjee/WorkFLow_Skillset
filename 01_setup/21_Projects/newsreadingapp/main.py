import requests

print("If you want to read from News API then enter 1")
print("If you want to read from GNews then enter 2")
choice = int(input("Enter your choice: "))

topic = input("Enter the topic you want to read about: ")

if choice == 1:
    # News API
    api = "476854c16d91497b8b44f5d4e09361eb"
    response = requests.get(f"https://newsapi.org/v2/everything?q={topic}&apiKey={api}")


elif choice == 2:
    # GNews
    api = "caafc58195a6118dd6a6d6e7924dfa15"
    response = requests.get(f"https://gnews.io/api/v4/search?q={topic}&apikey={api}")

else:
    print("Invalid choice.")
    exit()

# Process the response for either API
if response.status_code == 200:
    data = response.json()
    i=0
    for  item in data['articles']:
        title = item['title']
        description = item['description']
        url = item['url']
        print(f"{i +1}. Title: {title}")
        print(f"Description: {description}")
        # print(f"URL: {url}")
        print("\n*****************************\n")
        i+=1
else:
    print("Failed to fetch articles. Please check your API key or internet connection.")
