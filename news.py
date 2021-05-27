import requests


class NewsFeed:
    """Representing multiple news titles and links as a single string
    """
    base_url = "https://newsapi.org/v2/everything"
    api_key = "9f0f2c87fc7b4694b4d23cfca8b6e115"

    def __init__(self, interest, from_date, to_date, language='en'):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language  # ISO-639-1 code

    def get(self):
        url = self._build_url()
        articles = self._get_articles(url)

        email_body = ""
        for article in articles:
            email_body = email_body + article['title'] + '\n' + article['url'] + '\n\n'

        return email_body

    def _get_articles(self, url):
        response = requests.get(url)
        content = response.json()
        articles = content['articles']
        return articles

    def _build_url(self):
        url = f"{self.base_url}?" \
              f"qInTitle={self.interest}&" \
              f"from={self.from_date}&" \
              f"to={self.to_date}&" \
              f"language={self.language}&" \
              f"apiKey={self.api_key}"
        return url
