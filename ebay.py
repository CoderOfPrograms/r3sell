import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def get_item_description(item_url):
    response = requests.get(item_url)
    soup = BeautifulSoup(response.text,  'html.parser')

    iframe = soup.find(id='desc_ifr')
    if iframe:
        iframe_src = iframe['src']
        iframe_response = requests.get(iframe_src)
        iframe_soup = BeautifulSoup(iframe_response.text, 'html.parser')
        return iframe_soup.get_text(strip=True)
    else:
        return 'No Description'


def search_ebay_sold_items(search_query):
    # Replace spaces in the search query with '+'
    query = search_query.replace(' ', '+')
    counter = 0

    prices = []
    img_urls = []
    for pgn in range(2):
        
        if (counter == 100):
            break
        counter += 1
    # eBay URL for sold listings
        url = f"https://www.ebay.com/sch/i.html?_nkw={query}&_sop=12&LH_Sold=1&LH_Complete=1&rt=nc&LH_ItemCondition=3000&_pgn={pgn}"

        # Send a request to the eBay URL
        response = requests.get(url)

        # Parse the response using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find listings - Adjust the selector as needed
        listings = soup.find_all('li', class_='s-item')


        # Extract and print details from each listing
        for item in listings[1:]:
            price = item.find('span', class_='s-item__price').text if item.find('span', class_='s-item__price') else 'No Price'

            img_div = item.find('div', class_='s-item__image-wrapper')
            img_url = img_div.find('img')['src'] if img_div and img_div.find('img') else 'No Image URL'
            try:
                prices.append(float(price.replace("$","").replace(",",'')))
            except:
                pass
            img_urls.append(img_url)

        prices = np.array(prices)
        stats = min(prices), np.percentile(prices, 25), np.percentile(prices, 50), np.percentile(prices, 75), max(prices)

        return stats 




