import pandas as pd 
import requests

def get_zach(page):
    
    '''input string is a page name. Function will return a dataframe filled the items in the key specified'''
    
    base_url = 'https://python.zach.lol/api/v1/'
    url = base_url + page
    
    response = requests.get(url)
    data = response.json()
    n = data['payload']['max_page']
    
    new_list = []
    
    for i in range(1, n+1):
        new_url = url + '?page=' + str(i)
        response = requests.get(new_url)
        data = response.json()
        page_items = data['payload'][page]
        new_list += page_items
    
    return pd.DataFrame(new_list)