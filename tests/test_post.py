import unittest
from app.models import Blogpost

class PostTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Post class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_post = Blogpost(id=56,title='My post',subtitle = 'goofy',author='manka',date_posted='1/4/2018',content='I can post all day long',user_id= 15)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Blogpost))