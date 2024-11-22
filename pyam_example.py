
import pandas as pd
import pyam
import silicone.database_crunchers
from silicone.stats import rolling_window_find_quantiles
from silicone.utils import (
    _get_unit_of_variable,
    find_matching_scenarios,
    _make_interpolator,
    _make_wide_db,
    get_sr15_scenarios,
    download_or_load_sr15,
)

# pyam est un outil développé par la communauté IAMC
# afin de faciliter l'utilisation et l'importation de scénario des bases de données du GIEC
# il s'agit ici de se familiriser avec cet outil, et d'assyer de recréer des analyses du TP sur d'autres ensembles de scénarios

# load 1.5 database and select some scenarios / variables

# TODO: se familairiser avec la doc:
#doc: https://pyam-iamc.readthedocs.io/en/stable/api/iamdataframe.html

#available database
conn = pyam.iiasa.Connection()
conn.valid_connections

# laod data
df = pyam.read_iiasa(
        'iamc15'
#    #model='MESSAGEix*',
    model=['MESSAGE*'],
    variable=['Final Energy*'],
    region=['World'],
    meta='category'
)

# look at data
df.model
df.scenario
df.variable
df.timeseries()

# select scenarios
sc_selection = ['LowEnergyDemand', 'SSP2-19']

model="MESSAGE-GLOBIOM 1.0"
# convert in pandas dataframe
df = df.as_pandas(meta_cols=False)
df_msg = pd.concat( [ df[ df['scenario']==sc] for sc in sc_selection])

model = list(set( df['model']))[1]
unit = list(set( df['unit']))[0]
variables = list(set( df['variable']))
variables.sort()

df_msg = df_msg.drop(['model','region','unit'], axis=1)


