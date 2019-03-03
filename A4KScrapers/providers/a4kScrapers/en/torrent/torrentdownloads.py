# -*- coding: utf-8 -*-

from lib import core

class sources(core.DefaultExtraQuerySources):
    def __init__(self):
        super(sources, self).__init__(__name__)

    def soup_filter(self, response):
        return core.beautifulSoup(response) \
                   .find_all('div', { 'class': 'inner_container' })[1] \
                   .find_all('div', { 'class': 'grey_bar3' })

    def find_title(self, el):
        return el.find_all('a')[0].text

    def find_url(self, el):
        return el.find_all('a')[0]['href']

    def find_seeds(self, el):
        return el.find_all('span')[2].text
