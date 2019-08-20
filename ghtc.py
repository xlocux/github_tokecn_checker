#!/usr/bin/env python
# -*- coding: utf-8 -*-
# github_token_checker 
# By Locu

# Import libraries
import sys
import argparse
from github import Github

# Command line Arguments
parser = argparse.ArgumentParser()
parser.add_argument('-t', '--token', help='GitHub Token', action='store')

if len(sys.argv)<2:
	print('eg: python %s -t your_token' % sys.argv[0])
	args = parser.parse_args(['-h'])
else:
	args = parser.parse_args()

def parser_error(errmsg):

    print('Usage: python %s [Options] use -h for help' % sys.argv[0])
    print('Error: %s' % errmsg)
    sys.exit()

if args.token:
	token = args.token

g = Github(token)
user = g.get_user()

try:
	print('\nUSERNAME:\n ' + user.login + ' \n\nAVAILABLE REPOs:')
	for repo in g.get_user().get_repos():
		print(repo.name)
		
    
except Exception as e:
    print('\nINVALID TOKEN!\n')
