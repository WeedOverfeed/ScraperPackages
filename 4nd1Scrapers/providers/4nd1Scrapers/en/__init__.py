# -*- coding: utf-8 -*-    

try:
    import hosters
except:
    from providers.4nd1Scrapers.en import hosters

def get_hosters():    
    return hosters.__all__    
