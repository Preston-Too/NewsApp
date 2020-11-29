class News:

    '''
    News class that will define the objects of the news
    '''

    def __init__(self,id, author, title, description, url, urlToImage, publishedAt):
        self.author = author
        self.id = id
        self.title = title
        self.description = description
        self.publishedAt = publishedAt
        self.url = url
        self.urlToImage = urlToImage



