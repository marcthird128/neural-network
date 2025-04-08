#!/usr/bin/python

# imports
import json
import random

# load the config file
def load_config():
	global config
	config_file = open('config.json', 'r')
	config = config_file.read()
	config = json.loads(config)
	config_file.close()
	print("Loaded config")

# initialize network
# each layer is a list. Each element
# in this list is a list of weights
# to the neurons in the previous layer,
# with the bias prepended
def init():
	global net
	net = []
	layerDat = config["network"]["layers"]
	lastDat = {}
	for dat in layerDat:
		lastDat = dat
		if dat["type"] == "input": continue
		neurons = [] # array of weights
		for i in range(dat["size"]):
			weights = [random.random()] # bias added first
			
			# random weights
			for j in range(lastDat["size"]):
				weights.append(random.random())
			neurons.append(weights)
			
		net.append(neurons)
	
	print("Initialized netowrk")

# load net from file
def load():
	global net
	net_file = open(config["network"]["location"], 'r')
	net = net_file.read()
	net = json.loads(net)
	net_file.close()
	print("Loaded network")

# save net to file
def save():
	net_file = open(config["network"]["location"], 'w')
	net_file.write(json.dumps(net, indent=3))
	net_file.close()
	print("Saved network")

# set up
load_config()
print(config['name'])
print("")
print("Enter commands. type 'help' for help")

# loop with a command line interface
while True:
	print("")
	command = input("> ")
	print("")
	args = command.split()
	
	if args[0] == "exit":
		print("Exited")
		break
		
	elif args[0] == "help":
		print("Commands:")
		print("")
		print("exit: exit the script")
		print("help: show this menu")
		print("config: reload config")
		print("init: initialize neural network randomly")
		print("load: load network")
		print("save: save network")
		
	elif args[0] == "config":
		load_config()
			
	elif args[0] == "init":
		init()
	
	elif args[0] == "load":
		load()
	
	elif args[0] == "save":
		save()
		
	else:
		print("Unknown command. Type 'help' for help")
