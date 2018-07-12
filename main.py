import pandas as pd
import numpy as np


mcdonalds_julio = {'conos': 724009138, 'mcpollo': 724009126, 'bigmac': 724008146, 'cbo': 724008200}

julio_completo = {'Codigo': [724009126, 724009018, 724009138], 'Precio': ['4,90€', '3€', '0,50€'], 'Producto': ['Menú McPollo', 'Menú Hamburguesa con Queso o Chicken Burger BBQ', 'Cono']}


def simple_series():
    offers = pd.Series(mcdonalds_julio)
    print(offers)

def dataframe():
    gold_offers = pd.DataFrame(julio_completo)
    print(gold_offers)
    gold_offers.to_csv('mcdo_offers.csv')

def csv_treat():
    gold_offers_csv = pd.read_csv('mcdo_offers.csv')
    print(gold_offers_csv)

def excel_treat():
    data = pd.read_excel('climates.xlsx', sheet_name='Sea Level Stations', nrows=10)
    print(data)

def url():
    data = pd.read_table('https://github.com/cs109/2014_data/blob/master/countries.csv')
    print("URL")
    print(data.head(5))

if __name__ == "__main__":
    simple_series()
    dataframe()
    csv_treat()
    excel_treat()
    url()