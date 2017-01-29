from pythonwhois import shared, get_whois
from geopy.geocoders import Nominatim
from tqdm import tqdm
from geopy.exc import *
err = {}

def get_domain_info(url):
    try:
        domain = get_whois(url)
        return domain['contacts']
    except Exception as e:
        err['domain'] = url
        err['error'] = e
        err['step'] = 'get_domain_info'
        return err

def get_domain(url):
    domain = get_domain_info(url)
    if isinstance(domain,dict) is False:
        return domain
    if 'error' in domain:
        return domain
    if 'registrant' in domain:
        domain = domain['registrant']
    elif 'admin' in domain:
        domain = domain['admin']
    elif 'tech' in domain:
        domain = domain['tech']
    geolocator = Nominatim()
    try:
        location = geolocator.geocode('{}, {}'.format(domain['city'], domain['country']))
    except Exception as e:
        err['domain'] = url
        err['error'] = e
        err['step'] = 'get_domain/geocode'
        return err
    try:
        domain['lat'] = location.latitude
        domain['long'] = location.longitude
    except Exception as e:
        err['domain'] = url
        err['error'] = e
        err['step'] = 'get_domain/lat_long'
        return err
    domain['domain'] = url
    return domain
