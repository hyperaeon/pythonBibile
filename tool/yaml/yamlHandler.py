# coding:utf-8

import yaml
import sys

__author__ = 'hzliyong'

f = open('env.yaml')
env = yaml.load(f)
print(env)
print(env.get('hive_home'))

str = '9'
print(str.__sizeof__())
print(sys.getsizeof(str))