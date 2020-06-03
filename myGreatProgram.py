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
    'srlimit':'500',
    'srnamespace': '6',
    'format': 'json',
    }

# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)

url_list = []
for image in r.json()['query']['search']:

    URL = 'https://commons.wikimedia.org/wiki/Special:EntityData/M'+str(image['pageid'])+'.ttl'
    r = requests.get(url=URL)

    g = Graph()
    g.parse(io.StringIO(r.content.decode("utf-8") ), format="ttl")

    import pprint

    for stmt in g:
        if 'http://schema.org/contentUrl' == str(stmt[1]):
            imageURL = stmt[2]
            # print(imageURL)
            url_list.append(imageURL)

import pandas as pd
# url_list.to_csv("urllist",index=False)
af=pd.DataFrame(data={"object1":url_list})
af.to_csv("./attempt.csv",sep=',',index=False)

# import modules
from google.colab import files
import pandas as pd
import urllib.request
def url2jpg(i,url,file_path):
    """
    --i :number of images
    --url:url address
    --filepath:where to save the final image
    """
    filename='image-{}.jpg'.format(i)
    full_path="{}{}".format(file_path, filename)
    urllib.request.urlretrieve(url, filepath)
    return None
# set constants
filename="attempt.csv"
filepath='/elephants'

#read lists of url using pandas dataframe
urls=pd.read_csv(filename)
# save images to the directory by iterating through the list
for i,url in enumerate(urls.values):
    url2jpg(i,url[0],filepath)
    

import urllib.request
print('Beginning file download with urllib2...')
for url in url_list:
    filename = url.split('/')[-1]
    try:
      a=urllib.request.urlretrieve(url, filename)
    except OSError as oserr:
      if oserr.errno ==36:
        pass
      else:
        raise

! zip a.zip *
