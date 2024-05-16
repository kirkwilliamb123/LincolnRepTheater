import pandas as pd
from urllib.request import urlretrieve

name_basics_url = 'https://datasets.imdbws.com/'
name_basics_file = 'name.basics.tsv.gz'

name_basics = urlretrieve(url, name_basics_file)