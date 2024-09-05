import pandas as pd
import os
from pydantic import BaseModel
import json


data_dir = 'f:/python_apps/SocEcon/data/'


class JobTable():

    @staticmethod
    def fixyr(y):
        if type(y) == str:
            yy = y[0:4]
            return int(yy)

        elif type(y) == float:
            return int(y)
        else:
            raise Exception("Invalid year")

    @staticmethod
    def fixce(x):
        import re
        if ',' in x:
            xx = re.sub("[^0-9]", "", x)
            return int(xx)
        elif '(NA)' in x:
            return 0
        else:
            return int(x)




    def __init__(self, name: str, df: pd.DataFrame, save=False, fn=None):

        self.name = name
        self.json_fn = f"{fn}"

        self.df: pd.DataFrame = df

        self.ddict = self.df.to_dict()
        if os.path.exists(self.json_fn):
            if save:
                self.save()
            self.df = pd.read_json(self.json_fn)
        elif save:
            self.save()
        else:
            pass



    def save(self):
        self.df.to_json(self.json_fn)

ddict = {"Administration, business, financial, and legal":
                        {'totals': [1.0, 16.3, 15.4],
                         'children':
                             [
                                 {'Office administration': [0.5, 12.4, 11.9]},
                                 {'Business and financial': [0.1, 3.2, 3.1]},
                                 {'Legal': [0.4, 0.7, 0.3]},

                             ],
                         'categories': ['management'],
                         },

                    'Management':
                        {
                            'totals': [4.8, 13.2, 8.4],
                            'categories': ['management']
                        },

                    "Other service occupations":
                        {
                            'totals': [1.1, 13.1, 12.0],
                            "children": [
                                {'Food related': [0.4, 5.1, 4.7]},
                                {'Personal service': [0.2, 3.0, 2.8]},
                                {'Arts, media, and sports': [0.3, 3.2, 2.9]},
                                {'Protective service': [0.2, 1.9, 1.7]},

                            ],
                            'categories': ['services'],

                        },

                    "Healthcare":
                        {'totals': [1.0, 9.5, 8.5],
                         'children':
                             [
                                 {'Healthcare professionals': [1.0, 6.3, 5.3]},
                                 {'Healthcare support': [0.0, 3.2, 3.2]},
                             ],
                         'categories': ['healthcare']
                         },

                    'Sales': {'totals': [2.5, 8.7, 6.2],
                              'categories': ['retail-wholesale']},

                    "Construction, extraction, transportation, and moving":
                        {'totals': [10.2, 7.6, -2.6],
                         'children':
                             [
                                 {'Construction and extraction': [7.6, 4.0, -3.6]},
                                 {'Transportation and moving': [0.1, 7.4, 7.3]},

                             ],
                         'categories': ['production']
                         },

                    "Science, math, architecture, and engineering":
                        {'totals': [0.1, 7.4, 7.3],
                         'children': [
                             {'Mathematical': [0.0, 4.1, 4.1]},
                             {'Architecture and engineering': [0.1, 2.5, 2.4]},
                             {'Scientists': [0.0, 0.8, 0.8]},

                         ],
                         'categories': ['professionals'],
                         },

                    "Cleaning, maintenance, and repair":
                        {'totals': [10.5, 6.8, -3.7],
                         'children': [
                             {'Cleaning and maintenance': [8.2, 3.9, -4.3]},
                             {'Maintenance and repair': [2.4, 2.9, 0.5]},

                         ],
                         'categories': ['maintenance-repair']
                         },

                    "Production": {'totals': [14.2, 6.5, -7.6],
                                   'categories': ['production']},
                    "Education, library, and social service":
                        {'totals': [1.8, 6.1, 4.2],
                         'children': [
                             {'Education and library': [1.4, 4.9, 3.5]},
                             {'Social service': [0.5, 1.2, 0.7]}
                         ],
                         'categories': ['public']
                         },

                    "Laborers": {'totals': [9.6, 3.6, -6.1],
                                 'categories': ['production', 'maintenance-repair']
                                 },
                    "Farm, fishing, and forestry": {'totals': [43.2, 1.2, -42.1],
                                                    'categories': ['Agg']
                                                    }

                    }


outfile: str = f"{data_dir}/AI/cfed1_orig_datadict.json"


class DataDic(BaseModel):
    outfile: str = f"{data_dir}/AI/cfed1_orig_datadict.json"

    datadict: dict = None


    def save_doc(self, doutfile=outfile):
        d = self.model_dump()
        with open(doutfile, "w") as f:
            json.dump(d, f)

    @staticmethod
    def load_doc(doutfile=outfile):
        with open(doutfile) as f:
            d = json.load(f)
            dd = d['datadict']
        return DataDic(datadict=dd)

    @staticmethod
    def getData(doutfile=outfile):
        import pathlib
        path = pathlib.Path(doutfile)
        if path.exists():
            return DataDic.load_doc()
        else:
            return DataDic(datadict=ddict)


