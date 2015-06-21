from collections import namedtuple
from datetime import datetime
import json
import requests
import time


# Voivodeships codes
DOLNOSLASKIE        = 2
KUJAWSKO_POMORSKIE  = 4
LUBELSKIE           = 6
LUBUSKIE            = 8
LODZKIE             = 10
MALOPOLSKIE         = 12
MAZOWIECKIE         = 14
OPOLSKIE            = 16
PODKARPACKIE        = 18
PODLASKIE           = 20
POMORSKIE           = 22
SLASKIE             = 24
SWIETOKRZYSKIE      = 26
WARMINSKO_MAZURSKIE = 28
WIELKOPOLSKIE       = 30
ZACHODNIOPOMORSKIE  = 32


HOST = 'http://rozklad.plk-sa.pl'

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36'


def difficulties_by_voivodeship(voivodeship, dt=datetime.now()):
    """


    :param voivodeship: Voivodeship numeric value.
    :return: Difficulties by voivodeship in JSON format.
    """
    session = requests.Session()
    session.headers.update({'User-Agent': USER_AGENT})
    session.headers.update({'X-Requested-With': 'XMLHttpRequest'})
    
    session.get('{}/Mapa/'.format(HOST))
    
    url = '{}/Mapa/PodajUtrudnieniaWWojewodztwie?KodWojewodztwa={}&_={}'.format(HOST, str(voivodeship), _datetime_to_asp_date(dt))
    response = session.get(url)
    
    json_data = response.json() if len(response.text) > 0 else '{}'
    
    #return json.load(urllib2.urlopen(url))
    return json.load(json_data)
# end-of-function difficulties_by_voivodeship    


def trains_by_voivodeship(voivodeship, dt=datetime.now()):
    """

    :param voivodeship: Voivodeship numeric value.
    :return: Trains by voivodeship in JSON format.
    """
    url = '{}/Mapa/PodajJadacePociagiWWojewodztwie?KodWojewodztwa={}&_={}'.format(HOST, str(voivodeship), _datetime_to_asp_date(dt))
    return json.load(urllib2.urlopen(url))
# end-of-function trains_by_voivodeship     


def _datetime_to_asp_date(dt):
    date = int(time.mktime(dt.timetuple()))
    date = date * 1000 + 137  # 
    return date
# end-of-function _datetime_to_asp_date 
    

##
# Entry point
if __name__ == '__main__':
    pass
    
    
    #diff = difficulties_by_voivodeship(SLASKIE)
    #print len(diff)
    