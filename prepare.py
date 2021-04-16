import pandas as pd
import numpy as np
import datetime


def get_sales():
    sales = pd.read_csv('sales.csv',index_col=0)
    stores = pd.read_csv('stores.csv', index_col=0)
    items = pd.read_csv('items.csv', index_col=0)
    
    store_items = sales.merge(stores, left_on='store',right_on='store_id')
    store_items = store_items.merge(items, left_on='item', right_on='item_id')
    store_items = store_items.drop(columns=['item','store'])
    
    store_items.sale_date = store_items.sale_date.str.replace('GMT','')
    store_items.sale_date = store_items.sale_date.str.slice(start=4)
    store_items.sale_date = pd.to_datetime(store_items.sale_date)
    
    store_items = store_items.set_index('sale_date').sort_index()
    
    store_items['month'] = store_items.index.month_name()
    store_items['day_of_week'] = store_items.index.day_name()
    store_items['sales_total'] = store_items.sale_amount * store_items.item_price
    
    return store_items

def get_germany():
    
    germany = pd.read_csv('opsd_germany_daily.csv')
    germany.Date = pd.to_datetime(germany.Date)
    
    germany = germany.set_index('Date').sort_index()
    germany['month'] = germany.index.month_name()     
    germany['year'] = germany.index.year
    germany_filled = germany.fillna(germany.mean())
    
    return germany_filled

