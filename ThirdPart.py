import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class ThirdPart:

    def movies_rating(self):
        ratings = pd.read_csv('ml-latest-small/ratings.csv')
        ratings.rating.plot.hist(bins=30)
        plt.title('Distribution of users ratings')
        plt.ylabel('count of users')
        plt.xlabel('rates')
        plt.show()

    def execute(self):
        self.movies_rating()