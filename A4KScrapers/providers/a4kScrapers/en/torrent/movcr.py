# -*- coding: utf-8 -*-

from lib import core

class sources(core.DefaultExtraQuerySources):
    def __init__(self):
        super(sources, self).__init__(__name__)

    def parse_seeds(self, seeds):
        return seeds.split('/')[0]
