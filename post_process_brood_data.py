### CALCULATE REGION OF BROOD ###
import pandas as pd
import deeplabcut
import numpy as np
#import time_in_each_roi #need to download this and put in the same folder

#path_to_brood_csv = input("Path to brood coordinate csv file? \n")
#fps = input("what is the frame rate of the videos? \n")
#path_to_h5_files = input("Path to the h5 files to be analysed? \n")

path_to_brood_csv = '/home/rb17990/Documents/BROOD ANALYSIS PIPELINE/brood_regions.csv'
## read in csv file into pandas dataframe

broodData = pd.read_csv('brood_regions.csv')

## add columns to find next coordinates
## CHECK THESE
broodData['top_right_x'] = broodData['top_left_x'] + broodData['width']
broodData['top_right_y'] = broodData['top_left_y'] 
#broodData['bottom_left_x'] = broodData['top_left_x']
#broodData['bottom_left_y'] = broodData['top_left_y'] + broodData['height']
broodData['bottom_right_x'] = broodData['top_left_x'] + broodData['width']
broodData['bottom_right_y'] = broodData['top_left_y'] + broodData['height']
print(broodData)



# read dlc h5 files in, maybe change working directory

# choose a body part, e.g. thorax

# calculate velocity of body part
# x y and velocity numbers in np.array

#https://github.com/DeepLabCut/DLCutils/blob/master/Demo_loadandanalyzeDLCdata.ipynb

# use coordinates calculated to input bounding box, top left and bottom right XY

# output results from code into another big csv that can be statistically analysed
# change code to reflect only one bounding box per video
# loop through data - match to file_name prefixes to h5 files
