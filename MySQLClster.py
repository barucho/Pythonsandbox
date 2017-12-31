#!/usr/bin/python 

#####################
#by baruch create MySQL cluster via python 
#
##################
import os
import pdb
import json
import itertools
#from subprocess import call
#from subprocess import Popen
import subprocess
## debug 
#pdb.set_trace()




##

def create_dir(directory):
 print("create dir",directory)
 if not os.path.exists(directory):
   os.makedirs(directory)




##
my_cnf_file_name="my.cnf"
config_file_name="config.json"
## read config.json file
if config_file_name:
    with open(config_file_name, 'r') as config_file:
        datastore = json.load(config_file)



## open my.cnf template  
temp_my_cnf_file = open('my.tm', 'r')
tempstr_my_cnf = temp_my_cnf_file.read()
## create directoris 
for node_number in range(1,datastore["config"]["number_of_nodes"]+1):
  path=datastore["config"]["datadir"]+str(node_number)
  node_port=datastore["config"]["node"+str(node_number)]["port"]
  create_dir(path)
  ## create my.cnf 
  device_values = {'$port':str(node_port),'$server_id':str(node_number),}
  for key,val in device_values.items():
    tempstr_my_cnf = tempstr_my_cnf.replace(key,val)
  #write new my.cnf file 
  my_cnf_file = open(path+'/'+'my.cnf','w')
  my_cnf_file.write(tempstr_my_cnf)
  my_cnf_file.close
  #re-read my.cnf template 
  temp_my_cnf_file.seek(0)
  tempstr_my_cnf = temp_my_cnf_file.read()
# clean open file 
temp_my_cnf_file.close()















## run init 

#proc1 = subprocess.Popen(['ps', 'cax'], stdout=subprocess.PIPE)
#proc2 = subprocess.Popen(['grep', 'python'], stdin=proc1.stdout,stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#proc1.stdout.close() # Allow proc1 to receive a SIGPIPE if proc2 exits.
#out, err = proc2.communicate()
#print('out: {0}'.format(out))
#print('err: {0}'.format(err))


