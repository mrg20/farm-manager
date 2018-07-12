import pandas as pd
import numpy as np


mcdonalds_julio = {'conos': 2234342342, 'mcpollo': 235443453452, 'bigmac': 3453453453454, 'Boston': 23235234}


def simple_series():
    offers = pd.Series(mcdonalds_julio)
    print(offers)


if __name__ == "__main__":
    simple_series()