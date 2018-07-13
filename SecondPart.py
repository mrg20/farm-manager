import pandas as pd
import numpy as np

class SecondPart:

    top_rates=None

    def slicer(self):
        ratings = pd.read_csv('ml-latest-small/ratings.csv')
        self.top_rates = ratings[ratings.rating==5.0]
        self.movies = pd.read_csv('ml-latest-small/movies.csv')
        print(self.top_rates)

    def apply(self):
        self.top_rates = self.top_rates[['movieId','rating']]
        self.top_rates = self.top_rates.drop_duplicates()
        print(self.top_rates)

    def combine(self):
        result = pd.merge(self.top_rates, self.movies, on='movieId')
        print(result[['title', 'rating']])

    def execute(self):
        print('----------------------------SECOND PART------------------------------')
        self.slicer()
        self.apply()
        self.combine()