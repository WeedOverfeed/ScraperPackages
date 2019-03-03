# -*- coding: utf-8 -*-    

try:
    import hosters
except:
    from providers.CivitasScrapers.en import hosters

def get_hosters():    
    return hosters.__all__    
