from collections import namedtuple

SITE_URL = 'https://rent.591.com.tw'
API_URL = 'https://bff.591.com.tw'
LIST_ENDPOINT = '{}/home/search/rsList?is_new_list=1&type=1&is_format_data=1'.format(SITE_URL)
SESSION_ENDPOINT = '{}/?kind=0&region=6'.format(SITE_URL)

ListRequestMeta = namedtuple('ListRequestMeta', ['id', 'name', 'page'])

DetailRequestMeta = namedtuple('DetailRequestMeta', ['id'])
