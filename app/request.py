import urllib.request,json
from .models import News,Sources



#instance to get the API key
apiKey = None

#instance to get the base url
base_url = None
article_url = None


def configure_request(app):
    global apiKey, base_url, article_url
    apiKey = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    article_url = app.config['ARTICLE_API_BASE_URL']


def get_news_category(category):
    
    get_news_url = base_url.format(category, apiKey)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)

    return news_results