class CFED1(JobTable):
    short_occ_names = ['Administration','Management', 'Other Service',
                       'Healthcare', 'Sales', 'Cons-Extract', 'Sci-Eng', 'Maintenance',
                       'Production', 'Ed-Social', 'Laborers', 'Farm']

    desc = "US structural occupation share changes: 1860-2015"
    # sfn = 'EC_201909.pdf'
    # source_fn = f"{data_dir}{sfn}"
    source_url = """https://www.clevelandfed.org/publications/economic-commentary/2019/ec-201909-changes-in-us-occupational-structure"""
    headerCols = ['Occupational group', '1860_share', '2015_share', 'Change in share']
    all_categories = ['management', 'professional', 'services', 'production', 'healthcare',
                      'maintenance-repair', 'retail-wholeale', 'agg', 'public']
    all_services = ['professional', 'services','healthcare','maintenance-repair',
                    'public', 'retail-wholeale']
    all_production = ['production']
    datadict = DataDic.getData().datadict


    # @staticmethod
    # def CFED_pdf2df():
    #     # reads table from pdf file
    #     dff = read_pdf(f"{CFED1.source_fn}", pages="all")  # address of pdf file
    #     # print(tabulate(df))
    #     return dff

    @staticmethod
    def cleanCFED(df: pd.DataFrame):
        dff: pd.DataFrame = df.iloc[2:, ].copy(deep=True)
        dff.reset_index(drop=True, inplace=True)
        dff['shares'] = dff['1860_2015'].apply(lambda x: (float(x.split(' ')[0]), float(x.split(' ')[1])))
        dff['s1860'] = dff.shares.apply(lambda t: t[0])
        dff['s2015'] = dff.shares.apply(lambda t: t[1])
        dff.change_2015 = dff.change_2015.astype(float)
        return dff[['Occupation_Group', 's1860', 's2015', 'change_2015']].copy(deep=True)

    @staticmethod
    def fromCFED():
        import os
        nm = "Occupational Group Employment Shares in the Contiguous United States in 1860 and 2015"
        fn = "occ_grp_shares_1860_2015_df.json"
        fnn = f"{data_dir}{fn}"
        if os.path.exists(fnn):
            dff = pd.read_json(fnn)
        else:
            raise FileNotFoundError(f"{fnn} not found")
        cfed = CFED1(nm, dff, save=True, fn=fnn)
        return cfed

    def __init__(self, name, df: pd.DataFrame, save=True, fn=None):
        super().__init__(name, df, save=save,fn=fn)
        self.setCategories()
        self.topOccs = self.getTopOccs()


    def getTopOccs(self):
        # set category feature on data frame
        cfed_df: pd.DataFrame = self.df.copy(deep=True)
        lkeys = list(CFED1.datadict.keys())
        cfed_df['isTop'] = cfed_df.Occupation_Group.apply(lambda x: True if x in lkeys else False)
        mask = cfed_df.isTop == True
        topdf: pd.DataFrame = cfed_df[mask].copy(deep=True)
        topdf['short_occ_name'] = CFED1.short_occ_names


        return topdf

    def setCategories(self):
        if 'categories' in list(self.df.columns):
            print("categories already set in dataframe")
            return
        else:

            grp_nms = []
            cat_nms = []
            for k in self.datadict.keys():
                grp_nms.append(k)
                cat = self.datadict[k]['categories'][0]
                cat_nms.append(cat)
                children = self.datadict[k].get('children', None)
                if children:
                    for c in children:
                        ckeys = list(c.keys())
                        grp_nms.append(ckeys[0])
                        cat_nms.append(cat)
            self.cats = zip(grp_nms,cat_nms)
            occ_groups = list(self.df.Occupation_Group)
            dcats = {k:v for (k, v) in self.cats}
            grp_cats = []
            for g in occ_groups:
                c = dcats.get(g)
                grp_cats.append(c)

            self.df['category'] =grp_cats


class BLS_PW(JobTable):

    @staticmethod
    def from_US_Fed_Emp() -> JobTable:
        # consolidated columns (before split)
        cols = ['yr', 'Total_civ_emp1', 'dod1', 'civ_ag1', 'po1',
                'yr2', 'Total_civ_emp2', 'dod2', 'civ_ag2', 'po2']

        # source pdf from St. Louis Fed
        fnpdf = 'US_pub_employment.pdf'
        dir = f"{data_dir}AI/"
        #  Output json file for dataframe storage
        outfile = f"{dir}US_pub_employment.json"
        if os.path.exists(outfile):
            dfff = pd.read_json(outfile)
            nm = "US Public Federal Civilian Employment 1900 to 2020"
            return JobTable(nm, dfff, save=True, fn=outfile)
        else:
            raise FileNotFoundError(f"{outfile}")


















