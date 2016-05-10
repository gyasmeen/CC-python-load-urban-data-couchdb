

# python  load_urban_data_couchdb.py --couchdb_ip=115.146.95.99:5984 --dbname='urban-data'

from couchdb import Server

import argparse
parser = argparse.ArgumentParser(description='')
parser.add_argument('--couchdb_ip', '-ip', help='ip of couchdb')
parser.add_argument('--dbname', '-db', help='urban db name')
args = parser.parse_args()
server = Server('http://'+args.couchdb_ip+'/')
try:
    db = server[args.dbname]
except:
    db = server.create(args.dbname)

import json
from pprint import pprint

savecount =0
count=1
with open('aurin_selected_medians.json','r') as json_data:
    d = json.load(json_data)
    json_data.close()
#    print len(d['features'])
    for row in d['features']:
        row.update({'_id':row['properties']['feature_name']+'aurin-income', 'id': row['properties']['feature_name'], 'Source': 'aurin-income'})
        try:
            db.save(row)
	    savecount = savecount+1
#            print count , ': is saved !!!!'
        except:
	     print count , ': already exist !!!'
        count = count + 1
print savecount, ' docs are added to the couchdb'


import h5py
import numpy as np
import time
from scipy.io import loadmat
import pycurl
from StringIO import StringIO

mat1= loadmat('VicHealth_Data.mat',squeeze_me=True)
header=mat1['Suburbs_list_Header']
data=mat1['Suburbs_list_raw']
ps1 = mat1['ps']


numrows = len(data)    # 34 rows 
numcols = len(data[0]) # 231 columns in your example

savecount=0

for i in range (0,numrows):
    doc = dict()
    for j  in range (0,numcols):
	doc.update({header[1,j] : data[i,j]})
    doc.update({'_id' : data[i,0]+'vic-health', 'id' : data[i,0] ,'ps' : int(ps1[i]) , 'Source' : 'vic-health'})
    try:
	db.save(doc)
	savecount=savecount+1
#	print i , ': is saved !!!!'
    except:
	print i , ': already exist !!!'


print savecount, ' docs are added to the couchdb'

