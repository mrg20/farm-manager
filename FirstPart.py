import pandas as pd
import numpy as np

class FirstPart:

    mcdonalds_julio = {'conos': 724009138, 'mcpollo': 724009126, 'bigmac': 724008146, 'cbo': 724008200}

    julio_completo = {'Codigo': [724009126, 724009018, 724009138], 'Precio': ['4,90€', '3€', '0,50€'], 
        'Producto': ['Menú McPollo', 'Menú Hamburguesa con Queso o Chicken Burger BBQ', 'Cono']}

    def simple_series(self):
        offers = pd.Series(self.mcdonalds_julio)
        print(offers)

    def dataframe(self):
        gold_offers = pd.DataFrame(self.julio_completo)
        print(gold_offers)
        gold_offers.to_csv('mcdo_offers.csv')

    def csv_treat(self):
        gold_offers_csv = pd.read_csv('mcdo_offers.csv')
        print(gold_offers_csv)

    def excel_treat(self):
        data = pd.read_excel('climates.xlsx', sheet_name='Sea Level Stations', nrows=10)
        print(data)

    def url(self):
        data = pd.read_table('https://github.com/cs109/2014_data/blob/master/countries.csv')
        print("URL")
        print(data.head(5))

    def execute(self):
        self.simple_series()
        self.dataframe()
        self.csv_treat()
        self.excel_treat()
        self.url()
