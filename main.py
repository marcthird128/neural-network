#!/usr/bin/python

# imports
import json

# load the config file
def load_config():
	global config
	config_file = open('config.json', 'r')
	config = config_file.read()
	config = json.loads(config)
	config_file.close()
	print("Loaded config")

# save the config
def save_config():
	config_file = open('config.json', 'w')
	config_file.write(json.dumps(config, indent=4))
	print("Saved config")

# initialize network
def init_net():
	print("Initialized netowrk")

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
		print("init: save network")
		
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
