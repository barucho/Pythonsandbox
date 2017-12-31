#!/usr/bin/python 

#####################
#by baruch create MySQL cluster via python 
#
##################
import os
import pdb
import json
import itertools

## debug 
#pdb.set_trace()




##

def create_dir(directory):
 print("create dir",directory)
 if not os.path.exists(directory):
   os.makedirs(directory)


##
config_file_name="config.json"
## read config.json file
if config_file_name:
    with open(config_file_name, 'r') as config_file:
        datastore = json.load(config_file)
#print datastore["config"]["number_of_nodes"]

for node_number in range(1,datastore["config"]["number_of_nodes"]+1):
  print("create directory tree for: ",node_number)
  create_dir(datastore["config"]["datadir"]+node_number)