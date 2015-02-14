'''Scrape artists from a festival'''

from bs4 import BeautifulSoup

import urllib2

class FestivalScraper(object):
    '''Scrape from one specific festival'''
    def __init__(self, webpage):
        '''Setup'''
        headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36' }
        req = urllib2.Request(webpage, None, headers)
        base_html = urllib2.urlopen(req).read()
        self.soup = BeautifulSoup(base_html)

    def get_artists(self):
        '''Artists at this festival'''
        artist_div = self.soup.findAll(attrs={'class': 'lineupguide'})
        artist_tags = [r.find_all('li') for r in artist_div][0]
        artist_list = [a.contents[0] for a in artist_tags]
        return artist_list
