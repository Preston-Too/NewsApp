import unittest
from .models import News,Sources

class NewsTest(unittest.TestCase):

    '''
    test instance to check the behavior of the news class
    '''
    def setUp(self):

        '''
        This method runs before every test
        '''
        self.news1 = News("New York Times", "Trump is a genius", "I don't have DNA, I have USA", "12th October 2020" )

    def test_instance(self):
        self.assertTrue(isinstance(self.news1,News))

class SourceTest:
    '''
    test source class and its behaviours
    '''
    def setUp(self):
        self.new_source = Source(123, 'preston', 'description', 'url')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source))
