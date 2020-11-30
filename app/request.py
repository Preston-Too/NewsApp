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



def process_results(news_list):
    
    '''
    This function processes the results and transforms them to become into a list of objects
    
    Args:
        news_list: A list of dictionaries that contains the news details
    Returns :
        news_results: A list of news objects
    '''

    news_results = []

    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        category = news_item.get('category')
        url = news_item.get('url')

        source_object = Sources(id, name, description, category, url)
        news_results.append(source_object)

    return news_results