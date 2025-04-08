#!/usr/bin/python

# imports
import json

# open configuration file
config_file = open('config.json', 'r')
config = config_file.read()
config = json.loads(config);

# print initial message
print(config['name']);
