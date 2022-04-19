import requests
#key: '0cc913ce4bb1b776d2e5f84ad059c224'
#step: wide configuration

CONFIG_PATTERN = 'http://api.themoviedb.org/3/configuration?api_key=0cc913ce4bb1b776d2e5f84ad059c224'
KEY = '0cc913ce4bb1b776d2e5f84ad059c224'

url = CONFIG_PATTERN.format(key=KEY)
r = requests.get(url)
config = r.json()
""" 
content like this: 
{'change_keys': ['adult',
                  'also_known_as',
                  ...,
                  'translations'],
 'images': {'backdrop_sizes': ['w300', 'w780', 'w1280', 'original'],
             'base_url': 'http://d3gtl9l2a4fn1j.cloudfront.net/t/p/',
             'logo_sizes': ['w45', 'w92', 'w154', 'w185', 'w300', 'w500', 'original'],
             'poster_sizes': ['w92', 'w154', 'w185', 'w342', 'w500', 'original'],
             'profile_sizes': ['w45', 'w185', 'h632', 'original'],
             'secure_base_url': 'https://d3gtl9l2a4fn1j.cloudfront.net/t/p/'}}
"""

# base_url: this is where the images are stored.
# poster_sizes: those are the available sizes.
base_url = config['images']['base_url']
sizes = config['images']['poster_sizes']

"""
    'sizes' should be sorted in ascending order, so
        max_size = sizes[-1]
    should get the largest size as well.        
"""
def size_str_to_int(x):
    return float("inf") if x == 'original' else int(x[1:])
max_size = max(sizes, key=size_str_to_int)

print(config)