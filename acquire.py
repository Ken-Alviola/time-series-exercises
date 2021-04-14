import pandas as pd 
import requests

def get_zach(endpoint):
    
    '''input string the endpoint of the url. Function will return a dataframe filled with items in the key specified (items, sales, stores, etc)'''
    
    #base + endpoint
    base_url = 'https://python.zach.lol/api/v1/'
    url = base_url + endpoint
    
    #reading json and getting max page
    response = requests.get(url)
    data = response.json()
    n = data['payload']['max_page']
    
    #new list for the loop
    new_list = []
    
    #looping through all pages and pulling data
    for i in range(1, n+1):
        new_url = url + '?page=' + str(i)
        response = requests.get(new_url)
        data = response.json()
        page_items = data['payload'][endpoint]
        new_list += page_items
    
    #returns a dataframe of the list items from the loop
    return pd.DataFrame(new_list)