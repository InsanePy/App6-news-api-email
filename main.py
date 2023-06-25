import requests

API_KEY = "12739400fab64ab1921079afe96c44ec"

url = "https://newsapi.org/v2/everything?q=tesla&from=2023-05-25&" \
      "sortBy=publishedAt&" \
      "apiKey=12739400fab64ab1921079afe96c44ec"
# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article title and descriptions
for article in content['articles']:
    print(article['title'])
