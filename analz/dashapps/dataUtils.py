import pandas as pd


class US_Gov_Employment:
    US_gov_data = {'Year': [1984, 1990, 1993, 1996, 1999, 2002, 2005, 2010, 2015, 2017, 2020],
                   'Federal': [2.083, 2.174, 2.139, 1.891, 1.778, 1.756, 1.83, 2.128, 2.042, 2.062, 2.206],
                   'Military': [2.138, 2.044, 1.705, 1.472, 1.386, 1.412, 1.518, 1.384, 1.315, 1.334, 1.364],
                   'Postal': [0.673, 0.761, 0.692, 0.761, 0.798, 0.753, 0.705, 0.584, 0.492, 0.509, 0.497],
                   'Contract': [3.666, 3.427, 3.245, 3.042, 2.398, 2.791, 3.882, 4.845, 3.702, 3.629, 5.032629],
                   'Grant': [1.234, 1.352, 1.344, 1.351, 1.415, 1.236, 1.578, 2.344, 1.583, 1.189, 1.817],
                   }
    df = pd.DataFrame(US_gov_data)
    title = 'US Government Employment, 1982 - 2020'

    def __init__(self):
        self.dff = US_Gov_Employment.df.copy()
        self.dfmelt = pd.melt(self.dff, id_vars=['Year'],
                              value_vars=['Federal', 'Military', 'Postal', 'Contract', 'Grant'])
        self.dff.set_index('Year', inplace=True, drop=True)
        self.dff = self.dff * 1000000
        self.dff = self.dff.astype(int)
        self.dfmelt.set_index('Year', inplace=True, drop=True)
        self.dfmelt.value = self.dfmelt.value * 1000000
        self.dfmelt.value = self.dfmelt.value.astype(int)
        self.dff['total'] = self.dff.sum(axis=1)
        self.total_2020 = self.dff.loc[2020,'total']
        self.str_total_2020 = f"{self.total_2020:,}"




