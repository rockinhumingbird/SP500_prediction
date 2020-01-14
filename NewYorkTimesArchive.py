# -*- coding: utf-8 -*-
"""
Created on Mon 01 01 2020

"""
import sys, csv, json
reload(sys)
sys.setdefaultencoding('utf8')
import config # with my nyt key
import requests
"""
About:
Python wrapper for the New York Times Archive API 
https://developer.nytimes.com/article_search_v2.json
"""
class APIKeyException(Exception):
    def __init__(self, message): self.message = message 

class InvalidQueryException(Exception):
    def __init__(self, message): self.message = message 

class ArchiveAPI(object):
    def __init__(self, key=None):
        """
        Initializes the ArchiveAPI class. Raises an exception if no API key is given.
        :param key: New York Times API Key
        """
        self.key = key
        self.root = 'http://api.nytimes.com/svc/archive/v1/{}/{}.json?api-key={}' 
        if not self.key:
            nyt_dev_page = 'http://developer.nytimes.com/docs/reference/keys'
            exception_str = 'Warning: API Key required. Please visit {}'
            raise NoAPIKeyException(exception_str.format(nyt_dev_page))

    def query(self, year=None, month=None, key=None,):
        """
        Calls the archive API and returns the results as a dictionary.
        :param key: Defaults to the API key used to initialize the ArchiveAPI class.
        """
        if not key: key = self.key
        if (year < 1882) or not (0 < month < 13):
            # currently the Archive API only supports year >= 1882
            exception_str = 'Invalid query: See http://developer.nytimes.com/archive_api.json'
            raise InvalidQueryException(exception_str)
        url = self.root.format(year, month, key)
        r = requests.get(url)
        return r.json()


api = ArchiveAPI(config.nytkey)

years = [2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010]
#years = [2020]
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for year in years:
    for month in months:
        mydict = api.query(year, month)
        file_str = '/Users/zoe/' + str(year) + '-' + '{:02}'.format(month) + '.json' #dump my json files into a folder
        with open(file_str, 'w') as fout:
            json.dump(mydict, fout)
        fout.close()

