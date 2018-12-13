import json
import sys
import os.path

def get_data():
   topo_path = os.path.abspath(os.path.dirname(__file__))
   path = os.path.join(topo_path, "../config/Topology_file.json")
   with open(path) as data_file:
      data = json.load(data_file)
   return data
