import io

import requests
from rdflib import Graph

#?action=query&list=search&srsearch=haswbstatement:P180=Q7378&srnamespace=6&format=json
URL = "https://commons.wikimedia.org/w/api.php"

# defining a params dict for the parameters to be sent to the API
PARAMS = {
    'action' :'query',
    'list': 'search',
    'srsearch': 'haswbstatement:P180=Q7378',
    'srnamespace': '6',
    'format': 'json',
    }

# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)


for image in r.json()['query']['search']:
    print(image['pageid'])
    URL = 'https://commons.wikimedia.org/wiki/Special:EntityData/M'+str(image['pageid'])+'.ttl'
    r = requests.get(url=URL)
    print(r.content)

    g = Graph()
    print(io.StringIO(r.content.decode("utf-8") ))
    g.parse(io.StringIO(r.content.decode("utf-8") ), format="ttl")

    print(len(g))  # prints 2

    import pprint

    for stmt in g:
        if 'http://schema.org/contentUrl' == str(stmt[1]):
            imageURL = print(stmt[2])