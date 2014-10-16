import authorization
import json
import requests
from urls import *
import argparse
import sys


def make_parser():
	""" Construct the cli parser"""
	description = "Get the corresponding information from twitter"
	parser = argparse.ArgumentParser(description=description)
	subparsers = parser.add_subparsers(dest="command", help="Available commands")
	#timeline
	t_parser = subparsers.add_parser("timeline", help="print out the home timeline")
	#users
	u_parser = subparsers.add_parser("users", help="print out the user information")
	#retweets_of_me
	r_parser = subparsers.add_parser("retweets_of_me", help="print out the most recent authored by the authenticating user that have been retweeted by others")
	return parser
 


def main():
	""" Main function """
	parser = make_parser()
	arguments=parser.parse_args(sys.argv[1:])
	# convert parsed arguments from Namespace to dictionaries
	arguments=vars(arguments)
	command = arguments.pop("command")
	auth=authorization.authorize()
	if command == "timeline":
		response = requests.get(TIMELINE_URL, auth=auth)
		#json.dumps function to format the output nicely
		print json.dumps(response.json(),indent=4)
	elif command == "users":
		response = requests.get(USERS_URL, auth=auth)
		print json.dumps(response.json(),indent=4)
	elif command == "retweets_of_me":
		response = requests.get(RTM_URL, auth=auth)
		print json.dumps(response.json(),indent=4)
	else:
		return

if __name__ == "__main__":
	main()