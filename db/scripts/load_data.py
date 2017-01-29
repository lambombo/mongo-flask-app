from tqdm import tqdm
from get_domain import *
from pprint import pprint
import json

import datetime
import json

def datetime_handler(x):
    if isinstance(x, datetime.datetime):
        return x.isoformat()
    raise TypeError("Unknown type")

def load_domain():
    with open('host_list.txt') as f:
        lst = f.read().split('\n')
    data = list()
    for i in tqdm(range(1, len(lst))):
        domain = {}
        domain = get_domain(lst[i])
        domain['id'] = i + 1
        if 'error' not in domain:
            data.append(domain)

    with open('host_list.json', 'w') as outfile:
        json.dump(data, outfile, default=datetime_handler)

load_domain()
