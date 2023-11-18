from ebay import search_ebay_sold_items

from llava import get_quality
from os.path import abspath

name = "miles morales jordan 1"
print(search_ebay_sold_items(name))
print(get_quality(abspath('shoes.jpeg')))