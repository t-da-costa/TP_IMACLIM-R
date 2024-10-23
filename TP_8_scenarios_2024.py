############################################################
# header: importing useful modules and functions
import csv, os #lecture ecriture de csv; os management
import numpy as np #traitement de matrice de type numpy array
import matplotlib.pyplot as plt #librairy graphique
import pandas as pd

###########################
############################################################
#Reading data
############################################################

path_data='data/'
data_tp = {} # import data n a python dictionnary
for fil in [fil for fil in os.listdir(path_data) if '.csv' in fil]:
    data_tp[ fil.replace('.csv', '')] = np.array([line for line in csv.reader(open( path_data+fil,'r'))][1:],dtype=float)
print(data_tp.keys()) # print key to access data in the dictionnary

# improt years from the first 'POP_w' csv - 2015-2100 years
years = np.array([line for line in csv.reader(open('data/Pop_w.csv','r'))][0],dtype=float)

drivers_names=np.array([line for line in csv.reader(open('data/drivers.csv','r'))][0],dtype=str) #import names of the groups of parameters

# create output folder
output_path = 'figures/'
os.mkdir(output_path)

# alternative to read files
eco2 = np.array([line for line in csv.reader(open(path_data+'ECO2_w.csv','r'))][1:],dtype=float)#global CO2 emissions
eco2 = np.genfromtxt( path_data+'ECO2_w.csv', dtype=None, delimiter=',', skip_header=1) 
eco2 = pd.read_csv( path_data+'ECO2_w.csv', delimiter=',').to_numpy()

headder = pd.read_csv( path_data+'ECO2_w.csv', delimiter=',').columns.to_numpy()

# import other variables
# gdp_per_cap, gdp, ei, ci


###########################
# Section A.1
###########################

#Choosing a baseline (between 1 and 216)
base_nb=
# drivers: 0,1,1,2,1,2,0,0
# 'mitigation', 'leader growth', 'productivity catch-up', 'fossil fuels', 'energy demand behavior', 'energy efficiency', 'low-carbon technologies', 'labor markets rigidities']

### Fig. 1 ###
# plot the global emissions over 2015-2100
plt.clf()
plt.figure()
plt.plot(years,np.transpose( data_tp['ECO2_w'][base_nb-1,:]),color="k", linewidth=3, label="Global CO2 emissions")
plt.legend(loc=0)
plt.xlabel('years')
plt.ylabel('evolution / 2015')

plt.savefig( output_path + "td_fig1_emissions.pdf")

