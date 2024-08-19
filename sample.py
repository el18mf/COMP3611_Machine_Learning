import pandas as pd
from matplotlib import pyplot as plt
import csv 
import numpy as np
import random
import scipy 
from scipy.stats import pearsonr
import seaborn as sns
plt.style.use('seaborn-v0_8-paper')
#plotting of all features in a table of histograms to easier total visual comparison
TD.hist(bins=100,figsize=(12,12), edgecolor = 'black', color='skyblue', histtype = 'stepfilled', linewidth = 1, alpha = 0.7)
plt.show()
plt.close()
#Histogram of Target
TP.hist(bins=100,figsize=(12,12), edgecolor = 'black', color='skyblue', histtype = 'stepfilled', linewidth = 1, alpha = 0.7)
plt.show()
plt.close()
#iterates through each index of the list keys, using the key/title to plot, manipulate, show and then save individual histograms of each feature for use in finer detail visual comparison
for x in keys:  
    #plots histogram with a randomised colour (minimsed the possiblity of yellow popping up as it hurts my eyes), step type histogram and display the title
    plt.hist(TD[x],bins=1000, align="mid", edgecolor = 'black',color=(random.randint(1,9)/10,random.randint(1,5)/10,random.randint(1,9)/10),stacked=True,alpha=0.8)   
    #Adds the title to the histogram from the corresponding entry in the data_points_split list whose index is given by returning which 0-30 feature it is currently creating the histogram for by using x in keys (which returns the location inside keys which corresponds to the title in data_points_split)
    plt.title(data_points_split[(keys.index(x))])   
    #Adds the x and y axis labels and adjusts their size to font 14
    plt.xlabel("X-Axis - Data Value",size=14)
    plt.ylabel("Y-Axis - Frequency in Data Frame",size=14) 
    #this stretches the histogram to the right to make it easier to visually see the data by a factor of 1.5
    plt.subplots_adjust(right=3,top=1.5)   
    plt.close()
#There seems to be several outliers in almost all of the Data Frames with several single data points appearing outside the general range of the majority of data points. There are also massive spikes in a couple of data sets such as in the first feature avgAnnCount, with a spike around 2000, and in the incidentRate around 400-500 (which I believe are the 1962.667684 & 453.5494221 values on inspection in the csv file which makes sense as more incidents means the average annual count would also increase)