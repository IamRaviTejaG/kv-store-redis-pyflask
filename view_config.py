""" Test file for printing session configuration """

import pprint

import yaml

import constants

print(f'{constants.DECORATOR}\nSESSION CONFIGURATION:\n{constants.DECORATOR}')
pprint.pprint(yaml.full_load(open('config.yml')))
print(f'{constants.DECORATOR}')
