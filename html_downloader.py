# -*- coding: utf-8 -*-
import urllib.request

class HtmlDownlo1ader(object):
    
    
    def download(self,url):
        if url is None:
            return None
        response =urllib.request.urlopen(url)
        #print('has response')
        if response.getcode() != 200:
            return None
        return response.read().decode('utf-8','ignore')
    
    



