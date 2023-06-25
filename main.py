import requests

from send_email import send_email

API_KEY = "12739400fab64ab1921079afe96c44ec"
topic = "tesla"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&from=2023-05-25&" \
      "sortBy=publishedAt&" \
      "apiKey=12739400fab64ab1921079afe96c44ec&" \
      "language=en"
# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()
data = " "
# Access the article title and descriptions
for article in content['articles'][:20]:
    if article["title"] is not None:
        data = "Subject: Today's news" \
               + "\n" + data + article['title'] \
               + "\n" + article['description'] \
               + "\n" + article['url'] + 2*"\n"

data = data.encode('utf-8')
send_email(data)
