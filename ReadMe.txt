#################Required python modules
# h5py and scipy for loading .mat files

sudo apt-get install python-scipy
sudo apt-get install libhdf5-dev
sudo apt-get install cython
sudo pip install h5py


#pycurl
sudo aptitude install python-pycurl

# couchdb python client
wget http://pypi.python.org/packages/2.6/C/CouchDB/CouchDB-0.8-py2.6.egg
sudo easy_install CouchDB-0.8-py2.6.egg


####################running the application
python  load_urban_data_couchdb.py --couchdb_ip=115.146.95.99:5984 --dbname='urban-data'
